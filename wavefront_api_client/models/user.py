# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: support@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wavefront_api_client.models.user_settings import UserSettings  # noqa: F401,E501


class User(object):
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
        'api_token': 'str',
        'api_token2': 'str',
        'credential': 'str',
        'customer': 'str',
        'groups': 'list[str]',
        'identifier': 'str',
        'invalid_password_attempts': 'int',
        'last_logout': 'int',
        'last_successful_login': 'int',
        'onboarding_state': 'str',
        'provider': 'str',
        'reset_token': 'str',
        'reset_token_creation_millis': 'int',
        'settings': 'UserSettings',
        'sso_id': 'str',
        'super_admin': 'bool',
        'user_groups': 'list[str]'
    }

    attribute_map = {
        'api_token': 'apiToken',
        'api_token2': 'apiToken2',
        'credential': 'credential',
        'customer': 'customer',
        'groups': 'groups',
        'identifier': 'identifier',
        'invalid_password_attempts': 'invalidPasswordAttempts',
        'last_logout': 'lastLogout',
        'last_successful_login': 'lastSuccessfulLogin',
        'onboarding_state': 'onboardingState',
        'provider': 'provider',
        'reset_token': 'resetToken',
        'reset_token_creation_millis': 'resetTokenCreationMillis',
        'settings': 'settings',
        'sso_id': 'ssoId',
        'super_admin': 'superAdmin',
        'user_groups': 'userGroups'
    }

    def __init__(self, api_token=None, api_token2=None, credential=None, customer=None, groups=None, identifier=None, invalid_password_attempts=None, last_logout=None, last_successful_login=None, onboarding_state=None, provider=None, reset_token=None, reset_token_creation_millis=None, settings=None, sso_id=None, super_admin=None, user_groups=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501

        self._api_token = None
        self._api_token2 = None
        self._credential = None
        self._customer = None
        self._groups = None
        self._identifier = None
        self._invalid_password_attempts = None
        self._last_logout = None
        self._last_successful_login = None
        self._onboarding_state = None
        self._provider = None
        self._reset_token = None
        self._reset_token_creation_millis = None
        self._settings = None
        self._sso_id = None
        self._super_admin = None
        self._user_groups = None
        self.discriminator = None

        if api_token is not None:
            self.api_token = api_token
        if api_token2 is not None:
            self.api_token2 = api_token2
        if credential is not None:
            self.credential = credential
        if customer is not None:
            self.customer = customer
        if groups is not None:
            self.groups = groups
        if identifier is not None:
            self.identifier = identifier
        if invalid_password_attempts is not None:
            self.invalid_password_attempts = invalid_password_attempts
        if last_logout is not None:
            self.last_logout = last_logout
        if last_successful_login is not None:
            self.last_successful_login = last_successful_login
        if onboarding_state is not None:
            self.onboarding_state = onboarding_state
        if provider is not None:
            self.provider = provider
        if reset_token is not None:
            self.reset_token = reset_token
        if reset_token_creation_millis is not None:
            self.reset_token_creation_millis = reset_token_creation_millis
        if settings is not None:
            self.settings = settings
        if sso_id is not None:
            self.sso_id = sso_id
        if super_admin is not None:
            self.super_admin = super_admin
        if user_groups is not None:
            self.user_groups = user_groups

    @property
    def api_token(self):
        """Gets the api_token of this User.  # noqa: E501


        :return: The api_token of this User.  # noqa: E501
        :rtype: str
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token):
        """Sets the api_token of this User.


        :param api_token: The api_token of this User.  # noqa: E501
        :type: str
        """

        self._api_token = api_token

    @property
    def api_token2(self):
        """Gets the api_token2 of this User.  # noqa: E501


        :return: The api_token2 of this User.  # noqa: E501
        :rtype: str
        """
        return self._api_token2

    @api_token2.setter
    def api_token2(self, api_token2):
        """Sets the api_token2 of this User.


        :param api_token2: The api_token2 of this User.  # noqa: E501
        :type: str
        """

        self._api_token2 = api_token2

    @property
    def credential(self):
        """Gets the credential of this User.  # noqa: E501


        :return: The credential of this User.  # noqa: E501
        :rtype: str
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        """Sets the credential of this User.


        :param credential: The credential of this User.  # noqa: E501
        :type: str
        """

        self._credential = credential

    @property
    def customer(self):
        """Gets the customer of this User.  # noqa: E501


        :return: The customer of this User.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this User.


        :param customer: The customer of this User.  # noqa: E501
        :type: str
        """

        self._customer = customer

    @property
    def groups(self):
        """Gets the groups of this User.  # noqa: E501


        :return: The groups of this User.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this User.


        :param groups: The groups of this User.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def identifier(self):
        """Gets the identifier of this User.  # noqa: E501


        :return: The identifier of this User.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this User.


        :param identifier: The identifier of this User.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def invalid_password_attempts(self):
        """Gets the invalid_password_attempts of this User.  # noqa: E501


        :return: The invalid_password_attempts of this User.  # noqa: E501
        :rtype: int
        """
        return self._invalid_password_attempts

    @invalid_password_attempts.setter
    def invalid_password_attempts(self, invalid_password_attempts):
        """Sets the invalid_password_attempts of this User.


        :param invalid_password_attempts: The invalid_password_attempts of this User.  # noqa: E501
        :type: int
        """

        self._invalid_password_attempts = invalid_password_attempts

    @property
    def last_logout(self):
        """Gets the last_logout of this User.  # noqa: E501


        :return: The last_logout of this User.  # noqa: E501
        :rtype: int
        """
        return self._last_logout

    @last_logout.setter
    def last_logout(self, last_logout):
        """Sets the last_logout of this User.


        :param last_logout: The last_logout of this User.  # noqa: E501
        :type: int
        """

        self._last_logout = last_logout

    @property
    def last_successful_login(self):
        """Gets the last_successful_login of this User.  # noqa: E501


        :return: The last_successful_login of this User.  # noqa: E501
        :rtype: int
        """
        return self._last_successful_login

    @last_successful_login.setter
    def last_successful_login(self, last_successful_login):
        """Sets the last_successful_login of this User.


        :param last_successful_login: The last_successful_login of this User.  # noqa: E501
        :type: int
        """

        self._last_successful_login = last_successful_login

    @property
    def onboarding_state(self):
        """Gets the onboarding_state of this User.  # noqa: E501


        :return: The onboarding_state of this User.  # noqa: E501
        :rtype: str
        """
        return self._onboarding_state

    @onboarding_state.setter
    def onboarding_state(self, onboarding_state):
        """Sets the onboarding_state of this User.


        :param onboarding_state: The onboarding_state of this User.  # noqa: E501
        :type: str
        """

        self._onboarding_state = onboarding_state

    @property
    def provider(self):
        """Gets the provider of this User.  # noqa: E501


        :return: The provider of this User.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this User.


        :param provider: The provider of this User.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def reset_token(self):
        """Gets the reset_token of this User.  # noqa: E501


        :return: The reset_token of this User.  # noqa: E501
        :rtype: str
        """
        return self._reset_token

    @reset_token.setter
    def reset_token(self, reset_token):
        """Sets the reset_token of this User.


        :param reset_token: The reset_token of this User.  # noqa: E501
        :type: str
        """

        self._reset_token = reset_token

    @property
    def reset_token_creation_millis(self):
        """Gets the reset_token_creation_millis of this User.  # noqa: E501


        :return: The reset_token_creation_millis of this User.  # noqa: E501
        :rtype: int
        """
        return self._reset_token_creation_millis

    @reset_token_creation_millis.setter
    def reset_token_creation_millis(self, reset_token_creation_millis):
        """Sets the reset_token_creation_millis of this User.


        :param reset_token_creation_millis: The reset_token_creation_millis of this User.  # noqa: E501
        :type: int
        """

        self._reset_token_creation_millis = reset_token_creation_millis

    @property
    def settings(self):
        """Gets the settings of this User.  # noqa: E501


        :return: The settings of this User.  # noqa: E501
        :rtype: UserSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this User.


        :param settings: The settings of this User.  # noqa: E501
        :type: UserSettings
        """

        self._settings = settings

    @property
    def sso_id(self):
        """Gets the sso_id of this User.  # noqa: E501


        :return: The sso_id of this User.  # noqa: E501
        :rtype: str
        """
        return self._sso_id

    @sso_id.setter
    def sso_id(self, sso_id):
        """Sets the sso_id of this User.


        :param sso_id: The sso_id of this User.  # noqa: E501
        :type: str
        """

        self._sso_id = sso_id

    @property
    def super_admin(self):
        """Gets the super_admin of this User.  # noqa: E501


        :return: The super_admin of this User.  # noqa: E501
        :rtype: bool
        """
        return self._super_admin

    @super_admin.setter
    def super_admin(self, super_admin):
        """Sets the super_admin of this User.


        :param super_admin: The super_admin of this User.  # noqa: E501
        :type: bool
        """

        self._super_admin = super_admin

    @property
    def user_groups(self):
        """Gets the user_groups of this User.  # noqa: E501


        :return: The user_groups of this User.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        """Sets the user_groups of this User.


        :param user_groups: The user_groups of this User.  # noqa: E501
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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
