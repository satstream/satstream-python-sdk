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

class PSBTMissingData(object):
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
        'pubkeys': 'list[str]',
        'redeemscript': 'str',
        'signatures': 'list[str]',
        'witnessscript': 'str'
    }

    attribute_map = {
        'pubkeys': 'pubkeys',
        'redeemscript': 'redeemscript',
        'signatures': 'signatures',
        'witnessscript': 'witnessscript'
    }

    def __init__(self, pubkeys=None, redeemscript=None, signatures=None, witnessscript=None):  # noqa: E501
        """PSBTMissingData - a model defined in Swagger"""  # noqa: E501
        self._pubkeys = None
        self._redeemscript = None
        self._signatures = None
        self._witnessscript = None
        self.discriminator = None
        if pubkeys is not None:
            self.pubkeys = pubkeys
        if redeemscript is not None:
            self.redeemscript = redeemscript
        if signatures is not None:
            self.signatures = signatures
        if witnessscript is not None:
            self.witnessscript = witnessscript

    @property
    def pubkeys(self):
        """Gets the pubkeys of this PSBTMissingData.  # noqa: E501


        :return: The pubkeys of this PSBTMissingData.  # noqa: E501
        :rtype: list[str]
        """
        return self._pubkeys

    @pubkeys.setter
    def pubkeys(self, pubkeys):
        """Sets the pubkeys of this PSBTMissingData.


        :param pubkeys: The pubkeys of this PSBTMissingData.  # noqa: E501
        :type: list[str]
        """

        self._pubkeys = pubkeys

    @property
    def redeemscript(self):
        """Gets the redeemscript of this PSBTMissingData.  # noqa: E501


        :return: The redeemscript of this PSBTMissingData.  # noqa: E501
        :rtype: str
        """
        return self._redeemscript

    @redeemscript.setter
    def redeemscript(self, redeemscript):
        """Sets the redeemscript of this PSBTMissingData.


        :param redeemscript: The redeemscript of this PSBTMissingData.  # noqa: E501
        :type: str
        """

        self._redeemscript = redeemscript

    @property
    def signatures(self):
        """Gets the signatures of this PSBTMissingData.  # noqa: E501


        :return: The signatures of this PSBTMissingData.  # noqa: E501
        :rtype: list[str]
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures):
        """Sets the signatures of this PSBTMissingData.


        :param signatures: The signatures of this PSBTMissingData.  # noqa: E501
        :type: list[str]
        """

        self._signatures = signatures

    @property
    def witnessscript(self):
        """Gets the witnessscript of this PSBTMissingData.  # noqa: E501


        :return: The witnessscript of this PSBTMissingData.  # noqa: E501
        :rtype: str
        """
        return self._witnessscript

    @witnessscript.setter
    def witnessscript(self, witnessscript):
        """Sets the witnessscript of this PSBTMissingData.


        :param witnessscript: The witnessscript of this PSBTMissingData.  # noqa: E501
        :type: str
        """

        self._witnessscript = witnessscript

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
        if issubclass(PSBTMissingData, dict):
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
        if not isinstance(other, PSBTMissingData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other