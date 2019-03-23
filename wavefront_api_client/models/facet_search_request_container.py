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

from wavefront_api_client.models.search_query import SearchQuery  # noqa: F401,E501


class FacetSearchRequestContainer(object):
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
        'facet_query': 'str',
        'facet_query_matching_method': 'str',
        'limit': 'int',
        'offset': 'int',
        'query': 'list[SearchQuery]'
    }

    attribute_map = {
        'facet_query': 'facetQuery',
        'facet_query_matching_method': 'facetQueryMatchingMethod',
        'limit': 'limit',
        'offset': 'offset',
        'query': 'query'
    }

    def __init__(self, facet_query=None, facet_query_matching_method=None, limit=None, offset=None, query=None):  # noqa: E501
        """FacetSearchRequestContainer - a model defined in Swagger"""  # noqa: E501

        self._facet_query = None
        self._facet_query_matching_method = None
        self._limit = None
        self._offset = None
        self._query = None
        self.discriminator = None

        if facet_query is not None:
            self.facet_query = facet_query
        if facet_query_matching_method is not None:
            self.facet_query_matching_method = facet_query_matching_method
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if query is not None:
            self.query = query

    @property
    def facet_query(self):
        """Gets the facet_query of this FacetSearchRequestContainer.  # noqa: E501

        A string against which facet results are compared.  If the facet result CONTAINs, STARTSWITH, or is an EXACT match for this value, as specified by facetQueryMatchingMethod, then it is returned.  # noqa: E501

        :return: The facet_query of this FacetSearchRequestContainer.  # noqa: E501
        :rtype: str
        """
        return self._facet_query

    @facet_query.setter
    def facet_query(self, facet_query):
        """Sets the facet_query of this FacetSearchRequestContainer.

        A string against which facet results are compared.  If the facet result CONTAINs, STARTSWITH, or is an EXACT match for this value, as specified by facetQueryMatchingMethod, then it is returned.  # noqa: E501

        :param facet_query: The facet_query of this FacetSearchRequestContainer.  # noqa: E501
        :type: str
        """

        self._facet_query = facet_query

    @property
    def facet_query_matching_method(self):
        """Gets the facet_query_matching_method of this FacetSearchRequestContainer.  # noqa: E501

        The matching method used to filter when 'facetQuery' is used. Defaults to CONTAINS.  # noqa: E501

        :return: The facet_query_matching_method of this FacetSearchRequestContainer.  # noqa: E501
        :rtype: str
        """
        return self._facet_query_matching_method

    @facet_query_matching_method.setter
    def facet_query_matching_method(self, facet_query_matching_method):
        """Sets the facet_query_matching_method of this FacetSearchRequestContainer.

        The matching method used to filter when 'facetQuery' is used. Defaults to CONTAINS.  # noqa: E501

        :param facet_query_matching_method: The facet_query_matching_method of this FacetSearchRequestContainer.  # noqa: E501
        :type: str
        """
        allowed_values = ["CONTAINS", "STARTSWITH", "EXACT", "TAGPATH"]  # noqa: E501
        if facet_query_matching_method not in allowed_values:
            raise ValueError(
                "Invalid value for `facet_query_matching_method` ({0}), must be one of {1}"  # noqa: E501
                .format(facet_query_matching_method, allowed_values)
            )

        self._facet_query_matching_method = facet_query_matching_method

    @property
    def limit(self):
        """Gets the limit of this FacetSearchRequestContainer.  # noqa: E501

        The number of results to return.  Default: 100  # noqa: E501

        :return: The limit of this FacetSearchRequestContainer.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this FacetSearchRequestContainer.

        The number of results to return.  Default: 100  # noqa: E501

        :param limit: The limit of this FacetSearchRequestContainer.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this FacetSearchRequestContainer.  # noqa: E501

        The number of results to skip before returning values.  Default: 0  # noqa: E501

        :return: The offset of this FacetSearchRequestContainer.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this FacetSearchRequestContainer.

        The number of results to skip before returning values.  Default: 0  # noqa: E501

        :param offset: The offset of this FacetSearchRequestContainer.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def query(self):
        """Gets the query of this FacetSearchRequestContainer.  # noqa: E501

        A list of queries by which to limit the search results.  Entities that match ALL queries in the list are returned  # noqa: E501

        :return: The query of this FacetSearchRequestContainer.  # noqa: E501
        :rtype: list[SearchQuery]
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this FacetSearchRequestContainer.

        A list of queries by which to limit the search results.  Entities that match ALL queries in the list are returned  # noqa: E501

        :param query: The query of this FacetSearchRequestContainer.  # noqa: E501
        :type: list[SearchQuery]
        """

        self._query = query

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
        if issubclass(FacetSearchRequestContainer, dict):
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
        if not isinstance(other, FacetSearchRequestContainer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
