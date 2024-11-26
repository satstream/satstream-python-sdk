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

class RequestsTestMempoolAcceptRequest(object):
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
        'max_fee_rate': 'float',
        'raw_txs': 'list[str]'
    }

    attribute_map = {
        'max_fee_rate': 'max_fee_rate',
        'raw_txs': 'raw_txs'
    }

    def __init__(self, max_fee_rate=None, raw_txs=None):  # noqa: E501
        """RequestsTestMempoolAcceptRequest - a model defined in Swagger"""  # noqa: E501
        self._max_fee_rate = None
        self._raw_txs = None
        self.discriminator = None
        if max_fee_rate is not None:
            self.max_fee_rate = max_fee_rate
        if raw_txs is not None:
            self.raw_txs = raw_txs

    @property
    def max_fee_rate(self):
        """Gets the max_fee_rate of this RequestsTestMempoolAcceptRequest.  # noqa: E501

        Optional: Reject transactions whose fee rate is higher than this value (BTC/kvB)  # noqa: E501

        :return: The max_fee_rate of this RequestsTestMempoolAcceptRequest.  # noqa: E501
        :rtype: float
        """
        return self._max_fee_rate

    @max_fee_rate.setter
    def max_fee_rate(self, max_fee_rate):
        """Sets the max_fee_rate of this RequestsTestMempoolAcceptRequest.

        Optional: Reject transactions whose fee rate is higher than this value (BTC/kvB)  # noqa: E501

        :param max_fee_rate: The max_fee_rate of this RequestsTestMempoolAcceptRequest.  # noqa: E501
        :type: float
        """

        self._max_fee_rate = max_fee_rate

    @property
    def raw_txs(self):
        """Gets the raw_txs of this RequestsTestMempoolAcceptRequest.  # noqa: E501

        Array of hex-encoded raw transactions  # noqa: E501

        :return: The raw_txs of this RequestsTestMempoolAcceptRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._raw_txs

    @raw_txs.setter
    def raw_txs(self, raw_txs):
        """Sets the raw_txs of this RequestsTestMempoolAcceptRequest.

        Array of hex-encoded raw transactions  # noqa: E501

        :param raw_txs: The raw_txs of this RequestsTestMempoolAcceptRequest.  # noqa: E501
        :type: list[str]
        """

        self._raw_txs = raw_txs

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
        if issubclass(RequestsTestMempoolAcceptRequest, dict):
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
        if not isinstance(other, RequestsTestMempoolAcceptRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
