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

class GetRawMempoolRequest(object):
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
        'mempool_sequence': 'bool'
    }

    attribute_map = {
        'mempool_sequence': 'mempool_sequence'
    }

    def __init__(self, mempool_sequence=None):  # noqa: E501
        """GetRawMempoolRequest - a model defined in Swagger"""  # noqa: E501
        self._mempool_sequence = None
        self.discriminator = None
        if mempool_sequence is not None:
            self.mempool_sequence = mempool_sequence

    @property
    def mempool_sequence(self):
        """Gets the mempool_sequence of this GetRawMempoolRequest.  # noqa: E501

        Optional: Returns txids with mempool sequence number  # noqa: E501

        :return: The mempool_sequence of this GetRawMempoolRequest.  # noqa: E501
        :rtype: bool
        """
        return self._mempool_sequence

    @mempool_sequence.setter
    def mempool_sequence(self, mempool_sequence):
        """Sets the mempool_sequence of this GetRawMempoolRequest.

        Optional: Returns txids with mempool sequence number  # noqa: E501

        :param mempool_sequence: The mempool_sequence of this GetRawMempoolRequest.  # noqa: E501
        :type: bool
        """

        self._mempool_sequence = mempool_sequence

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
        if issubclass(GetRawMempoolRequest, dict):
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
        if not isinstance(other, GetRawMempoolRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
