# satstream_python_sdk.NetworkApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_chain_tx_stats**](NetworkApi.md#get_chain_tx_stats) | **POST** /chain/txstats | Get chain tx stats
[**get_difficulty**](NetworkApi.md#get_difficulty) | **GET** /chain/difficulty | Get difficulty

# **get_chain_tx_stats**
> InlineResponse20014 get_chain_tx_stats(body)

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
api_instance = satstream_python_sdk.NetworkApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsGetChainTxStatsRequest() # RequestsGetChainTxStatsRequest | Chain tx stats request parameters

try:
    # Get chain tx stats
    api_response = api_instance.get_chain_tx_stats(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_chain_tx_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsGetChainTxStatsRequest**](RequestsGetChainTxStatsRequest.md)| Chain tx stats request parameters | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_difficulty**
> InlineResponse20013 get_difficulty()

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
api_instance = satstream_python_sdk.NetworkApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Get difficulty
    api_response = api_instance.get_difficulty()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_difficulty: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

