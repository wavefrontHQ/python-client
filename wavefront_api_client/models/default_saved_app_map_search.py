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


class DefaultSavedAppMapSearch(object):
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
        'default_customer_search': 'SavedAppMapSearch',
        'default_user_search': 'SavedAppMapSearch'
    }

    attribute_map = {
        'default_customer_search': 'defaultCustomerSearch',
        'default_user_search': 'defaultUserSearch'
    }

    def __init__(self, default_customer_search=None, default_user_search=None, _configuration=None):  # noqa: E501
        """DefaultSavedAppMapSearch - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._default_customer_search = None
        self._default_user_search = None
        self.discriminator = None

        if default_customer_search is not None:
            self.default_customer_search = default_customer_search
        if default_user_search is not None:
            self.default_user_search = default_user_search

    @property
    def default_customer_search(self):
        """Gets the default_customer_search of this DefaultSavedAppMapSearch.  # noqa: E501


        :return: The default_customer_search of this DefaultSavedAppMapSearch.  # noqa: E501
        :rtype: SavedAppMapSearch
        """
        return self._default_customer_search

    @default_customer_search.setter
    def default_customer_search(self, default_customer_search):
        """Sets the default_customer_search of this DefaultSavedAppMapSearch.


        :param default_customer_search: The default_customer_search of this DefaultSavedAppMapSearch.  # noqa: E501
        :type: SavedAppMapSearch
        """

        self._default_customer_search = default_customer_search

    @property
    def default_user_search(self):
        """Gets the default_user_search of this DefaultSavedAppMapSearch.  # noqa: E501


        :return: The default_user_search of this DefaultSavedAppMapSearch.  # noqa: E501
        :rtype: SavedAppMapSearch
        """
        return self._default_user_search

    @default_user_search.setter
    def default_user_search(self, default_user_search):
        """Sets the default_user_search of this DefaultSavedAppMapSearch.


        :param default_user_search: The default_user_search of this DefaultSavedAppMapSearch.  # noqa: E501
        :type: SavedAppMapSearch
        """

        self._default_user_search = default_user_search

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
        if issubclass(DefaultSavedAppMapSearch, dict):
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
        if not isinstance(other, DefaultSavedAppMapSearch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DefaultSavedAppMapSearch):
            return True

        return self.to_dict() != other.to_dict()
