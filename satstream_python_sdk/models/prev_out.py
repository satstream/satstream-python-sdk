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

class PrevOut(object):
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
        'generated': 'bool',
        'height': 'int',
        'script_pub_key': 'ScriptPubKey',
        'value': 'float'
    }

    attribute_map = {
        'generated': 'generated',
        'height': 'height',
        'script_pub_key': 'scriptPubKey',
        'value': 'value'
    }

    def __init__(self, generated=None, height=None, script_pub_key=None, value=None):  # noqa: E501
        """PrevOut - a model defined in Swagger"""  # noqa: E501
        self._generated = None
        self._height = None
        self._script_pub_key = None
        self._value = None
        self.discriminator = None
        if generated is not None:
            self.generated = generated
        if height is not None:
            self.height = height
        if script_pub_key is not None:
            self.script_pub_key = script_pub_key
        if value is not None:
            self.value = value

    @property
    def generated(self):
        """Gets the generated of this PrevOut.  # noqa: E501


        :return: The generated of this PrevOut.  # noqa: E501
        :rtype: bool
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this PrevOut.


        :param generated: The generated of this PrevOut.  # noqa: E501
        :type: bool
        """

        self._generated = generated

    @property
    def height(self):
        """Gets the height of this PrevOut.  # noqa: E501


        :return: The height of this PrevOut.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this PrevOut.


        :param height: The height of this PrevOut.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def script_pub_key(self):
        """Gets the script_pub_key of this PrevOut.  # noqa: E501


        :return: The script_pub_key of this PrevOut.  # noqa: E501
        :rtype: ScriptPubKey
        """
        return self._script_pub_key

    @script_pub_key.setter
    def script_pub_key(self, script_pub_key):
        """Sets the script_pub_key of this PrevOut.


        :param script_pub_key: The script_pub_key of this PrevOut.  # noqa: E501
        :type: ScriptPubKey
        """

        self._script_pub_key = script_pub_key

    @property
    def value(self):
        """Gets the value of this PrevOut.  # noqa: E501


        :return: The value of this PrevOut.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PrevOut.


        :param value: The value of this PrevOut.  # noqa: E501
        :type: float
        """

        self._value = value

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
        if issubclass(PrevOut, dict):
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
        if not isinstance(other, PrevOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
