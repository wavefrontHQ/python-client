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


class ResponseContainerPagedMonitoredCluster(object):
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
        'response': 'PagedMonitoredCluster',
        'status': 'ResponseStatus'
    }

    attribute_map = {
        'response': 'response',
        'status': 'status'
    }

    def __init__(self, response=None, status=None, _configuration=None):  # noqa: E501
        """ResponseContainerPagedMonitoredCluster - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._response = None
        self._status = None
        self.discriminator = None

        if response is not None:
            self.response = response
        self.status = status

    @property
    def response(self):
        """Gets the response of this ResponseContainerPagedMonitoredCluster.  # noqa: E501


        :return: The response of this ResponseContainerPagedMonitoredCluster.  # noqa: E501
        :rtype: PagedMonitoredCluster
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this ResponseContainerPagedMonitoredCluster.


        :param response: The response of this ResponseContainerPagedMonitoredCluster.  # noqa: E501
        :type: PagedMonitoredCluster
        """

        self._response = response

    @property
    def status(self):
        """Gets the status of this ResponseContainerPagedMonitoredCluster.  # noqa: E501


        :return: The status of this ResponseContainerPagedMonitoredCluster.  # noqa: E501
        :rtype: ResponseStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseContainerPagedMonitoredCluster.


        :param status: The status of this ResponseContainerPagedMonitoredCluster.  # noqa: E501
        :type: ResponseStatus
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if issubclass(ResponseContainerPagedMonitoredCluster, dict):
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
        if not isinstance(other, ResponseContainerPagedMonitoredCluster):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseContainerPagedMonitoredCluster):
            return True

        return self.to_dict() != other.to_dict()
