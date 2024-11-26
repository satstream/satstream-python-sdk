# satstream_python_sdk.SatoshisApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_satoshi**](SatoshisApi.md#get_satoshi) | **GET** /sat/{number} | Get satoshi info

# **get_satoshi**
> InlineResponse20028 get_satoshi(number)

Get satoshi info

Retrieve information about a specific satoshi

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
api_instance = satstream_python_sdk.SatoshisApi(satstream_python_sdk.ApiClient(configuration))
number = 56 # int | Satoshi Number

try:
    # Get satoshi info
    api_response = api_instance.get_satoshi(number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SatoshisApi->get_satoshi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **int**| Satoshi Number | 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

