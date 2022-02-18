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


class CustomerFacingUserObject(object):
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
        'escaped_identifier': 'str',
        'gravatar_url': 'str',
        'groups': 'list[str]',
        'id': 'str',
        'identifier': 'str',
        'ingestion_policy_id': 'str',
        'last_successful_login': 'int',
        '_self': 'bool',
        'united_permissions': 'list[str]',
        'united_roles': 'list[str]',
        'user_groups': 'list[str]'
    }

    attribute_map = {
        'customer': 'customer',
        'escaped_identifier': 'escapedIdentifier',
        'gravatar_url': 'gravatarUrl',
        'groups': 'groups',
        'id': 'id',
        'identifier': 'identifier',
        'ingestion_policy_id': 'ingestionPolicyId',
        'last_successful_login': 'lastSuccessfulLogin',
        '_self': 'self',
        'united_permissions': 'unitedPermissions',
        'united_roles': 'unitedRoles',
        'user_groups': 'userGroups'
    }

    def __init__(self, customer=None, escaped_identifier=None, gravatar_url=None, groups=None, id=None, identifier=None, ingestion_policy_id=None, last_successful_login=None, _self=None, united_permissions=None, united_roles=None, user_groups=None, _configuration=None):  # noqa: E501
        """CustomerFacingUserObject - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._customer = None
        self._escaped_identifier = None
        self._gravatar_url = None
        self._groups = None
        self._id = None
        self._identifier = None
        self._ingestion_policy_id = None
        self._last_successful_login = None
        self.__self = None
        self._united_permissions = None
        self._united_roles = None
        self._user_groups = None
        self.discriminator = None

        self.customer = customer
        if escaped_identifier is not None:
            self.escaped_identifier = escaped_identifier
        if gravatar_url is not None:
            self.gravatar_url = gravatar_url
        if groups is not None:
            self.groups = groups
        self.id = id
        self.identifier = identifier
        if ingestion_policy_id is not None:
            self.ingestion_policy_id = ingestion_policy_id
        if last_successful_login is not None:
            self.last_successful_login = last_successful_login
        self._self = _self
        if united_permissions is not None:
            self.united_permissions = united_permissions
        if united_roles is not None:
            self.united_roles = united_roles
        if user_groups is not None:
            self.user_groups = user_groups

    @property
    def customer(self):
        """Gets the customer of this CustomerFacingUserObject.  # noqa: E501

        The id of the customer to which the user belongs  # noqa: E501

        :return: The customer of this CustomerFacingUserObject.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this CustomerFacingUserObject.

        The id of the customer to which the user belongs  # noqa: E501

        :param customer: The customer of this CustomerFacingUserObject.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def escaped_identifier(self):
        """Gets the escaped_identifier of this CustomerFacingUserObject.  # noqa: E501

        URL Escaped Identifier  # noqa: E501

        :return: The escaped_identifier of this CustomerFacingUserObject.  # noqa: E501
        :rtype: str
        """
        return self._escaped_identifier

    @escaped_identifier.setter
    def escaped_identifier(self, escaped_identifier):
        """Sets the escaped_identifier of this CustomerFacingUserObject.

        URL Escaped Identifier  # noqa: E501

        :param escaped_identifier: The escaped_identifier of this CustomerFacingUserObject.  # noqa: E501
        :type: str
        """

        self._escaped_identifier = escaped_identifier

    @property
    def gravatar_url(self):
        """Gets the gravatar_url of this CustomerFacingUserObject.  # noqa: E501

        URL id For User's gravatar (see gravatar.com), if one exists.  # noqa: E501

        :return: The gravatar_url of this CustomerFacingUserObject.  # noqa: E501
        :rtype: str
        """
        return self._gravatar_url

    @gravatar_url.setter
    def gravatar_url(self, gravatar_url):
        """Sets the gravatar_url of this CustomerFacingUserObject.

        URL id For User's gravatar (see gravatar.com), if one exists.  # noqa: E501

        :param gravatar_url: The gravatar_url of this CustomerFacingUserObject.  # noqa: E501
        :type: str
        """

        self._gravatar_url = gravatar_url

    @property
    def groups(self):
        """Gets the groups of this CustomerFacingUserObject.  # noqa: E501

        List of permission groups this user has been granted access to  # noqa: E501

        :return: The groups of this CustomerFacingUserObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this CustomerFacingUserObject.

        List of permission groups this user has been granted access to  # noqa: E501

        :param groups: The groups of this CustomerFacingUserObject.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def id(self):
        """Gets the id of this CustomerFacingUserObject.  # noqa: E501

        The unique identifier of this user, which should be their valid email address  # noqa: E501

        :return: The id of this CustomerFacingUserObject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomerFacingUserObject.

        The unique identifier of this user, which should be their valid email address  # noqa: E501

        :param id: The id of this CustomerFacingUserObject.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def identifier(self):
        """Gets the identifier of this CustomerFacingUserObject.  # noqa: E501

        The unique identifier of this user, which should be their valid email address  # noqa: E501

        :return: The identifier of this CustomerFacingUserObject.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this CustomerFacingUserObject.

        The unique identifier of this user, which should be their valid email address  # noqa: E501

        :param identifier: The identifier of this CustomerFacingUserObject.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def ingestion_policy_id(self):
        """Gets the ingestion_policy_id of this CustomerFacingUserObject.  # noqa: E501

        The identifier of the ingestion policy linked with user.  # noqa: E501

        :return: The ingestion_policy_id of this CustomerFacingUserObject.  # noqa: E501
        :rtype: str
        """
        return self._ingestion_policy_id

    @ingestion_policy_id.setter
    def ingestion_policy_id(self, ingestion_policy_id):
        """Sets the ingestion_policy_id of this CustomerFacingUserObject.

        The identifier of the ingestion policy linked with user.  # noqa: E501

        :param ingestion_policy_id: The ingestion_policy_id of this CustomerFacingUserObject.  # noqa: E501
        :type: str
        """

        self._ingestion_policy_id = ingestion_policy_id

    @property
    def last_successful_login(self):
        """Gets the last_successful_login of this CustomerFacingUserObject.  # noqa: E501

        The last time the user logged in, in epoch milliseconds  # noqa: E501

        :return: The last_successful_login of this CustomerFacingUserObject.  # noqa: E501
        :rtype: int
        """
        return self._last_successful_login

    @last_successful_login.setter
    def last_successful_login(self, last_successful_login):
        """Sets the last_successful_login of this CustomerFacingUserObject.

        The last time the user logged in, in epoch milliseconds  # noqa: E501

        :param last_successful_login: The last_successful_login of this CustomerFacingUserObject.  # noqa: E501
        :type: int
        """

        self._last_successful_login = last_successful_login

    @property
    def _self(self):
        """Gets the _self of this CustomerFacingUserObject.  # noqa: E501

        Whether this user is the one calling the API  # noqa: E501

        :return: The _self of this CustomerFacingUserObject.  # noqa: E501
        :rtype: bool
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this CustomerFacingUserObject.

        Whether this user is the one calling the API  # noqa: E501

        :param _self: The _self of this CustomerFacingUserObject.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and _self is None:
            raise ValueError("Invalid value for `_self`, must not be `None`")  # noqa: E501

        self.__self = _self

    @property
    def united_permissions(self):
        """Gets the united_permissions of this CustomerFacingUserObject.  # noqa: E501

        The list of account's permissions assigned directly or through united roles assigned to it  # noqa: E501

        :return: The united_permissions of this CustomerFacingUserObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._united_permissions

    @united_permissions.setter
    def united_permissions(self, united_permissions):
        """Sets the united_permissions of this CustomerFacingUserObject.

        The list of account's permissions assigned directly or through united roles assigned to it  # noqa: E501

        :param united_permissions: The united_permissions of this CustomerFacingUserObject.  # noqa: E501
        :type: list[str]
        """

        self._united_permissions = united_permissions

    @property
    def united_roles(self):
        """Gets the united_roles of this CustomerFacingUserObject.  # noqa: E501

        The list of account's roles assigned directly or through user groups assigned to it  # noqa: E501

        :return: The united_roles of this CustomerFacingUserObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._united_roles

    @united_roles.setter
    def united_roles(self, united_roles):
        """Sets the united_roles of this CustomerFacingUserObject.

        The list of account's roles assigned directly or through user groups assigned to it  # noqa: E501

        :param united_roles: The united_roles of this CustomerFacingUserObject.  # noqa: E501
        :type: list[str]
        """

        self._united_roles = united_roles

    @property
    def user_groups(self):
        """Gets the user_groups of this CustomerFacingUserObject.  # noqa: E501

        List of user group identifiers this user belongs to  # noqa: E501

        :return: The user_groups of this CustomerFacingUserObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        """Sets the user_groups of this CustomerFacingUserObject.

        List of user group identifiers this user belongs to  # noqa: E501

        :param user_groups: The user_groups of this CustomerFacingUserObject.  # noqa: E501
        :type: list[str]
        """

        self._user_groups = user_groups

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
        if issubclass(CustomerFacingUserObject, dict):
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
        if not isinstance(other, CustomerFacingUserObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerFacingUserObject):
            return True

        return self.to_dict() != other.to_dict()
