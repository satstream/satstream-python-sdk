# satstream_python_sdk.OutputsApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_output_by_outpoint**](OutputsApi.md#get_output_by_outpoint) | **GET** /output/{outpoint} | Get output info by outpoint
[**get_outputs**](OutputsApi.md#get_outputs) | **POST** /outputs | Get multiple outputs

# **get_output_by_outpoint**
> InlineResponse20025 get_output_by_outpoint(outpoint)

Get output info by outpoint

Retrieve information about a specific UTXO using outpoint string

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
api_instance = satstream_python_sdk.OutputsApi(satstream_python_sdk.ApiClient(configuration))
outpoint = 'outpoint_example' # str | Outpoint

try:
    # Get output info by outpoint
    api_response = api_instance.get_output_by_outpoint(outpoint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutputsApi->get_output_by_outpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outpoint** | **str**| Outpoint | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outputs**
> InlineResponse2002 get_outputs(body)

Get multiple outputs

Retrieve information about multiple UTXOs

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
api_instance = satstream_python_sdk.OutputsApi(satstream_python_sdk.ApiClient(configuration))
body = ['body_example'] # list[str] | Outpoints

try:
    # Get multiple outputs
    api_response = api_instance.get_outputs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutputsApi->get_outputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| Outpoints | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

