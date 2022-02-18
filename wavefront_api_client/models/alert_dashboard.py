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


class AlertDashboard(object):
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
        'dashboard_id': 'str',
        'description': 'str',
        'parameters': 'dict(str, dict(str, str))'
    }

    attribute_map = {
        'dashboard_id': 'dashboardId',
        'description': 'description',
        'parameters': 'parameters'
    }

    def __init__(self, dashboard_id=None, description=None, parameters=None, _configuration=None):  # noqa: E501
        """AlertDashboard - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dashboard_id = None
        self._description = None
        self._parameters = None
        self.discriminator = None

        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if description is not None:
            self.description = description
        if parameters is not None:
            self.parameters = parameters

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this AlertDashboard.  # noqa: E501


        :return: The dashboard_id of this AlertDashboard.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this AlertDashboard.


        :param dashboard_id: The dashboard_id of this AlertDashboard.  # noqa: E501
        :type: str
        """

        self._dashboard_id = dashboard_id

    @property
    def description(self):
        """Gets the description of this AlertDashboard.  # noqa: E501


        :return: The description of this AlertDashboard.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AlertDashboard.


        :param description: The description of this AlertDashboard.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def parameters(self):
        """Gets the parameters of this AlertDashboard.  # noqa: E501


        :return: The parameters of this AlertDashboard.  # noqa: E501
        :rtype: dict(str, dict(str, str))
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this AlertDashboard.


        :param parameters: The parameters of this AlertDashboard.  # noqa: E501
        :type: dict(str, dict(str, str))
        """

        self._parameters = parameters

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
        if issubclass(AlertDashboard, dict):
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
        if not isinstance(other, AlertDashboard):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertDashboard):
            return True

        return self.to_dict() != other.to_dict()
