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

class MempoolFees(object):
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
        'ancestor': 'float',
        'base': 'float',
        'descendant': 'float',
        'modified': 'float'
    }

    attribute_map = {
        'ancestor': 'ancestor',
        'base': 'base',
        'descendant': 'descendant',
        'modified': 'modified'
    }

    def __init__(self, ancestor=None, base=None, descendant=None, modified=None):  # noqa: E501
        """MempoolFees - a model defined in Swagger"""  # noqa: E501
        self._ancestor = None
        self._base = None
        self._descendant = None
        self._modified = None
        self.discriminator = None
        if ancestor is not None:
            self.ancestor = ancestor
        if base is not None:
            self.base = base
        if descendant is not None:
            self.descendant = descendant
        if modified is not None:
            self.modified = modified

    @property
    def ancestor(self):
        """Gets the ancestor of this MempoolFees.  # noqa: E501

        Ancestor transaction fees in BTC  # noqa: E501

        :return: The ancestor of this MempoolFees.  # noqa: E501
        :rtype: float
        """
        return self._ancestor

    @ancestor.setter
    def ancestor(self, ancestor):
        """Sets the ancestor of this MempoolFees.

        Ancestor transaction fees in BTC  # noqa: E501

        :param ancestor: The ancestor of this MempoolFees.  # noqa: E501
        :type: float
        """

        self._ancestor = ancestor

    @property
    def base(self):
        """Gets the base of this MempoolFees.  # noqa: E501

        Base transaction fee in BTC  # noqa: E501

        :return: The base of this MempoolFees.  # noqa: E501
        :rtype: float
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this MempoolFees.

        Base transaction fee in BTC  # noqa: E501

        :param base: The base of this MempoolFees.  # noqa: E501
        :type: float
        """

        self._base = base

    @property
    def descendant(self):
        """Gets the descendant of this MempoolFees.  # noqa: E501

        Descendant transaction fees in BTC  # noqa: E501

        :return: The descendant of this MempoolFees.  # noqa: E501
        :rtype: float
        """
        return self._descendant

    @descendant.setter
    def descendant(self, descendant):
        """Sets the descendant of this MempoolFees.

        Descendant transaction fees in BTC  # noqa: E501

        :param descendant: The descendant of this MempoolFees.  # noqa: E501
        :type: float
        """

        self._descendant = descendant

    @property
    def modified(self):
        """Gets the modified of this MempoolFees.  # noqa: E501

        Modified transaction fee in BTC  # noqa: E501

        :return: The modified of this MempoolFees.  # noqa: E501
        :rtype: float
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this MempoolFees.

        Modified transaction fee in BTC  # noqa: E501

        :param modified: The modified of this MempoolFees.  # noqa: E501
        :type: float
        """

        self._modified = modified

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
        if issubclass(MempoolFees, dict):
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
        if not isinstance(other, MempoolFees):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
