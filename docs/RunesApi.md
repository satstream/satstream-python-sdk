# satstream_python_sdk.RunesApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_runes_holders**](RunesApi.md#get_runes_holders) | **GET** /runes/{runeId}/holders | Get rune holders
[**get_runes_info**](RunesApi.md#get_runes_info) | **GET** /runes/{runeId} | Get rune info
[**get_runes_info_list**](RunesApi.md#get_runes_info_list) | **GET** /runes | Get runes info list

# **get_runes_holders**
> ResponsesGetRuneHolders get_runes_holders(rune_id)

Get rune holders

Get a list of addresses holding a specific rune

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
rune_id = 'rune_id_example' # str | Rune ID

try:
    # Get rune holders
    api_response = api_instance.get_runes_holders(rune_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunesApi->get_runes_holders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rune_id** | **str**| Rune ID | 

### Return type

[**ResponsesGetRuneHolders**](ResponsesGetRuneHolders.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runes_info**
> ResponsesGetRuneInfo get_runes_info(rune_id)

Get rune info

Get detailed information about a specific rune

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
rune_id = 'rune_id_example' # str | Rune ID

try:
    # Get rune info
    api_response = api_instance.get_runes_info(rune_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunesApi->get_runes_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rune_id** | **str**| Rune ID | 

### Return type

[**ResponsesGetRuneInfo**](ResponsesGetRuneInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runes_info_list**
> ResponsesGetRunesInfoList get_runes_info_list(page=page, per_page=per_page)

Get runes info list

Get information about all runes

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
page = 56 # int | Page number (default: 1) (optional)
per_page = 56 # int | Items per page (default: 10) (optional)

try:
    # Get runes info list
    api_response = api_instance.get_runes_info_list(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunesApi->get_runes_info_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (default: 1) | [optional] 
 **per_page** | **int**| Items per page (default: 10) | [optional] 

### Return type

[**ResponsesGetRunesInfoList**](ResponsesGetRunesInfoList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

