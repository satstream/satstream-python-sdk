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

class ResponsesNonInscriptionUTXO(object):
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
        'address': 'str',
        'code_type': 'int',
        'height': 'int',
        'idx': 'int',
        'is_op_in_rbf': 'bool',
        'is_spent': 'bool',
        'satoshi': 'BigInt',
        'script_pk': 'str',
        'script_type': 'str',
        'txid': 'str',
        'vout': 'int'
    }

    attribute_map = {
        'address': 'address',
        'code_type': 'codeType',
        'height': 'height',
        'idx': 'idx',
        'is_op_in_rbf': 'isOpInRBF',
        'is_spent': 'isSpent',
        'satoshi': 'satoshi',
        'script_pk': 'scriptPk',
        'script_type': 'scriptType',
        'txid': 'txid',
        'vout': 'vout'
    }

    def __init__(self, address=None, code_type=None, height=None, idx=None, is_op_in_rbf=None, is_spent=None, satoshi=None, script_pk=None, script_type=None, txid=None, vout=None):  # noqa: E501
        """ResponsesNonInscriptionUTXO - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._code_type = None
        self._height = None
        self._idx = None
        self._is_op_in_rbf = None
        self._is_spent = None
        self._satoshi = None
        self._script_pk = None
        self._script_type = None
        self._txid = None
        self._vout = None
        self.discriminator = None
        if address is not None:
            self.address = address
        if code_type is not None:
            self.code_type = code_type
        if height is not None:
            self.height = height
        if idx is not None:
            self.idx = idx
        if is_op_in_rbf is not None:
            self.is_op_in_rbf = is_op_in_rbf
        if is_spent is not None:
            self.is_spent = is_spent
        if satoshi is not None:
            self.satoshi = satoshi
        if script_pk is not None:
            self.script_pk = script_pk
        if script_type is not None:
            self.script_type = script_type
        if txid is not None:
            self.txid = txid
        if vout is not None:
            self.vout = vout

    @property
    def address(self):
        """Gets the address of this ResponsesNonInscriptionUTXO.  # noqa: E501


        :return: The address of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ResponsesNonInscriptionUTXO.


        :param address: The address of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def code_type(self):
        """Gets the code_type of this ResponsesNonInscriptionUTXO.  # noqa: E501


        :return: The code_type of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :rtype: int
        """
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        """Sets the code_type of this ResponsesNonInscriptionUTXO.


        :param code_type: The code_type of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :type: int
        """

        self._code_type = code_type

    @property
    def height(self):
        """Gets the height of this ResponsesNonInscriptionUTXO.  # noqa: E501


        :return: The height of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ResponsesNonInscriptionUTXO.


        :param height: The height of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def idx(self):
        """Gets the idx of this ResponsesNonInscriptionUTXO.  # noqa: E501


        :return: The idx of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :rtype: int
        """
        return self._idx

    @idx.setter
    def idx(self, idx):
        """Sets the idx of this ResponsesNonInscriptionUTXO.


        :param idx: The idx of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :type: int
        """

        self._idx = idx

    @property
    def is_op_in_rbf(self):
        """Gets the is_op_in_rbf of this ResponsesNonInscriptionUTXO.  # noqa: E501


        :return: The is_op_in_rbf of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :rtype: bool
        """
        return self._is_op_in_rbf

    @is_op_in_rbf.setter
    def is_op_in_rbf(self, is_op_in_rbf):
        """Sets the is_op_in_rbf of this ResponsesNonInscriptionUTXO.


        :param is_op_in_rbf: The is_op_in_rbf of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :type: bool
        """

        self._is_op_in_rbf = is_op_in_rbf

    @property
    def is_spent(self):
        """Gets the is_spent of this ResponsesNonInscriptionUTXO.  # noqa: E501


        :return: The is_spent of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :rtype: bool
        """
        return self._is_spent

    @is_spent.setter
    def is_spent(self, is_spent):
        """Sets the is_spent of this ResponsesNonInscriptionUTXO.


        :param is_spent: The is_spent of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :type: bool
        """

        self._is_spent = is_spent

    @property
    def satoshi(self):
        """Gets the satoshi of this ResponsesNonInscriptionUTXO.  # noqa: E501


        :return: The satoshi of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :rtype: BigInt
        """
        return self._satoshi

    @satoshi.setter
    def satoshi(self, satoshi):
        """Sets the satoshi of this ResponsesNonInscriptionUTXO.


        :param satoshi: The satoshi of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :type: BigInt
        """

        self._satoshi = satoshi

    @property
    def script_pk(self):
        """Gets the script_pk of this ResponsesNonInscriptionUTXO.  # noqa: E501


        :return: The script_pk of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :rtype: str
        """
        return self._script_pk

    @script_pk.setter
    def script_pk(self, script_pk):
        """Sets the script_pk of this ResponsesNonInscriptionUTXO.


        :param script_pk: The script_pk of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :type: str
        """

        self._script_pk = script_pk

    @property
    def script_type(self):
        """Gets the script_type of this ResponsesNonInscriptionUTXO.  # noqa: E501


        :return: The script_type of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :rtype: str
        """
        return self._script_type

    @script_type.setter
    def script_type(self, script_type):
        """Sets the script_type of this ResponsesNonInscriptionUTXO.


        :param script_type: The script_type of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :type: str
        """

        self._script_type = script_type

    @property
    def txid(self):
        """Gets the txid of this ResponsesNonInscriptionUTXO.  # noqa: E501


        :return: The txid of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this ResponsesNonInscriptionUTXO.


        :param txid: The txid of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :type: str
        """

        self._txid = txid

    @property
    def vout(self):
        """Gets the vout of this ResponsesNonInscriptionUTXO.  # noqa: E501


        :return: The vout of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :rtype: int
        """
        return self._vout

    @vout.setter
    def vout(self, vout):
        """Sets the vout of this ResponsesNonInscriptionUTXO.


        :param vout: The vout of this ResponsesNonInscriptionUTXO.  # noqa: E501
        :type: int
        """

        self._vout = vout

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
        if issubclass(ResponsesNonInscriptionUTXO, dict):
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
        if not isinstance(other, ResponsesNonInscriptionUTXO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
