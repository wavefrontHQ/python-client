# coding: utf-8

"""
    Wavefront REST API Documentation

    <p>The REST API enables you to interact with the Wavefront service by using standard REST API tools. You can use the REST API to automate commonly executed operations, for example to tag sources automatically.</p><p>When you make REST API calls outside the REST API documentation UI, to authenticate to the service, you must use an API token associated with a user account or a service account. For information on how to get the API token and examples, see <a href=\"http://docs.wavefront.com/using_wavefront_api.html\">Use the Wavefront REST API.</a></p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wavefront_api_client.configuration import Configuration


class RolePropertiesDTO(object):
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
        'deletable': 'bool',
        'name_editable': 'bool',
        'perms_editable': 'bool',
        'users_addable': 'bool',
        'users_removable': 'bool'
    }

    attribute_map = {
        'deletable': 'deletable',
        'name_editable': 'nameEditable',
        'perms_editable': 'permsEditable',
        'users_addable': 'usersAddable',
        'users_removable': 'usersRemovable'
    }

    def __init__(self, deletable=None, name_editable=None, perms_editable=None, users_addable=None, users_removable=None, _configuration=None):  # noqa: E501
        """RolePropertiesDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._deletable = None
        self._name_editable = None
        self._perms_editable = None
        self._users_addable = None
        self._users_removable = None
        self.discriminator = None

        if deletable is not None:
            self.deletable = deletable
        if name_editable is not None:
            self.name_editable = name_editable
        if perms_editable is not None:
            self.perms_editable = perms_editable
        if users_addable is not None:
            self.users_addable = users_addable
        if users_removable is not None:
            self.users_removable = users_removable

    @property
    def deletable(self):
        """Gets the deletable of this RolePropertiesDTO.  # noqa: E501


        :return: The deletable of this RolePropertiesDTO.  # noqa: E501
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        """Sets the deletable of this RolePropertiesDTO.


        :param deletable: The deletable of this RolePropertiesDTO.  # noqa: E501
        :type: bool
        """

        self._deletable = deletable

    @property
    def name_editable(self):
        """Gets the name_editable of this RolePropertiesDTO.  # noqa: E501


        :return: The name_editable of this RolePropertiesDTO.  # noqa: E501
        :rtype: bool
        """
        return self._name_editable

    @name_editable.setter
    def name_editable(self, name_editable):
        """Sets the name_editable of this RolePropertiesDTO.


        :param name_editable: The name_editable of this RolePropertiesDTO.  # noqa: E501
        :type: bool
        """

        self._name_editable = name_editable

    @property
    def perms_editable(self):
        """Gets the perms_editable of this RolePropertiesDTO.  # noqa: E501


        :return: The perms_editable of this RolePropertiesDTO.  # noqa: E501
        :rtype: bool
        """
        return self._perms_editable

    @perms_editable.setter
    def perms_editable(self, perms_editable):
        """Sets the perms_editable of this RolePropertiesDTO.


        :param perms_editable: The perms_editable of this RolePropertiesDTO.  # noqa: E501
        :type: bool
        """

        self._perms_editable = perms_editable

    @property
    def users_addable(self):
        """Gets the users_addable of this RolePropertiesDTO.  # noqa: E501


        :return: The users_addable of this RolePropertiesDTO.  # noqa: E501
        :rtype: bool
        """
        return self._users_addable

    @users_addable.setter
    def users_addable(self, users_addable):
        """Sets the users_addable of this RolePropertiesDTO.


        :param users_addable: The users_addable of this RolePropertiesDTO.  # noqa: E501
        :type: bool
        """

        self._users_addable = users_addable

    @property
    def users_removable(self):
        """Gets the users_removable of this RolePropertiesDTO.  # noqa: E501


        :return: The users_removable of this RolePropertiesDTO.  # noqa: E501
        :rtype: bool
        """
        return self._users_removable

    @users_removable.setter
    def users_removable(self, users_removable):
        """Sets the users_removable of this RolePropertiesDTO.


        :param users_removable: The users_removable of this RolePropertiesDTO.  # noqa: E501
        :type: bool
        """

        self._users_removable = users_removable

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
        if issubclass(RolePropertiesDTO, dict):
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
        if not isinstance(other, RolePropertiesDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RolePropertiesDTO):
            return True

        return self.to_dict() != other.to_dict()