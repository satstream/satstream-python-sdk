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

class BlockResponse(object):
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
        'best_height': 'int',
        'hash': 'str',
        'height': 'int',
        'inscriptions': 'list[str]',
        'runes': 'list[str]',
        'target': 'str',
        'transactions': 'list[Transaction]'
    }

    attribute_map = {
        'best_height': 'best_height',
        'hash': 'hash',
        'height': 'height',
        'inscriptions': 'inscriptions',
        'runes': 'runes',
        'target': 'target',
        'transactions': 'transactions'
    }

    def __init__(self, best_height=None, hash=None, height=None, inscriptions=None, runes=None, target=None, transactions=None):  # noqa: E501
        """BlockResponse - a model defined in Swagger"""  # noqa: E501
        self._best_height = None
        self._hash = None
        self._height = None
        self._inscriptions = None
        self._runes = None
        self._target = None
        self._transactions = None
        self.discriminator = None
        if best_height is not None:
            self.best_height = best_height
        if hash is not None:
            self.hash = hash
        if height is not None:
            self.height = height
        if inscriptions is not None:
            self.inscriptions = inscriptions
        if runes is not None:
            self.runes = runes
        if target is not None:
            self.target = target
        if transactions is not None:
            self.transactions = transactions

    @property
    def best_height(self):
        """Gets the best_height of this BlockResponse.  # noqa: E501


        :return: The best_height of this BlockResponse.  # noqa: E501
        :rtype: int
        """
        return self._best_height

    @best_height.setter
    def best_height(self, best_height):
        """Sets the best_height of this BlockResponse.


        :param best_height: The best_height of this BlockResponse.  # noqa: E501
        :type: int
        """

        self._best_height = best_height

    @property
    def hash(self):
        """Gets the hash of this BlockResponse.  # noqa: E501


        :return: The hash of this BlockResponse.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this BlockResponse.


        :param hash: The hash of this BlockResponse.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def height(self):
        """Gets the height of this BlockResponse.  # noqa: E501


        :return: The height of this BlockResponse.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this BlockResponse.


        :param height: The height of this BlockResponse.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def inscriptions(self):
        """Gets the inscriptions of this BlockResponse.  # noqa: E501


        :return: The inscriptions of this BlockResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._inscriptions

    @inscriptions.setter
    def inscriptions(self, inscriptions):
        """Sets the inscriptions of this BlockResponse.


        :param inscriptions: The inscriptions of this BlockResponse.  # noqa: E501
        :type: list[str]
        """

        self._inscriptions = inscriptions

    @property
    def runes(self):
        """Gets the runes of this BlockResponse.  # noqa: E501


        :return: The runes of this BlockResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._runes

    @runes.setter
    def runes(self, runes):
        """Sets the runes of this BlockResponse.


        :param runes: The runes of this BlockResponse.  # noqa: E501
        :type: list[str]
        """

        self._runes = runes

    @property
    def target(self):
        """Gets the target of this BlockResponse.  # noqa: E501


        :return: The target of this BlockResponse.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this BlockResponse.


        :param target: The target of this BlockResponse.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def transactions(self):
        """Gets the transactions of this BlockResponse.  # noqa: E501


        :return: The transactions of this BlockResponse.  # noqa: E501
        :rtype: list[Transaction]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this BlockResponse.


        :param transactions: The transactions of this BlockResponse.  # noqa: E501
        :type: list[Transaction]
        """

        self._transactions = transactions

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
        if issubclass(BlockResponse, dict):
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
        if not isinstance(other, BlockResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
