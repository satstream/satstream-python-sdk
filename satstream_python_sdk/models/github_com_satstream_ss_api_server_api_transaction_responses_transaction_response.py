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

class GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse(object):
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
        'code': 'int',
        'data': 'GithubComSatstreamSsUtilsOrdServerResponsesTransactionResponse',
        'msg': 'str'
    }

    attribute_map = {
        'code': 'code',
        'data': 'data',
        'msg': 'msg'
    }

    def __init__(self, code=None, data=None, msg=None):  # noqa: E501
        """GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._data = None
        self._msg = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if data is not None:
            self.data = data
        if msg is not None:
            self.msg = msg

    @property
    def code(self):
        """Gets the code of this GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse.  # noqa: E501


        :return: The code of this GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse.


        :param code: The code of this GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def data(self):
        """Gets the data of this GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse.  # noqa: E501


        :return: The data of this GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse.  # noqa: E501
        :rtype: GithubComSatstreamSsUtilsOrdServerResponsesTransactionResponse
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse.


        :param data: The data of this GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse.  # noqa: E501
        :type: GithubComSatstreamSsUtilsOrdServerResponsesTransactionResponse
        """

        self._data = data

    @property
    def msg(self):
        """Gets the msg of this GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse.  # noqa: E501


        :return: The msg of this GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse.


        :param msg: The msg of this GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse.  # noqa: E501
        :type: str
        """

        self._msg = msg

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
        if issubclass(GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse, dict):
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
        if not isinstance(other, GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
