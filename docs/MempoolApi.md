# satstream_python_sdk.MempoolApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_address_mempool_transactions**](MempoolApi.md#get_address_mempool_transactions) | **GET** /mempool/addresses/{address}/transactions | Get address mempool transactions
[**get_mempool_transaction_info**](MempoolApi.md#get_mempool_transaction_info) | **GET** /mempool/transactions/{txid} | Get mempool transaction info
[**get_mempool_transactions**](MempoolApi.md#get_mempool_transactions) | **GET** /mempool/transactions | Get mempool transactions

# **get_address_mempool_transactions**
> ResponsesGetAddressMempoolTxs get_address_mempool_transactions(address)

Get address mempool transactions

Get all mempool transactions for a specific address

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
api_instance = satstream_python_sdk.MempoolApi(satstream_python_sdk.ApiClient(configuration))
address = 'address_example' # str | Bitcoin address

try:
    # Get address mempool transactions
    api_response = api_instance.get_address_mempool_transactions(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MempoolApi->get_address_mempool_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Bitcoin address | 

### Return type

[**ResponsesGetAddressMempoolTxs**](ResponsesGetAddressMempoolTxs.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mempool_transaction_info**
> ResponsesGetMempoolTxInfo get_mempool_transaction_info(txid)

Get mempool transaction info

Get information about a specific transaction in the mempool

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
api_instance = satstream_python_sdk.MempoolApi(satstream_python_sdk.ApiClient(configuration))
txid = 'txid_example' # str | Transaction ID

try:
    # Get mempool transaction info
    api_response = api_instance.get_mempool_transaction_info(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MempoolApi->get_mempool_transaction_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Transaction ID | 

### Return type

[**ResponsesGetMempoolTxInfo**](ResponsesGetMempoolTxInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mempool_transactions**
> ResponsesGetMempoolTransactions get_mempool_transactions()

Get mempool transactions

Get all transactions currently in the mempool

### Example
```python
from __future__ import print_function
import time
import satstream_python_sdk
from satstream_python_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = satstream_python_sdk.MempoolApi()

try:
    # Get mempool transactions
    api_response = api_instance.get_mempool_transactions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MempoolApi->get_mempool_transactions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponsesGetMempoolTransactions**](ResponsesGetMempoolTransactions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

