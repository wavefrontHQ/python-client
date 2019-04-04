# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AccessControlListSimple(object):
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
        'can_modify': 'list[str]',
        'can_view': 'list[str]'
    }

    attribute_map = {
        'can_modify': 'canModify',
        'can_view': 'canView'
    }

    def __init__(self, can_modify=None, can_view=None):  # noqa: E501
        """AccessControlListSimple - a model defined in Swagger"""  # noqa: E501

        self._can_modify = None
        self._can_view = None
        self.discriminator = None

        if can_modify is not None:
            self.can_modify = can_modify
        if can_view is not None:
            self.can_view = can_view

    @property
    def can_modify(self):
        """Gets the can_modify of this AccessControlListSimple.  # noqa: E501


        :return: The can_modify of this AccessControlListSimple.  # noqa: E501
        :rtype: list[str]
        """
        return self._can_modify

    @can_modify.setter
    def can_modify(self, can_modify):
        """Sets the can_modify of this AccessControlListSimple.


        :param can_modify: The can_modify of this AccessControlListSimple.  # noqa: E501
        :type: list[str]
        """

        self._can_modify = can_modify

    @property
    def can_view(self):
        """Gets the can_view of this AccessControlListSimple.  # noqa: E501


        :return: The can_view of this AccessControlListSimple.  # noqa: E501
        :rtype: list[str]
        """
        return self._can_view

    @can_view.setter
    def can_view(self, can_view):
        """Sets the can_view of this AccessControlListSimple.


        :param can_view: The can_view of this AccessControlListSimple.  # noqa: E501
        :type: list[str]
        """

        self._can_view = can_view

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
        if issubclass(AccessControlListSimple, dict):
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
        if not isinstance(other, AccessControlListSimple):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
