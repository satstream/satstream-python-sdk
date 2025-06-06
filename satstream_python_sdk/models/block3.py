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

class Block3(object):
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
        'bits': 'str',
        'chainwork': 'str',
        'confirmations': 'int',
        'difficulty': 'float',
        'hash': 'str',
        'height': 'int',
        'mediantime': 'int',
        'merkleroot': 'str',
        'n_tx': 'int',
        'nextblockhash': 'str',
        'nonce': 'int',
        'previousblockhash': 'str',
        'size': 'int',
        'strippedsize': 'int',
        'time': 'int',
        'tx': 'list[BtcTx3]',
        'version': 'int',
        'version_hex': 'str',
        'weight': 'int'
    }

    attribute_map = {
        'bits': 'bits',
        'chainwork': 'chainwork',
        'confirmations': 'confirmations',
        'difficulty': 'difficulty',
        'hash': 'hash',
        'height': 'height',
        'mediantime': 'mediantime',
        'merkleroot': 'merkleroot',
        'n_tx': 'nTx',
        'nextblockhash': 'nextblockhash',
        'nonce': 'nonce',
        'previousblockhash': 'previousblockhash',
        'size': 'size',
        'strippedsize': 'strippedsize',
        'time': 'time',
        'tx': 'tx',
        'version': 'version',
        'version_hex': 'versionHex',
        'weight': 'weight'
    }

    def __init__(self, bits=None, chainwork=None, confirmations=None, difficulty=None, hash=None, height=None, mediantime=None, merkleroot=None, n_tx=None, nextblockhash=None, nonce=None, previousblockhash=None, size=None, strippedsize=None, time=None, tx=None, version=None, version_hex=None, weight=None):  # noqa: E501
        """Block3 - a model defined in Swagger"""  # noqa: E501
        self._bits = None
        self._chainwork = None
        self._confirmations = None
        self._difficulty = None
        self._hash = None
        self._height = None
        self._mediantime = None
        self._merkleroot = None
        self._n_tx = None
        self._nextblockhash = None
        self._nonce = None
        self._previousblockhash = None
        self._size = None
        self._strippedsize = None
        self._time = None
        self._tx = None
        self._version = None
        self._version_hex = None
        self._weight = None
        self.discriminator = None
        if bits is not None:
            self.bits = bits
        if chainwork is not None:
            self.chainwork = chainwork
        if confirmations is not None:
            self.confirmations = confirmations
        if difficulty is not None:
            self.difficulty = difficulty
        if hash is not None:
            self.hash = hash
        if height is not None:
            self.height = height
        if mediantime is not None:
            self.mediantime = mediantime
        if merkleroot is not None:
            self.merkleroot = merkleroot
        if n_tx is not None:
            self.n_tx = n_tx
        if nextblockhash is not None:
            self.nextblockhash = nextblockhash
        if nonce is not None:
            self.nonce = nonce
        if previousblockhash is not None:
            self.previousblockhash = previousblockhash
        if size is not None:
            self.size = size
        if strippedsize is not None:
            self.strippedsize = strippedsize
        if time is not None:
            self.time = time
        if tx is not None:
            self.tx = tx
        if version is not None:
            self.version = version
        if version_hex is not None:
            self.version_hex = version_hex
        if weight is not None:
            self.weight = weight

    @property
    def bits(self):
        """Gets the bits of this Block3.  # noqa: E501


        :return: The bits of this Block3.  # noqa: E501
        :rtype: str
        """
        return self._bits

    @bits.setter
    def bits(self, bits):
        """Sets the bits of this Block3.


        :param bits: The bits of this Block3.  # noqa: E501
        :type: str
        """

        self._bits = bits

    @property
    def chainwork(self):
        """Gets the chainwork of this Block3.  # noqa: E501


        :return: The chainwork of this Block3.  # noqa: E501
        :rtype: str
        """
        return self._chainwork

    @chainwork.setter
    def chainwork(self, chainwork):
        """Sets the chainwork of this Block3.


        :param chainwork: The chainwork of this Block3.  # noqa: E501
        :type: str
        """

        self._chainwork = chainwork

    @property
    def confirmations(self):
        """Gets the confirmations of this Block3.  # noqa: E501


        :return: The confirmations of this Block3.  # noqa: E501
        :rtype: int
        """
        return self._confirmations

    @confirmations.setter
    def confirmations(self, confirmations):
        """Sets the confirmations of this Block3.


        :param confirmations: The confirmations of this Block3.  # noqa: E501
        :type: int
        """

        self._confirmations = confirmations

    @property
    def difficulty(self):
        """Gets the difficulty of this Block3.  # noqa: E501


        :return: The difficulty of this Block3.  # noqa: E501
        :rtype: float
        """
        return self._difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        """Sets the difficulty of this Block3.


        :param difficulty: The difficulty of this Block3.  # noqa: E501
        :type: float
        """

        self._difficulty = difficulty

    @property
    def hash(self):
        """Gets the hash of this Block3.  # noqa: E501


        :return: The hash of this Block3.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this Block3.


        :param hash: The hash of this Block3.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def height(self):
        """Gets the height of this Block3.  # noqa: E501


        :return: The height of this Block3.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Block3.


        :param height: The height of this Block3.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def mediantime(self):
        """Gets the mediantime of this Block3.  # noqa: E501


        :return: The mediantime of this Block3.  # noqa: E501
        :rtype: int
        """
        return self._mediantime

    @mediantime.setter
    def mediantime(self, mediantime):
        """Sets the mediantime of this Block3.


        :param mediantime: The mediantime of this Block3.  # noqa: E501
        :type: int
        """

        self._mediantime = mediantime

    @property
    def merkleroot(self):
        """Gets the merkleroot of this Block3.  # noqa: E501


        :return: The merkleroot of this Block3.  # noqa: E501
        :rtype: str
        """
        return self._merkleroot

    @merkleroot.setter
    def merkleroot(self, merkleroot):
        """Sets the merkleroot of this Block3.


        :param merkleroot: The merkleroot of this Block3.  # noqa: E501
        :type: str
        """

        self._merkleroot = merkleroot

    @property
    def n_tx(self):
        """Gets the n_tx of this Block3.  # noqa: E501


        :return: The n_tx of this Block3.  # noqa: E501
        :rtype: int
        """
        return self._n_tx

    @n_tx.setter
    def n_tx(self, n_tx):
        """Sets the n_tx of this Block3.


        :param n_tx: The n_tx of this Block3.  # noqa: E501
        :type: int
        """

        self._n_tx = n_tx

    @property
    def nextblockhash(self):
        """Gets the nextblockhash of this Block3.  # noqa: E501


        :return: The nextblockhash of this Block3.  # noqa: E501
        :rtype: str
        """
        return self._nextblockhash

    @nextblockhash.setter
    def nextblockhash(self, nextblockhash):
        """Sets the nextblockhash of this Block3.


        :param nextblockhash: The nextblockhash of this Block3.  # noqa: E501
        :type: str
        """

        self._nextblockhash = nextblockhash

    @property
    def nonce(self):
        """Gets the nonce of this Block3.  # noqa: E501


        :return: The nonce of this Block3.  # noqa: E501
        :rtype: int
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """Sets the nonce of this Block3.


        :param nonce: The nonce of this Block3.  # noqa: E501
        :type: int
        """

        self._nonce = nonce

    @property
    def previousblockhash(self):
        """Gets the previousblockhash of this Block3.  # noqa: E501


        :return: The previousblockhash of this Block3.  # noqa: E501
        :rtype: str
        """
        return self._previousblockhash

    @previousblockhash.setter
    def previousblockhash(self, previousblockhash):
        """Sets the previousblockhash of this Block3.


        :param previousblockhash: The previousblockhash of this Block3.  # noqa: E501
        :type: str
        """

        self._previousblockhash = previousblockhash

    @property
    def size(self):
        """Gets the size of this Block3.  # noqa: E501


        :return: The size of this Block3.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Block3.


        :param size: The size of this Block3.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def strippedsize(self):
        """Gets the strippedsize of this Block3.  # noqa: E501


        :return: The strippedsize of this Block3.  # noqa: E501
        :rtype: int
        """
        return self._strippedsize

    @strippedsize.setter
    def strippedsize(self, strippedsize):
        """Sets the strippedsize of this Block3.


        :param strippedsize: The strippedsize of this Block3.  # noqa: E501
        :type: int
        """

        self._strippedsize = strippedsize

    @property
    def time(self):
        """Gets the time of this Block3.  # noqa: E501


        :return: The time of this Block3.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Block3.


        :param time: The time of this Block3.  # noqa: E501
        :type: int
        """

        self._time = time

    @property
    def tx(self):
        """Gets the tx of this Block3.  # noqa: E501

        List of fully detailed transactions  # noqa: E501

        :return: The tx of this Block3.  # noqa: E501
        :rtype: list[BtcTx3]
        """
        return self._tx

    @tx.setter
    def tx(self, tx):
        """Sets the tx of this Block3.

        List of fully detailed transactions  # noqa: E501

        :param tx: The tx of this Block3.  # noqa: E501
        :type: list[BtcTx3]
        """

        self._tx = tx

    @property
    def version(self):
        """Gets the version of this Block3.  # noqa: E501


        :return: The version of this Block3.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Block3.


        :param version: The version of this Block3.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def version_hex(self):
        """Gets the version_hex of this Block3.  # noqa: E501


        :return: The version_hex of this Block3.  # noqa: E501
        :rtype: str
        """
        return self._version_hex

    @version_hex.setter
    def version_hex(self, version_hex):
        """Sets the version_hex of this Block3.


        :param version_hex: The version_hex of this Block3.  # noqa: E501
        :type: str
        """

        self._version_hex = version_hex

    @property
    def weight(self):
        """Gets the weight of this Block3.  # noqa: E501


        :return: The weight of this Block3.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Block3.


        :param weight: The weight of this Block3.  # noqa: E501
        :type: int
        """

        self._weight = weight

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
        if issubclass(Block3, dict):
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
        if not isinstance(other, Block3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
