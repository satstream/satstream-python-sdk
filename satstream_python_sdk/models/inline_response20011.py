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
from satstream_python_sdk.models.utils_response_envelope import UtilsResponseEnvelope  # noqa: F401,E501

class InlineResponse20011(UtilsResponseEnvelope):
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
        'data': 'RawFeeEstimate'
    }
    if hasattr(UtilsResponseEnvelope, "swagger_types"):
        swagger_types.update(UtilsResponseEnvelope.swagger_types)

    attribute_map = {
        'data': 'data'
    }
    if hasattr(UtilsResponseEnvelope, "attribute_map"):
        attribute_map.update(UtilsResponseEnvelope.attribute_map)

    def __init__(self, data=None, *args, **kwargs):  # noqa: E501
        """InlineResponse20011 - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self.discriminator = None
        if data is not None:
            self.data = data
        UtilsResponseEnvelope.__init__(self, *args, **kwargs)

    @property
    def data(self):
        """Gets the data of this InlineResponse20011.  # noqa: E501


        :return: The data of this InlineResponse20011.  # noqa: E501
        :rtype: RawFeeEstimate
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse20011.


        :param data: The data of this InlineResponse20011.  # noqa: E501
        :type: RawFeeEstimate
        """

        self._data = data

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
        if issubclass(InlineResponse20011, dict):
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
        if not isinstance(other, InlineResponse20011):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
