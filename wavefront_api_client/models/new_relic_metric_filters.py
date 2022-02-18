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


class NewRelicMetricFilters(object):
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
        'app_name': 'str',
        'metric_filter_regex': 'str'
    }

    attribute_map = {
        'app_name': 'appName',
        'metric_filter_regex': 'metricFilterRegex'
    }

    def __init__(self, app_name=None, metric_filter_regex=None, _configuration=None):  # noqa: E501
        """NewRelicMetricFilters - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._app_name = None
        self._metric_filter_regex = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if metric_filter_regex is not None:
            self.metric_filter_regex = metric_filter_regex

    @property
    def app_name(self):
        """Gets the app_name of this NewRelicMetricFilters.  # noqa: E501


        :return: The app_name of this NewRelicMetricFilters.  # noqa: E501
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this NewRelicMetricFilters.


        :param app_name: The app_name of this NewRelicMetricFilters.  # noqa: E501
        :type: str
        """

        self._app_name = app_name

    @property
    def metric_filter_regex(self):
        """Gets the metric_filter_regex of this NewRelicMetricFilters.  # noqa: E501


        :return: The metric_filter_regex of this NewRelicMetricFilters.  # noqa: E501
        :rtype: str
        """
        return self._metric_filter_regex

    @metric_filter_regex.setter
    def metric_filter_regex(self, metric_filter_regex):
        """Sets the metric_filter_regex of this NewRelicMetricFilters.


        :param metric_filter_regex: The metric_filter_regex of this NewRelicMetricFilters.  # noqa: E501
        :type: str
        """

        self._metric_filter_regex = metric_filter_regex

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
        if issubclass(NewRelicMetricFilters, dict):
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
        if not isinstance(other, NewRelicMetricFilters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewRelicMetricFilters):
            return True

        return self.to_dict() != other.to_dict()
