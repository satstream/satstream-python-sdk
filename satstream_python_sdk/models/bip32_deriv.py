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

class Bip32Deriv(object):
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
        'master_fingerprint': 'str',
        'path': 'str'
    }

    attribute_map = {
        'master_fingerprint': 'master_fingerprint',
        'path': 'path'
    }

    def __init__(self, master_fingerprint=None, path=None):  # noqa: E501
        """Bip32Deriv - a model defined in Swagger"""  # noqa: E501
        self._master_fingerprint = None
        self._path = None
        self.discriminator = None
        if master_fingerprint is not None:
            self.master_fingerprint = master_fingerprint
        if path is not None:
            self.path = path

    @property
    def master_fingerprint(self):
        """Gets the master_fingerprint of this Bip32Deriv.  # noqa: E501

        The fingerprint of the master key  # noqa: E501

        :return: The master_fingerprint of this Bip32Deriv.  # noqa: E501
        :rtype: str
        """
        return self._master_fingerprint

    @master_fingerprint.setter
    def master_fingerprint(self, master_fingerprint):
        """Sets the master_fingerprint of this Bip32Deriv.

        The fingerprint of the master key  # noqa: E501

        :param master_fingerprint: The master_fingerprint of this Bip32Deriv.  # noqa: E501
        :type: str
        """

        self._master_fingerprint = master_fingerprint

    @property
    def path(self):
        """Gets the path of this Bip32Deriv.  # noqa: E501

        The derivation path  # noqa: E501

        :return: The path of this Bip32Deriv.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Bip32Deriv.

        The derivation path  # noqa: E501

        :param path: The path of this Bip32Deriv.  # noqa: E501
        :type: str
        """

        self._path = path

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
        if issubclass(Bip32Deriv, dict):
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
        if not isinstance(other, Bip32Deriv):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
