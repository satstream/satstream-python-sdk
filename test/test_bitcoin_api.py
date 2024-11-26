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
from satstream_python_sdk.api.bitcoin_api import BitcoinApi  # noqa: E501
from satstream_python_sdk.rest import ApiException


class TestBitcoinApi(unittest.TestCase):
    """BitcoinApi unit test stubs"""

    def setUp(self):
        self.api = BitcoinApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_analyze_psbt(self):
        """Test case for analyze_psbt

        Analyze PSBT  # noqa: E501
        """
        pass

    def test_combine_psbt(self):
        """Test case for combine_psbt

        Combine PSBTs  # noqa: E501
        """
        pass

    def test_combine_raw_transaction(self):
        """Test case for combine_raw_transaction

        Combine Raw Transactions  # noqa: E501
        """
        pass

    def test_convert_to_psbt(self):
        """Test case for convert_to_psbt

        Convert Raw Transaction to PSBT  # noqa: E501
        """
        pass

    def test_create_psbt(self):
        """Test case for create_psbt

        Create PSBT  # noqa: E501
        """
        pass

    def test_create_raw_transaction(self):
        """Test case for create_raw_transaction

        Create Raw Transaction  # noqa: E501
        """
        pass

    def test_decode_psbt(self):
        """Test case for decode_psbt

        Decode PSBT  # noqa: E501
        """
        pass

    def test_decode_script(self):
        """Test case for decode_script

        Decode Script  # noqa: E501
        """
        pass

    def test_estimate_raw_fee(self):
        """Test case for estimate_raw_fee

        Estimate Raw Fee  # noqa: E501
        """
        pass

    def test_estimate_smart_fee(self):
        """Test case for estimate_smart_fee

        Estimate smart fee  # noqa: E501
        """
        pass

    def test_get_block_by_hash_decoded(self):
        """Test case for get_block_by_hash_decoded

        Get block by hash (verbosity 2)  # noqa: E501
        """
        pass

    def test_get_block_by_hash_hex(self):
        """Test case for get_block_by_hash_hex

        Get block by hash (verbosity 0)  # noqa: E501
        """
        pass

    def test_get_block_by_hash_prevout(self):
        """Test case for get_block_by_hash_prevout

        Get block by hash (verbosity 3)  # noqa: E501
        """
        pass

    def test_get_block_by_hash_summary(self):
        """Test case for get_block_by_hash_summary

        Get block by hash (verbosity 1)  # noqa: E501
        """
        pass

    def test_get_block_by_height_decoded(self):
        """Test case for get_block_by_height_decoded

        Get block by height (verbosity 2)  # noqa: E501
        """
        pass

    def test_get_block_by_height_hex(self):
        """Test case for get_block_by_height_hex

        Get block by height (verbosity 0)  # noqa: E501
        """
        pass

    def test_get_block_by_height_prevout(self):
        """Test case for get_block_by_height_prevout

        Get block by height (verbosity 3)  # noqa: E501
        """
        pass

    def test_get_block_by_height_summary(self):
        """Test case for get_block_by_height_summary

        Get block by height (verbosity 1)  # noqa: E501
        """
        pass

    def test_get_block_stats(self):
        """Test case for get_block_stats

        Get block stats  # noqa: E501
        """
        pass

    def test_get_blockchain_info(self):
        """Test case for get_blockchain_info

        Get blockchain information  # noqa: E501
        """
        pass

    def test_get_chain_tx_stats(self):
        """Test case for get_chain_tx_stats

        Get chain tx stats  # noqa: E501
        """
        pass

    def test_get_difficulty(self):
        """Test case for get_difficulty

        Get difficulty  # noqa: E501
        """
        pass

    def test_get_mempool_ancestors(self):
        """Test case for get_mempool_ancestors

        Get mempool ancestors  # noqa: E501
        """
        pass

    def test_get_mempool_descendants(self):
        """Test case for get_mempool_descendants

        Get mempool descendants  # noqa: E501
        """
        pass

    def test_get_mempool_info(self):
        """Test case for get_mempool_info

        Get mempool information  # noqa: E501
        """
        pass

    def test_get_mining_info(self):
        """Test case for get_mining_info

        Get mining information  # noqa: E501
        """
        pass

    def test_get_network_hashps(self):
        """Test case for get_network_hashps

        Get network hash per second  # noqa: E501
        """
        pass

    def test_get_raw_mempool(self):
        """Test case for get_raw_mempool

        Get raw mempool  # noqa: E501
        """
        pass

    def test_get_raw_transaction_decoded(self):
        """Test case for get_raw_transaction_decoded

        Get raw transaction (verbosity 1)  # noqa: E501
        """
        pass

    def test_get_raw_transaction_hex(self):
        """Test case for get_raw_transaction_hex

        Get raw transaction (verbosity 0)  # noqa: E501
        """
        pass

    def test_get_raw_transaction_prevout(self):
        """Test case for get_raw_transaction_prevout

        Get raw transaction (verbosity 2)  # noqa: E501
        """
        pass

    def test_get_tx_out(self):
        """Test case for get_tx_out

        Get transaction output  # noqa: E501
        """
        pass

    def test_get_tx_out_proof(self):
        """Test case for get_tx_out_proof

        Get transaction output proof  # noqa: E501
        """
        pass

    def test_get_tx_out_set_info(self):
        """Test case for get_tx_out_set_info

        Get transaction output set information  # noqa: E501
        """
        pass

    def test_get_tx_spending_prevout(self):
        """Test case for get_tx_spending_prevout

        Get transaction spending prevout  # noqa: E501
        """
        pass

    def test_join_psbts(self):
        """Test case for join_psbts

        Join PSBTs  # noqa: E501
        """
        pass

    def test_send_raw_transaction(self):
        """Test case for send_raw_transaction

        Send raw transaction  # noqa: E501
        """
        pass

    def test_test_mempool_accept(self):
        """Test case for test_mempool_accept

        Test mempool accept  # noqa: E501
        """
        pass

    def test_validate_address(self):
        """Test case for validate_address

        Validate address  # noqa: E501
        """
        pass

    def test_verify_message(self):
        """Test case for verify_message

        Verify message  # noqa: E501
        """
        pass

    def test_verify_tx_out_proof(self):
        """Test case for verify_tx_out_proof

        Verify transaction output proof  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
