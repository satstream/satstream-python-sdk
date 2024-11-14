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

class GithubComSatstreamSsUtilsRpcUtxoRune(object):
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
        'amount': 'BigInt',
        'rune_id': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'rune_id': 'rune_id'
    }

    def __init__(self, amount=None, rune_id=None):  # noqa: E501
        """GithubComSatstreamSsUtilsRpcUtxoRune - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._rune_id = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if rune_id is not None:
            self.rune_id = rune_id

    @property
    def amount(self):
        """Gets the amount of this GithubComSatstreamSsUtilsRpcUtxoRune.  # noqa: E501


        :return: The amount of this GithubComSatstreamSsUtilsRpcUtxoRune.  # noqa: E501
        :rtype: BigInt
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GithubComSatstreamSsUtilsRpcUtxoRune.


        :param amount: The amount of this GithubComSatstreamSsUtilsRpcUtxoRune.  # noqa: E501
        :type: BigInt
        """

        self._amount = amount

    @property
    def rune_id(self):
        """Gets the rune_id of this GithubComSatstreamSsUtilsRpcUtxoRune.  # noqa: E501


        :return: The rune_id of this GithubComSatstreamSsUtilsRpcUtxoRune.  # noqa: E501
        :rtype: str
        """
        return self._rune_id

    @rune_id.setter
    def rune_id(self, rune_id):
        """Sets the rune_id of this GithubComSatstreamSsUtilsRpcUtxoRune.


        :param rune_id: The rune_id of this GithubComSatstreamSsUtilsRpcUtxoRune.  # noqa: E501
        :type: str
        """

        self._rune_id = rune_id

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
        if issubclass(GithubComSatstreamSsUtilsRpcUtxoRune, dict):
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
        if not isinstance(other, GithubComSatstreamSsUtilsRpcUtxoRune):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
