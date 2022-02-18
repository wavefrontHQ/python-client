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


class UserGroup(object):
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
        'customer': 'str',
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'properties': 'UserGroupPropertiesDTO',
        'roles': 'list[RoleDTO]',
        'user_count': 'int',
        'users': 'list[str]'
    }

    attribute_map = {
        'customer': 'customer',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'properties': 'properties',
        'roles': 'roles',
        'user_count': 'userCount',
        'users': 'users'
    }

    def __init__(self, customer=None, description=None, id=None, name=None, properties=None, roles=None, user_count=None, users=None, _configuration=None):  # noqa: E501
        """UserGroup - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._customer = None
        self._description = None
        self._id = None
        self._name = None
        self._properties = None
        self._roles = None
        self._user_count = None
        self._users = None
        self.discriminator = None

        if customer is not None:
            self.customer = customer
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if properties is not None:
            self.properties = properties
        if roles is not None:
            self.roles = roles
        if user_count is not None:
            self.user_count = user_count
        if users is not None:
            self.users = users

    @property
    def customer(self):
        """Gets the customer of this UserGroup.  # noqa: E501

        ID of the customer to which the user group belongs  # noqa: E501

        :return: The customer of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this UserGroup.

        ID of the customer to which the user group belongs  # noqa: E501

        :param customer: The customer of this UserGroup.  # noqa: E501
        :type: str
        """

        self._customer = customer

    @property
    def description(self):
        """Gets the description of this UserGroup.  # noqa: E501

        The description of the user group  # noqa: E501

        :return: The description of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserGroup.

        The description of the user group  # noqa: E501

        :param description: The description of this UserGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this UserGroup.  # noqa: E501

        Unique ID for the user group  # noqa: E501

        :return: The id of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserGroup.

        Unique ID for the user group  # noqa: E501

        :param id: The id of this UserGroup.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this UserGroup.  # noqa: E501

        Name of the user group  # noqa: E501

        :return: The name of this UserGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserGroup.

        Name of the user group  # noqa: E501

        :param name: The name of this UserGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this UserGroup.  # noqa: E501

        The properties of the user group(name editable, users editable, etc.)  # noqa: E501

        :return: The properties of this UserGroup.  # noqa: E501
        :rtype: UserGroupPropertiesDTO
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UserGroup.

        The properties of the user group(name editable, users editable, etc.)  # noqa: E501

        :param properties: The properties of this UserGroup.  # noqa: E501
        :type: UserGroupPropertiesDTO
        """

        self._properties = properties

    @property
    def roles(self):
        """Gets the roles of this UserGroup.  # noqa: E501

        List of roles the user group has been linked to  # noqa: E501

        :return: The roles of this UserGroup.  # noqa: E501
        :rtype: list[RoleDTO]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserGroup.

        List of roles the user group has been linked to  # noqa: E501

        :param roles: The roles of this UserGroup.  # noqa: E501
        :type: list[RoleDTO]
        """

        self._roles = roles

    @property
    def user_count(self):
        """Gets the user_count of this UserGroup.  # noqa: E501

        Total number of users that are members of the user group  # noqa: E501

        :return: The user_count of this UserGroup.  # noqa: E501
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this UserGroup.

        Total number of users that are members of the user group  # noqa: E501

        :param user_count: The user_count of this UserGroup.  # noqa: E501
        :type: int
        """

        self._user_count = user_count

    @property
    def users(self):
        """Gets the users of this UserGroup.  # noqa: E501

        List of Users that are members of the user group. Maybe incomplete.  # noqa: E501

        :return: The users of this UserGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this UserGroup.

        List of Users that are members of the user group. Maybe incomplete.  # noqa: E501

        :param users: The users of this UserGroup.  # noqa: E501
        :type: list[str]
        """

        self._users = users

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
        if issubclass(UserGroup, dict):
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
        if not isinstance(other, UserGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserGroup):
            return True

        return self.to_dict() != other.to_dict()
