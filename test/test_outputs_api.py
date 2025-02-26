# coding: utf-8

"""
    Satstream API

    Satstream API  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: team@satstream.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import satstream_python_sdk
from satstream_python_sdk.api.outputs_api import OutputsApi  # noqa: E501
from satstream_python_sdk.rest import ApiException


class TestOutputsApi(unittest.TestCase):
    """OutputsApi unit test stubs"""

    def setUp(self):
        self.api = OutputsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_output_by_outpoint(self):
        """Test case for get_output_by_outpoint

        Get output info by outpoint  # noqa: E501
        """
        pass

    def test_get_outputs(self):
        """Test case for get_outputs

        Get multiple outputs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
