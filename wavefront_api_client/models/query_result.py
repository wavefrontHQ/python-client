# coding: utf-8

"""
    Wavefront Public API

    <p>The Wavefront public API enables you to interact with Wavefront servers using standard web service API tools. You can use the API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make API calls outside the Wavefront API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p><p>For legacy versions of the Wavefront API, see the <a href=\"/api-docs/ui/deprecated\">legacy API documentation</a>.</p>  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wavefront_api_client.models.query_event import QueryEvent  # noqa: F401,E501
from wavefront_api_client.models.stats_model import StatsModel  # noqa: F401,E501
from wavefront_api_client.models.timeseries import Timeseries  # noqa: F401,E501


class QueryResult(object):
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
        'warnings': 'str',
        'name': 'str',
        'query': 'str',
        'stats': 'StatsModel',
        'events': 'list[QueryEvent]',
        'timeseries': 'list[Timeseries]',
        'granularity': 'int'
    }

    attribute_map = {
        'warnings': 'warnings',
        'name': 'name',
        'query': 'query',
        'stats': 'stats',
        'events': 'events',
        'timeseries': 'timeseries',
        'granularity': 'granularity'
    }

    def __init__(self, warnings=None, name=None, query=None, stats=None, events=None, timeseries=None, granularity=None):  # noqa: E501
        """QueryResult - a model defined in Swagger"""  # noqa: E501

        self._warnings = None
        self._name = None
        self._query = None
        self._stats = None
        self._events = None
        self._timeseries = None
        self._granularity = None
        self.discriminator = None

        if warnings is not None:
            self.warnings = warnings
        if name is not None:
            self.name = name
        if query is not None:
            self.query = query
        if stats is not None:
            self.stats = stats
        if events is not None:
            self.events = events
        if timeseries is not None:
            self.timeseries = timeseries
        if granularity is not None:
            self.granularity = granularity

    @property
    def warnings(self):
        """Gets the warnings of this QueryResult.  # noqa: E501

        The warnings incurred by this query  # noqa: E501

        :return: The warnings of this QueryResult.  # noqa: E501
        :rtype: str
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this QueryResult.

        The warnings incurred by this query  # noqa: E501

        :param warnings: The warnings of this QueryResult.  # noqa: E501
        :type: str
        """

        self._warnings = warnings

    @property
    def name(self):
        """Gets the name of this QueryResult.  # noqa: E501

        The name of this query  # noqa: E501

        :return: The name of this QueryResult.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueryResult.

        The name of this query  # noqa: E501

        :param name: The name of this QueryResult.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def query(self):
        """Gets the query of this QueryResult.  # noqa: E501

        The query used to obtain this result  # noqa: E501

        :return: The query of this QueryResult.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this QueryResult.

        The query used to obtain this result  # noqa: E501

        :param query: The query of this QueryResult.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def stats(self):
        """Gets the stats of this QueryResult.  # noqa: E501


        :return: The stats of this QueryResult.  # noqa: E501
        :rtype: StatsModel
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this QueryResult.


        :param stats: The stats of this QueryResult.  # noqa: E501
        :type: StatsModel
        """

        self._stats = stats

    @property
    def events(self):
        """Gets the events of this QueryResult.  # noqa: E501


        :return: The events of this QueryResult.  # noqa: E501
        :rtype: list[QueryEvent]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this QueryResult.


        :param events: The events of this QueryResult.  # noqa: E501
        :type: list[QueryEvent]
        """

        self._events = events

    @property
    def timeseries(self):
        """Gets the timeseries of this QueryResult.  # noqa: E501


        :return: The timeseries of this QueryResult.  # noqa: E501
        :rtype: list[Timeseries]
        """
        return self._timeseries

    @timeseries.setter
    def timeseries(self, timeseries):
        """Sets the timeseries of this QueryResult.


        :param timeseries: The timeseries of this QueryResult.  # noqa: E501
        :type: list[Timeseries]
        """

        self._timeseries = timeseries

    @property
    def granularity(self):
        """Gets the granularity of this QueryResult.  # noqa: E501

        The granularity of the returned results, in seconds  # noqa: E501

        :return: The granularity of this QueryResult.  # noqa: E501
        :rtype: int
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity):
        """Sets the granularity of this QueryResult.

        The granularity of the returned results, in seconds  # noqa: E501

        :param granularity: The granularity of this QueryResult.  # noqa: E501
        :type: int
        """

        self._granularity = granularity

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QueryResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
