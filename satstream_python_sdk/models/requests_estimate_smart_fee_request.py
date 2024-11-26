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

class RequestsEstimateSmartFeeRequest(object):
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
        'conf_target': 'int',
        'estimate_mode': 'str'
    }

    attribute_map = {
        'conf_target': 'conf_target',
        'estimate_mode': 'estimate_mode'
    }

    def __init__(self, conf_target=None, estimate_mode=None):  # noqa: E501
        """RequestsEstimateSmartFeeRequest - a model defined in Swagger"""  # noqa: E501
        self._conf_target = None
        self._estimate_mode = None
        self.discriminator = None
        if conf_target is not None:
            self.conf_target = conf_target
        if estimate_mode is not None:
            self.estimate_mode = estimate_mode

    @property
    def conf_target(self):
        """Gets the conf_target of this RequestsEstimateSmartFeeRequest.  # noqa: E501

        Required: Confirmation target in blocks (1 - 1008)  # noqa: E501

        :return: The conf_target of this RequestsEstimateSmartFeeRequest.  # noqa: E501
        :rtype: int
        """
        return self._conf_target

    @conf_target.setter
    def conf_target(self, conf_target):
        """Sets the conf_target of this RequestsEstimateSmartFeeRequest.

        Required: Confirmation target in blocks (1 - 1008)  # noqa: E501

        :param conf_target: The conf_target of this RequestsEstimateSmartFeeRequest.  # noqa: E501
        :type: int
        """

        self._conf_target = conf_target

    @property
    def estimate_mode(self):
        """Gets the estimate_mode of this RequestsEstimateSmartFeeRequest.  # noqa: E501

        Optional: The fee estimate mode (unset, economical, conservative)  # noqa: E501

        :return: The estimate_mode of this RequestsEstimateSmartFeeRequest.  # noqa: E501
        :rtype: str
        """
        return self._estimate_mode

    @estimate_mode.setter
    def estimate_mode(self, estimate_mode):
        """Sets the estimate_mode of this RequestsEstimateSmartFeeRequest.

        Optional: The fee estimate mode (unset, economical, conservative)  # noqa: E501

        :param estimate_mode: The estimate_mode of this RequestsEstimateSmartFeeRequest.  # noqa: E501
        :type: str
        """

        self._estimate_mode = estimate_mode

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
        if issubclass(RequestsEstimateSmartFeeRequest, dict):
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
        if not isinstance(other, RequestsEstimateSmartFeeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
