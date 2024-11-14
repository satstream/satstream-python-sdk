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

class ResponsesGetTxInfoData(object):
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
        'blkid': 'str',
        'height': 'int',
        'idx': 'int',
        'in_satoshi': 'BigInt',
        'locktime': 'int',
        'n_in': 'int',
        'n_in_inscription': 'int',
        'n_lost_inscription': 'int',
        'n_new_inscription': 'int',
        'n_out': 'int',
        'n_out_inscription': 'int',
        'out_satoshi': 'BigInt',
        'size': 'int',
        'txid': 'str'
    }

    attribute_map = {
        'blkid': 'blkid',
        'height': 'height',
        'idx': 'idx',
        'in_satoshi': 'inSatoshi',
        'locktime': 'locktime',
        'n_in': 'nIn',
        'n_in_inscription': 'nInInscription',
        'n_lost_inscription': 'nLostInscription',
        'n_new_inscription': 'nNewInscription',
        'n_out': 'nOut',
        'n_out_inscription': 'nOutInscription',
        'out_satoshi': 'outSatoshi',
        'size': 'size',
        'txid': 'txid'
    }

    def __init__(self, blkid=None, height=None, idx=None, in_satoshi=None, locktime=None, n_in=None, n_in_inscription=None, n_lost_inscription=None, n_new_inscription=None, n_out=None, n_out_inscription=None, out_satoshi=None, size=None, txid=None):  # noqa: E501
        """ResponsesGetTxInfoData - a model defined in Swagger"""  # noqa: E501
        self._blkid = None
        self._height = None
        self._idx = None
        self._in_satoshi = None
        self._locktime = None
        self._n_in = None
        self._n_in_inscription = None
        self._n_lost_inscription = None
        self._n_new_inscription = None
        self._n_out = None
        self._n_out_inscription = None
        self._out_satoshi = None
        self._size = None
        self._txid = None
        self.discriminator = None
        if blkid is not None:
            self.blkid = blkid
        if height is not None:
            self.height = height
        if idx is not None:
            self.idx = idx
        if in_satoshi is not None:
            self.in_satoshi = in_satoshi
        if locktime is not None:
            self.locktime = locktime
        if n_in is not None:
            self.n_in = n_in
        if n_in_inscription is not None:
            self.n_in_inscription = n_in_inscription
        if n_lost_inscription is not None:
            self.n_lost_inscription = n_lost_inscription
        if n_new_inscription is not None:
            self.n_new_inscription = n_new_inscription
        if n_out is not None:
            self.n_out = n_out
        if n_out_inscription is not None:
            self.n_out_inscription = n_out_inscription
        if out_satoshi is not None:
            self.out_satoshi = out_satoshi
        if size is not None:
            self.size = size
        if txid is not None:
            self.txid = txid

    @property
    def blkid(self):
        """Gets the blkid of this ResponsesGetTxInfoData.  # noqa: E501


        :return: The blkid of this ResponsesGetTxInfoData.  # noqa: E501
        :rtype: str
        """
        return self._blkid

    @blkid.setter
    def blkid(self, blkid):
        """Sets the blkid of this ResponsesGetTxInfoData.


        :param blkid: The blkid of this ResponsesGetTxInfoData.  # noqa: E501
        :type: str
        """

        self._blkid = blkid

    @property
    def height(self):
        """Gets the height of this ResponsesGetTxInfoData.  # noqa: E501


        :return: The height of this ResponsesGetTxInfoData.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ResponsesGetTxInfoData.


        :param height: The height of this ResponsesGetTxInfoData.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def idx(self):
        """Gets the idx of this ResponsesGetTxInfoData.  # noqa: E501


        :return: The idx of this ResponsesGetTxInfoData.  # noqa: E501
        :rtype: int
        """
        return self._idx

    @idx.setter
    def idx(self, idx):
        """Sets the idx of this ResponsesGetTxInfoData.


        :param idx: The idx of this ResponsesGetTxInfoData.  # noqa: E501
        :type: int
        """

        self._idx = idx

    @property
    def in_satoshi(self):
        """Gets the in_satoshi of this ResponsesGetTxInfoData.  # noqa: E501


        :return: The in_satoshi of this ResponsesGetTxInfoData.  # noqa: E501
        :rtype: BigInt
        """
        return self._in_satoshi

    @in_satoshi.setter
    def in_satoshi(self, in_satoshi):
        """Sets the in_satoshi of this ResponsesGetTxInfoData.


        :param in_satoshi: The in_satoshi of this ResponsesGetTxInfoData.  # noqa: E501
        :type: BigInt
        """

        self._in_satoshi = in_satoshi

    @property
    def locktime(self):
        """Gets the locktime of this ResponsesGetTxInfoData.  # noqa: E501


        :return: The locktime of this ResponsesGetTxInfoData.  # noqa: E501
        :rtype: int
        """
        return self._locktime

    @locktime.setter
    def locktime(self, locktime):
        """Sets the locktime of this ResponsesGetTxInfoData.


        :param locktime: The locktime of this ResponsesGetTxInfoData.  # noqa: E501
        :type: int
        """

        self._locktime = locktime

    @property
    def n_in(self):
        """Gets the n_in of this ResponsesGetTxInfoData.  # noqa: E501


        :return: The n_in of this ResponsesGetTxInfoData.  # noqa: E501
        :rtype: int
        """
        return self._n_in

    @n_in.setter
    def n_in(self, n_in):
        """Sets the n_in of this ResponsesGetTxInfoData.


        :param n_in: The n_in of this ResponsesGetTxInfoData.  # noqa: E501
        :type: int
        """

        self._n_in = n_in

    @property
    def n_in_inscription(self):
        """Gets the n_in_inscription of this ResponsesGetTxInfoData.  # noqa: E501


        :return: The n_in_inscription of this ResponsesGetTxInfoData.  # noqa: E501
        :rtype: int
        """
        return self._n_in_inscription

    @n_in_inscription.setter
    def n_in_inscription(self, n_in_inscription):
        """Sets the n_in_inscription of this ResponsesGetTxInfoData.


        :param n_in_inscription: The n_in_inscription of this ResponsesGetTxInfoData.  # noqa: E501
        :type: int
        """

        self._n_in_inscription = n_in_inscription

    @property
    def n_lost_inscription(self):
        """Gets the n_lost_inscription of this ResponsesGetTxInfoData.  # noqa: E501


        :return: The n_lost_inscription of this ResponsesGetTxInfoData.  # noqa: E501
        :rtype: int
        """
        return self._n_lost_inscription

    @n_lost_inscription.setter
    def n_lost_inscription(self, n_lost_inscription):
        """Sets the n_lost_inscription of this ResponsesGetTxInfoData.


        :param n_lost_inscription: The n_lost_inscription of this ResponsesGetTxInfoData.  # noqa: E501
        :type: int
        """

        self._n_lost_inscription = n_lost_inscription

    @property
    def n_new_inscription(self):
        """Gets the n_new_inscription of this ResponsesGetTxInfoData.  # noqa: E501


        :return: The n_new_inscription of this ResponsesGetTxInfoData.  # noqa: E501
        :rtype: int
        """
        return self._n_new_inscription

    @n_new_inscription.setter
    def n_new_inscription(self, n_new_inscription):
        """Sets the n_new_inscription of this ResponsesGetTxInfoData.


        :param n_new_inscription: The n_new_inscription of this ResponsesGetTxInfoData.  # noqa: E501
        :type: int
        """

        self._n_new_inscription = n_new_inscription

    @property
    def n_out(self):
        """Gets the n_out of this ResponsesGetTxInfoData.  # noqa: E501


        :return: The n_out of this ResponsesGetTxInfoData.  # noqa: E501
        :rtype: int
        """
        return self._n_out

    @n_out.setter
    def n_out(self, n_out):
        """Sets the n_out of this ResponsesGetTxInfoData.


        :param n_out: The n_out of this ResponsesGetTxInfoData.  # noqa: E501
        :type: int
        """

        self._n_out = n_out

    @property
    def n_out_inscription(self):
        """Gets the n_out_inscription of this ResponsesGetTxInfoData.  # noqa: E501


        :return: The n_out_inscription of this ResponsesGetTxInfoData.  # noqa: E501
        :rtype: int
        """
        return self._n_out_inscription

    @n_out_inscription.setter
    def n_out_inscription(self, n_out_inscription):
        """Sets the n_out_inscription of this ResponsesGetTxInfoData.


        :param n_out_inscription: The n_out_inscription of this ResponsesGetTxInfoData.  # noqa: E501
        :type: int
        """

        self._n_out_inscription = n_out_inscription

    @property
    def out_satoshi(self):
        """Gets the out_satoshi of this ResponsesGetTxInfoData.  # noqa: E501


        :return: The out_satoshi of this ResponsesGetTxInfoData.  # noqa: E501
        :rtype: BigInt
        """
        return self._out_satoshi

    @out_satoshi.setter
    def out_satoshi(self, out_satoshi):
        """Sets the out_satoshi of this ResponsesGetTxInfoData.


        :param out_satoshi: The out_satoshi of this ResponsesGetTxInfoData.  # noqa: E501
        :type: BigInt
        """

        self._out_satoshi = out_satoshi

    @property
    def size(self):
        """Gets the size of this ResponsesGetTxInfoData.  # noqa: E501


        :return: The size of this ResponsesGetTxInfoData.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ResponsesGetTxInfoData.


        :param size: The size of this ResponsesGetTxInfoData.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def txid(self):
        """Gets the txid of this ResponsesGetTxInfoData.  # noqa: E501


        :return: The txid of this ResponsesGetTxInfoData.  # noqa: E501
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this ResponsesGetTxInfoData.


        :param txid: The txid of this ResponsesGetTxInfoData.  # noqa: E501
        :type: str
        """

        self._txid = txid

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
        if issubclass(ResponsesGetTxInfoData, dict):
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
        if not isinstance(other, ResponsesGetTxInfoData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
