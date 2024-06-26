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


class SearchQuery(object):
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
        'end': 'int',
        'key': 'str',
        'matching_method': 'str',
        'negated': 'bool',
        'start': 'int',
        'value': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'end': 'end',
        'key': 'key',
        'matching_method': 'matchingMethod',
        'negated': 'negated',
        'start': 'start',
        'value': 'value',
        'values': 'values'
    }

    def __init__(self, end=None, key=None, matching_method=None, negated=None, start=None, value=None, values=None, _configuration=None):  # noqa: E501
        """SearchQuery - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._end = None
        self._key = None
        self._matching_method = None
        self._negated = None
        self._start = None
        self._value = None
        self._values = None
        self.discriminator = None

        if end is not None:
            self.end = end
        self.key = key
        if matching_method is not None:
            self.matching_method = matching_method
        if negated is not None:
            self.negated = negated
        if start is not None:
            self.start = start
        if value is not None:
            self.value = value
        if values is not None:
            self.values = values

    @property
    def end(self):
        """Gets the end of this SearchQuery.  # noqa: E501

        The end point of the range. At least one of start or end points should be available for range search.  # noqa: E501

        :return: The end of this SearchQuery.  # noqa: E501
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this SearchQuery.

        The end point of the range. At least one of start or end points should be available for range search.  # noqa: E501

        :param end: The end of this SearchQuery.  # noqa: E501
        :type: int
        """

        self._end = end

    @property
    def key(self):
        """Gets the key of this SearchQuery.  # noqa: E501

        The entity facet (key) by which to search.  Valid keys are any property keys returned by the JSON representation of the entity.  Examples are 'creatorId', 'name', etc.  The following special key keywords are also valid:  'tags' performs a search on entity tags, 'tagpath' performs a hierarchical search on tags, with  periods (.) as path level separators.  'freetext' performs a free text search across many fields of the entity  # noqa: E501

        :return: The key of this SearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SearchQuery.

        The entity facet (key) by which to search.  Valid keys are any property keys returned by the JSON representation of the entity.  Examples are 'creatorId', 'name', etc.  The following special key keywords are also valid:  'tags' performs a search on entity tags, 'tagpath' performs a hierarchical search on tags, with  periods (.) as path level separators.  'freetext' performs a free text search across many fields of the entity  # noqa: E501

        :param key: The key of this SearchQuery.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def matching_method(self):
        """Gets the matching_method of this SearchQuery.  # noqa: E501

        The method by which search matching is performed.  Default: CONTAINS  # noqa: E501

        :return: The matching_method of this SearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._matching_method

    @matching_method.setter
    def matching_method(self, matching_method):
        """Sets the matching_method of this SearchQuery.

        The method by which search matching is performed.  Default: CONTAINS  # noqa: E501

        :param matching_method: The matching_method of this SearchQuery.  # noqa: E501
        :type: str
        """
        allowed_values = ["CONTAINS", "STARTSWITH", "EXACT", "TAGPATH"]  # noqa: E501
        if (self._configuration.client_side_validation and
                matching_method not in allowed_values):
            raise ValueError(
                "Invalid value for `matching_method` ({0}), must be one of {1}"  # noqa: E501
                .format(matching_method, allowed_values)
            )

        self._matching_method = matching_method

    @property
    def negated(self):
        """Gets the negated of this SearchQuery.  # noqa: E501

        The flag to create a NOT operation. Default: false  # noqa: E501

        :return: The negated of this SearchQuery.  # noqa: E501
        :rtype: bool
        """
        return self._negated

    @negated.setter
    def negated(self, negated):
        """Sets the negated of this SearchQuery.

        The flag to create a NOT operation. Default: false  # noqa: E501

        :param negated: The negated of this SearchQuery.  # noqa: E501
        :type: bool
        """

        self._negated = negated

    @property
    def start(self):
        """Gets the start of this SearchQuery.  # noqa: E501

        The start point of the range. At least one of start or end points should be available for range search.  # noqa: E501

        :return: The start of this SearchQuery.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this SearchQuery.

        The start point of the range. At least one of start or end points should be available for range search.  # noqa: E501

        :param start: The start of this SearchQuery.  # noqa: E501
        :type: int
        """

        self._start = start

    @property
    def value(self):
        """Gets the value of this SearchQuery.  # noqa: E501

        The entity facet value for which to search. Either value or values field is required. If both are set, values takes precedence.  # noqa: E501

        :return: The value of this SearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SearchQuery.

        The entity facet value for which to search. Either value or values field is required. If both are set, values takes precedence.  # noqa: E501

        :param value: The value of this SearchQuery.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def values(self):
        """Gets the values of this SearchQuery.  # noqa: E501

        The entity facet values for which to search based on OR operation. Either value or values field is required. If both are set, values takes precedence.  # noqa: E501

        :return: The values of this SearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this SearchQuery.

        The entity facet values for which to search based on OR operation. Either value or values field is required. If both are set, values takes precedence.  # noqa: E501

        :param values: The values of this SearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._values = values

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
        if issubclass(SearchQuery, dict):
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
        if not isinstance(other, SearchQuery):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchQuery):
            return True

        return self.to_dict() != other.to_dict()
