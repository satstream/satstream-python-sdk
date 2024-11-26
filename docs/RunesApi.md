# satstream_python_sdk.RunesApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_latest_runes**](RunesApi.md#get_latest_runes) | **GET** /runes | Get latest runes
[**get_latest_runes_page**](RunesApi.md#get_latest_runes_page) | **GET** /runes/{page} | Get latest runes page
[**get_rune**](RunesApi.md#get_rune) | **GET** /rune/{rune_name} | Get rune info

# **get_latest_runes**
> InlineResponse20030 get_latest_runes()

Get latest runes

Retrieve information about the last 100 inscribed runes (first page)

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
api_instance = satstream_python_sdk.RunesApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Get latest runes
    api_response = api_instance.get_latest_runes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunesApi->get_latest_runes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_runes_page**
> InlineResponse20030 get_latest_runes_page(page)

Get latest runes page

Retrieve a specific page of 100 inscribed runes

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
api_instance = satstream_python_sdk.RunesApi(satstream_python_sdk.ApiClient(configuration))
page = 56 # int | Page number

try:
    # Get latest runes page
    api_response = api_instance.get_latest_runes_page(page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunesApi->get_latest_runes_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rune**
> InlineResponse20029 get_rune(rune_name)

Get rune info

Retrieve information about a specific rune

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
api_instance = satstream_python_sdk.RunesApi(satstream_python_sdk.ApiClient(configuration))
rune_name = 'rune_name_example' # str | Rune Name

try:
    # Get rune info
    api_response = api_instance.get_rune(rune_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunesApi->get_rune: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rune_name** | **str**| Rune Name | 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

