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

class InscriptionData(object):
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
        'body': 'list[int]',
        'content_encoding': 'str',
        'content_type': 'list[int]',
        'delegate': 'str',
        'duplicate_field': 'bool',
        'incomplete_field': 'bool',
        'metadata': 'str',
        'metaprotocol': 'str',
        'parents': 'list[str]',
        'pointer': 'str',
        'rune': 'str',
        'unrecognized_even_field': 'bool'
    }

    attribute_map = {
        'body': 'body',
        'content_encoding': 'content_encoding',
        'content_type': 'content_type',
        'delegate': 'delegate',
        'duplicate_field': 'duplicate_field',
        'incomplete_field': 'incomplete_field',
        'metadata': 'metadata',
        'metaprotocol': 'metaprotocol',
        'parents': 'parents',
        'pointer': 'pointer',
        'rune': 'rune',
        'unrecognized_even_field': 'unrecognized_even_field'
    }

    def __init__(self, body=None, content_encoding=None, content_type=None, delegate=None, duplicate_field=None, incomplete_field=None, metadata=None, metaprotocol=None, parents=None, pointer=None, rune=None, unrecognized_even_field=None):  # noqa: E501
        """InscriptionData - a model defined in Swagger"""  # noqa: E501
        self._body = None
        self._content_encoding = None
        self._content_type = None
        self._delegate = None
        self._duplicate_field = None
        self._incomplete_field = None
        self._metadata = None
        self._metaprotocol = None
        self._parents = None
        self._pointer = None
        self._rune = None
        self._unrecognized_even_field = None
        self.discriminator = None
        if body is not None:
            self.body = body
        if content_encoding is not None:
            self.content_encoding = content_encoding
        if content_type is not None:
            self.content_type = content_type
        if delegate is not None:
            self.delegate = delegate
        if duplicate_field is not None:
            self.duplicate_field = duplicate_field
        if incomplete_field is not None:
            self.incomplete_field = incomplete_field
        if metadata is not None:
            self.metadata = metadata
        if metaprotocol is not None:
            self.metaprotocol = metaprotocol
        if parents is not None:
            self.parents = parents
        if pointer is not None:
            self.pointer = pointer
        if rune is not None:
            self.rune = rune
        if unrecognized_even_field is not None:
            self.unrecognized_even_field = unrecognized_even_field

    @property
    def body(self):
        """Gets the body of this InscriptionData.  # noqa: E501


        :return: The body of this InscriptionData.  # noqa: E501
        :rtype: list[int]
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this InscriptionData.


        :param body: The body of this InscriptionData.  # noqa: E501
        :type: list[int]
        """

        self._body = body

    @property
    def content_encoding(self):
        """Gets the content_encoding of this InscriptionData.  # noqa: E501


        :return: The content_encoding of this InscriptionData.  # noqa: E501
        :rtype: str
        """
        return self._content_encoding

    @content_encoding.setter
    def content_encoding(self, content_encoding):
        """Sets the content_encoding of this InscriptionData.


        :param content_encoding: The content_encoding of this InscriptionData.  # noqa: E501
        :type: str
        """

        self._content_encoding = content_encoding

    @property
    def content_type(self):
        """Gets the content_type of this InscriptionData.  # noqa: E501


        :return: The content_type of this InscriptionData.  # noqa: E501
        :rtype: list[int]
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this InscriptionData.


        :param content_type: The content_type of this InscriptionData.  # noqa: E501
        :type: list[int]
        """

        self._content_type = content_type

    @property
    def delegate(self):
        """Gets the delegate of this InscriptionData.  # noqa: E501


        :return: The delegate of this InscriptionData.  # noqa: E501
        :rtype: str
        """
        return self._delegate

    @delegate.setter
    def delegate(self, delegate):
        """Sets the delegate of this InscriptionData.


        :param delegate: The delegate of this InscriptionData.  # noqa: E501
        :type: str
        """

        self._delegate = delegate

    @property
    def duplicate_field(self):
        """Gets the duplicate_field of this InscriptionData.  # noqa: E501


        :return: The duplicate_field of this InscriptionData.  # noqa: E501
        :rtype: bool
        """
        return self._duplicate_field

    @duplicate_field.setter
    def duplicate_field(self, duplicate_field):
        """Sets the duplicate_field of this InscriptionData.


        :param duplicate_field: The duplicate_field of this InscriptionData.  # noqa: E501
        :type: bool
        """

        self._duplicate_field = duplicate_field

    @property
    def incomplete_field(self):
        """Gets the incomplete_field of this InscriptionData.  # noqa: E501


        :return: The incomplete_field of this InscriptionData.  # noqa: E501
        :rtype: bool
        """
        return self._incomplete_field

    @incomplete_field.setter
    def incomplete_field(self, incomplete_field):
        """Sets the incomplete_field of this InscriptionData.


        :param incomplete_field: The incomplete_field of this InscriptionData.  # noqa: E501
        :type: bool
        """

        self._incomplete_field = incomplete_field

    @property
    def metadata(self):
        """Gets the metadata of this InscriptionData.  # noqa: E501


        :return: The metadata of this InscriptionData.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this InscriptionData.


        :param metadata: The metadata of this InscriptionData.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def metaprotocol(self):
        """Gets the metaprotocol of this InscriptionData.  # noqa: E501


        :return: The metaprotocol of this InscriptionData.  # noqa: E501
        :rtype: str
        """
        return self._metaprotocol

    @metaprotocol.setter
    def metaprotocol(self, metaprotocol):
        """Sets the metaprotocol of this InscriptionData.


        :param metaprotocol: The metaprotocol of this InscriptionData.  # noqa: E501
        :type: str
        """

        self._metaprotocol = metaprotocol

    @property
    def parents(self):
        """Gets the parents of this InscriptionData.  # noqa: E501


        :return: The parents of this InscriptionData.  # noqa: E501
        :rtype: list[str]
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this InscriptionData.


        :param parents: The parents of this InscriptionData.  # noqa: E501
        :type: list[str]
        """

        self._parents = parents

    @property
    def pointer(self):
        """Gets the pointer of this InscriptionData.  # noqa: E501


        :return: The pointer of this InscriptionData.  # noqa: E501
        :rtype: str
        """
        return self._pointer

    @pointer.setter
    def pointer(self, pointer):
        """Sets the pointer of this InscriptionData.


        :param pointer: The pointer of this InscriptionData.  # noqa: E501
        :type: str
        """

        self._pointer = pointer

    @property
    def rune(self):
        """Gets the rune of this InscriptionData.  # noqa: E501


        :return: The rune of this InscriptionData.  # noqa: E501
        :rtype: str
        """
        return self._rune

    @rune.setter
    def rune(self, rune):
        """Sets the rune of this InscriptionData.


        :param rune: The rune of this InscriptionData.  # noqa: E501
        :type: str
        """

        self._rune = rune

    @property
    def unrecognized_even_field(self):
        """Gets the unrecognized_even_field of this InscriptionData.  # noqa: E501


        :return: The unrecognized_even_field of this InscriptionData.  # noqa: E501
        :rtype: bool
        """
        return self._unrecognized_even_field

    @unrecognized_even_field.setter
    def unrecognized_even_field(self, unrecognized_even_field):
        """Sets the unrecognized_even_field of this InscriptionData.


        :param unrecognized_even_field: The unrecognized_even_field of this InscriptionData.  # noqa: E501
        :type: bool
        """

        self._unrecognized_even_field = unrecognized_even_field

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
        if issubclass(InscriptionData, dict):
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
        if not isinstance(other, InscriptionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
