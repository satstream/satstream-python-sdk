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
from satstream_python_sdk.api.status_api import StatusApi  # noqa: E501
from satstream_python_sdk.rest import ApiException


class TestStatusApi(unittest.TestCase):
    """StatusApi unit test stubs"""

    def setUp(self):
        self.api = StatusApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_status(self):
        """Test case for get_status

        Get server status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
