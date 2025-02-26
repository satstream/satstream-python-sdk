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
from satstream_python_sdk.api.blocks_api import BlocksApi  # noqa: E501
from satstream_python_sdk.rest import ApiException


class TestBlocksApi(unittest.TestCase):
    """BlocksApi unit test stubs"""

    def setUp(self):
        self.api = BlocksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_block_count(self):
        """Test case for get_block_count

        Get the height of the latest block  # noqa: E501
        """
        pass

    def test_get_block_decoded(self):
        """Test case for get_block_decoded

        Get block by hash or height (verbosity 2)  # noqa: E501
        """
        pass

    def test_get_block_hash_by_height(self):
        """Test case for get_block_hash_by_height

        Returns blockhash of specified block.  # noqa: E501
        """
        pass

    def test_get_block_hex(self):
        """Test case for get_block_hex

        Get block by hash or height (verbosity 0)  # noqa: E501
        """
        pass

    def test_get_block_info(self):
        """Test case for get_block_info

        Get block info by hash or height  # noqa: E501
        """
        pass

    def test_get_block_prevout(self):
        """Test case for get_block_prevout

        Get block by hash or height (verbosity 3)  # noqa: E501
        """
        pass

    def test_get_block_stats(self):
        """Test case for get_block_stats

        Get block stats  # noqa: E501
        """
        pass

    def test_get_block_summary(self):
        """Test case for get_block_summary

        Get block by hash or height (verbosity 1)  # noqa: E501
        """
        pass

    def test_get_blockchain_info(self):
        """Test case for get_blockchain_info

        Get blockchain information  # noqa: E501
        """
        pass

    def test_get_blocks(self):
        """Test case for get_blocks

        Returns the latest block height, last 100 block hashes, and featured inscriptions  # noqa: E501
        """
        pass

    def test_get_latest_block_height(self):
        """Test case for get_latest_block_height

        Returns the height of the latest block.  # noqa: E501
        """
        pass

    def test_get_latest_blockhash(self):
        """Test case for get_latest_blockhash

        Returns blockhash for the latest block.  # noqa: E501
        """
        pass

    def test_get_latest_blocktime(self):
        """Test case for get_latest_blocktime

        Get the timestamp of the latest block  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
