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

import satstream-python-sdk
from satstream-python-sdk.api.blocks_api import BlocksApi  # noqa: E501
from satstream-python-sdk.rest import ApiException


class TestBlocksApi(unittest.TestCase):
    """BlocksApi unit test stubs"""

    def setUp(self):
        self.api = BlocksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_block_by_hash(self):
        """Test case for get_block_by_hash

        Get block by hash  # noqa: E501
        """
        pass

    def test_get_block_info(self):
        """Test case for get_block_info

        Get block info  # noqa: E501
        """
        pass

    def test_get_block_transactions(self):
        """Test case for get_block_transactions

        Get block transactions  # noqa: E501
        """
        pass

    def test_get_current_block_height(self):
        """Test case for get_current_block_height

        Get current block height  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
