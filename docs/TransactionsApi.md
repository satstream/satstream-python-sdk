# satstream_python_sdk.TransactionsApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**combine_raw_transaction**](TransactionsApi.md#combine_raw_transaction) | **POST** /tx/combine | Combine Raw Transactions
[**convert_to_psbt**](TransactionsApi.md#convert_to_psbt) | **POST** /tx/convert-to-psbt | Convert Raw Transaction to PSBT
[**create_raw_transaction**](TransactionsApi.md#create_raw_transaction) | **POST** /tx/create | Create Raw Transaction
[**decode_tx**](TransactionsApi.md#decode_tx) | **GET** /tx/{txid}/decode | Decode a transaction
[**get_raw_transaction_decoded**](TransactionsApi.md#get_raw_transaction_decoded) | **GET** /tx/{txid}/decoded | Get raw transaction (verbosity 1)
[**get_raw_transaction_hex**](TransactionsApi.md#get_raw_transaction_hex) | **GET** /tx/{txid}/hex | Get raw transaction (verbosity 0)
[**get_raw_transaction_prevout**](TransactionsApi.md#get_raw_transaction_prevout) | **GET** /tx/{txid}/prevout | Get raw transaction (verbosity 2)
[**get_transaction**](TransactionsApi.md#get_transaction) | **GET** /tx/{txid} | Get transaction info
[**get_tx_out**](TransactionsApi.md#get_tx_out) | **POST** /tx/out | Get transaction output
[**get_tx_out_proof**](TransactionsApi.md#get_tx_out_proof) | **POST** /tx/outproof | Get transaction output proof
[**get_tx_out_set_info**](TransactionsApi.md#get_tx_out_set_info) | **POST** /tx/out/set/info | Get transaction output set information
[**get_tx_spending_prevout**](TransactionsApi.md#get_tx_spending_prevout) | **POST** /tx/spending-prevout | Get transaction spending prevout
[**send_raw_transaction**](TransactionsApi.md#send_raw_transaction) | **POST** /tx/send | Send raw transaction
[**verify_tx_out_proof**](TransactionsApi.md#verify_tx_out_proof) | **POST** /tx/outproof/verify | Verify transaction output proof

# **combine_raw_transaction**
> CombineRawTransactionResponse combine_raw_transaction(body)

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
api_instance = satstream_python_sdk.TransactionsApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.TransactionCombineRawTransactionRequest() # TransactionCombineRawTransactionRequest | Array of hex-encoded raw transactions

try:
    # Combine Raw Transactions
    api_response = api_instance.combine_raw_transaction(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->combine_raw_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionCombineRawTransactionRequest**](TransactionCombineRawTransactionRequest.md)| Array of hex-encoded raw transactions | 

### Return type

[**CombineRawTransactionResponse**](CombineRawTransactionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_to_psbt**
> ConvertToPSBTResponse convert_to_psbt(body)

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
api_instance = satstream_python_sdk.TransactionsApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.TransactionConvertToPSBTRequest() # TransactionConvertToPSBTRequest | Raw transaction conversion parameters

try:
    # Convert Raw Transaction to PSBT
    api_response = api_instance.convert_to_psbt(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->convert_to_psbt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionConvertToPSBTRequest**](TransactionConvertToPSBTRequest.md)| Raw transaction conversion parameters | 

### Return type

[**ConvertToPSBTResponse**](ConvertToPSBTResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_raw_transaction**
> CreateRawTransactionResponse create_raw_transaction(body)

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
api_instance = satstream_python_sdk.TransactionsApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.TransactionCreateRawTxRequest() # TransactionCreateRawTxRequest | Transaction parameters

try:
    # Create Raw Transaction
    api_response = api_instance.create_raw_transaction(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->create_raw_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionCreateRawTxRequest**](TransactionCreateRawTxRequest.md)| Transaction parameters | 

### Return type

[**CreateRawTransactionResponse**](CreateRawTransactionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decode_tx**
> DecodeTransactionResponse decode_tx(txid)

Decode a transaction

Decodes a transaction and returns its inscriptions and runestone data

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
api_instance = satstream_python_sdk.TransactionsApi(satstream_python_sdk.ApiClient(configuration))
txid = 'txid_example' # str | Transaction ID

try:
    # Decode a transaction
    api_response = api_instance.decode_tx(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->decode_tx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Transaction ID | 

### Return type

[**DecodeTransactionResponse**](DecodeTransactionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_transaction_decoded**
> GetRawTransactionDecodedResponse get_raw_transaction_decoded(txid)

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
api_instance = satstream_python_sdk.TransactionsApi(satstream_python_sdk.ApiClient(configuration))
txid = 'txid_example' # str | Transaction ID

try:
    # Get raw transaction (verbosity 1)
    api_response = api_instance.get_raw_transaction_decoded(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_raw_transaction_decoded: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Transaction ID | 

### Return type

[**GetRawTransactionDecodedResponse**](GetRawTransactionDecodedResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_transaction_hex**
> GetRawTransactionHexResponse get_raw_transaction_hex(txid)

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
api_instance = satstream_python_sdk.TransactionsApi(satstream_python_sdk.ApiClient(configuration))
txid = 'txid_example' # str | Transaction ID

try:
    # Get raw transaction (verbosity 0)
    api_response = api_instance.get_raw_transaction_hex(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_raw_transaction_hex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Transaction ID | 

### Return type

[**GetRawTransactionHexResponse**](GetRawTransactionHexResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_transaction_prevout**
> GetRawTransactionPrevoutResponse get_raw_transaction_prevout(txid)

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
api_instance = satstream_python_sdk.TransactionsApi(satstream_python_sdk.ApiClient(configuration))
txid = 'txid_example' # str | Transaction ID

try:
    # Get raw transaction (verbosity 2)
    api_response = api_instance.get_raw_transaction_prevout(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_raw_transaction_prevout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Transaction ID | 

### Return type

[**GetRawTransactionPrevoutResponse**](GetRawTransactionPrevoutResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> GetTransactionResponse get_transaction(txid)

Get transaction info

Retrieve information about a specific transaction

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
api_instance = satstream_python_sdk.TransactionsApi(satstream_python_sdk.ApiClient(configuration))
txid = 'txid_example' # str | Transaction ID

try:
    # Get transaction info
    api_response = api_instance.get_transaction(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Transaction ID | 

### Return type

[**GetTransactionResponse**](GetTransactionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tx_out**
> GetTxOutResponse get_tx_out(body)

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
api_instance = satstream_python_sdk.TransactionsApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.TransactionGetTxOutRequest() # TransactionGetTxOutRequest | Transaction output request parameters

try:
    # Get transaction output
    api_response = api_instance.get_tx_out(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_tx_out: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionGetTxOutRequest**](TransactionGetTxOutRequest.md)| Transaction output request parameters | 

### Return type

[**GetTxOutResponse**](GetTxOutResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tx_out_proof**
> GetTxOutProofResponse get_tx_out_proof(body)

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
api_instance = satstream_python_sdk.TransactionsApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.TransactionGetTxOutProofRequest() # TransactionGetTxOutProofRequest | Transaction proof request parameters

try:
    # Get transaction output proof
    api_response = api_instance.get_tx_out_proof(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_tx_out_proof: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionGetTxOutProofRequest**](TransactionGetTxOutProofRequest.md)| Transaction proof request parameters | 

### Return type

[**GetTxOutProofResponse**](GetTxOutProofResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tx_out_set_info**
> InlineResponse2002 get_tx_out_set_info(body)

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
api_instance = satstream_python_sdk.TransactionsApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.TransactionGetTxOutSetInfoRequest() # TransactionGetTxOutSetInfoRequest | UTXO set info request parameters

try:
    # Get transaction output set information
    api_response = api_instance.get_tx_out_set_info(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_tx_out_set_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionGetTxOutSetInfoRequest**](TransactionGetTxOutSetInfoRequest.md)| UTXO set info request parameters | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tx_spending_prevout**
> GetTxSpendingPrevoutResponse get_tx_spending_prevout(body)

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
api_instance = satstream_python_sdk.TransactionsApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.TransactionGetTxSpendingPrevoutRequest() # TransactionGetTxSpendingPrevoutRequest | Transaction spending prevout request

try:
    # Get transaction spending prevout
    api_response = api_instance.get_tx_spending_prevout(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_tx_spending_prevout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionGetTxSpendingPrevoutRequest**](TransactionGetTxSpendingPrevoutRequest.md)| Transaction spending prevout request | 

### Return type

[**GetTxSpendingPrevoutResponse**](GetTxSpendingPrevoutResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_raw_transaction**
> SendRawTransactionResponse send_raw_transaction(body)

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
api_instance = satstream_python_sdk.TransactionsApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.TransactionSendRawTransactionRequest() # TransactionSendRawTransactionRequest | Raw transaction to send

try:
    # Send raw transaction
    api_response = api_instance.send_raw_transaction(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->send_raw_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionSendRawTransactionRequest**](TransactionSendRawTransactionRequest.md)| Raw transaction to send | 

### Return type

[**SendRawTransactionResponse**](SendRawTransactionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_tx_out_proof**
> VerifyTxOutProofResponse verify_tx_out_proof(body)

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
api_instance = satstream_python_sdk.TransactionsApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.TransactionVerifyTxOutProofRequest() # TransactionVerifyTxOutProofRequest | Proof to verify

try:
    # Verify transaction output proof
    api_response = api_instance.verify_tx_out_proof(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->verify_tx_out_proof: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionVerifyTxOutProofRequest**](TransactionVerifyTxOutProofRequest.md)| Proof to verify | 

### Return type

[**VerifyTxOutProofResponse**](VerifyTxOutProofResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

