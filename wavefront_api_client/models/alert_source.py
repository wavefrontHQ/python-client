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


class AlertSource(object):
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
        'alert_source_type': 'list[str]',
        'color': 'str',
        'description': 'str',
        'hidden': 'bool',
        'name': 'str',
        'query': 'str',
        'query_builder_enabled': 'bool',
        'query_builder_serialization': 'str',
        'query_type': 'str'
    }

    attribute_map = {
        'alert_source_type': 'alertSourceType',
        'color': 'color',
        'description': 'description',
        'hidden': 'hidden',
        'name': 'name',
        'query': 'query',
        'query_builder_enabled': 'queryBuilderEnabled',
        'query_builder_serialization': 'queryBuilderSerialization',
        'query_type': 'queryType'
    }

    def __init__(self, alert_source_type=None, color=None, description=None, hidden=None, name=None, query=None, query_builder_enabled=None, query_builder_serialization=None, query_type=None, _configuration=None):  # noqa: E501
        """AlertSource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alert_source_type = None
        self._color = None
        self._description = None
        self._hidden = None
        self._name = None
        self._query = None
        self._query_builder_enabled = None
        self._query_builder_serialization = None
        self._query_type = None
        self.discriminator = None

        if alert_source_type is not None:
            self.alert_source_type = alert_source_type
        if color is not None:
            self.color = color
        if description is not None:
            self.description = description
        if hidden is not None:
            self.hidden = hidden
        if name is not None:
            self.name = name
        if query is not None:
            self.query = query
        if query_builder_enabled is not None:
            self.query_builder_enabled = query_builder_enabled
        if query_builder_serialization is not None:
            self.query_builder_serialization = query_builder_serialization
        if query_type is not None:
            self.query_type = query_type

    @property
    def alert_source_type(self):
        """Gets the alert_source_type of this AlertSource.  # noqa: E501

        The types of the alert source (an array of CONDITION, AUDIT, VARIABLE) and the default one is [VARIABLE]. CONDITION alert source is the condition query in the alert. AUDIT alert source is the query to get more details when the alert changes state. VARIABLE alert source is a variable used in the other queries.  # noqa: E501

        :return: The alert_source_type of this AlertSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._alert_source_type

    @alert_source_type.setter
    def alert_source_type(self, alert_source_type):
        """Sets the alert_source_type of this AlertSource.

        The types of the alert source (an array of CONDITION, AUDIT, VARIABLE) and the default one is [VARIABLE]. CONDITION alert source is the condition query in the alert. AUDIT alert source is the query to get more details when the alert changes state. VARIABLE alert source is a variable used in the other queries.  # noqa: E501

        :param alert_source_type: The alert_source_type of this AlertSource.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["VARIABLE", "CONDITION", "AUDIT"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(alert_source_type).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `alert_source_type` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(alert_source_type) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._alert_source_type = alert_source_type

    @property
    def color(self):
        """Gets the color of this AlertSource.  # noqa: E501

        The color of the alert source.  # noqa: E501

        :return: The color of this AlertSource.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this AlertSource.

        The color of the alert source.  # noqa: E501

        :param color: The color of this AlertSource.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def description(self):
        """Gets the description of this AlertSource.  # noqa: E501

        The additional long description of the alert source.  # noqa: E501

        :return: The description of this AlertSource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AlertSource.

        The additional long description of the alert source.  # noqa: E501

        :param description: The description of this AlertSource.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hidden(self):
        """Gets the hidden of this AlertSource.  # noqa: E501

        A flag to indicate whether the alert source is hidden or not.  # noqa: E501

        :return: The hidden of this AlertSource.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this AlertSource.

        A flag to indicate whether the alert source is hidden or not.  # noqa: E501

        :param hidden: The hidden of this AlertSource.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def name(self):
        """Gets the name of this AlertSource.  # noqa: E501

        The alert source query name. Used as the variable name in the other query.  # noqa: E501

        :return: The name of this AlertSource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AlertSource.

        The alert source query name. Used as the variable name in the other query.  # noqa: E501

        :param name: The name of this AlertSource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def query(self):
        """Gets the query of this AlertSource.  # noqa: E501

        The alert query. Support both Wavefront Query and Prometheus Query.  # noqa: E501

        :return: The query of this AlertSource.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this AlertSource.

        The alert query. Support both Wavefront Query and Prometheus Query.  # noqa: E501

        :param query: The query of this AlertSource.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def query_builder_enabled(self):
        """Gets the query_builder_enabled of this AlertSource.  # noqa: E501

        A flag indicate whether the alert source query builder enabled or not.  # noqa: E501

        :return: The query_builder_enabled of this AlertSource.  # noqa: E501
        :rtype: bool
        """
        return self._query_builder_enabled

    @query_builder_enabled.setter
    def query_builder_enabled(self, query_builder_enabled):
        """Sets the query_builder_enabled of this AlertSource.

        A flag indicate whether the alert source query builder enabled or not.  # noqa: E501

        :param query_builder_enabled: The query_builder_enabled of this AlertSource.  # noqa: E501
        :type: bool
        """

        self._query_builder_enabled = query_builder_enabled

    @property
    def query_builder_serialization(self):
        """Gets the query_builder_serialization of this AlertSource.  # noqa: E501

        The string serialization of the alert source query builder, mostly used by Wavefront UI.  # noqa: E501

        :return: The query_builder_serialization of this AlertSource.  # noqa: E501
        :rtype: str
        """
        return self._query_builder_serialization

    @query_builder_serialization.setter
    def query_builder_serialization(self, query_builder_serialization):
        """Sets the query_builder_serialization of this AlertSource.

        The string serialization of the alert source query builder, mostly used by Wavefront UI.  # noqa: E501

        :param query_builder_serialization: The query_builder_serialization of this AlertSource.  # noqa: E501
        :type: str
        """

        self._query_builder_serialization = query_builder_serialization

    @property
    def query_type(self):
        """Gets the query_type of this AlertSource.  # noqa: E501

        The type of the alert query. Supported types are [PROMQL, WQL].  # noqa: E501

        :return: The query_type of this AlertSource.  # noqa: E501
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this AlertSource.

        The type of the alert query. Supported types are [PROMQL, WQL].  # noqa: E501

        :param query_type: The query_type of this AlertSource.  # noqa: E501
        :type: str
        """
        allowed_values = ["WQL", "PROMQL", "HYBRID"]  # noqa: E501
        if (self._configuration.client_side_validation and
                query_type not in allowed_values):
            raise ValueError(
                "Invalid value for `query_type` ({0}), must be one of {1}"  # noqa: E501
                .format(query_type, allowed_values)
            )

        self._query_type = query_type

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
        if issubclass(AlertSource, dict):
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
        if not isinstance(other, AlertSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertSource):
            return True

        return self.to_dict() != other.to_dict()