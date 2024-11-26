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

class TestMempoolFees(object):
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
        'base': 'float'
    }

    attribute_map = {
        'base': 'base'
    }

    def __init__(self, base=None):  # noqa: E501
        """TestMempoolFees - a model defined in Swagger"""  # noqa: E501
        self._base = None
        self.discriminator = None
        if base is not None:
            self.base = base

    @property
    def base(self):
        """Gets the base of this TestMempoolFees.  # noqa: E501

        Transaction fee in BTC  # noqa: E501

        :return: The base of this TestMempoolFees.  # noqa: E501
        :rtype: float
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this TestMempoolFees.

        Transaction fee in BTC  # noqa: E501

        :param base: The base of this TestMempoolFees.  # noqa: E501
        :type: float
        """

        self._base = base

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
        if issubclass(TestMempoolFees, dict):
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
        if not isinstance(other, TestMempoolFees):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other