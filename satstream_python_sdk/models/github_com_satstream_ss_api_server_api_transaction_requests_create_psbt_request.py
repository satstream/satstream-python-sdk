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

class GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest(object):
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
        'inputs': 'list[GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTInput]',
        'locktime': 'int',
        'outputs': 'list[GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTOutput]',
        'replaceable': 'bool'
    }

    attribute_map = {
        'inputs': 'inputs',
        'locktime': 'locktime',
        'outputs': 'outputs',
        'replaceable': 'replaceable'
    }

    def __init__(self, inputs=None, locktime=None, outputs=None, replaceable=None):  # noqa: E501
        """GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest - a model defined in Swagger"""  # noqa: E501
        self._inputs = None
        self._locktime = None
        self._outputs = None
        self._replaceable = None
        self.discriminator = None
        self.inputs = inputs
        if locktime is not None:
            self.locktime = locktime
        self.outputs = outputs
        if replaceable is not None:
            self.replaceable = replaceable

    @property
    def inputs(self):
        """Gets the inputs of this GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest.  # noqa: E501

        The inputs for the transaction  # noqa: E501

        :return: The inputs of this GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest.  # noqa: E501
        :rtype: list[GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTInput]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest.

        The inputs for the transaction  # noqa: E501

        :param inputs: The inputs of this GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest.  # noqa: E501
        :type: list[GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTInput]
        """
        if inputs is None:
            raise ValueError("Invalid value for `inputs`, must not be `None`")  # noqa: E501

        self._inputs = inputs

    @property
    def locktime(self):
        """Gets the locktime of this GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest.  # noqa: E501

        Raw locktime. Non-0 value also locktime-activates inputs Optional, defaults to 0  # noqa: E501

        :return: The locktime of this GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest.  # noqa: E501
        :rtype: int
        """
        return self._locktime

    @locktime.setter
    def locktime(self, locktime):
        """Sets the locktime of this GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest.

        Raw locktime. Non-0 value also locktime-activates inputs Optional, defaults to 0  # noqa: E501

        :param locktime: The locktime of this GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest.  # noqa: E501
        :type: int
        """

        self._locktime = locktime

    @property
    def outputs(self):
        """Gets the outputs of this GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest.  # noqa: E501

        The outputs for the transaction Each address can only appear once and there can only be one 'data' object  # noqa: E501

        :return: The outputs of this GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest.  # noqa: E501
        :rtype: list[GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest.

        The outputs for the transaction Each address can only appear once and there can only be one 'data' object  # noqa: E501

        :param outputs: The outputs of this GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest.  # noqa: E501
        :type: list[GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTOutput]
        """
        if outputs is None:
            raise ValueError("Invalid value for `outputs`, must not be `None`")  # noqa: E501

        self._outputs = outputs

    @property
    def replaceable(self):
        """Gets the replaceable of this GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest.  # noqa: E501

        Marks this transaction as BIP125-replaceable Allows this transaction to be replaced by a transaction with higher fees If provided, it is an error if explicit sequence numbers are incompatible Optional, defaults to true  # noqa: E501

        :return: The replaceable of this GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest.  # noqa: E501
        :rtype: bool
        """
        return self._replaceable

    @replaceable.setter
    def replaceable(self, replaceable):
        """Sets the replaceable of this GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest.

        Marks this transaction as BIP125-replaceable Allows this transaction to be replaced by a transaction with higher fees If provided, it is an error if explicit sequence numbers are incompatible Optional, defaults to true  # noqa: E501

        :param replaceable: The replaceable of this GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest.  # noqa: E501
        :type: bool
        """

        self._replaceable = replaceable

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
        if issubclass(GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest, dict):
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
        if not isinstance(other, GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
