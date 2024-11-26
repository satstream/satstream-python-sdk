# satstream_python_sdk.MiningApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mining_info**](MiningApi.md#get_mining_info) | **GET** /mining/info | Get mining information
[**get_network_hashps**](MiningApi.md#get_network_hashps) | **POST** /mining/networkhashps | Get network hash per second

# **get_mining_info**
> InlineResponse20024 get_mining_info()

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
api_instance = satstream_python_sdk.MiningApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Get mining information
    api_response = api_instance.get_mining_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiningApi->get_mining_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_hashps**
> InlineResponse20013 get_network_hashps(body)

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
api_instance = satstream_python_sdk.MiningApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsGetNetworkHashPSRequest() # RequestsGetNetworkHashPSRequest | Network hash rate parameters

try:
    # Get network hash per second
    api_response = api_instance.get_network_hashps(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiningApi->get_network_hashps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsGetNetworkHashPSRequest**](RequestsGetNetworkHashPSRequest.md)| Network hash rate parameters | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

