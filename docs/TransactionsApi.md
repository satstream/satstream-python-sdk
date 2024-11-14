# satstream_python_sdk.TransactionsApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**broadcast_transaction**](TransactionsApi.md#broadcast_transaction) | **POST** /transactions/broadcast | Broadcast transaction
[**get_transaction**](TransactionsApi.md#get_transaction) | **GET** /indexer/tx/{hash} | Get transaction
[**get_transaction_info**](TransactionsApi.md#get_transaction_info) | **GET** /transactions/{txid} | Get transaction info

# **broadcast_transaction**
> ResponsesSendRawTransaction broadcast_transaction(body)

Broadcast transaction

Broadcast a raw transaction to the Bitcoin network

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
body = 'body_example' # str | Raw transaction hex

try:
    # Broadcast transaction
    api_response = api_instance.broadcast_transaction(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->broadcast_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Raw transaction hex | 

### Return type

[**ResponsesSendRawTransaction**](ResponsesSendRawTransaction.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> ResponsesGetTransaction get_transaction(hash)

Get transaction

Get a transaction by its hash

### Example
```python
from __future__ import print_function
import time
import satstream_python_sdk
from satstream_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = satstream_python_sdk.TransactionsApi()
hash = 'hash_example' # str | Transaction hash

try:
    # Get transaction
    api_response = api_instance.get_transaction(hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Transaction hash | 

### Return type

[**ResponsesGetTransaction**](ResponsesGetTransaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_info**
> ResponsesGetTxInfo get_transaction_info(txid)

Get transaction info

Get detailed information about a specific transaction

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
    api_response = api_instance.get_transaction_info(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transaction_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Transaction ID | 

### Return type

[**ResponsesGetTxInfo**](ResponsesGetTxInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

