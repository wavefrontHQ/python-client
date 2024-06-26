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


class IngestionPolicyReadModel(object):
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
        'accounts': 'list[AccessControlElement]',
        'alert': 'Alert',
        'customer': 'str',
        'description': 'str',
        'groups': 'list[AccessControlElement]',
        'id': 'str',
        'is_limited': 'bool',
        'last_updated_account_id': 'str',
        'last_updated_ms': 'int',
        'limit_pps': 'int',
        'metadata': 'IngestionPolicyMetadata',
        'name': 'str',
        'namespaces': 'list[str]',
        'point_tags': 'list[Annotation]',
        'scope': 'str',
        'sources': 'list[str]',
        'tags_anded': 'bool'
    }

    attribute_map = {
        'accounts': 'accounts',
        'alert': 'alert',
        'customer': 'customer',
        'description': 'description',
        'groups': 'groups',
        'id': 'id',
        'is_limited': 'isLimited',
        'last_updated_account_id': 'lastUpdatedAccountId',
        'last_updated_ms': 'lastUpdatedMs',
        'limit_pps': 'limitPPS',
        'metadata': 'metadata',
        'name': 'name',
        'namespaces': 'namespaces',
        'point_tags': 'pointTags',
        'scope': 'scope',
        'sources': 'sources',
        'tags_anded': 'tagsAnded'
    }

    def __init__(self, accounts=None, alert=None, customer=None, description=None, groups=None, id=None, is_limited=None, last_updated_account_id=None, last_updated_ms=None, limit_pps=None, metadata=None, name=None, namespaces=None, point_tags=None, scope=None, sources=None, tags_anded=None, _configuration=None):  # noqa: E501
        """IngestionPolicyReadModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accounts = None
        self._alert = None
        self._customer = None
        self._description = None
        self._groups = None
        self._id = None
        self._is_limited = None
        self._last_updated_account_id = None
        self._last_updated_ms = None
        self._limit_pps = None
        self._metadata = None
        self._name = None
        self._namespaces = None
        self._point_tags = None
        self._scope = None
        self._sources = None
        self._tags_anded = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts
        if alert is not None:
            self.alert = alert
        if customer is not None:
            self.customer = customer
        if description is not None:
            self.description = description
        if groups is not None:
            self.groups = groups
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
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if namespaces is not None:
            self.namespaces = namespaces
        if point_tags is not None:
            self.point_tags = point_tags
        if scope is not None:
            self.scope = scope
        if sources is not None:
            self.sources = sources
        if tags_anded is not None:
            self.tags_anded = tags_anded

    @property
    def accounts(self):
        """Gets the accounts of this IngestionPolicyReadModel.  # noqa: E501

        The accounts associated with the ingestion policy  # noqa: E501

        :return: The accounts of this IngestionPolicyReadModel.  # noqa: E501
        :rtype: list[AccessControlElement]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this IngestionPolicyReadModel.

        The accounts associated with the ingestion policy  # noqa: E501

        :param accounts: The accounts of this IngestionPolicyReadModel.  # noqa: E501
        :type: list[AccessControlElement]
        """

        self._accounts = accounts

    @property
    def alert(self):
        """Gets the alert of this IngestionPolicyReadModel.  # noqa: E501

        The alert object connected with the ingestion policy.  # noqa: E501

        :return: The alert of this IngestionPolicyReadModel.  # noqa: E501
        :rtype: Alert
        """
        return self._alert

    @alert.setter
    def alert(self, alert):
        """Sets the alert of this IngestionPolicyReadModel.

        The alert object connected with the ingestion policy.  # noqa: E501

        :param alert: The alert of this IngestionPolicyReadModel.  # noqa: E501
        :type: Alert
        """

        self._alert = alert

    @property
    def customer(self):
        """Gets the customer of this IngestionPolicyReadModel.  # noqa: E501

        ID of the customer to which the ingestion policy belongs  # noqa: E501

        :return: The customer of this IngestionPolicyReadModel.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this IngestionPolicyReadModel.

        ID of the customer to which the ingestion policy belongs  # noqa: E501

        :param customer: The customer of this IngestionPolicyReadModel.  # noqa: E501
        :type: str
        """

        self._customer = customer

    @property
    def description(self):
        """Gets the description of this IngestionPolicyReadModel.  # noqa: E501

        The description of the ingestion policy  # noqa: E501

        :return: The description of this IngestionPolicyReadModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IngestionPolicyReadModel.

        The description of the ingestion policy  # noqa: E501

        :param description: The description of this IngestionPolicyReadModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def groups(self):
        """Gets the groups of this IngestionPolicyReadModel.  # noqa: E501

        The groups associated with the ingestion policy  # noqa: E501

        :return: The groups of this IngestionPolicyReadModel.  # noqa: E501
        :rtype: list[AccessControlElement]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this IngestionPolicyReadModel.

        The groups associated with the ingestion policy  # noqa: E501

        :param groups: The groups of this IngestionPolicyReadModel.  # noqa: E501
        :type: list[AccessControlElement]
        """

        self._groups = groups

    @property
    def id(self):
        """Gets the id of this IngestionPolicyReadModel.  # noqa: E501

        The unique ID for the ingestion policy  # noqa: E501

        :return: The id of this IngestionPolicyReadModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IngestionPolicyReadModel.

        The unique ID for the ingestion policy  # noqa: E501

        :param id: The id of this IngestionPolicyReadModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_limited(self):
        """Gets the is_limited of this IngestionPolicyReadModel.  # noqa: E501

        Whether the ingestion policy is limited  # noqa: E501

        :return: The is_limited of this IngestionPolicyReadModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_limited

    @is_limited.setter
    def is_limited(self, is_limited):
        """Sets the is_limited of this IngestionPolicyReadModel.

        Whether the ingestion policy is limited  # noqa: E501

        :param is_limited: The is_limited of this IngestionPolicyReadModel.  # noqa: E501
        :type: bool
        """

        self._is_limited = is_limited

    @property
    def last_updated_account_id(self):
        """Gets the last_updated_account_id of this IngestionPolicyReadModel.  # noqa: E501

        The account that updated this ingestion policy last time  # noqa: E501

        :return: The last_updated_account_id of this IngestionPolicyReadModel.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_account_id

    @last_updated_account_id.setter
    def last_updated_account_id(self, last_updated_account_id):
        """Sets the last_updated_account_id of this IngestionPolicyReadModel.

        The account that updated this ingestion policy last time  # noqa: E501

        :param last_updated_account_id: The last_updated_account_id of this IngestionPolicyReadModel.  # noqa: E501
        :type: str
        """

        self._last_updated_account_id = last_updated_account_id

    @property
    def last_updated_ms(self):
        """Gets the last_updated_ms of this IngestionPolicyReadModel.  # noqa: E501

        The last time when the ingestion policy is updated, in epoch milliseconds  # noqa: E501

        :return: The last_updated_ms of this IngestionPolicyReadModel.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_ms

    @last_updated_ms.setter
    def last_updated_ms(self, last_updated_ms):
        """Sets the last_updated_ms of this IngestionPolicyReadModel.

        The last time when the ingestion policy is updated, in epoch milliseconds  # noqa: E501

        :param last_updated_ms: The last_updated_ms of this IngestionPolicyReadModel.  # noqa: E501
        :type: int
        """

        self._last_updated_ms = last_updated_ms

    @property
    def limit_pps(self):
        """Gets the limit_pps of this IngestionPolicyReadModel.  # noqa: E501

        The PPS limit of the ingestion policy  # noqa: E501

        :return: The limit_pps of this IngestionPolicyReadModel.  # noqa: E501
        :rtype: int
        """
        return self._limit_pps

    @limit_pps.setter
    def limit_pps(self, limit_pps):
        """Sets the limit_pps of this IngestionPolicyReadModel.

        The PPS limit of the ingestion policy  # noqa: E501

        :param limit_pps: The limit_pps of this IngestionPolicyReadModel.  # noqa: E501
        :type: int
        """

        self._limit_pps = limit_pps

    @property
    def metadata(self):
        """Gets the metadata of this IngestionPolicyReadModel.  # noqa: E501

        metadata associated with the ingestion policy  # noqa: E501

        :return: The metadata of this IngestionPolicyReadModel.  # noqa: E501
        :rtype: IngestionPolicyMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IngestionPolicyReadModel.

        metadata associated with the ingestion policy  # noqa: E501

        :param metadata: The metadata of this IngestionPolicyReadModel.  # noqa: E501
        :type: IngestionPolicyMetadata
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this IngestionPolicyReadModel.  # noqa: E501

        The name of the ingestion policy  # noqa: E501

        :return: The name of this IngestionPolicyReadModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IngestionPolicyReadModel.

        The name of the ingestion policy  # noqa: E501

        :param name: The name of this IngestionPolicyReadModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespaces(self):
        """Gets the namespaces of this IngestionPolicyReadModel.  # noqa: E501

        The namespaces associated with the ingestion policy  # noqa: E501

        :return: The namespaces of this IngestionPolicyReadModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this IngestionPolicyReadModel.

        The namespaces associated with the ingestion policy  # noqa: E501

        :param namespaces: The namespaces of this IngestionPolicyReadModel.  # noqa: E501
        :type: list[str]
        """

        self._namespaces = namespaces

    @property
    def point_tags(self):
        """Gets the point_tags of this IngestionPolicyReadModel.  # noqa: E501

        The point tags associated with the ingestion policy  # noqa: E501

        :return: The point_tags of this IngestionPolicyReadModel.  # noqa: E501
        :rtype: list[Annotation]
        """
        return self._point_tags

    @point_tags.setter
    def point_tags(self, point_tags):
        """Sets the point_tags of this IngestionPolicyReadModel.

        The point tags associated with the ingestion policy  # noqa: E501

        :param point_tags: The point_tags of this IngestionPolicyReadModel.  # noqa: E501
        :type: list[Annotation]
        """

        self._point_tags = point_tags

    @property
    def scope(self):
        """Gets the scope of this IngestionPolicyReadModel.  # noqa: E501

        The scope of the ingestion policy  # noqa: E501

        :return: The scope of this IngestionPolicyReadModel.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this IngestionPolicyReadModel.

        The scope of the ingestion policy  # noqa: E501

        :param scope: The scope of this IngestionPolicyReadModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACCOUNT", "GROUP", "NAMESPACE", "SOURCE", "TAGS"]  # noqa: E501
        if (self._configuration.client_side_validation and
                scope not in allowed_values):
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

    @property
    def sources(self):
        """Gets the sources of this IngestionPolicyReadModel.  # noqa: E501

        The sources associated with the ingestion policy  # noqa: E501

        :return: The sources of this IngestionPolicyReadModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this IngestionPolicyReadModel.

        The sources associated with the ingestion policy  # noqa: E501

        :param sources: The sources of this IngestionPolicyReadModel.  # noqa: E501
        :type: list[str]
        """

        self._sources = sources

    @property
    def tags_anded(self):
        """Gets the tags_anded of this IngestionPolicyReadModel.  # noqa: E501

        Whether tags should be AND-ed or OR-ed.If true, a metric must contain all tags in order for the ingestion policy to apply. If false, the tags are OR-ed, and a metric must contain one of the tags. Default: false  # noqa: E501

        :return: The tags_anded of this IngestionPolicyReadModel.  # noqa: E501
        :rtype: bool
        """
        return self._tags_anded

    @tags_anded.setter
    def tags_anded(self, tags_anded):
        """Sets the tags_anded of this IngestionPolicyReadModel.

        Whether tags should be AND-ed or OR-ed.If true, a metric must contain all tags in order for the ingestion policy to apply. If false, the tags are OR-ed, and a metric must contain one of the tags. Default: false  # noqa: E501

        :param tags_anded: The tags_anded of this IngestionPolicyReadModel.  # noqa: E501
        :type: bool
        """

        self._tags_anded = tags_anded

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
        if issubclass(IngestionPolicyReadModel, dict):
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
        if not isinstance(other, IngestionPolicyReadModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IngestionPolicyReadModel):
            return True

        return self.to_dict() != other.to_dict()
