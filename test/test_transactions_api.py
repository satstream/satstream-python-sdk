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
from satstream_python_sdk.api.transactions_api import TransactionsApi  # noqa: E501
from satstream_python_sdk.rest import ApiException


class TestTransactionsApi(unittest.TestCase):
    """TransactionsApi unit test stubs"""

    def setUp(self):
        self.api = TransactionsApi()  # noqa: E501

    def tearDown(self):
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

    def test_create_raw_transaction(self):
        """Test case for create_raw_transaction

        Create Raw Transaction  # noqa: E501
        """
        pass

    def test_decode_tx_inscriptions(self):
        """Test case for decode_tx_inscriptions

        Decode transaction inscriptions  # noqa: E501
        """
        pass

    def test_get_raw_transaction(self):
        """Test case for get_raw_transaction

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

        Get raw transaction with prevouts (verbosity 2)  # noqa: E501
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

    def test_get_tx_spending_prevout(self):
        """Test case for get_tx_spending_prevout

        Get transaction spending prevout  # noqa: E501
        """
        pass

    def test_send_raw_transaction(self):
        """Test case for send_raw_transaction

        Send raw transaction  # noqa: E501
        """
        pass

    def test_verify_tx_out_proof(self):
        """Test case for verify_tx_out_proof

        Verify transaction output proof  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
