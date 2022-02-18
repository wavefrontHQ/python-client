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


class IngestionPolicy(object):
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
        'account_count': 'int',
        'customer': 'str',
        'description': 'str',
        'group_count': 'int',
        'id': 'str',
        'is_limited': 'bool',
        'last_updated_account_id': 'str',
        'last_updated_ms': 'int',
        'limit_pps': 'int',
        'name': 'str',
        'sampled_accounts': 'list[str]',
        'sampled_groups': 'list[UserGroup]',
        'sampled_service_accounts': 'list[str]',
        'sampled_user_accounts': 'list[str]',
        'scope': 'str',
        'service_account_count': 'int',
        'user_account_count': 'int'
    }

    attribute_map = {
        'account_count': 'accountCount',
        'customer': 'customer',
        'description': 'description',
        'group_count': 'groupCount',
        'id': 'id',
        'is_limited': 'isLimited',
        'last_updated_account_id': 'lastUpdatedAccountId',
        'last_updated_ms': 'lastUpdatedMs',
        'limit_pps': 'limitPPS',
        'name': 'name',
        'sampled_accounts': 'sampledAccounts',
        'sampled_groups': 'sampledGroups',
        'sampled_service_accounts': 'sampledServiceAccounts',
        'sampled_user_accounts': 'sampledUserAccounts',
        'scope': 'scope',
        'service_account_count': 'serviceAccountCount',
        'user_account_count': 'userAccountCount'
    }

    def __init__(self, account_count=None, customer=None, description=None, group_count=None, id=None, is_limited=None, last_updated_account_id=None, last_updated_ms=None, limit_pps=None, name=None, sampled_accounts=None, sampled_groups=None, sampled_service_accounts=None, sampled_user_accounts=None, scope=None, service_account_count=None, user_account_count=None, _configuration=None):  # noqa: E501
        """IngestionPolicy - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_count = None
        self._customer = None
        self._description = None
        self._group_count = None
        self._id = None
        self._is_limited = None
        self._last_updated_account_id = None
        self._last_updated_ms = None
        self._limit_pps = None
        self._name = None
        self._sampled_accounts = None
        self._sampled_groups = None
        self._sampled_service_accounts = None
        self._sampled_user_accounts = None
        self._scope = None
        self._service_account_count = None
        self._user_account_count = None
        self.discriminator = None

        if account_count is not None:
            self.account_count = account_count
        if customer is not None:
            self.customer = customer
        if description is not None:
            self.description = description
        if group_count is not None:
            self.group_count = group_count
        if id is not None:
            self.id = id
        if is_limited is not None:
            self.is_limited = is_limited
        if last_updated_account_id is not None:
            self.last_updated_account_id = last_updated_account_id
        if last_updated_ms is not None:
            self.last_updated_ms = last_updated_ms
        if limit_pps is not None:
            self.limit_pps = limit_pps
        if name is not None:
            self.name = name
        if sampled_accounts is not None:
            self.sampled_accounts = sampled_accounts
        if sampled_groups is not None:
            self.sampled_groups = sampled_groups
        if sampled_service_accounts is not None:
            self.sampled_service_accounts = sampled_service_accounts
        if sampled_user_accounts is not None:
            self.sampled_user_accounts = sampled_user_accounts
        if scope is not None:
            self.scope = scope
        if service_account_count is not None:
            self.service_account_count = service_account_count
        if user_account_count is not None:
            self.user_account_count = user_account_count

    @property
    def account_count(self):
        """Gets the account_count of this IngestionPolicy.  # noqa: E501

        Total number of accounts that are linked to the ingestion policy  # noqa: E501

        :return: The account_count of this IngestionPolicy.  # noqa: E501
        :rtype: int
        """
        return self._account_count

    @account_count.setter
    def account_count(self, account_count):
        """Sets the account_count of this IngestionPolicy.

        Total number of accounts that are linked to the ingestion policy  # noqa: E501

        :param account_count: The account_count of this IngestionPolicy.  # noqa: E501
        :type: int
        """

        self._account_count = account_count

    @property
    def customer(self):
        """Gets the customer of this IngestionPolicy.  # noqa: E501

        ID of the customer to which the ingestion policy belongs  # noqa: E501

        :return: The customer of this IngestionPolicy.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this IngestionPolicy.

        ID of the customer to which the ingestion policy belongs  # noqa: E501

        :param customer: The customer of this IngestionPolicy.  # noqa: E501
        :type: str
        """

        self._customer = customer

    @property
    def description(self):
        """Gets the description of this IngestionPolicy.  # noqa: E501

        The description of the ingestion policy  # noqa: E501

        :return: The description of this IngestionPolicy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IngestionPolicy.

        The description of the ingestion policy  # noqa: E501

        :param description: The description of this IngestionPolicy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def group_count(self):
        """Gets the group_count of this IngestionPolicy.  # noqa: E501

        Total number of groups that are linked to the ingestion policy  # noqa: E501

        :return: The group_count of this IngestionPolicy.  # noqa: E501
        :rtype: int
        """
        return self._group_count

    @group_count.setter
    def group_count(self, group_count):
        """Sets the group_count of this IngestionPolicy.

        Total number of groups that are linked to the ingestion policy  # noqa: E501

        :param group_count: The group_count of this IngestionPolicy.  # noqa: E501
        :type: int
        """

        self._group_count = group_count

    @property
    def id(self):
        """Gets the id of this IngestionPolicy.  # noqa: E501

        The unique ID for the ingestion policy  # noqa: E501

        :return: The id of this IngestionPolicy.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IngestionPolicy.

        The unique ID for the ingestion policy  # noqa: E501

        :param id: The id of this IngestionPolicy.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_limited(self):
        """Gets the is_limited of this IngestionPolicy.  # noqa: E501

        Whether the ingestion policy is limited  # noqa: E501

        :return: The is_limited of this IngestionPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._is_limited

    @is_limited.setter
    def is_limited(self, is_limited):
        """Sets the is_limited of this IngestionPolicy.

        Whether the ingestion policy is limited  # noqa: E501

        :param is_limited: The is_limited of this IngestionPolicy.  # noqa: E501
        :type: bool
        """

        self._is_limited = is_limited

    @property
    def last_updated_account_id(self):
        """Gets the last_updated_account_id of this IngestionPolicy.  # noqa: E501

        The account that updated this ingestion policy last time  # noqa: E501

        :return: The last_updated_account_id of this IngestionPolicy.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_account_id

    @last_updated_account_id.setter
    def last_updated_account_id(self, last_updated_account_id):
        """Sets the last_updated_account_id of this IngestionPolicy.

        The account that updated this ingestion policy last time  # noqa: E501

        :param last_updated_account_id: The last_updated_account_id of this IngestionPolicy.  # noqa: E501
        :type: str
        """

        self._last_updated_account_id = last_updated_account_id

    @property
    def last_updated_ms(self):
        """Gets the last_updated_ms of this IngestionPolicy.  # noqa: E501

        The last time when the ingestion policy is updated, in epoch milliseconds  # noqa: E501

        :return: The last_updated_ms of this IngestionPolicy.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_ms

    @last_updated_ms.setter
    def last_updated_ms(self, last_updated_ms):
        """Sets the last_updated_ms of this IngestionPolicy.

        The last time when the ingestion policy is updated, in epoch milliseconds  # noqa: E501

        :param last_updated_ms: The last_updated_ms of this IngestionPolicy.  # noqa: E501
        :type: int
        """

        self._last_updated_ms = last_updated_ms

    @property
    def limit_pps(self):
        """Gets the limit_pps of this IngestionPolicy.  # noqa: E501

        The PPS limit of the ingestion policy  # noqa: E501

        :return: The limit_pps of this IngestionPolicy.  # noqa: E501
        :rtype: int
        """
        return self._limit_pps

    @limit_pps.setter
    def limit_pps(self, limit_pps):
        """Sets the limit_pps of this IngestionPolicy.

        The PPS limit of the ingestion policy  # noqa: E501

        :param limit_pps: The limit_pps of this IngestionPolicy.  # noqa: E501
        :type: int
        """

        self._limit_pps = limit_pps

    @property
    def name(self):
        """Gets the name of this IngestionPolicy.  # noqa: E501

        The name of the ingestion policy  # noqa: E501

        :return: The name of this IngestionPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IngestionPolicy.

        The name of the ingestion policy  # noqa: E501

        :param name: The name of this IngestionPolicy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sampled_accounts(self):
        """Gets the sampled_accounts of this IngestionPolicy.  # noqa: E501

        A sample of the accounts assigned to this ingestion policy. Please use the Ingestion Policy facet of the Account Search API to get the full list of accounts for this policy  # noqa: E501

        :return: The sampled_accounts of this IngestionPolicy.  # noqa: E501
        :rtype: list[str]
        """
        return self._sampled_accounts

    @sampled_accounts.setter
    def sampled_accounts(self, sampled_accounts):
        """Sets the sampled_accounts of this IngestionPolicy.

        A sample of the accounts assigned to this ingestion policy. Please use the Ingestion Policy facet of the Account Search API to get the full list of accounts for this policy  # noqa: E501

        :param sampled_accounts: The sampled_accounts of this IngestionPolicy.  # noqa: E501
        :type: list[str]
        """

        self._sampled_accounts = sampled_accounts

    @property
    def sampled_groups(self):
        """Gets the sampled_groups of this IngestionPolicy.  # noqa: E501

        A sample of the groups assigned to this ingestion policy. Please use the Ingestion Policy facet of the Group Search API to get the full list of groups for this policy  # noqa: E501

        :return: The sampled_groups of this IngestionPolicy.  # noqa: E501
        :rtype: list[UserGroup]
        """
        return self._sampled_groups

    @sampled_groups.setter
    def sampled_groups(self, sampled_groups):
        """Sets the sampled_groups of this IngestionPolicy.

        A sample of the groups assigned to this ingestion policy. Please use the Ingestion Policy facet of the Group Search API to get the full list of groups for this policy  # noqa: E501

        :param sampled_groups: The sampled_groups of this IngestionPolicy.  # noqa: E501
        :type: list[UserGroup]
        """

        self._sampled_groups = sampled_groups

    @property
    def sampled_service_accounts(self):
        """Gets the sampled_service_accounts of this IngestionPolicy.  # noqa: E501

        A sample of the service accounts accounts assigned to this ingestion policy. Please use the Ingestion Policy facet of the Account Search API to get the full list of service accounts for this policy  # noqa: E501

        :return: The sampled_service_accounts of this IngestionPolicy.  # noqa: E501
        :rtype: list[str]
        """
        return self._sampled_service_accounts

    @sampled_service_accounts.setter
    def sampled_service_accounts(self, sampled_service_accounts):
        """Sets the sampled_service_accounts of this IngestionPolicy.

        A sample of the service accounts accounts assigned to this ingestion policy. Please use the Ingestion Policy facet of the Account Search API to get the full list of service accounts for this policy  # noqa: E501

        :param sampled_service_accounts: The sampled_service_accounts of this IngestionPolicy.  # noqa: E501
        :type: list[str]
        """

        self._sampled_service_accounts = sampled_service_accounts

    @property
    def sampled_user_accounts(self):
        """Gets the sampled_user_accounts of this IngestionPolicy.  # noqa: E501

        A sample of the user accounts assigned to this ingestion policy. Please use the Ingestion Policy facet of the Account Search API to get the full list of users for this policy  # noqa: E501

        :return: The sampled_user_accounts of this IngestionPolicy.  # noqa: E501
        :rtype: list[str]
        """
        return self._sampled_user_accounts

    @sampled_user_accounts.setter
    def sampled_user_accounts(self, sampled_user_accounts):
        """Sets the sampled_user_accounts of this IngestionPolicy.

        A sample of the user accounts assigned to this ingestion policy. Please use the Ingestion Policy facet of the Account Search API to get the full list of users for this policy  # noqa: E501

        :param sampled_user_accounts: The sampled_user_accounts of this IngestionPolicy.  # noqa: E501
        :type: list[str]
        """

        self._sampled_user_accounts = sampled_user_accounts

    @property
    def scope(self):
        """Gets the scope of this IngestionPolicy.  # noqa: E501

        The scope of the ingestion policy  # noqa: E501

        :return: The scope of this IngestionPolicy.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this IngestionPolicy.

        The scope of the ingestion policy  # noqa: E501

        :param scope: The scope of this IngestionPolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACCOUNT", "GROUP"]  # noqa: E501
        if (self._configuration.client_side_validation and
                scope not in allowed_values):
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

    @property
    def service_account_count(self):
        """Gets the service_account_count of this IngestionPolicy.  # noqa: E501

        Total number of service accounts that are linked to the ingestion policy  # noqa: E501

        :return: The service_account_count of this IngestionPolicy.  # noqa: E501
        :rtype: int
        """
        return self._service_account_count

    @service_account_count.setter
    def service_account_count(self, service_account_count):
        """Sets the service_account_count of this IngestionPolicy.

        Total number of service accounts that are linked to the ingestion policy  # noqa: E501

        :param service_account_count: The service_account_count of this IngestionPolicy.  # noqa: E501
        :type: int
        """

        self._service_account_count = service_account_count

    @property
    def user_account_count(self):
        """Gets the user_account_count of this IngestionPolicy.  # noqa: E501

        Total number of user accounts that are linked to the ingestion policy  # noqa: E501

        :return: The user_account_count of this IngestionPolicy.  # noqa: E501
        :rtype: int
        """
        return self._user_account_count

    @user_account_count.setter
    def user_account_count(self, user_account_count):
        """Sets the user_account_count of this IngestionPolicy.

        Total number of user accounts that are linked to the ingestion policy  # noqa: E501

        :param user_account_count: The user_account_count of this IngestionPolicy.  # noqa: E501
        :type: int
        """

        self._user_account_count = user_account_count

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
        if issubclass(IngestionPolicy, dict):
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
        if not isinstance(other, IngestionPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IngestionPolicy):
            return True

        return self.to_dict() != other.to_dict()
