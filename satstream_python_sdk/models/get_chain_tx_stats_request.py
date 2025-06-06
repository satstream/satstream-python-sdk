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

class GetChainTxStatsRequest(object):
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
        'nblocks': 'int'
    }

    attribute_map = {
        'blockhash': 'blockhash',
        'nblocks': 'nblocks'
    }

    def __init__(self, blockhash=None, nblocks=None):  # noqa: E501
        """GetChainTxStatsRequest - a model defined in Swagger"""  # noqa: E501
        self._blockhash = None
        self._nblocks = None
        self.discriminator = None
        if blockhash is not None:
            self.blockhash = blockhash
        if nblocks is not None:
            self.nblocks = nblocks

    @property
    def blockhash(self):
        """Gets the blockhash of this GetChainTxStatsRequest.  # noqa: E501

        Optional: The hash of the block that ends the window  # noqa: E501

        :return: The blockhash of this GetChainTxStatsRequest.  # noqa: E501
        :rtype: str
        """
        return self._blockhash

    @blockhash.setter
    def blockhash(self, blockhash):
        """Sets the blockhash of this GetChainTxStatsRequest.

        Optional: The hash of the block that ends the window  # noqa: E501

        :param blockhash: The blockhash of this GetChainTxStatsRequest.  # noqa: E501
        :type: str
        """

        self._blockhash = blockhash

    @property
    def nblocks(self):
        """Gets the nblocks of this GetChainTxStatsRequest.  # noqa: E501

        Optional: Size of the window in number of blocks  # noqa: E501

        :return: The nblocks of this GetChainTxStatsRequest.  # noqa: E501
        :rtype: int
        """
        return self._nblocks

    @nblocks.setter
    def nblocks(self, nblocks):
        """Sets the nblocks of this GetChainTxStatsRequest.

        Optional: Size of the window in number of blocks  # noqa: E501

        :param nblocks: The nblocks of this GetChainTxStatsRequest.  # noqa: E501
        :type: int
        """

        self._nblocks = nblocks

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
        if issubclass(GetChainTxStatsRequest, dict):
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
        if not isinstance(other, GetChainTxStatsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
