# coding: utf-8

"""
    Satstream API

    Satstream API  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: team@satstream.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RequestsGetBlockStatsRequest(object):
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
        'hash_or_height': 'object',
        'stats': 'list[str]'
    }

    attribute_map = {
        'hash_or_height': 'hash_or_height',
        'stats': 'stats'
    }

    def __init__(self, hash_or_height=None, stats=None):  # noqa: E501
        """RequestsGetBlockStatsRequest - a model defined in Swagger"""  # noqa: E501
        self._hash_or_height = None
        self._stats = None
        self.discriminator = None
        if hash_or_height is not None:
            self.hash_or_height = hash_or_height
        if stats is not None:
            self.stats = stats

    @property
    def hash_or_height(self):
        """Gets the hash_or_height of this RequestsGetBlockStatsRequest.  # noqa: E501

        Required: The block hash (string) or height (numeric)  # noqa: E501

        :return: The hash_or_height of this RequestsGetBlockStatsRequest.  # noqa: E501
        :rtype: object
        """
        return self._hash_or_height

    @hash_or_height.setter
    def hash_or_height(self, hash_or_height):
        """Sets the hash_or_height of this RequestsGetBlockStatsRequest.

        Required: The block hash (string) or height (numeric)  # noqa: E501

        :param hash_or_height: The hash_or_height of this RequestsGetBlockStatsRequest.  # noqa: E501
        :type: object
        """

        self._hash_or_height = hash_or_height

    @property
    def stats(self):
        """Gets the stats of this RequestsGetBlockStatsRequest.  # noqa: E501

        Optional: Values to plot (if empty, all values will be included)  # noqa: E501

        :return: The stats of this RequestsGetBlockStatsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this RequestsGetBlockStatsRequest.

        Optional: Values to plot (if empty, all values will be included)  # noqa: E501

        :param stats: The stats of this RequestsGetBlockStatsRequest.  # noqa: E501
        :type: list[str]
        """

        self._stats = stats

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
        if issubclass(RequestsGetBlockStatsRequest, dict):
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
        if not isinstance(other, RequestsGetBlockStatsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
