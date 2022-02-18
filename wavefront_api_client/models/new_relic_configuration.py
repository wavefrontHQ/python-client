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


class NewRelicConfiguration(object):
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
        'api_key': 'str',
        'app_filter_regex': 'str',
        'host_filter_regex': 'str',
        'new_relic_metric_filters': 'list[NewRelicMetricFilters]'
    }

    attribute_map = {
        'api_key': 'apiKey',
        'app_filter_regex': 'appFilterRegex',
        'host_filter_regex': 'hostFilterRegex',
        'new_relic_metric_filters': 'newRelicMetricFilters'
    }

    def __init__(self, api_key=None, app_filter_regex=None, host_filter_regex=None, new_relic_metric_filters=None, _configuration=None):  # noqa: E501
        """NewRelicConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._api_key = None
        self._app_filter_regex = None
        self._host_filter_regex = None
        self._new_relic_metric_filters = None
        self.discriminator = None

        self.api_key = api_key
        if app_filter_regex is not None:
            self.app_filter_regex = app_filter_regex
        if host_filter_regex is not None:
            self.host_filter_regex = host_filter_regex
        if new_relic_metric_filters is not None:
            self.new_relic_metric_filters = new_relic_metric_filters

    @property
    def api_key(self):
        """Gets the api_key of this NewRelicConfiguration.  # noqa: E501

        New Relic REST API Key.  # noqa: E501

        :return: The api_key of this NewRelicConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this NewRelicConfiguration.

        New Relic REST API Key.  # noqa: E501

        :param api_key: The api_key of this NewRelicConfiguration.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and api_key is None:
            raise ValueError("Invalid value for `api_key`, must not be `None`")  # noqa: E501

        self._api_key = api_key

    @property
    def app_filter_regex(self):
        """Gets the app_filter_regex of this NewRelicConfiguration.  # noqa: E501

        A regular expression that a application name must match (case-insensitively) in order to collect metrics.  # noqa: E501

        :return: The app_filter_regex of this NewRelicConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._app_filter_regex

    @app_filter_regex.setter
    def app_filter_regex(self, app_filter_regex):
        """Sets the app_filter_regex of this NewRelicConfiguration.

        A regular expression that a application name must match (case-insensitively) in order to collect metrics.  # noqa: E501

        :param app_filter_regex: The app_filter_regex of this NewRelicConfiguration.  # noqa: E501
        :type: str
        """

        self._app_filter_regex = app_filter_regex

    @property
    def host_filter_regex(self):
        """Gets the host_filter_regex of this NewRelicConfiguration.  # noqa: E501

        A regular expression that a host name must match (case-insensitively) in order to collect metrics.  # noqa: E501

        :return: The host_filter_regex of this NewRelicConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._host_filter_regex

    @host_filter_regex.setter
    def host_filter_regex(self, host_filter_regex):
        """Sets the host_filter_regex of this NewRelicConfiguration.

        A regular expression that a host name must match (case-insensitively) in order to collect metrics.  # noqa: E501

        :param host_filter_regex: The host_filter_regex of this NewRelicConfiguration.  # noqa: E501
        :type: str
        """

        self._host_filter_regex = host_filter_regex

    @property
    def new_relic_metric_filters(self):
        """Gets the new_relic_metric_filters of this NewRelicConfiguration.  # noqa: E501

        Application specific metric filter  # noqa: E501

        :return: The new_relic_metric_filters of this NewRelicConfiguration.  # noqa: E501
        :rtype: list[NewRelicMetricFilters]
        """
        return self._new_relic_metric_filters

    @new_relic_metric_filters.setter
    def new_relic_metric_filters(self, new_relic_metric_filters):
        """Sets the new_relic_metric_filters of this NewRelicConfiguration.

        Application specific metric filter  # noqa: E501

        :param new_relic_metric_filters: The new_relic_metric_filters of this NewRelicConfiguration.  # noqa: E501
        :type: list[NewRelicMetricFilters]
        """

        self._new_relic_metric_filters = new_relic_metric_filters

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
        if issubclass(NewRelicConfiguration, dict):
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
        if not isinstance(other, NewRelicConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewRelicConfiguration):
            return True

        return self.to_dict() != other.to_dict()
