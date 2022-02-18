# coding: utf-8

"""
    Wavefront REST API Documentation

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wavefront_api_client.configuration import Configuration


class Trace(object):
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
        'end_ms': 'int',
        'spans': 'list[Span]',
        'start_ms': 'int',
        'total_duration_ms': 'int',
        'trace_id': 'str'
    }

    attribute_map = {
        'end_ms': 'end_ms',
        'spans': 'spans',
        'start_ms': 'start_ms',
        'total_duration_ms': 'total_duration_ms',
        'trace_id': 'traceId'
    }

    def __init__(self, end_ms=None, spans=None, start_ms=None, total_duration_ms=None, trace_id=None, _configuration=None):  # noqa: E501
        """Trace - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._end_ms = None
        self._spans = None
        self._start_ms = None
        self._total_duration_ms = None
        self._trace_id = None
        self.discriminator = None

        if end_ms is not None:
            self.end_ms = end_ms
        if spans is not None:
            self.spans = spans
        if start_ms is not None:
            self.start_ms = start_ms
        if total_duration_ms is not None:
            self.total_duration_ms = total_duration_ms
        if trace_id is not None:
            self.trace_id = trace_id

    @property
    def end_ms(self):
        """Gets the end_ms of this Trace.  # noqa: E501

        Trace end time (in milliseconds)  # noqa: E501

        :return: The end_ms of this Trace.  # noqa: E501
        :rtype: int
        """
        return self._end_ms

    @end_ms.setter
    def end_ms(self, end_ms):
        """Sets the end_ms of this Trace.

        Trace end time (in milliseconds)  # noqa: E501

        :param end_ms: The end_ms of this Trace.  # noqa: E501
        :type: int
        """

        self._end_ms = end_ms

    @property
    def spans(self):
        """Gets the spans of this Trace.  # noqa: E501

        Spans associated with this trace  # noqa: E501

        :return: The spans of this Trace.  # noqa: E501
        :rtype: list[Span]
        """
        return self._spans

    @spans.setter
    def spans(self, spans):
        """Sets the spans of this Trace.

        Spans associated with this trace  # noqa: E501

        :param spans: The spans of this Trace.  # noqa: E501
        :type: list[Span]
        """

        self._spans = spans

    @property
    def start_ms(self):
        """Gets the start_ms of this Trace.  # noqa: E501

        Trace start time (in milliseconds)  # noqa: E501

        :return: The start_ms of this Trace.  # noqa: E501
        :rtype: int
        """
        return self._start_ms

    @start_ms.setter
    def start_ms(self, start_ms):
        """Sets the start_ms of this Trace.

        Trace start time (in milliseconds)  # noqa: E501

        :param start_ms: The start_ms of this Trace.  # noqa: E501
        :type: int
        """

        self._start_ms = start_ms

    @property
    def total_duration_ms(self):
        """Gets the total_duration_ms of this Trace.  # noqa: E501

        Trace total duration (in milliseconds)  # noqa: E501

        :return: The total_duration_ms of this Trace.  # noqa: E501
        :rtype: int
        """
        return self._total_duration_ms

    @total_duration_ms.setter
    def total_duration_ms(self, total_duration_ms):
        """Sets the total_duration_ms of this Trace.

        Trace total duration (in milliseconds)  # noqa: E501

        :param total_duration_ms: The total_duration_ms of this Trace.  # noqa: E501
        :type: int
        """

        self._total_duration_ms = total_duration_ms

    @property
    def trace_id(self):
        """Gets the trace_id of this Trace.  # noqa: E501

        Trace ID  # noqa: E501

        :return: The trace_id of this Trace.  # noqa: E501
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this Trace.

        Trace ID  # noqa: E501

        :param trace_id: The trace_id of this Trace.  # noqa: E501
        :type: str
        """

        self._trace_id = trace_id

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
        if issubclass(Trace, dict):
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
        if not isinstance(other, Trace):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Trace):
            return True

        return self.to_dict() != other.to_dict()
