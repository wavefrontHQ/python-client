# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import socket
import requests
from pyformance.reporters.reporter import Reporter
from . import delta

if sys.version_info[0] > 2:
    from urllib.parse import urlparse
else:
    from urlparse import urlparse


class WavefrontReporter(Reporter):
    """
    Base reporter for reporting data in Wavefront format.
    """

    def __init__(self, source="wavefront-pyformance", registry=None, reporting_interval=10, clock=None, prefix="", tags={}):
        super(WavefrontReporter, self).__init__(registry=registry,
                                                reporting_interval=reporting_interval,
                                                clock=clock)
        self.source = source
        self.prefix = prefix
        tags = tags or {}
        self.tagStr = ' '.join(['\"%s\"=\"%s\"' % (k,v) for (k,v) in tags.items()])

    def report_now(self, registry=None, timestamp=None):
        raise NotImplementedError('use WavefrontProxyReporter or WavefrontDirectReporter')

    def _collect_metrics(self, registry, timestamp=None):
        metrics = registry.dump_metrics()
        metrics_data = []
        for key in metrics.keys():
            is_delta = delta.is_delta_counter(key, registry)
            for value_key in metrics[key].keys():
                if is_delta:
                    registry.counter(key).dec(metrics[key][value_key]) # decrement delta counter
                metric_name = self._get_metric_name(self.prefix, key, value_key, is_delta=is_delta)
                metric_line = self._get_metric_line(metric_name, metrics[key][value_key], timestamp)
                metrics_data.append(metric_line)
        return metrics_data

    def _get_metric_line(self, name, value, timestamp):
        if timestamp:
            return "%s %s %s source=\"%s\" %s" % (name, value, timestamp, self.source, self.tagStr)
        else:
            return "%s %s source=\"%s\" %s" % (name, value, self.source, self.tagStr)

    def _get_metric_name(self, prefix, name, value_key, is_delta=False):
        return delta.get_delta_name(prefix, name, value_key) if is_delta else "%s%s.%s" % (prefix, name, value_key)


class WavefrontProxyReporter(WavefrontReporter):
    """
    This reporter requires a host and port to report data to a Wavefront proxy.
    """

    def __init__(self, host, port=2878, source="wavefront-pyformance", registry=None, reporting_interval=10, clock=None,
                 prefix="proxy.", tags={}):
        super(WavefrontProxyReporter, self).__init__(source=source,
                                                     registry=registry,
                                                     reporting_interval=reporting_interval,
                                                     clock=clock,
                                                     prefix=prefix,
                                                     tags=tags)
        self.host = host
        self.port = port
        self.socket_factory = socket.socket
        self.proxy_socket = None

    def report_now(self, registry=None, timestamp=None):
        timestamp = timestamp or int(round(self.clock.time()))
        metrics = self._collect_metrics(registry or self.registry, timestamp)
        if metrics:
            self._report_points(metrics)

    def stop(self):
        super(WavefrontProxyReporter, self).stop()
        if self.proxy_socket:
            self.proxy_socket.close()

    def _report_points(self, metrics, reconnect=True):
        try:
            if not self.proxy_socket:
                self._connect()
            for line in metrics:
                self.proxy_socket.send(line.encode('utf-8') + "\n")
        except socket.error as e:
            if reconnect:
                self.proxy_socket = None
                self._report_points(metrics, reconnect=False)
            else:
                print("error reporting to wavefront proxy:", e, file=sys.stderr)
        except Exception as e:
            print("error reporting to wavefront proxy:", e, file=sys.stderr)

    def _connect(self):
        self.proxy_socket = self.socket_factory(socket.AF_INET, socket.SOCK_STREAM)
        self.proxy_socket.connect((self.host, self.port))


class WavefrontDirectReporter(WavefrontReporter):
    """
    This reporter requires a server and a token to report data directly to a Wavefront server.
    """

    def __init__(self, server, token, source="wavefront-pyformance", registry=None, reporting_interval=10, clock=None,
                 prefix="direct.", tags={}):
        super(WavefrontDirectReporter, self).__init__(source=source,
                                                      registry=registry,
                                                      reporting_interval=reporting_interval,
                                                      clock=clock,
                                                      prefix=prefix,
                                                      tags=tags)
        self.server = self._validate_url(server)
        self.token = token
        self.batch_size = 10000
        self.headers = {'Content-Type': 'text/plain',
                             'Authorization': 'Bearer ' + token}
        self.params = {'f': 'graphite_v2'}

    def _validate_url(self, server):
        parsed_url = urlparse(server)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError("invalid server url")
        return server

    def report_now(self, registry=None, timestamp=None):
        metrics = self._collect_metrics(registry or self.registry)
        if metrics:
            # limit to batch_size per api call
            chunks = self._get_chunks(metrics, self.batch_size)
            for chunk in chunks:
                metrics_str = u'\n'.join(chunk).encode('utf-8')
                self._report_points(metrics_str)

    def _get_chunks(self, metrics, chunk_size):
        """
        returns a lazy list generator
        """
        for i in range(0, len(metrics), chunk_size):
            yield metrics[i:i+chunk_size]

    def _report_points(self, points):
        try:
            r = requests.post(self.server+'/report', params=self.params, headers=self.headers, data=points)
            r.raise_for_status()
        except Exception as e:
            print(e, file=sys.stderr)


