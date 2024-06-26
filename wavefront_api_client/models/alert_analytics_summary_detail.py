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


class AlertAnalyticsSummaryDetail(object):
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
        'alert_id': 'int',
        'alert_name': 'str',
        'avg_key_cardinality': 'int',
        'avg_latency': 'int',
        'avg_points': 'int',
        'checking_frequency': 'int',
        'creator_id': 'str',
        'error_groups_summary': 'list[AlertErrorGroupSummary]',
        'failure_percentage': 'float',
        'failure_percentage_range': 'str',
        'is_no_data': 'bool',
        'is_no_target': 'bool',
        'last_event_time': 'str',
        'last_updated_time': 'str',
        'last_updated_user_id': 'str',
        'tags': 'list[str]',
        'total_evaluated': 'int',
        'total_failed': 'int'
    }

    attribute_map = {
        'alert_id': 'alertId',
        'alert_name': 'alertName',
        'avg_key_cardinality': 'avgKeyCardinality',
        'avg_latency': 'avgLatency',
        'avg_points': 'avgPoints',
        'checking_frequency': 'checkingFrequency',
        'creator_id': 'creatorId',
        'error_groups_summary': 'errorGroupsSummary',
        'failure_percentage': 'failurePercentage',
        'failure_percentage_range': 'failurePercentageRange',
        'is_no_data': 'isNoData',
        'is_no_target': 'isNoTarget',
        'last_event_time': 'lastEventTime',
        'last_updated_time': 'lastUpdatedTime',
        'last_updated_user_id': 'lastUpdatedUserId',
        'tags': 'tags',
        'total_evaluated': 'totalEvaluated',
        'total_failed': 'totalFailed'
    }

    def __init__(self, alert_id=None, alert_name=None, avg_key_cardinality=None, avg_latency=None, avg_points=None, checking_frequency=None, creator_id=None, error_groups_summary=None, failure_percentage=None, failure_percentage_range=None, is_no_data=None, is_no_target=None, last_event_time=None, last_updated_time=None, last_updated_user_id=None, tags=None, total_evaluated=None, total_failed=None, _configuration=None):  # noqa: E501
        """AlertAnalyticsSummaryDetail - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alert_id = None
        self._alert_name = None
        self._avg_key_cardinality = None
        self._avg_latency = None
        self._avg_points = None
        self._checking_frequency = None
        self._creator_id = None
        self._error_groups_summary = None
        self._failure_percentage = None
        self._failure_percentage_range = None
        self._is_no_data = None
        self._is_no_target = None
        self._last_event_time = None
        self._last_updated_time = None
        self._last_updated_user_id = None
        self._tags = None
        self._total_evaluated = None
        self._total_failed = None
        self.discriminator = None

        if alert_id is not None:
            self.alert_id = alert_id
        if alert_name is not None:
            self.alert_name = alert_name
        if avg_key_cardinality is not None:
            self.avg_key_cardinality = avg_key_cardinality
        if avg_latency is not None:
            self.avg_latency = avg_latency
        if avg_points is not None:
            self.avg_points = avg_points
        if checking_frequency is not None:
            self.checking_frequency = checking_frequency
        if creator_id is not None:
            self.creator_id = creator_id
        if error_groups_summary is not None:
            self.error_groups_summary = error_groups_summary
        if failure_percentage is not None:
            self.failure_percentage = failure_percentage
        if failure_percentage_range is not None:
            self.failure_percentage_range = failure_percentage_range
        if is_no_data is not None:
            self.is_no_data = is_no_data
        if is_no_target is not None:
            self.is_no_target = is_no_target
        if last_event_time is not None:
            self.last_event_time = last_event_time
        if last_updated_time is not None:
            self.last_updated_time = last_updated_time
        if last_updated_user_id is not None:
            self.last_updated_user_id = last_updated_user_id
        if tags is not None:
            self.tags = tags
        if total_evaluated is not None:
            self.total_evaluated = total_evaluated
        if total_failed is not None:
            self.total_failed = total_failed

    @property
    def alert_id(self):
        """Gets the alert_id of this AlertAnalyticsSummaryDetail.  # noqa: E501

        The alert id  # noqa: E501

        :return: The alert_id of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :rtype: int
        """
        return self._alert_id

    @alert_id.setter
    def alert_id(self, alert_id):
        """Sets the alert_id of this AlertAnalyticsSummaryDetail.

        The alert id  # noqa: E501

        :param alert_id: The alert_id of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :type: int
        """

        self._alert_id = alert_id

    @property
    def alert_name(self):
        """Gets the alert_name of this AlertAnalyticsSummaryDetail.  # noqa: E501

        The alert name  # noqa: E501

        :return: The alert_name of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :rtype: str
        """
        return self._alert_name

    @alert_name.setter
    def alert_name(self, alert_name):
        """Sets the alert_name of this AlertAnalyticsSummaryDetail.

        The alert name  # noqa: E501

        :param alert_name: The alert_name of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :type: str
        """

        self._alert_name = alert_name

    @property
    def avg_key_cardinality(self):
        """Gets the avg_key_cardinality of this AlertAnalyticsSummaryDetail.  # noqa: E501

        The average cardinality across all alert execution logs.  # noqa: E501

        :return: The avg_key_cardinality of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :rtype: int
        """
        return self._avg_key_cardinality

    @avg_key_cardinality.setter
    def avg_key_cardinality(self, avg_key_cardinality):
        """Sets the avg_key_cardinality of this AlertAnalyticsSummaryDetail.

        The average cardinality across all alert execution logs.  # noqa: E501

        :param avg_key_cardinality: The avg_key_cardinality of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :type: int
        """

        self._avg_key_cardinality = avg_key_cardinality

    @property
    def avg_latency(self):
        """Gets the avg_latency of this AlertAnalyticsSummaryDetail.  # noqa: E501

        The average latency across all alert execution logs.  # noqa: E501

        :return: The avg_latency of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :rtype: int
        """
        return self._avg_latency

    @avg_latency.setter
    def avg_latency(self, avg_latency):
        """Sets the avg_latency of this AlertAnalyticsSummaryDetail.

        The average latency across all alert execution logs.  # noqa: E501

        :param avg_latency: The avg_latency of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :type: int
        """

        self._avg_latency = avg_latency

    @property
    def avg_points(self):
        """Gets the avg_points of this AlertAnalyticsSummaryDetail.  # noqa: E501

        The average points across all alert execution logs.  # noqa: E501

        :return: The avg_points of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :rtype: int
        """
        return self._avg_points

    @avg_points.setter
    def avg_points(self, avg_points):
        """Sets the avg_points of this AlertAnalyticsSummaryDetail.

        The average points across all alert execution logs.  # noqa: E501

        :param avg_points: The avg_points of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :type: int
        """

        self._avg_points = avg_points

    @property
    def checking_frequency(self):
        """Gets the checking_frequency of this AlertAnalyticsSummaryDetail.  # noqa: E501

        The checking frequency of the alert.  # noqa: E501

        :return: The checking_frequency of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :rtype: int
        """
        return self._checking_frequency

    @checking_frequency.setter
    def checking_frequency(self, checking_frequency):
        """Sets the checking_frequency of this AlertAnalyticsSummaryDetail.

        The checking frequency of the alert.  # noqa: E501

        :param checking_frequency: The checking_frequency of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :type: int
        """

        self._checking_frequency = checking_frequency

    @property
    def creator_id(self):
        """Gets the creator_id of this AlertAnalyticsSummaryDetail.  # noqa: E501


        :return: The creator_id of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this AlertAnalyticsSummaryDetail.


        :param creator_id: The creator_id of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :type: str
        """

        self._creator_id = creator_id

    @property
    def error_groups_summary(self):
        """Gets the error_groups_summary of this AlertAnalyticsSummaryDetail.  # noqa: E501


        :return: The error_groups_summary of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :rtype: list[AlertErrorGroupSummary]
        """
        return self._error_groups_summary

    @error_groups_summary.setter
    def error_groups_summary(self, error_groups_summary):
        """Sets the error_groups_summary of this AlertAnalyticsSummaryDetail.


        :param error_groups_summary: The error_groups_summary of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :type: list[AlertErrorGroupSummary]
        """

        self._error_groups_summary = error_groups_summary

    @property
    def failure_percentage(self):
        """Gets the failure_percentage of this AlertAnalyticsSummaryDetail.  # noqa: E501


        :return: The failure_percentage of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :rtype: float
        """
        return self._failure_percentage

    @failure_percentage.setter
    def failure_percentage(self, failure_percentage):
        """Sets the failure_percentage of this AlertAnalyticsSummaryDetail.


        :param failure_percentage: The failure_percentage of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :type: float
        """

        self._failure_percentage = failure_percentage

    @property
    def failure_percentage_range(self):
        """Gets the failure_percentage_range of this AlertAnalyticsSummaryDetail.  # noqa: E501


        :return: The failure_percentage_range of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :rtype: str
        """
        return self._failure_percentage_range

    @failure_percentage_range.setter
    def failure_percentage_range(self, failure_percentage_range):
        """Sets the failure_percentage_range of this AlertAnalyticsSummaryDetail.


        :param failure_percentage_range: The failure_percentage_range of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :type: str
        """

        self._failure_percentage_range = failure_percentage_range

    @property
    def is_no_data(self):
        """Gets the is_no_data of this AlertAnalyticsSummaryDetail.  # noqa: E501


        :return: The is_no_data of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_no_data

    @is_no_data.setter
    def is_no_data(self, is_no_data):
        """Sets the is_no_data of this AlertAnalyticsSummaryDetail.


        :param is_no_data: The is_no_data of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :type: bool
        """

        self._is_no_data = is_no_data

    @property
    def is_no_target(self):
        """Gets the is_no_target of this AlertAnalyticsSummaryDetail.  # noqa: E501


        :return: The is_no_target of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_no_target

    @is_no_target.setter
    def is_no_target(self, is_no_target):
        """Sets the is_no_target of this AlertAnalyticsSummaryDetail.


        :param is_no_target: The is_no_target of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :type: bool
        """

        self._is_no_target = is_no_target

    @property
    def last_event_time(self):
        """Gets the last_event_time of this AlertAnalyticsSummaryDetail.  # noqa: E501


        :return: The last_event_time of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :rtype: str
        """
        return self._last_event_time

    @last_event_time.setter
    def last_event_time(self, last_event_time):
        """Sets the last_event_time of this AlertAnalyticsSummaryDetail.


        :param last_event_time: The last_event_time of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :type: str
        """

        self._last_event_time = last_event_time

    @property
    def last_updated_time(self):
        """Gets the last_updated_time of this AlertAnalyticsSummaryDetail.  # noqa: E501


        :return: The last_updated_time of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_time

    @last_updated_time.setter
    def last_updated_time(self, last_updated_time):
        """Sets the last_updated_time of this AlertAnalyticsSummaryDetail.


        :param last_updated_time: The last_updated_time of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :type: str
        """

        self._last_updated_time = last_updated_time

    @property
    def last_updated_user_id(self):
        """Gets the last_updated_user_id of this AlertAnalyticsSummaryDetail.  # noqa: E501


        :return: The last_updated_user_id of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_user_id

    @last_updated_user_id.setter
    def last_updated_user_id(self, last_updated_user_id):
        """Sets the last_updated_user_id of this AlertAnalyticsSummaryDetail.


        :param last_updated_user_id: The last_updated_user_id of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :type: str
        """

        self._last_updated_user_id = last_updated_user_id

    @property
    def tags(self):
        """Gets the tags of this AlertAnalyticsSummaryDetail.  # noqa: E501


        :return: The tags of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AlertAnalyticsSummaryDetail.


        :param tags: The tags of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def total_evaluated(self):
        """Gets the total_evaluated of this AlertAnalyticsSummaryDetail.  # noqa: E501


        :return: The total_evaluated of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :rtype: int
        """
        return self._total_evaluated

    @total_evaluated.setter
    def total_evaluated(self, total_evaluated):
        """Sets the total_evaluated of this AlertAnalyticsSummaryDetail.


        :param total_evaluated: The total_evaluated of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :type: int
        """

        self._total_evaluated = total_evaluated

    @property
    def total_failed(self):
        """Gets the total_failed of this AlertAnalyticsSummaryDetail.  # noqa: E501


        :return: The total_failed of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :rtype: int
        """
        return self._total_failed

    @total_failed.setter
    def total_failed(self, total_failed):
        """Sets the total_failed of this AlertAnalyticsSummaryDetail.


        :param total_failed: The total_failed of this AlertAnalyticsSummaryDetail.  # noqa: E501
        :type: int
        """

        self._total_failed = total_failed

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
        if issubclass(AlertAnalyticsSummaryDetail, dict):
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
        if not isinstance(other, AlertAnalyticsSummaryDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertAnalyticsSummaryDetail):
            return True

        return self.to_dict() != other.to_dict()
