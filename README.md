# satstream_python_sdk
Satstream API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0.5
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://satstream.io](https://satstream.io)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import satstream_python_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import satstream_python_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import satstream_python_sdk
from satstream_python_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = satstream_python_sdk.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = satstream_python_sdk.AddressesApi(satstream_python_sdk.ApiClient(configuration))
address = 'address_example' # str | Bitcoin address

try:
    # Get address balance
    api_response = api_instance.get_address_balance(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_address_balance: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = satstream_python_sdk.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = satstream_python_sdk.AddressesApi(satstream_python_sdk.ApiClient(configuration))
address = 'address_example' # str | Bitcoin address

try:
    # Get address non-inscription UTXOs
    api_response = api_instance.get_address_non_inscription_utxos(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_address_non_inscription_utxos: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = satstream_python_sdk.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = satstream_python_sdk.AddressesApi(satstream_python_sdk.ApiClient(configuration))
address = 'address_example' # str | Bitcoin address
runeid = 'runeid_example' # str | Rune ID

try:
    # Get address rune balance
    api_response = api_instance.get_address_rune_balance(address, runeid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_address_rune_balance: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = satstream_python_sdk.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = satstream_python_sdk.AddressesApi(satstream_python_sdk.ApiClient(configuration))
address = 'address_example' # str | Bitcoin address

try:
    # Get address runes balance list
    api_response = api_instance.get_address_runes_balance_list(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_address_runes_balance_list: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = satstream_python_sdk.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = satstream_python_sdk.AddressesApi(satstream_python_sdk.ApiClient(configuration))
address = 'address_example' # str | Bitcoin address
timeframe = 'timeframe_example' # str | Timeframe
token = 'token_example' # str | Token (optional)

try:
    # Get address timeframe balance
    api_response = api_instance.get_address_timeframe_balance(address, timeframe, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_address_timeframe_balance: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.satstream.io/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AddressesApi* | [**get_address_balance**](docs/AddressesApi.md#get_address_balance) | **GET** /addresses/{address}/balance | Get address balance
*AddressesApi* | [**get_address_non_inscription_utxos**](docs/AddressesApi.md#get_address_non_inscription_utxos) | **GET** /addresses/{address}/utxos | Get address non-inscription UTXOs
*AddressesApi* | [**get_address_rune_balance**](docs/AddressesApi.md#get_address_rune_balance) | **GET** /addresses/{address}/runes/{runeid} | Get address rune balance
*AddressesApi* | [**get_address_runes_balance_list**](docs/AddressesApi.md#get_address_runes_balance_list) | **GET** /addresses/{address}/runes | Get address runes balance list
*AddressesApi* | [**get_address_timeframe_balance**](docs/AddressesApi.md#get_address_timeframe_balance) | **GET** /addresses/{address}/balance/timeframe | Get address timeframe balance
*BlocksApi* | [**get_block_by_hash**](docs/BlocksApi.md#get_block_by_hash) | **GET** /blocks/hash/{hash} | Get block by hash
*BlocksApi* | [**get_block_info**](docs/BlocksApi.md#get_block_info) | **GET** /blocks/{height} | Get block info
*BlocksApi* | [**get_block_transactions**](docs/BlocksApi.md#get_block_transactions) | **GET** /blocks/{height}/transactions | Get block transactions
*BlocksApi* | [**get_current_block_height**](docs/BlocksApi.md#get_current_block_height) | **GET** /blocks/current-height | Get current block height
*FeesApi* | [**get_recommended_fees**](docs/FeesApi.md#get_recommended_fees) | **GET** /fees | Get recommended fees
*MempoolApi* | [**get_address_mempool_transactions**](docs/MempoolApi.md#get_address_mempool_transactions) | **GET** /mempool/addresses/{address}/transactions | Get address mempool transactions
*MempoolApi* | [**get_mempool_transaction_info**](docs/MempoolApi.md#get_mempool_transaction_info) | **GET** /mempool/transactions/{txid} | Get mempool transaction info
*MempoolApi* | [**get_mempool_transactions**](docs/MempoolApi.md#get_mempool_transactions) | **GET** /mempool/transactions | Get mempool transactions
*RunesApi* | [**get_runes_holders**](docs/RunesApi.md#get_runes_holders) | **GET** /runes/{runeId}/holders | Get rune holders
*RunesApi* | [**get_runes_info**](docs/RunesApi.md#get_runes_info) | **GET** /runes/{runeId} | Get rune info
*RunesApi* | [**get_runes_info_list**](docs/RunesApi.md#get_runes_info_list) | **GET** /runes | Get runes info list
*TransactionsApi* | [**broadcast_transaction**](docs/TransactionsApi.md#broadcast_transaction) | **POST** /transactions/broadcast | Broadcast transaction
*TransactionsApi* | [**get_transaction**](docs/TransactionsApi.md#get_transaction) | **GET** /indexer/tx/{hash} | Get transaction
*TransactionsApi* | [**get_transaction_info**](docs/TransactionsApi.md#get_transaction_info) | **GET** /transactions/{txid} | Get transaction info

## Documentation For Models

 - [AllOfresponsesGetAddressTimeframeBalanceItemBlockRange](docs/AllOfresponsesGetAddressTimeframeBalanceItemBlockRange.md)
 - [BigInt](docs/BigInt.md)
 - [GithubComSatstreamSsApiServerApiAddressesResponsesError](docs/GithubComSatstreamSsApiServerApiAddressesResponsesError.md)
 - [GithubComSatstreamSsApiServerApiBlocksResponsesError](docs/GithubComSatstreamSsApiServerApiBlocksResponsesError.md)
 - [GithubComSatstreamSsApiServerApiRunesResponsesError](docs/GithubComSatstreamSsApiServerApiRunesResponsesError.md)
 - [GithubComSatstreamSsApiServerApiTransactionsResponsesError](docs/GithubComSatstreamSsApiServerApiTransactionsResponsesError.md)
 - [GithubComSatstreamSsUtilsOrdinalsTerms](docs/GithubComSatstreamSsUtilsOrdinalsTerms.md)
 - [GithubComSatstreamSsUtilsOrdinalsTermsRange](docs/GithubComSatstreamSsUtilsOrdinalsTermsRange.md)
 - [GithubComSatstreamSsUtilsRpcBlock](docs/GithubComSatstreamSsUtilsRpcBlock.md)
 - [GithubComSatstreamSsUtilsRpcBtcTx](docs/GithubComSatstreamSsUtilsRpcBtcTx.md)
 - [GithubComSatstreamSsUtilsRpcPrevOut](docs/GithubComSatstreamSsUtilsRpcPrevOut.md)
 - [GithubComSatstreamSsUtilsRpcScriptPubKey](docs/GithubComSatstreamSsUtilsRpcScriptPubKey.md)
 - [GithubComSatstreamSsUtilsRpcScriptSig](docs/GithubComSatstreamSsUtilsRpcScriptSig.md)
 - [GithubComSatstreamSsUtilsRpcUtxoRune](docs/GithubComSatstreamSsUtilsRpcUtxoRune.md)
 - [GithubComSatstreamSsUtilsRpcVin](docs/GithubComSatstreamSsUtilsRpcVin.md)
 - [GithubComSatstreamSsUtilsRpcVout](docs/GithubComSatstreamSsUtilsRpcVout.md)
 - [GithubComSatstreamSsUtilsStoreTransactionDocument](docs/GithubComSatstreamSsUtilsStoreTransactionDocument.md)
 - [ResponsesBlockRange](docs/ResponsesBlockRange.md)
 - [ResponsesGetAddressBalance](docs/ResponsesGetAddressBalance.md)
 - [ResponsesGetAddressBalanceData](docs/ResponsesGetAddressBalanceData.md)
 - [ResponsesGetAddressMempoolTxs](docs/ResponsesGetAddressMempoolTxs.md)
 - [ResponsesGetAddressNonInscriptionUTXO](docs/ResponsesGetAddressNonInscriptionUTXO.md)
 - [ResponsesGetAddressNonInscriptionUTXOData](docs/ResponsesGetAddressNonInscriptionUTXOData.md)
 - [ResponsesGetAddressRuneBalance](docs/ResponsesGetAddressRuneBalance.md)
 - [ResponsesGetAddressRuneBalanceData](docs/ResponsesGetAddressRuneBalanceData.md)
 - [ResponsesGetAddressRunesBalanceList](docs/ResponsesGetAddressRunesBalanceList.md)
 - [ResponsesGetAddressRunesBalanceListData](docs/ResponsesGetAddressRunesBalanceListData.md)
 - [ResponsesGetAddressRunesBalanceListItem](docs/ResponsesGetAddressRunesBalanceListItem.md)
 - [ResponsesGetAddressTimeframeBalance](docs/ResponsesGetAddressTimeframeBalance.md)
 - [ResponsesGetAddressTimeframeBalanceData](docs/ResponsesGetAddressTimeframeBalanceData.md)
 - [ResponsesGetAddressTimeframeBalanceItem](docs/ResponsesGetAddressTimeframeBalanceItem.md)
 - [ResponsesGetBlockByHash](docs/ResponsesGetBlockByHash.md)
 - [ResponsesGetBlockHeight](docs/ResponsesGetBlockHeight.md)
 - [ResponsesGetBlockHeightData](docs/ResponsesGetBlockHeightData.md)
 - [ResponsesGetBlockInfo](docs/ResponsesGetBlockInfo.md)
 - [ResponsesGetBlockTransactions](docs/ResponsesGetBlockTransactions.md)
 - [ResponsesGetFees](docs/ResponsesGetFees.md)
 - [ResponsesGetFeesData](docs/ResponsesGetFeesData.md)
 - [ResponsesGetMempoolTransactions](docs/ResponsesGetMempoolTransactions.md)
 - [ResponsesGetMempoolTxInfo](docs/ResponsesGetMempoolTxInfo.md)
 - [ResponsesGetRuneHolders](docs/ResponsesGetRuneHolders.md)
 - [ResponsesGetRuneHoldersData](docs/ResponsesGetRuneHoldersData.md)
 - [ResponsesGetRuneInfo](docs/ResponsesGetRuneInfo.md)
 - [ResponsesGetRunesInfoList](docs/ResponsesGetRunesInfoList.md)
 - [ResponsesGetRunesInfoListData](docs/ResponsesGetRunesInfoListData.md)
 - [ResponsesGetTransaction](docs/ResponsesGetTransaction.md)
 - [ResponsesGetTxInfo](docs/ResponsesGetTxInfo.md)
 - [ResponsesGetTxInfoData](docs/ResponsesGetTxInfoData.md)
 - [ResponsesNonInscriptionUTXO](docs/ResponsesNonInscriptionUTXO.md)
 - [ResponsesPaginationInfo](docs/ResponsesPaginationInfo.md)
 - [ResponsesRuneHolder](docs/ResponsesRuneHolder.md)
 - [ResponsesRuneInfo](docs/ResponsesRuneInfo.md)
 - [ResponsesSendRawTransaction](docs/ResponsesSendRawTransaction.md)
 - [ResponsesSendRawTransactionData](docs/ResponsesSendRawTransactionData.md)

## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header


## Author

team@satstream.io
