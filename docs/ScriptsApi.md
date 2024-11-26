# satstream_python_sdk.ScriptsApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**decode_script**](ScriptsApi.md#decode_script) | **POST** /script/decode | Decode Script

# **decode_script**
> DecodeScriptResponse decode_script(body)

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
api_instance = satstream_python_sdk.ScriptsApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.DecodeScriptRequest() # DecodeScriptRequest | Script to decode

try:
    # Decode Script
    api_response = api_instance.decode_script(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScriptsApi->decode_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DecodeScriptRequest**](DecodeScriptRequest.md)| Script to decode | 

### Return type

[**DecodeScriptResponse**](DecodeScriptResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

