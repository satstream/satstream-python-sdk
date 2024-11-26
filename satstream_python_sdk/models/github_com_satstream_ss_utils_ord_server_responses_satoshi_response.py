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

class GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse(object):
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
        'block': 'int',
        'charms': 'list[str]',
        'cycle': 'int',
        'decimal': 'str',
        'degree': 'str',
        'epoch': 'int',
        'inscriptions': 'list[str]',
        'name': 'str',
        'number': 'int',
        'offset': 'int',
        'percentile': 'str',
        'period': 'int',
        'rarity': 'str',
        'satpoint': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'block': 'block',
        'charms': 'charms',
        'cycle': 'cycle',
        'decimal': 'decimal',
        'degree': 'degree',
        'epoch': 'epoch',
        'inscriptions': 'inscriptions',
        'name': 'name',
        'number': 'number',
        'offset': 'offset',
        'percentile': 'percentile',
        'period': 'period',
        'rarity': 'rarity',
        'satpoint': 'satpoint',
        'timestamp': 'timestamp'
    }

    def __init__(self, block=None, charms=None, cycle=None, decimal=None, degree=None, epoch=None, inscriptions=None, name=None, number=None, offset=None, percentile=None, period=None, rarity=None, satpoint=None, timestamp=None):  # noqa: E501
        """GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse - a model defined in Swagger"""  # noqa: E501
        self._block = None
        self._charms = None
        self._cycle = None
        self._decimal = None
        self._degree = None
        self._epoch = None
        self._inscriptions = None
        self._name = None
        self._number = None
        self._offset = None
        self._percentile = None
        self._period = None
        self._rarity = None
        self._satpoint = None
        self._timestamp = None
        self.discriminator = None
        if block is not None:
            self.block = block
        if charms is not None:
            self.charms = charms
        if cycle is not None:
            self.cycle = cycle
        if decimal is not None:
            self.decimal = decimal
        if degree is not None:
            self.degree = degree
        if epoch is not None:
            self.epoch = epoch
        if inscriptions is not None:
            self.inscriptions = inscriptions
        if name is not None:
            self.name = name
        if number is not None:
            self.number = number
        if offset is not None:
            self.offset = offset
        if percentile is not None:
            self.percentile = percentile
        if period is not None:
            self.period = period
        if rarity is not None:
            self.rarity = rarity
        if satpoint is not None:
            self.satpoint = satpoint
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def block(self):
        """Gets the block of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501


        :return: The block of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :rtype: int
        """
        return self._block

    @block.setter
    def block(self, block):
        """Sets the block of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.


        :param block: The block of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :type: int
        """

        self._block = block

    @property
    def charms(self):
        """Gets the charms of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501


        :return: The charms of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._charms

    @charms.setter
    def charms(self, charms):
        """Sets the charms of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.


        :param charms: The charms of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :type: list[str]
        """

        self._charms = charms

    @property
    def cycle(self):
        """Gets the cycle of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501


        :return: The cycle of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :rtype: int
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.


        :param cycle: The cycle of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :type: int
        """

        self._cycle = cycle

    @property
    def decimal(self):
        """Gets the decimal of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501


        :return: The decimal of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :rtype: str
        """
        return self._decimal

    @decimal.setter
    def decimal(self, decimal):
        """Sets the decimal of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.


        :param decimal: The decimal of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :type: str
        """

        self._decimal = decimal

    @property
    def degree(self):
        """Gets the degree of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501


        :return: The degree of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :rtype: str
        """
        return self._degree

    @degree.setter
    def degree(self, degree):
        """Sets the degree of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.


        :param degree: The degree of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :type: str
        """

        self._degree = degree

    @property
    def epoch(self):
        """Gets the epoch of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501


        :return: The epoch of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :rtype: int
        """
        return self._epoch

    @epoch.setter
    def epoch(self, epoch):
        """Sets the epoch of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.


        :param epoch: The epoch of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :type: int
        """

        self._epoch = epoch

    @property
    def inscriptions(self):
        """Gets the inscriptions of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501


        :return: The inscriptions of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._inscriptions

    @inscriptions.setter
    def inscriptions(self, inscriptions):
        """Sets the inscriptions of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.


        :param inscriptions: The inscriptions of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :type: list[str]
        """

        self._inscriptions = inscriptions

    @property
    def name(self):
        """Gets the name of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501


        :return: The name of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.


        :param name: The name of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501


        :return: The number of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.


        :param number: The number of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def offset(self):
        """Gets the offset of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501


        :return: The offset of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.


        :param offset: The offset of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def percentile(self):
        """Gets the percentile of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501


        :return: The percentile of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :rtype: str
        """
        return self._percentile

    @percentile.setter
    def percentile(self, percentile):
        """Sets the percentile of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.


        :param percentile: The percentile of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :type: str
        """

        self._percentile = percentile

    @property
    def period(self):
        """Gets the period of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501


        :return: The period of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.


        :param period: The period of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def rarity(self):
        """Gets the rarity of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501


        :return: The rarity of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :rtype: str
        """
        return self._rarity

    @rarity.setter
    def rarity(self, rarity):
        """Sets the rarity of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.


        :param rarity: The rarity of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :type: str
        """

        self._rarity = rarity

    @property
    def satpoint(self):
        """Gets the satpoint of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501


        :return: The satpoint of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :rtype: str
        """
        return self._satpoint

    @satpoint.setter
    def satpoint(self, satpoint):
        """Sets the satpoint of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.


        :param satpoint: The satpoint of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :type: str
        """

        self._satpoint = satpoint

    @property
    def timestamp(self):
        """Gets the timestamp of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501


        :return: The timestamp of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.


        :param timestamp: The timestamp of this GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

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
        if issubclass(GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse, dict):
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
        if not isinstance(other, GithubComSatstreamSsUtilsOrdServerResponsesSatoshiResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
