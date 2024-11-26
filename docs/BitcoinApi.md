# satstream_python_sdk.BitcoinApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_psbt**](BitcoinApi.md#analyze_psbt) | **POST** /psbt/analyze | Analyze PSBT
[**combine_psbt**](BitcoinApi.md#combine_psbt) | **POST** /psbt/combine | Combine PSBTs
[**combine_raw_transaction**](BitcoinApi.md#combine_raw_transaction) | **POST** /tx/combine | Combine Raw Transactions
[**convert_to_psbt**](BitcoinApi.md#convert_to_psbt) | **POST** /tx/convert-to-psbt | Convert Raw Transaction to PSBT
[**create_psbt**](BitcoinApi.md#create_psbt) | **POST** /psbt/create | Create PSBT
[**create_raw_transaction**](BitcoinApi.md#create_raw_transaction) | **POST** /tx/create | Create Raw Transaction
[**decode_psbt**](BitcoinApi.md#decode_psbt) | **POST** /psbt/decode | Decode PSBT
[**decode_script**](BitcoinApi.md#decode_script) | **POST** /script/decode | Decode Script
[**estimate_raw_fee**](BitcoinApi.md#estimate_raw_fee) | **POST** /fee/estimate-raw | Estimate Raw Fee
[**estimate_smart_fee**](BitcoinApi.md#estimate_smart_fee) | **POST** /fee/estimate-smart | Estimate smart fee
[**get_block_by_hash_decoded**](BitcoinApi.md#get_block_by_hash_decoded) | **GET** /block/hash/{hash}/decoded | Get block by hash (verbosity 2)
[**get_block_by_hash_hex**](BitcoinApi.md#get_block_by_hash_hex) | **GET** /block/hash/{hash}/hex | Get block by hash (verbosity 0)
[**get_block_by_hash_prevout**](BitcoinApi.md#get_block_by_hash_prevout) | **GET** /block/hash/{hash}/prevout | Get block by hash (verbosity 3)
[**get_block_by_hash_summary**](BitcoinApi.md#get_block_by_hash_summary) | **GET** /block/hash/{hash}/summary | Get block by hash (verbosity 1)
[**get_block_by_height_decoded**](BitcoinApi.md#get_block_by_height_decoded) | **GET** /block/height/{height}/decoded | Get block by height (verbosity 2)
[**get_block_by_height_hex**](BitcoinApi.md#get_block_by_height_hex) | **GET** /block/height/{height}/hex | Get block by height (verbosity 0)
[**get_block_by_height_prevout**](BitcoinApi.md#get_block_by_height_prevout) | **GET** /block/height/{height}/prevout | Get block by height (verbosity 3)
[**get_block_by_height_summary**](BitcoinApi.md#get_block_by_height_summary) | **GET** /block/height/{height}/summary | Get block by height (verbosity 1)
[**get_block_stats**](BitcoinApi.md#get_block_stats) | **POST** /block/stats | Get block stats
[**get_blockchain_info**](BitcoinApi.md#get_blockchain_info) | **GET** /blockchain/info | Get blockchain information
[**get_chain_tx_stats**](BitcoinApi.md#get_chain_tx_stats) | **POST** /chain/txstats | Get chain tx stats
[**get_difficulty**](BitcoinApi.md#get_difficulty) | **GET** /difficulty | Get difficulty
[**get_mempool_ancestors**](BitcoinApi.md#get_mempool_ancestors) | **POST** /mempool/ancestors | Get mempool ancestors
[**get_mempool_descendants**](BitcoinApi.md#get_mempool_descendants) | **POST** /mempool/descendants | Get mempool descendants
[**get_mempool_info**](BitcoinApi.md#get_mempool_info) | **GET** /mempool/info | Get mempool information
[**get_mining_info**](BitcoinApi.md#get_mining_info) | **GET** /mining/info | Get mining information
[**get_network_hashps**](BitcoinApi.md#get_network_hashps) | **POST** /network/hashps | Get network hash per second
[**get_raw_mempool**](BitcoinApi.md#get_raw_mempool) | **POST** /mempool/raw | Get raw mempool
[**get_raw_transaction_decoded**](BitcoinApi.md#get_raw_transaction_decoded) | **GET** /tx/{txid}/decoded | Get raw transaction (verbosity 1)
[**get_raw_transaction_hex**](BitcoinApi.md#get_raw_transaction_hex) | **GET** /tx/{txid}/hex | Get raw transaction (verbosity 0)
[**get_raw_transaction_prevout**](BitcoinApi.md#get_raw_transaction_prevout) | **GET** /tx/{txid}/prevout | Get raw transaction (verbosity 2)
[**get_tx_out**](BitcoinApi.md#get_tx_out) | **POST** /tx/out | Get transaction output
[**get_tx_out_proof**](BitcoinApi.md#get_tx_out_proof) | **POST** /tx/out/proof | Get transaction output proof
[**get_tx_out_set_info**](BitcoinApi.md#get_tx_out_set_info) | **POST** /tx/out/set/info | Get transaction output set information
[**get_tx_spending_prevout**](BitcoinApi.md#get_tx_spending_prevout) | **POST** /tx/spending/prevout | Get transaction spending prevout
[**join_psbts**](BitcoinApi.md#join_psbts) | **POST** /psbt/join | Join PSBTs
[**send_raw_transaction**](BitcoinApi.md#send_raw_transaction) | **POST** /tx/send | Send raw transaction
[**test_mempool_accept**](BitcoinApi.md#test_mempool_accept) | **POST** /mempool/test-accept | Test mempool accept
[**validate_address**](BitcoinApi.md#validate_address) | **GET** /address/{address}/validate | Validate address
[**verify_message**](BitcoinApi.md#verify_message) | **POST** /address/verify-message | Verify message
[**verify_tx_out_proof**](BitcoinApi.md#verify_tx_out_proof) | **POST** /tx/out/proof/verify | Verify transaction output proof

# **analyze_psbt**
> ResponsesAnalyzePSBTResponse analyze_psbt(body)

Analyze PSBT

Analyzes and provides information about the current status of a PSBT and its inputs

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsAnalyzePSBTRequest() # RequestsAnalyzePSBTRequest | PSBT to analyze

try:
    # Analyze PSBT
    api_response = api_instance.analyze_psbt(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->analyze_psbt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsAnalyzePSBTRequest**](RequestsAnalyzePSBTRequest.md)| PSBT to analyze | 

### Return type

[**ResponsesAnalyzePSBTResponse**](ResponsesAnalyzePSBTResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **combine_psbt**
> ResponsesCombinePSBTResponse combine_psbt(body)

Combine PSBTs

Combines multiple partially signed Bitcoin transactions into one transaction

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsCombinePSBTRequest() # RequestsCombinePSBTRequest | Array of PSBTs to combine

try:
    # Combine PSBTs
    api_response = api_instance.combine_psbt(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->combine_psbt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsCombinePSBTRequest**](RequestsCombinePSBTRequest.md)| Array of PSBTs to combine | 

### Return type

[**ResponsesCombinePSBTResponse**](ResponsesCombinePSBTResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **combine_raw_transaction**
> ResponsesCombineRawTransactionResponse combine_raw_transaction(body)

Combine Raw Transactions

Combines multiple partially signed transactions into one transaction

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsCombineRawTransactionRequest() # RequestsCombineRawTransactionRequest | Array of hex-encoded raw transactions

try:
    # Combine Raw Transactions
    api_response = api_instance.combine_raw_transaction(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->combine_raw_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsCombineRawTransactionRequest**](RequestsCombineRawTransactionRequest.md)| Array of hex-encoded raw transactions | 

### Return type

[**ResponsesCombineRawTransactionResponse**](ResponsesCombineRawTransactionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_to_psbt**
> ResponsesConvertToPSBTResponse convert_to_psbt(body)

Convert Raw Transaction to PSBT

Converts a network serialized transaction to a PSBT. This should be used only with createrawtransaction and fundrawtransaction. createpsbt and walletcreatefundedpsbt should be used for new applications.

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsConvertToPSBTRequest() # RequestsConvertToPSBTRequest | Raw transaction conversion parameters

try:
    # Convert Raw Transaction to PSBT
    api_response = api_instance.convert_to_psbt(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->convert_to_psbt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsConvertToPSBTRequest**](RequestsConvertToPSBTRequest.md)| Raw transaction conversion parameters | 

### Return type

[**ResponsesConvertToPSBTResponse**](ResponsesConvertToPSBTResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_psbt**
> ResponsesCreatePSBTResponse create_psbt(body)

Create PSBT

Creates a transaction in the Partially Signed Transaction format. Implements the Creator role.

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.GithubComSatstreamSsApiServerApiPsbtRequestsCreatePSBTRequest() # GithubComSatstreamSsApiServerApiPsbtRequestsCreatePSBTRequest | Transaction parameters

try:
    # Create PSBT
    api_response = api_instance.create_psbt(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->create_psbt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GithubComSatstreamSsApiServerApiPsbtRequestsCreatePSBTRequest**](GithubComSatstreamSsApiServerApiPsbtRequestsCreatePSBTRequest.md)| Transaction parameters | 

### Return type

[**ResponsesCreatePSBTResponse**](ResponsesCreatePSBTResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_raw_transaction**
> ResponsesCreateRawTransactionResponse create_raw_transaction(body)

Create Raw Transaction

Creates a raw transaction spending the given inputs and creating new outputs. Note that the transaction's inputs are not signed, and it is not stored in the wallet or transmitted to the network.

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest() # GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest | Transaction parameters

try:
    # Create Raw Transaction
    api_response = api_instance.create_raw_transaction(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->create_raw_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest**](GithubComSatstreamSsApiServerApiTransactionRequestsCreatePSBTRequest.md)| Transaction parameters | 

### Return type

[**ResponsesCreateRawTransactionResponse**](ResponsesCreateRawTransactionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decode_psbt**
> ResponsesDecodePSBTResponse decode_psbt(body)

Decode PSBT

Return a JSON object representing the serialized, base64-encoded partially signed Bitcoin transaction.

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsAnalyzePSBTRequest() # RequestsAnalyzePSBTRequest | PSBT to decode

try:
    # Decode PSBT
    api_response = api_instance.decode_psbt(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->decode_psbt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsAnalyzePSBTRequest**](RequestsAnalyzePSBTRequest.md)| PSBT to decode | 

### Return type

[**ResponsesDecodePSBTResponse**](ResponsesDecodePSBTResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decode_script**
> ResponsesDecodeScriptResponse decode_script(body)

Decode Script

Decode a hex-encoded script and return detailed information about it.

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsDecodeScriptRequest() # RequestsDecodeScriptRequest | Script to decode

try:
    # Decode Script
    api_response = api_instance.decode_script(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->decode_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsDecodeScriptRequest**](RequestsDecodeScriptRequest.md)| Script to decode | 

### Return type

[**ResponsesDecodeScriptResponse**](ResponsesDecodeScriptResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **estimate_raw_fee**
> ResponsesEstimateRawFeeResponse estimate_raw_fee(body)

Estimate Raw Fee

Estimates the approximate fee per kilobyte needed for a transaction to begin confirmation within conf_target blocks if possible.

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsEstimateRawFeeRequest() # RequestsEstimateRawFeeRequest | Fee estimation parameters

try:
    # Estimate Raw Fee
    api_response = api_instance.estimate_raw_fee(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->estimate_raw_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsEstimateRawFeeRequest**](RequestsEstimateRawFeeRequest.md)| Fee estimation parameters | 

### Return type

[**ResponsesEstimateRawFeeResponse**](ResponsesEstimateRawFeeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **estimate_smart_fee**
> ResponsesEstimateSmartFeeResponse estimate_smart_fee(body)

Estimate smart fee

Estimates the approximate fee per kilobyte needed for a transaction to begin confirmation within conf_target blocks

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsEstimateSmartFeeRequest() # RequestsEstimateSmartFeeRequest | Fee estimation parameters

try:
    # Estimate smart fee
    api_response = api_instance.estimate_smart_fee(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->estimate_smart_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsEstimateSmartFeeRequest**](RequestsEstimateSmartFeeRequest.md)| Fee estimation parameters | 

### Return type

[**ResponsesEstimateSmartFeeResponse**](ResponsesEstimateSmartFeeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_by_hash_decoded**
> ResponsesGetBlockDecodedResponse get_block_by_hash_decoded(hash)

Get block by hash (verbosity 2)

Get block by hash as a decoded object

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
hash = 'hash_example' # str | Block hash

try:
    # Get block by hash (verbosity 2)
    api_response = api_instance.get_block_by_hash_decoded(hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_block_by_hash_decoded: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Block hash | 

### Return type

[**ResponsesGetBlockDecodedResponse**](ResponsesGetBlockDecodedResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_by_hash_hex**
> ResponsesGetBlockHexResponse get_block_by_hash_hex(hash)

Get block by hash (verbosity 0)

Get block by hash as a raw hex string

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
hash = 'hash_example' # str | Block hash

try:
    # Get block by hash (verbosity 0)
    api_response = api_instance.get_block_by_hash_hex(hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_block_by_hash_hex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Block hash | 

### Return type

[**ResponsesGetBlockHexResponse**](ResponsesGetBlockHexResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_by_hash_prevout**
> ResponsesGetBlockPrevoutResponse get_block_by_hash_prevout(hash)

Get block by hash (verbosity 3)

Get block by hash with prevout information

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
hash = 'hash_example' # str | Block hash

try:
    # Get block by hash (verbosity 3)
    api_response = api_instance.get_block_by_hash_prevout(hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_block_by_hash_prevout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Block hash | 

### Return type

[**ResponsesGetBlockPrevoutResponse**](ResponsesGetBlockPrevoutResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_by_hash_summary**
> ResponsesGetBlockSummaryResponse get_block_by_hash_summary(hash)

Get block by hash (verbosity 1)

Get block by hash as a summary object

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
hash = 'hash_example' # str | Block hash

try:
    # Get block by hash (verbosity 1)
    api_response = api_instance.get_block_by_hash_summary(hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_block_by_hash_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Block hash | 

### Return type

[**ResponsesGetBlockSummaryResponse**](ResponsesGetBlockSummaryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_by_height_decoded**
> ResponsesGetBlockDecodedResponse get_block_by_height_decoded(height)

Get block by height (verbosity 2)

Get block by height as a decoded object

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
height = 56 # int | Block height

try:
    # Get block by height (verbosity 2)
    api_response = api_instance.get_block_by_height_decoded(height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_block_by_height_decoded: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | **int**| Block height | 

### Return type

[**ResponsesGetBlockDecodedResponse**](ResponsesGetBlockDecodedResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_by_height_hex**
> ResponsesGetBlockHexResponse get_block_by_height_hex(height)

Get block by height (verbosity 0)

Get block by height as a raw hex string

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
height = 56 # int | Block height

try:
    # Get block by height (verbosity 0)
    api_response = api_instance.get_block_by_height_hex(height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_block_by_height_hex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | **int**| Block height | 

### Return type

[**ResponsesGetBlockHexResponse**](ResponsesGetBlockHexResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_by_height_prevout**
> ResponsesGetBlockPrevoutResponse get_block_by_height_prevout(height)

Get block by height (verbosity 3)

Get block by height with prevout information

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
height = 56 # int | Block height

try:
    # Get block by height (verbosity 3)
    api_response = api_instance.get_block_by_height_prevout(height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_block_by_height_prevout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | **int**| Block height | 

### Return type

[**ResponsesGetBlockPrevoutResponse**](ResponsesGetBlockPrevoutResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_by_height_summary**
> ResponsesGetBlockSummaryResponse get_block_by_height_summary(height)

Get block by height (verbosity 1)

Get block by height as a summary object

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
height = 56 # int | Block height

try:
    # Get block by height (verbosity 1)
    api_response = api_instance.get_block_by_height_summary(height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_block_by_height_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | **int**| Block height | 

### Return type

[**ResponsesGetBlockSummaryResponse**](ResponsesGetBlockSummaryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_stats**
> ResponsesGetBlockStatsResponse get_block_stats(body)

Get block stats

Computes per block statistics for a given window

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsGetBlockStatsRequest() # RequestsGetBlockStatsRequest | Block stats request parameters

try:
    # Get block stats
    api_response = api_instance.get_block_stats(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_block_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsGetBlockStatsRequest**](RequestsGetBlockStatsRequest.md)| Block stats request parameters | 

### Return type

[**ResponsesGetBlockStatsResponse**](ResponsesGetBlockStatsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blockchain_info**
> ResponsesGetBlockchainInfoResponse get_blockchain_info()

Get blockchain information

Returns an object containing various state info regarding blockchain processing

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Get blockchain information
    api_response = api_instance.get_blockchain_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_blockchain_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponsesGetBlockchainInfoResponse**](ResponsesGetBlockchainInfoResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chain_tx_stats**
> ResponsesGetChainTxStatsResponse get_chain_tx_stats(body)

Get chain tx stats

Computes statistics about the total number and rate of transactions in the chain

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsGetChainTxStatsRequest() # RequestsGetChainTxStatsRequest | Chain tx stats request parameters

try:
    # Get chain tx stats
    api_response = api_instance.get_chain_tx_stats(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_chain_tx_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsGetChainTxStatsRequest**](RequestsGetChainTxStatsRequest.md)| Chain tx stats request parameters | 

### Return type

[**ResponsesGetChainTxStatsResponse**](ResponsesGetChainTxStatsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_difficulty**
> ResponsesGetDifficultyResponse get_difficulty()

Get difficulty

Returns the proof-of-work difficulty as a multiple of the minimum difficulty

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Get difficulty
    api_response = api_instance.get_difficulty()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_difficulty: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponsesGetDifficultyResponse**](ResponsesGetDifficultyResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mempool_ancestors**
> ResponsesGetMempoolAncestorsResponse get_mempool_ancestors(body)

Get mempool ancestors

Returns all in-mempool ancestors for a transaction in the mempool

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsGetMempoolAncestorsRequest() # RequestsGetMempoolAncestorsRequest | Mempool ancestors request parameters

try:
    # Get mempool ancestors
    api_response = api_instance.get_mempool_ancestors(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_mempool_ancestors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsGetMempoolAncestorsRequest**](RequestsGetMempoolAncestorsRequest.md)| Mempool ancestors request parameters | 

### Return type

[**ResponsesGetMempoolAncestorsResponse**](ResponsesGetMempoolAncestorsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mempool_descendants**
> ResponsesGetMempoolDescendantsResponse get_mempool_descendants(body)

Get mempool descendants

Returns all in-mempool descendants for a transaction in the mempool

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsGetMempoolDescendantsRequest() # RequestsGetMempoolDescendantsRequest | Mempool descendants request parameters

try:
    # Get mempool descendants
    api_response = api_instance.get_mempool_descendants(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_mempool_descendants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsGetMempoolDescendantsRequest**](RequestsGetMempoolDescendantsRequest.md)| Mempool descendants request parameters | 

### Return type

[**ResponsesGetMempoolDescendantsResponse**](ResponsesGetMempoolDescendantsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mempool_info**
> ResponsesGetMempoolInfoResponse get_mempool_info()

Get mempool information

Returns details on the active state of the TX memory pool

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Get mempool information
    api_response = api_instance.get_mempool_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_mempool_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponsesGetMempoolInfoResponse**](ResponsesGetMempoolInfoResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mining_info**
> ResponsesGetMiningInfoResponse get_mining_info()

Get mining information

Returns a json object containing mining-related information

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Get mining information
    api_response = api_instance.get_mining_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_mining_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponsesGetMiningInfoResponse**](ResponsesGetMiningInfoResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_hashps**
> ResponsesGetNetworkHashPSResponse get_network_hashps(body)

Get network hash per second

Returns the estimated network hashes per second based on the last n blocks

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsGetNetworkHashPSRequest() # RequestsGetNetworkHashPSRequest | Network hash rate parameters

try:
    # Get network hash per second
    api_response = api_instance.get_network_hashps(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_network_hashps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsGetNetworkHashPSRequest**](RequestsGetNetworkHashPSRequest.md)| Network hash rate parameters | 

### Return type

[**ResponsesGetNetworkHashPSResponse**](ResponsesGetNetworkHashPSResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_mempool**
> ResponsesGetRawMempoolResponse get_raw_mempool(body)

Get raw mempool

Returns all transaction ids in memory pool

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsGetRawMempoolRequest() # RequestsGetRawMempoolRequest | Raw mempool request parameters

try:
    # Get raw mempool
    api_response = api_instance.get_raw_mempool(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_raw_mempool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsGetRawMempoolRequest**](RequestsGetRawMempoolRequest.md)| Raw mempool request parameters | 

### Return type

[**ResponsesGetRawMempoolResponse**](ResponsesGetRawMempoolResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_transaction_decoded**
> ResponsesGetRawTransactionDecodedResponse get_raw_transaction_decoded(txid)

Get raw transaction (verbosity 1)

Get raw transaction as a decoded object

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
txid = 'txid_example' # str | Transaction ID

try:
    # Get raw transaction (verbosity 1)
    api_response = api_instance.get_raw_transaction_decoded(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_raw_transaction_decoded: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Transaction ID | 

### Return type

[**ResponsesGetRawTransactionDecodedResponse**](ResponsesGetRawTransactionDecodedResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_transaction_hex**
> ResponsesGetRawTransactionHexResponse get_raw_transaction_hex(txid)

Get raw transaction (verbosity 0)

Get raw transaction as a raw hex string

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
txid = 'txid_example' # str | Transaction ID

try:
    # Get raw transaction (verbosity 0)
    api_response = api_instance.get_raw_transaction_hex(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_raw_transaction_hex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Transaction ID | 

### Return type

[**ResponsesGetRawTransactionHexResponse**](ResponsesGetRawTransactionHexResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_transaction_prevout**
> ResponsesGetRawTransactionPrevoutResponse get_raw_transaction_prevout(txid)

Get raw transaction (verbosity 2)

Get raw transaction with prevout information

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
txid = 'txid_example' # str | Transaction ID

try:
    # Get raw transaction (verbosity 2)
    api_response = api_instance.get_raw_transaction_prevout(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_raw_transaction_prevout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Transaction ID | 

### Return type

[**ResponsesGetRawTransactionPrevoutResponse**](ResponsesGetRawTransactionPrevoutResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tx_out**
> ResponsesGetTxOutResponse get_tx_out(body)

Get transaction output

Returns details about an unspent transaction output

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsGetTxOutRequest() # RequestsGetTxOutRequest | Transaction output request parameters

try:
    # Get transaction output
    api_response = api_instance.get_tx_out(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_tx_out: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsGetTxOutRequest**](RequestsGetTxOutRequest.md)| Transaction output request parameters | 

### Return type

[**ResponsesGetTxOutResponse**](ResponsesGetTxOutResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tx_out_proof**
> ResponsesGetTxOutProofResponse get_tx_out_proof(body)

Get transaction output proof

Returns a hex-encoded proof that one or more specified transactions were included in a block

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsGetTxOutProofRequest() # RequestsGetTxOutProofRequest | Transaction proof request parameters

try:
    # Get transaction output proof
    api_response = api_instance.get_tx_out_proof(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_tx_out_proof: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsGetTxOutProofRequest**](RequestsGetTxOutProofRequest.md)| Transaction proof request parameters | 

### Return type

[**ResponsesGetTxOutProofResponse**](ResponsesGetTxOutProofResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tx_out_set_info**
> ResponsesGetTxOutSetInfoResponse get_tx_out_set_info(body)

Get transaction output set information

Returns statistics about the unspent transaction output set

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsGetTxOutSetInfoRequest() # RequestsGetTxOutSetInfoRequest | UTXO set info request parameters

try:
    # Get transaction output set information
    api_response = api_instance.get_tx_out_set_info(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_tx_out_set_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsGetTxOutSetInfoRequest**](RequestsGetTxOutSetInfoRequest.md)| UTXO set info request parameters | 

### Return type

[**ResponsesGetTxOutSetInfoResponse**](ResponsesGetTxOutSetInfoResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tx_spending_prevout**
> ResponsesGetTxSpendingPrevoutResponse get_tx_spending_prevout(body)

Get transaction spending prevout

Scans the mempool to find transactions spending any of the given outputs

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsGetTxSpendingPrevoutRequest() # RequestsGetTxSpendingPrevoutRequest | Transaction spending prevout request

try:
    # Get transaction spending prevout
    api_response = api_instance.get_tx_spending_prevout(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->get_tx_spending_prevout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsGetTxSpendingPrevoutRequest**](RequestsGetTxSpendingPrevoutRequest.md)| Transaction spending prevout request | 

### Return type

[**ResponsesGetTxSpendingPrevoutResponse**](ResponsesGetTxSpendingPrevoutResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_psbts**
> ResponsesJoinPSBTsResponse join_psbts(body)

Join PSBTs

Joins multiple distinct PSBTs with different inputs and outputs into one PSBT

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsJoinPSBTsRequest() # RequestsJoinPSBTsRequest | PSBTs to join

try:
    # Join PSBTs
    api_response = api_instance.join_psbts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->join_psbts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsJoinPSBTsRequest**](RequestsJoinPSBTsRequest.md)| PSBTs to join | 

### Return type

[**ResponsesJoinPSBTsResponse**](ResponsesJoinPSBTsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_raw_transaction**
> ResponsesSendRawTransactionResponse send_raw_transaction(body)

Send raw transaction

Submits a raw transaction to local node and network

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsSendRawTransactionRequest() # RequestsSendRawTransactionRequest | Raw transaction to send

try:
    # Send raw transaction
    api_response = api_instance.send_raw_transaction(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->send_raw_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsSendRawTransactionRequest**](RequestsSendRawTransactionRequest.md)| Raw transaction to send | 

### Return type

[**ResponsesSendRawTransactionResponse**](ResponsesSendRawTransactionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_mempool_accept**
> ResponsesTestMempoolAcceptResponse test_mempool_accept(body)

Test mempool accept

Tests whether raw transactions would be accepted by mempool

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsTestMempoolAcceptRequest() # RequestsTestMempoolAcceptRequest | Raw transactions to test

try:
    # Test mempool accept
    api_response = api_instance.test_mempool_accept(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->test_mempool_accept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsTestMempoolAcceptRequest**](RequestsTestMempoolAcceptRequest.md)| Raw transactions to test | 

### Return type

[**ResponsesTestMempoolAcceptResponse**](ResponsesTestMempoolAcceptResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_address**
> ResponsesValidateAddressResponse validate_address(address)

Validate address

Returns information about the given Bitcoin address

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
address = 'address_example' # str | Bitcoin address to validate

try:
    # Validate address
    api_response = api_instance.validate_address(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->validate_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Bitcoin address to validate | 

### Return type

[**ResponsesValidateAddressResponse**](ResponsesValidateAddressResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_message**
> ResponsesVerifyMessageResponse verify_message(body)

Verify message

Verifies a signed message

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsVerifyMessageRequest() # RequestsVerifyMessageRequest | Message verification parameters

try:
    # Verify message
    api_response = api_instance.verify_message(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->verify_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsVerifyMessageRequest**](RequestsVerifyMessageRequest.md)| Message verification parameters | 

### Return type

[**ResponsesVerifyMessageResponse**](ResponsesVerifyMessageResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_tx_out_proof**
> ResponsesVerifyTxOutProofResponse verify_tx_out_proof(body)

Verify transaction output proof

Verifies that a proof points to a transaction in a block

### Example
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
api_instance = satstream_python_sdk.BitcoinApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsVerifyTxOutProofRequest() # RequestsVerifyTxOutProofRequest | Proof to verify

try:
    # Verify transaction output proof
    api_response = api_instance.verify_tx_out_proof(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BitcoinApi->verify_tx_out_proof: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsVerifyTxOutProofRequest**](RequestsVerifyTxOutProofRequest.md)| Proof to verify | 

### Return type

[**ResponsesVerifyTxOutProofResponse**](ResponsesVerifyTxOutProofResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

