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

class OutputResponse(object):
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
        'address': 'str',
        'indexed': 'bool',
        'inscriptions': 'list[str]',
        'outpoint': 'str',
        'runes': 'dict(str, GithubComSatstreamSsUtilsOrdServerResponsesRuneDetails)',
        'sat_ranges': 'list[list[int]]',
        'script_pubkey': 'str',
        'spent': 'bool',
        'transaction': 'str',
        'value': 'int'
    }

    attribute_map = {
        'address': 'address',
        'indexed': 'indexed',
        'inscriptions': 'inscriptions',
        'outpoint': 'outpoint',
        'runes': 'runes',
        'sat_ranges': 'sat_ranges',
        'script_pubkey': 'script_pubkey',
        'spent': 'spent',
        'transaction': 'transaction',
        'value': 'value'
    }

    def __init__(self, address=None, indexed=None, inscriptions=None, outpoint=None, runes=None, sat_ranges=None, script_pubkey=None, spent=None, transaction=None, value=None):  # noqa: E501
        """OutputResponse - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._indexed = None
        self._inscriptions = None
        self._outpoint = None
        self._runes = None
        self._sat_ranges = None
        self._script_pubkey = None
        self._spent = None
        self._transaction = None
        self._value = None
        self.discriminator = None
        if address is not None:
            self.address = address
        if indexed is not None:
            self.indexed = indexed
        if inscriptions is not None:
            self.inscriptions = inscriptions
        if outpoint is not None:
            self.outpoint = outpoint
        if runes is not None:
            self.runes = runes
        if sat_ranges is not None:
            self.sat_ranges = sat_ranges
        if script_pubkey is not None:
            self.script_pubkey = script_pubkey
        if spent is not None:
            self.spent = spent
        if transaction is not None:
            self.transaction = transaction
        if value is not None:
            self.value = value

    @property
    def address(self):
        """Gets the address of this OutputResponse.  # noqa: E501


        :return: The address of this OutputResponse.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this OutputResponse.


        :param address: The address of this OutputResponse.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def indexed(self):
        """Gets the indexed of this OutputResponse.  # noqa: E501


        :return: The indexed of this OutputResponse.  # noqa: E501
        :rtype: bool
        """
        return self._indexed

    @indexed.setter
    def indexed(self, indexed):
        """Sets the indexed of this OutputResponse.


        :param indexed: The indexed of this OutputResponse.  # noqa: E501
        :type: bool
        """

        self._indexed = indexed

    @property
    def inscriptions(self):
        """Gets the inscriptions of this OutputResponse.  # noqa: E501


        :return: The inscriptions of this OutputResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._inscriptions

    @inscriptions.setter
    def inscriptions(self, inscriptions):
        """Sets the inscriptions of this OutputResponse.


        :param inscriptions: The inscriptions of this OutputResponse.  # noqa: E501
        :type: list[str]
        """

        self._inscriptions = inscriptions

    @property
    def outpoint(self):
        """Gets the outpoint of this OutputResponse.  # noqa: E501


        :return: The outpoint of this OutputResponse.  # noqa: E501
        :rtype: str
        """
        return self._outpoint

    @outpoint.setter
    def outpoint(self, outpoint):
        """Sets the outpoint of this OutputResponse.


        :param outpoint: The outpoint of this OutputResponse.  # noqa: E501
        :type: str
        """

        self._outpoint = outpoint

    @property
    def runes(self):
        """Gets the runes of this OutputResponse.  # noqa: E501


        :return: The runes of this OutputResponse.  # noqa: E501
        :rtype: dict(str, GithubComSatstreamSsUtilsOrdServerResponsesRuneDetails)
        """
        return self._runes

    @runes.setter
    def runes(self, runes):
        """Sets the runes of this OutputResponse.


        :param runes: The runes of this OutputResponse.  # noqa: E501
        :type: dict(str, GithubComSatstreamSsUtilsOrdServerResponsesRuneDetails)
        """

        self._runes = runes

    @property
    def sat_ranges(self):
        """Gets the sat_ranges of this OutputResponse.  # noqa: E501


        :return: The sat_ranges of this OutputResponse.  # noqa: E501
        :rtype: list[list[int]]
        """
        return self._sat_ranges

    @sat_ranges.setter
    def sat_ranges(self, sat_ranges):
        """Sets the sat_ranges of this OutputResponse.


        :param sat_ranges: The sat_ranges of this OutputResponse.  # noqa: E501
        :type: list[list[int]]
        """

        self._sat_ranges = sat_ranges

    @property
    def script_pubkey(self):
        """Gets the script_pubkey of this OutputResponse.  # noqa: E501


        :return: The script_pubkey of this OutputResponse.  # noqa: E501
        :rtype: str
        """
        return self._script_pubkey

    @script_pubkey.setter
    def script_pubkey(self, script_pubkey):
        """Sets the script_pubkey of this OutputResponse.


        :param script_pubkey: The script_pubkey of this OutputResponse.  # noqa: E501
        :type: str
        """

        self._script_pubkey = script_pubkey

    @property
    def spent(self):
        """Gets the spent of this OutputResponse.  # noqa: E501


        :return: The spent of this OutputResponse.  # noqa: E501
        :rtype: bool
        """
        return self._spent

    @spent.setter
    def spent(self, spent):
        """Sets the spent of this OutputResponse.


        :param spent: The spent of this OutputResponse.  # noqa: E501
        :type: bool
        """

        self._spent = spent

    @property
    def transaction(self):
        """Gets the transaction of this OutputResponse.  # noqa: E501


        :return: The transaction of this OutputResponse.  # noqa: E501
        :rtype: str
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this OutputResponse.


        :param transaction: The transaction of this OutputResponse.  # noqa: E501
        :type: str
        """

        self._transaction = transaction

    @property
    def value(self):
        """Gets the value of this OutputResponse.  # noqa: E501


        :return: The value of this OutputResponse.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OutputResponse.


        :param value: The value of this OutputResponse.  # noqa: E501
        :type: int
        """

        self._value = value

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
        if issubclass(OutputResponse, dict):
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
        if not isinstance(other, OutputResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
