# satstream_python_sdk.BlocksApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_block_by_hash**](BlocksApi.md#get_block_by_hash) | **GET** /block/hash/{block_hash} | Get block info by hash

# **get_block_by_hash**
> GithubComSatstreamSsApiServerApiBlockResponsesBlockResponse get_block_by_hash(block_hash)

Get block info by hash

Get detailed information about a specific block by hash

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
api_instance = satstream_python_sdk.BlocksApi(satstream_python_sdk.ApiClient(configuration))
block_hash = 'block_hash_example' # str | Block Hash

try:
    # Get block info by hash
    api_response = api_instance.get_block_by_hash(block_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_block_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_hash** | **str**| Block Hash | 

### Return type

[**GithubComSatstreamSsApiServerApiBlockResponsesBlockResponse**](GithubComSatstreamSsApiServerApiBlockResponsesBlockResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

