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

class GithubComSatstreamSsUtilsOrdinalsTerms(object):
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
        'amount': 'BigInt',
        'cap': 'BigInt',
        'height': 'GithubComSatstreamSsUtilsOrdinalsTermsRange',
        'offset': 'GithubComSatstreamSsUtilsOrdinalsTermsRange'
    }

    attribute_map = {
        'amount': 'amount',
        'cap': 'cap',
        'height': 'height',
        'offset': 'offset'
    }

    def __init__(self, amount=None, cap=None, height=None, offset=None):  # noqa: E501
        """GithubComSatstreamSsUtilsOrdinalsTerms - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._cap = None
        self._height = None
        self._offset = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if cap is not None:
            self.cap = cap
        if height is not None:
            self.height = height
        if offset is not None:
            self.offset = offset

    @property
    def amount(self):
        """Gets the amount of this GithubComSatstreamSsUtilsOrdinalsTerms.  # noqa: E501


        :return: The amount of this GithubComSatstreamSsUtilsOrdinalsTerms.  # noqa: E501
        :rtype: BigInt
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GithubComSatstreamSsUtilsOrdinalsTerms.


        :param amount: The amount of this GithubComSatstreamSsUtilsOrdinalsTerms.  # noqa: E501
        :type: BigInt
        """

        self._amount = amount

    @property
    def cap(self):
        """Gets the cap of this GithubComSatstreamSsUtilsOrdinalsTerms.  # noqa: E501


        :return: The cap of this GithubComSatstreamSsUtilsOrdinalsTerms.  # noqa: E501
        :rtype: BigInt
        """
        return self._cap

    @cap.setter
    def cap(self, cap):
        """Sets the cap of this GithubComSatstreamSsUtilsOrdinalsTerms.


        :param cap: The cap of this GithubComSatstreamSsUtilsOrdinalsTerms.  # noqa: E501
        :type: BigInt
        """

        self._cap = cap

    @property
    def height(self):
        """Gets the height of this GithubComSatstreamSsUtilsOrdinalsTerms.  # noqa: E501


        :return: The height of this GithubComSatstreamSsUtilsOrdinalsTerms.  # noqa: E501
        :rtype: GithubComSatstreamSsUtilsOrdinalsTermsRange
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this GithubComSatstreamSsUtilsOrdinalsTerms.


        :param height: The height of this GithubComSatstreamSsUtilsOrdinalsTerms.  # noqa: E501
        :type: GithubComSatstreamSsUtilsOrdinalsTermsRange
        """

        self._height = height

    @property
    def offset(self):
        """Gets the offset of this GithubComSatstreamSsUtilsOrdinalsTerms.  # noqa: E501


        :return: The offset of this GithubComSatstreamSsUtilsOrdinalsTerms.  # noqa: E501
        :rtype: GithubComSatstreamSsUtilsOrdinalsTermsRange
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this GithubComSatstreamSsUtilsOrdinalsTerms.


        :param offset: The offset of this GithubComSatstreamSsUtilsOrdinalsTerms.  # noqa: E501
        :type: GithubComSatstreamSsUtilsOrdinalsTermsRange
        """

        self._offset = offset

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
        if issubclass(GithubComSatstreamSsUtilsOrdinalsTerms, dict):
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
        if not isinstance(other, GithubComSatstreamSsUtilsOrdinalsTerms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
