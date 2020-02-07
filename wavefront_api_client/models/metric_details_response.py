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


class MetricDetailsResponse(object):
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
        'continuation_token': 'str',
        'hosts': 'list[MetricDetails]'
    }

    attribute_map = {
        'continuation_token': 'continuationToken',
        'hosts': 'hosts'
    }

    def __init__(self, continuation_token=None, hosts=None):  # noqa: E501
        """MetricDetailsResponse - a model defined in Swagger"""  # noqa: E501

        self._continuation_token = None
        self._hosts = None
        self.discriminator = None

        if continuation_token is not None:
            self.continuation_token = continuation_token
        if hosts is not None:
            self.hosts = hosts

    @property
    def continuation_token(self):
        """Gets the continuation_token of this MetricDetailsResponse.  # noqa: E501

        Token used for pagination of results  # noqa: E501

        :return: The continuation_token of this MetricDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._continuation_token

    @continuation_token.setter
    def continuation_token(self, continuation_token):
        """Sets the continuation_token of this MetricDetailsResponse.

        Token used for pagination of results  # noqa: E501

        :param continuation_token: The continuation_token of this MetricDetailsResponse.  # noqa: E501
        :type: str
        """

        self._continuation_token = continuation_token

    @property
    def hosts(self):
        """Gets the hosts of this MetricDetailsResponse.  # noqa: E501

        List of sources/hosts reporting this metric  # noqa: E501

        :return: The hosts of this MetricDetailsResponse.  # noqa: E501
        :rtype: list[MetricDetails]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this MetricDetailsResponse.

        List of sources/hosts reporting this metric  # noqa: E501

        :param hosts: The hosts of this MetricDetailsResponse.  # noqa: E501
        :type: list[MetricDetails]
        """

        self._hosts = hosts

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
        if issubclass(MetricDetailsResponse, dict):
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
        if not isinstance(other, MetricDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
