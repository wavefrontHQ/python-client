from pyformance import MetricsRegistry
from wavefront_pyformance.wavefront_reporter import WavefrontReporter, WavefrontProxyReporter, WavefrontDirectReporter
from wavefront_pyformance import delta
import time
import sys


def report_metrics(host, server, token):
    reg = MetricsRegistry()

    wf_proxy_reporter = WavefrontProxyReporter(host=host, port=2878, registry=reg, source="wavefront-pyformance-example", tags={"key1":"val1", "key2":"val2"}, prefix="python.proxy.")
    wf_direct_reporter = WavefrontDirectReporter(server=server, token=token, registry=reg, source="wavefront-pyformance-exmaple", tags={"key1":"val1", "key2": "val2"}, prefix="python.direct.")

    # counter
    c1 = reg.counter("foo_count")
    c1.inc()

    # delta counter
    d1 = delta.delta_counter(reg, "foo_delta_count")
    d1.inc()
    d1.inc()

    # gauge
    g1 = reg.gauge("foo_gauge")
    g1.set_value(2)

    # meter
    m1 = reg.meter("foo_meter")
    m1.mark()

    # timer
    t1 = reg.timer("foo_timer")
    timer_ctx = t1.time()
    time.sleep(3)
    timer_ctx.stop()

    # histogram
    h1 = reg.histogram("foo_histogram")
    h1.add(1.0)
    h1.add(1.5)

    wf_proxy_reporter.report_now()
    wf_proxy_reporter.stop()
    wf_direct_reporter.report_now()


if __name__ == "__main__":
    # python example.py proxy_host server_url server_token
    host = sys.argv[1]
    server = sys.argv[2]
    token = sys.argv[3]
    report_metrics(host, server, token)
