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

class TransactionGetTxOutProofRequest(object):
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
        'blockhash': 'str',
        'txids': 'list[str]'
    }

    attribute_map = {
        'blockhash': 'blockhash',
        'txids': 'txids'
    }

    def __init__(self, blockhash=None, txids=None):  # noqa: E501
        """TransactionGetTxOutProofRequest - a model defined in Swagger"""  # noqa: E501
        self._blockhash = None
        self._txids = None
        self.discriminator = None
        if blockhash is not None:
            self.blockhash = blockhash
        if txids is not None:
            self.txids = txids

    @property
    def blockhash(self):
        """Gets the blockhash of this TransactionGetTxOutProofRequest.  # noqa: E501

        Optional: If specified, looks for txid in the block with this hash  # noqa: E501

        :return: The blockhash of this TransactionGetTxOutProofRequest.  # noqa: E501
        :rtype: str
        """
        return self._blockhash

    @blockhash.setter
    def blockhash(self, blockhash):
        """Sets the blockhash of this TransactionGetTxOutProofRequest.

        Optional: If specified, looks for txid in the block with this hash  # noqa: E501

        :param blockhash: The blockhash of this TransactionGetTxOutProofRequest.  # noqa: E501
        :type: str
        """

        self._blockhash = blockhash

    @property
    def txids(self):
        """Gets the txids of this TransactionGetTxOutProofRequest.  # noqa: E501

        Required: Array of transaction ids to filter  # noqa: E501

        :return: The txids of this TransactionGetTxOutProofRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._txids

    @txids.setter
    def txids(self, txids):
        """Sets the txids of this TransactionGetTxOutProofRequest.

        Required: Array of transaction ids to filter  # noqa: E501

        :param txids: The txids of this TransactionGetTxOutProofRequest.  # noqa: E501
        :type: list[str]
        """

        self._txids = txids

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
        if issubclass(TransactionGetTxOutProofRequest, dict):
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
        if not isinstance(other, TransactionGetTxOutProofRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
