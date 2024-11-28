# satstream_python_sdk.RunesApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_latest_runes**](RunesApi.md#get_latest_runes) | **GET** /runes | Get latest runes
[**get_latest_runes_page**](RunesApi.md#get_latest_runes_page) | **GET** /runes/{page} | Get latest runes page
[**get_rune**](RunesApi.md#get_rune) | **GET** /rune/{identifier} | Get rune info

# **get_latest_runes**
> GetLatestRunesResponse get_latest_runes()

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

[**GetLatestRunesResponse**](GetLatestRunesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_runes_page**
> GetLatestRunesResponse get_latest_runes_page(page)

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

[**GetLatestRunesResponse**](GetLatestRunesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rune**
> GetRuneResponse get_rune(identifier)

Get rune info

Retrieve information about a specific rune by name or ID (e.g., \"UNCOMMON•GOODS\" or \"1:0\")

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
identifier = 'identifier_example' # str | Rune Name or ID

try:
    # Get rune info
    api_response = api_instance.get_rune(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunesApi->get_rune: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Rune Name or ID | 

### Return type

[**GetRuneResponse**](GetRuneResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

