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

class MempoolInfo(object):
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
        'bytes': 'int',
        'fullrbf': 'bool',
        'incrementalrelayfee': 'float',
        'loaded': 'bool',
        'maxmempool': 'int',
        'mempoolminfee': 'float',
        'minrelaytxfee': 'float',
        'size': 'int',
        'total_fee': 'float',
        'unbroadcastcount': 'int',
        'usage': 'int'
    }

    attribute_map = {
        'bytes': 'bytes',
        'fullrbf': 'fullrbf',
        'incrementalrelayfee': 'incrementalrelayfee',
        'loaded': 'loaded',
        'maxmempool': 'maxmempool',
        'mempoolminfee': 'mempoolminfee',
        'minrelaytxfee': 'minrelaytxfee',
        'size': 'size',
        'total_fee': 'total_fee',
        'unbroadcastcount': 'unbroadcastcount',
        'usage': 'usage'
    }

    def __init__(self, bytes=None, fullrbf=None, incrementalrelayfee=None, loaded=None, maxmempool=None, mempoolminfee=None, minrelaytxfee=None, size=None, total_fee=None, unbroadcastcount=None, usage=None):  # noqa: E501
        """MempoolInfo - a model defined in Swagger"""  # noqa: E501
        self._bytes = None
        self._fullrbf = None
        self._incrementalrelayfee = None
        self._loaded = None
        self._maxmempool = None
        self._mempoolminfee = None
        self._minrelaytxfee = None
        self._size = None
        self._total_fee = None
        self._unbroadcastcount = None
        self._usage = None
        self.discriminator = None
        if bytes is not None:
            self.bytes = bytes
        if fullrbf is not None:
            self.fullrbf = fullrbf
        if incrementalrelayfee is not None:
            self.incrementalrelayfee = incrementalrelayfee
        if loaded is not None:
            self.loaded = loaded
        if maxmempool is not None:
            self.maxmempool = maxmempool
        if mempoolminfee is not None:
            self.mempoolminfee = mempoolminfee
        if minrelaytxfee is not None:
            self.minrelaytxfee = minrelaytxfee
        if size is not None:
            self.size = size
        if total_fee is not None:
            self.total_fee = total_fee
        if unbroadcastcount is not None:
            self.unbroadcastcount = unbroadcastcount
        if usage is not None:
            self.usage = usage

    @property
    def bytes(self):
        """Gets the bytes of this MempoolInfo.  # noqa: E501

        Sum of all virtual transaction sizes  # noqa: E501

        :return: The bytes of this MempoolInfo.  # noqa: E501
        :rtype: int
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        """Sets the bytes of this MempoolInfo.

        Sum of all virtual transaction sizes  # noqa: E501

        :param bytes: The bytes of this MempoolInfo.  # noqa: E501
        :type: int
        """

        self._bytes = bytes

    @property
    def fullrbf(self):
        """Gets the fullrbf of this MempoolInfo.  # noqa: E501

        True if mempool accepts RBF without signaling inspection  # noqa: E501

        :return: The fullrbf of this MempoolInfo.  # noqa: E501
        :rtype: bool
        """
        return self._fullrbf

    @fullrbf.setter
    def fullrbf(self, fullrbf):
        """Sets the fullrbf of this MempoolInfo.

        True if mempool accepts RBF without signaling inspection  # noqa: E501

        :param fullrbf: The fullrbf of this MempoolInfo.  # noqa: E501
        :type: bool
        """

        self._fullrbf = fullrbf

    @property
    def incrementalrelayfee(self):
        """Gets the incrementalrelayfee of this MempoolInfo.  # noqa: E501

        Minimum fee rate increment for mempool limiting  # noqa: E501

        :return: The incrementalrelayfee of this MempoolInfo.  # noqa: E501
        :rtype: float
        """
        return self._incrementalrelayfee

    @incrementalrelayfee.setter
    def incrementalrelayfee(self, incrementalrelayfee):
        """Sets the incrementalrelayfee of this MempoolInfo.

        Minimum fee rate increment for mempool limiting  # noqa: E501

        :param incrementalrelayfee: The incrementalrelayfee of this MempoolInfo.  # noqa: E501
        :type: float
        """

        self._incrementalrelayfee = incrementalrelayfee

    @property
    def loaded(self):
        """Gets the loaded of this MempoolInfo.  # noqa: E501

        True if the mempool is fully loaded  # noqa: E501

        :return: The loaded of this MempoolInfo.  # noqa: E501
        :rtype: bool
        """
        return self._loaded

    @loaded.setter
    def loaded(self, loaded):
        """Sets the loaded of this MempoolInfo.

        True if the mempool is fully loaded  # noqa: E501

        :param loaded: The loaded of this MempoolInfo.  # noqa: E501
        :type: bool
        """

        self._loaded = loaded

    @property
    def maxmempool(self):
        """Gets the maxmempool of this MempoolInfo.  # noqa: E501

        Maximum memory usage for the mempool  # noqa: E501

        :return: The maxmempool of this MempoolInfo.  # noqa: E501
        :rtype: int
        """
        return self._maxmempool

    @maxmempool.setter
    def maxmempool(self, maxmempool):
        """Sets the maxmempool of this MempoolInfo.

        Maximum memory usage for the mempool  # noqa: E501

        :param maxmempool: The maxmempool of this MempoolInfo.  # noqa: E501
        :type: int
        """

        self._maxmempool = maxmempool

    @property
    def mempoolminfee(self):
        """Gets the mempoolminfee of this MempoolInfo.  # noqa: E501

        Minimum fee rate in BTC/kvB for tx to be accepted  # noqa: E501

        :return: The mempoolminfee of this MempoolInfo.  # noqa: E501
        :rtype: float
        """
        return self._mempoolminfee

    @mempoolminfee.setter
    def mempoolminfee(self, mempoolminfee):
        """Sets the mempoolminfee of this MempoolInfo.

        Minimum fee rate in BTC/kvB for tx to be accepted  # noqa: E501

        :param mempoolminfee: The mempoolminfee of this MempoolInfo.  # noqa: E501
        :type: float
        """

        self._mempoolminfee = mempoolminfee

    @property
    def minrelaytxfee(self):
        """Gets the minrelaytxfee of this MempoolInfo.  # noqa: E501

        Current minimum relay fee for transactions  # noqa: E501

        :return: The minrelaytxfee of this MempoolInfo.  # noqa: E501
        :rtype: float
        """
        return self._minrelaytxfee

    @minrelaytxfee.setter
    def minrelaytxfee(self, minrelaytxfee):
        """Sets the minrelaytxfee of this MempoolInfo.

        Current minimum relay fee for transactions  # noqa: E501

        :param minrelaytxfee: The minrelaytxfee of this MempoolInfo.  # noqa: E501
        :type: float
        """

        self._minrelaytxfee = minrelaytxfee

    @property
    def size(self):
        """Gets the size of this MempoolInfo.  # noqa: E501

        Current tx count  # noqa: E501

        :return: The size of this MempoolInfo.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this MempoolInfo.

        Current tx count  # noqa: E501

        :param size: The size of this MempoolInfo.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def total_fee(self):
        """Gets the total_fee of this MempoolInfo.  # noqa: E501

        Total fees for the mempool in BTC  # noqa: E501

        :return: The total_fee of this MempoolInfo.  # noqa: E501
        :rtype: float
        """
        return self._total_fee

    @total_fee.setter
    def total_fee(self, total_fee):
        """Sets the total_fee of this MempoolInfo.

        Total fees for the mempool in BTC  # noqa: E501

        :param total_fee: The total_fee of this MempoolInfo.  # noqa: E501
        :type: float
        """

        self._total_fee = total_fee

    @property
    def unbroadcastcount(self):
        """Gets the unbroadcastcount of this MempoolInfo.  # noqa: E501

        Number of unbroadcast transactions  # noqa: E501

        :return: The unbroadcastcount of this MempoolInfo.  # noqa: E501
        :rtype: int
        """
        return self._unbroadcastcount

    @unbroadcastcount.setter
    def unbroadcastcount(self, unbroadcastcount):
        """Sets the unbroadcastcount of this MempoolInfo.

        Number of unbroadcast transactions  # noqa: E501

        :param unbroadcastcount: The unbroadcastcount of this MempoolInfo.  # noqa: E501
        :type: int
        """

        self._unbroadcastcount = unbroadcastcount

    @property
    def usage(self):
        """Gets the usage of this MempoolInfo.  # noqa: E501

        Total memory usage for the mempool  # noqa: E501

        :return: The usage of this MempoolInfo.  # noqa: E501
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this MempoolInfo.

        Total memory usage for the mempool  # noqa: E501

        :param usage: The usage of this MempoolInfo.  # noqa: E501
        :type: int
        """

        self._usage = usage

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
        if issubclass(MempoolInfo, dict):
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
        if not isinstance(other, MempoolInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
