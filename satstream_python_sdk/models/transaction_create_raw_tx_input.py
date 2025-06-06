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

class TransactionCreateRawTxInput(object):
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
        'sequence': 'int',
        'txid': 'str',
        'vout': 'int'
    }

    attribute_map = {
        'sequence': 'sequence',
        'txid': 'txid',
        'vout': 'vout'
    }

    def __init__(self, sequence=None, txid=None, vout=None):  # noqa: E501
        """TransactionCreateRawTxInput - a model defined in Swagger"""  # noqa: E501
        self._sequence = None
        self._txid = None
        self._vout = None
        self.discriminator = None
        if sequence is not None:
            self.sequence = sequence
        self.txid = txid
        self.vout = vout

    @property
    def sequence(self):
        """Gets the sequence of this TransactionCreateRawTxInput.  # noqa: E501

        The sequence number Optional, default depends on the value of the 'replaceable' and 'locktime' arguments  # noqa: E501

        :return: The sequence of this TransactionCreateRawTxInput.  # noqa: E501
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this TransactionCreateRawTxInput.

        The sequence number Optional, default depends on the value of the 'replaceable' and 'locktime' arguments  # noqa: E501

        :param sequence: The sequence of this TransactionCreateRawTxInput.  # noqa: E501
        :type: int
        """

        self._sequence = sequence

    @property
    def txid(self):
        """Gets the txid of this TransactionCreateRawTxInput.  # noqa: E501

        The transaction id  # noqa: E501

        :return: The txid of this TransactionCreateRawTxInput.  # noqa: E501
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this TransactionCreateRawTxInput.

        The transaction id  # noqa: E501

        :param txid: The txid of this TransactionCreateRawTxInput.  # noqa: E501
        :type: str
        """
        if txid is None:
            raise ValueError("Invalid value for `txid`, must not be `None`")  # noqa: E501

        self._txid = txid

    @property
    def vout(self):
        """Gets the vout of this TransactionCreateRawTxInput.  # noqa: E501

        The output number  # noqa: E501

        :return: The vout of this TransactionCreateRawTxInput.  # noqa: E501
        :rtype: int
        """
        return self._vout

    @vout.setter
    def vout(self, vout):
        """Sets the vout of this TransactionCreateRawTxInput.

        The output number  # noqa: E501

        :param vout: The vout of this TransactionCreateRawTxInput.  # noqa: E501
        :type: int
        """
        if vout is None:
            raise ValueError("Invalid value for `vout`, must not be `None`")  # noqa: E501

        self._vout = vout

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
        if issubclass(TransactionCreateRawTxInput, dict):
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
        if not isinstance(other, TransactionCreateRawTxInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
