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

import swagger_client
from swagger_client.api.mempool_api import MempoolApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMempoolApi(unittest.TestCase):
    """MempoolApi unit test stubs"""

    def setUp(self):
        self.api = MempoolApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_address_mempool_transactions(self):
        """Test case for get_address_mempool_transactions

        Get address mempool transactions  # noqa: E501
        """
        pass

    def test_get_mempool_transaction_info(self):
        """Test case for get_mempool_transaction_info

        Get mempool transaction info  # noqa: E501
        """
        pass

    def test_get_mempool_transactions(self):
        """Test case for get_mempool_transactions

        Get mempool transactions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()