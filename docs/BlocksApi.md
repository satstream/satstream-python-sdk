# satstream-python-sdk.BlocksApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_block_by_hash**](BlocksApi.md#get_block_by_hash) | **GET** /blocks/hash/{hash} | Get block by hash
[**get_block_info**](BlocksApi.md#get_block_info) | **GET** /blocks/{height} | Get block info
[**get_block_transactions**](BlocksApi.md#get_block_transactions) | **GET** /blocks/{height}/transactions | Get block transactions
[**get_current_block_height**](BlocksApi.md#get_current_block_height) | **GET** /blocks/current-height | Get current block height

# **get_block_by_hash**
> ResponsesGetBlockByHash get_block_by_hash(hash)

Get block by hash

Get information about a specific block by its hash

### Example
```python
from __future__ import print_function
import time
import satstream-python-sdk
from satstream-python-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = satstream-python-sdk.BlocksApi()
hash = 'hash_example' # str | Block hash

try:
    # Get block by hash
    api_response = api_instance.get_block_by_hash(hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_block_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Block hash | 

### Return type

[**ResponsesGetBlockByHash**](ResponsesGetBlockByHash.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_info**
> ResponsesGetBlockInfo get_block_info(height)

Get block info

Get information about a specific block by height

### Example
```python
from __future__ import print_function
import time
import satstream-python-sdk
from satstream-python-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = satstream-python-sdk.BlocksApi()
height = 56 # int | Block height

try:
    # Get block info
    api_response = api_instance.get_block_info(height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_block_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | **int**| Block height | 

### Return type

[**ResponsesGetBlockInfo**](ResponsesGetBlockInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_transactions**
> ResponsesGetBlockTransactions get_block_transactions(height)

Get block transactions

Get transactions for a specific block height

### Example
```python
from __future__ import print_function
import time
import satstream-python-sdk
from satstream-python-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = satstream-python-sdk.BlocksApi()
height = 56 # int | Block height

try:
    # Get block transactions
    api_response = api_instance.get_block_transactions(height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_block_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | **int**| Block height | 

### Return type

[**ResponsesGetBlockTransactions**](ResponsesGetBlockTransactions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_block_height**
> ResponsesGetBlockHeight get_current_block_height()

Get current block height

Get the current block height of the Bitcoin blockchain

### Example
```python
from __future__ import print_function
import time
import satstream-python-sdk
from satstream-python-sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = satstream-python-sdk.BlocksApi()

try:
    # Get current block height
    api_response = api_instance.get_current_block_height()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_current_block_height: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponsesGetBlockHeight**](ResponsesGetBlockHeight.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

