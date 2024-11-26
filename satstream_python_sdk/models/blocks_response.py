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

class BlocksResponse(object):
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
        'blocks': 'list[str]',
        'featured_blocks': 'dict(str, list[str])',
        'last': 'int'
    }

    attribute_map = {
        'blocks': 'blocks',
        'featured_blocks': 'featured_blocks',
        'last': 'last'
    }

    def __init__(self, blocks=None, featured_blocks=None, last=None):  # noqa: E501
        """BlocksResponse - a model defined in Swagger"""  # noqa: E501
        self._blocks = None
        self._featured_blocks = None
        self._last = None
        self.discriminator = None
        if blocks is not None:
            self.blocks = blocks
        if featured_blocks is not None:
            self.featured_blocks = featured_blocks
        if last is not None:
            self.last = last

    @property
    def blocks(self):
        """Gets the blocks of this BlocksResponse.  # noqa: E501


        :return: The blocks of this BlocksResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._blocks

    @blocks.setter
    def blocks(self, blocks):
        """Sets the blocks of this BlocksResponse.


        :param blocks: The blocks of this BlocksResponse.  # noqa: E501
        :type: list[str]
        """

        self._blocks = blocks

    @property
    def featured_blocks(self):
        """Gets the featured_blocks of this BlocksResponse.  # noqa: E501


        :return: The featured_blocks of this BlocksResponse.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._featured_blocks

    @featured_blocks.setter
    def featured_blocks(self, featured_blocks):
        """Sets the featured_blocks of this BlocksResponse.


        :param featured_blocks: The featured_blocks of this BlocksResponse.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._featured_blocks = featured_blocks

    @property
    def last(self):
        """Gets the last of this BlocksResponse.  # noqa: E501


        :return: The last of this BlocksResponse.  # noqa: E501
        :rtype: int
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this BlocksResponse.


        :param last: The last of this BlocksResponse.  # noqa: E501
        :type: int
        """

        self._last = last

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
        if issubclass(BlocksResponse, dict):
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
        if not isinstance(other, BlocksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other