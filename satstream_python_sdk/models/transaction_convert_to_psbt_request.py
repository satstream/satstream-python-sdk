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

class TransactionConvertToPSBTRequest(object):
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
        'hexstring': 'str',
        'is_witness': 'bool',
        'permit_sigdata': 'bool'
    }

    attribute_map = {
        'hexstring': 'hexstring',
        'is_witness': 'is_witness',
        'permit_sigdata': 'permit_sigdata'
    }

    def __init__(self, hexstring=None, is_witness=None, permit_sigdata=None):  # noqa: E501
        """TransactionConvertToPSBTRequest - a model defined in Swagger"""  # noqa: E501
        self._hexstring = None
        self._is_witness = None
        self._permit_sigdata = None
        self.discriminator = None
        self.hexstring = hexstring
        if is_witness is not None:
            self.is_witness = is_witness
        if permit_sigdata is not None:
            self.permit_sigdata = permit_sigdata

    @property
    def hexstring(self):
        """Gets the hexstring of this TransactionConvertToPSBTRequest.  # noqa: E501

        The hex string of a raw transaction  # noqa: E501

        :return: The hexstring of this TransactionConvertToPSBTRequest.  # noqa: E501
        :rtype: str
        """
        return self._hexstring

    @hexstring.setter
    def hexstring(self, hexstring):
        """Sets the hexstring of this TransactionConvertToPSBTRequest.

        The hex string of a raw transaction  # noqa: E501

        :param hexstring: The hexstring of this TransactionConvertToPSBTRequest.  # noqa: E501
        :type: str
        """
        if hexstring is None:
            raise ValueError("Invalid value for `hexstring`, must not be `None`")  # noqa: E501

        self._hexstring = hexstring

    @property
    def is_witness(self):
        """Gets the is_witness of this TransactionConvertToPSBTRequest.  # noqa: E501

        Whether the transaction hex is a serialized witness transaction. If not provided, heuristic tests will be used in decoding. If true, only witness deserialization will be tried. If false, only non-witness deserialization will be tried. This boolean should reflect whether the transaction has inputs (e.g. fully valid, or on-chain transactions), if known by the caller. Optional, defaults to heuristic tests if not provided.  # noqa: E501

        :return: The is_witness of this TransactionConvertToPSBTRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_witness

    @is_witness.setter
    def is_witness(self, is_witness):
        """Sets the is_witness of this TransactionConvertToPSBTRequest.

        Whether the transaction hex is a serialized witness transaction. If not provided, heuristic tests will be used in decoding. If true, only witness deserialization will be tried. If false, only non-witness deserialization will be tried. This boolean should reflect whether the transaction has inputs (e.g. fully valid, or on-chain transactions), if known by the caller. Optional, defaults to heuristic tests if not provided.  # noqa: E501

        :param is_witness: The is_witness of this TransactionConvertToPSBTRequest.  # noqa: E501
        :type: bool
        """

        self._is_witness = is_witness

    @property
    def permit_sigdata(self):
        """Gets the permit_sigdata of this TransactionConvertToPSBTRequest.  # noqa: E501

        If true, any signatures in the input will be discarded and conversion will continue. If false, RPC will fail if any signatures are present. Optional, defaults to false if not provided.  # noqa: E501

        :return: The permit_sigdata of this TransactionConvertToPSBTRequest.  # noqa: E501
        :rtype: bool
        """
        return self._permit_sigdata

    @permit_sigdata.setter
    def permit_sigdata(self, permit_sigdata):
        """Sets the permit_sigdata of this TransactionConvertToPSBTRequest.

        If true, any signatures in the input will be discarded and conversion will continue. If false, RPC will fail if any signatures are present. Optional, defaults to false if not provided.  # noqa: E501

        :param permit_sigdata: The permit_sigdata of this TransactionConvertToPSBTRequest.  # noqa: E501
        :type: bool
        """

        self._permit_sigdata = permit_sigdata

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
        if issubclass(TransactionConvertToPSBTRequest, dict):
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
        if not isinstance(other, TransactionConvertToPSBTRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
