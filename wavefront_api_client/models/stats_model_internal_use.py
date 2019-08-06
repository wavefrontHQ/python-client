# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StatsModelInternalUse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'buffer_keys': 'int',
        'cached_compacted_keys': 'int',
        'compacted_keys': 'int',
        'compacted_points': 'int',
        'cpu_ns': 'int',
        'hosts_used': 'int',
        'keys': 'int',
        'latency': 'int',
        'metrics_used': 'int',
        'points': 'int',
        'queries': 'int',
        'query_tasks': 'int',
        's3_keys': 'int',
        'skipped_compacted_keys': 'int',
        'summaries': 'int'
    }

    attribute_map = {
        'buffer_keys': 'buffer_keys',
        'cached_compacted_keys': 'cached_compacted_keys',
        'compacted_keys': 'compacted_keys',
        'compacted_points': 'compacted_points',
        'cpu_ns': 'cpu_ns',
        'hosts_used': 'hosts_used',
        'keys': 'keys',
        'latency': 'latency',
        'metrics_used': 'metrics_used',
        'points': 'points',
        'queries': 'queries',
        'query_tasks': 'query_tasks',
        's3_keys': 's3_keys',
        'skipped_compacted_keys': 'skipped_compacted_keys',
        'summaries': 'summaries'
    }

    def __init__(self, buffer_keys=None, cached_compacted_keys=None, compacted_keys=None, compacted_points=None, cpu_ns=None, hosts_used=None, keys=None, latency=None, metrics_used=None, points=None, queries=None, query_tasks=None, s3_keys=None, skipped_compacted_keys=None, summaries=None):  # noqa: E501
        """StatsModelInternalUse - a model defined in Swagger"""  # noqa: E501

        self._buffer_keys = None
        self._cached_compacted_keys = None
        self._compacted_keys = None
        self._compacted_points = None
        self._cpu_ns = None
        self._hosts_used = None
        self._keys = None
        self._latency = None
        self._metrics_used = None
        self._points = None
        self._queries = None
        self._query_tasks = None
        self._s3_keys = None
        self._skipped_compacted_keys = None
        self._summaries = None
        self.discriminator = None

        if buffer_keys is not None:
            self.buffer_keys = buffer_keys
        if cached_compacted_keys is not None:
            self.cached_compacted_keys = cached_compacted_keys
        if compacted_keys is not None:
            self.compacted_keys = compacted_keys
        if compacted_points is not None:
            self.compacted_points = compacted_points
        if cpu_ns is not None:
            self.cpu_ns = cpu_ns
        if hosts_used is not None:
            self.hosts_used = hosts_used
        if keys is not None:
            self.keys = keys
        if latency is not None:
            self.latency = latency
        if metrics_used is not None:
            self.metrics_used = metrics_used
        if points is not None:
            self.points = points
        if queries is not None:
            self.queries = queries
        if query_tasks is not None:
            self.query_tasks = query_tasks
        if s3_keys is not None:
            self.s3_keys = s3_keys
        if skipped_compacted_keys is not None:
            self.skipped_compacted_keys = skipped_compacted_keys
        if summaries is not None:
            self.summaries = summaries

    @property
    def buffer_keys(self):
        """Gets the buffer_keys of this StatsModelInternalUse.  # noqa: E501


        :return: The buffer_keys of this StatsModelInternalUse.  # noqa: E501
        :rtype: int
        """
        return self._buffer_keys

    @buffer_keys.setter
    def buffer_keys(self, buffer_keys):
        """Sets the buffer_keys of this StatsModelInternalUse.


        :param buffer_keys: The buffer_keys of this StatsModelInternalUse.  # noqa: E501
        :type: int
        """

        self._buffer_keys = buffer_keys

    @property
    def cached_compacted_keys(self):
        """Gets the cached_compacted_keys of this StatsModelInternalUse.  # noqa: E501


        :return: The cached_compacted_keys of this StatsModelInternalUse.  # noqa: E501
        :rtype: int
        """
        return self._cached_compacted_keys

    @cached_compacted_keys.setter
    def cached_compacted_keys(self, cached_compacted_keys):
        """Sets the cached_compacted_keys of this StatsModelInternalUse.


        :param cached_compacted_keys: The cached_compacted_keys of this StatsModelInternalUse.  # noqa: E501
        :type: int
        """

        self._cached_compacted_keys = cached_compacted_keys

    @property
    def compacted_keys(self):
        """Gets the compacted_keys of this StatsModelInternalUse.  # noqa: E501


        :return: The compacted_keys of this StatsModelInternalUse.  # noqa: E501
        :rtype: int
        """
        return self._compacted_keys

    @compacted_keys.setter
    def compacted_keys(self, compacted_keys):
        """Sets the compacted_keys of this StatsModelInternalUse.


        :param compacted_keys: The compacted_keys of this StatsModelInternalUse.  # noqa: E501
        :type: int
        """

        self._compacted_keys = compacted_keys

    @property
    def compacted_points(self):
        """Gets the compacted_points of this StatsModelInternalUse.  # noqa: E501


        :return: The compacted_points of this StatsModelInternalUse.  # noqa: E501
        :rtype: int
        """
        return self._compacted_points

    @compacted_points.setter
    def compacted_points(self, compacted_points):
        """Sets the compacted_points of this StatsModelInternalUse.


        :param compacted_points: The compacted_points of this StatsModelInternalUse.  # noqa: E501
        :type: int
        """

        self._compacted_points = compacted_points

    @property
    def cpu_ns(self):
        """Gets the cpu_ns of this StatsModelInternalUse.  # noqa: E501


        :return: The cpu_ns of this StatsModelInternalUse.  # noqa: E501
        :rtype: int
        """
        return self._cpu_ns

    @cpu_ns.setter
    def cpu_ns(self, cpu_ns):
        """Sets the cpu_ns of this StatsModelInternalUse.


        :param cpu_ns: The cpu_ns of this StatsModelInternalUse.  # noqa: E501
        :type: int
        """

        self._cpu_ns = cpu_ns

    @property
    def hosts_used(self):
        """Gets the hosts_used of this StatsModelInternalUse.  # noqa: E501


        :return: The hosts_used of this StatsModelInternalUse.  # noqa: E501
        :rtype: int
        """
        return self._hosts_used

    @hosts_used.setter
    def hosts_used(self, hosts_used):
        """Sets the hosts_used of this StatsModelInternalUse.


        :param hosts_used: The hosts_used of this StatsModelInternalUse.  # noqa: E501
        :type: int
        """

        self._hosts_used = hosts_used

    @property
    def keys(self):
        """Gets the keys of this StatsModelInternalUse.  # noqa: E501


        :return: The keys of this StatsModelInternalUse.  # noqa: E501
        :rtype: int
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this StatsModelInternalUse.


        :param keys: The keys of this StatsModelInternalUse.  # noqa: E501
        :type: int
        """

        self._keys = keys

    @property
    def latency(self):
        """Gets the latency of this StatsModelInternalUse.  # noqa: E501


        :return: The latency of this StatsModelInternalUse.  # noqa: E501
        :rtype: int
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this StatsModelInternalUse.


        :param latency: The latency of this StatsModelInternalUse.  # noqa: E501
        :type: int
        """

        self._latency = latency

    @property
    def metrics_used(self):
        """Gets the metrics_used of this StatsModelInternalUse.  # noqa: E501


        :return: The metrics_used of this StatsModelInternalUse.  # noqa: E501
        :rtype: int
        """
        return self._metrics_used

    @metrics_used.setter
    def metrics_used(self, metrics_used):
        """Sets the metrics_used of this StatsModelInternalUse.


        :param metrics_used: The metrics_used of this StatsModelInternalUse.  # noqa: E501
        :type: int
        """

        self._metrics_used = metrics_used

    @property
    def points(self):
        """Gets the points of this StatsModelInternalUse.  # noqa: E501


        :return: The points of this StatsModelInternalUse.  # noqa: E501
        :rtype: int
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this StatsModelInternalUse.


        :param points: The points of this StatsModelInternalUse.  # noqa: E501
        :type: int
        """

        self._points = points

    @property
    def queries(self):
        """Gets the queries of this StatsModelInternalUse.  # noqa: E501


        :return: The queries of this StatsModelInternalUse.  # noqa: E501
        :rtype: int
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this StatsModelInternalUse.


        :param queries: The queries of this StatsModelInternalUse.  # noqa: E501
        :type: int
        """

        self._queries = queries

    @property
    def query_tasks(self):
        """Gets the query_tasks of this StatsModelInternalUse.  # noqa: E501


        :return: The query_tasks of this StatsModelInternalUse.  # noqa: E501
        :rtype: int
        """
        return self._query_tasks

    @query_tasks.setter
    def query_tasks(self, query_tasks):
        """Sets the query_tasks of this StatsModelInternalUse.


        :param query_tasks: The query_tasks of this StatsModelInternalUse.  # noqa: E501
        :type: int
        """

        self._query_tasks = query_tasks

    @property
    def s3_keys(self):
        """Gets the s3_keys of this StatsModelInternalUse.  # noqa: E501


        :return: The s3_keys of this StatsModelInternalUse.  # noqa: E501
        :rtype: int
        """
        return self._s3_keys

    @s3_keys.setter
    def s3_keys(self, s3_keys):
        """Sets the s3_keys of this StatsModelInternalUse.


        :param s3_keys: The s3_keys of this StatsModelInternalUse.  # noqa: E501
        :type: int
        """

        self._s3_keys = s3_keys

    @property
    def skipped_compacted_keys(self):
        """Gets the skipped_compacted_keys of this StatsModelInternalUse.  # noqa: E501


        :return: The skipped_compacted_keys of this StatsModelInternalUse.  # noqa: E501
        :rtype: int
        """
        return self._skipped_compacted_keys

    @skipped_compacted_keys.setter
    def skipped_compacted_keys(self, skipped_compacted_keys):
        """Sets the skipped_compacted_keys of this StatsModelInternalUse.


        :param skipped_compacted_keys: The skipped_compacted_keys of this StatsModelInternalUse.  # noqa: E501
        :type: int
        """

        self._skipped_compacted_keys = skipped_compacted_keys

    @property
    def summaries(self):
        """Gets the summaries of this StatsModelInternalUse.  # noqa: E501


        :return: The summaries of this StatsModelInternalUse.  # noqa: E501
        :rtype: int
        """
        return self._summaries

    @summaries.setter
    def summaries(self, summaries):
        """Sets the summaries of this StatsModelInternalUse.


        :param summaries: The summaries of this StatsModelInternalUse.  # noqa: E501
        :type: int
        """

        self._summaries = summaries

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StatsModelInternalUse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StatsModelInternalUse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
