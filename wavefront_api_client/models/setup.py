# coding: utf-8

"""
    Tanzu Observability REST API Documentation

    <p>The REST API enables you to interact with the Tanzu Observability service by using standard REST API tools. You can use the REST API to automate commonly executed operations, for example to tag sources automatically.</p><p>When you make REST API calls outside the REST API documentation UI, to authenticate to the service, you must use an API token associated with a user account or a service account. For information on how to get the API token and examples, see <a href=\"http://docs.wavefront.com/using_wavefront_api.html\">Use the Tanzu Observability REST API.</a></p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wavefront_api_client.configuration import Configuration


class Setup(object):
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
        'description': 'str',
        'file_path': 'str',
        'title': 'str',
        'type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'file_path': 'filePath',
        'title': 'title',
        'type': 'type'
    }

    def __init__(self, description=None, file_path=None, title=None, type=None, _configuration=None):  # noqa: E501
        """Setup - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._file_path = None
        self._title = None
        self._type = None
        self.discriminator = None

        self.description = description
        self.file_path = file_path
        if title is not None:
            self.title = title
        self.type = type

    @property
    def description(self):
        """Gets the description of this Setup.  # noqa: E501

        Setup description  # noqa: E501

        :return: The description of this Setup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Setup.

        Setup description  # noqa: E501

        :param description: The description of this Setup.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def file_path(self):
        """Gets the file_path of this Setup.  # noqa: E501

        Relative file path to the setup.md file  # noqa: E501

        :return: The file_path of this Setup.  # noqa: E501
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this Setup.

        Relative file path to the setup.md file  # noqa: E501

        :param file_path: The file_path of this Setup.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and file_path is None:
            raise ValueError("Invalid value for `file_path`, must not be `None`")  # noqa: E501

        self._file_path = file_path

    @property
    def title(self):
        """Gets the title of this Setup.  # noqa: E501

        Setup title  # noqa: E501

        :return: The title of this Setup.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Setup.

        Setup title  # noqa: E501

        :param title: The title of this Setup.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this Setup.  # noqa: E501

        Setup Type  # noqa: E501

        :return: The type of this Setup.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Setup.

        Setup Type  # noqa: E501

        :param type: The type of this Setup.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["METRICS", "LOGS"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(Setup, dict):
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
        if not isinstance(other, Setup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Setup):
            return True

        return self.to_dict() != other.to_dict()
