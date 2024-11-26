# satstream_python_sdk.InscriptionsApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_inscription_child**](InscriptionsApi.md#fetch_inscription_child) | **GET** /inscription/{inscription_id}/{child_index} | Get inscription child info
[**fetch_inscriptions**](InscriptionsApi.md#fetch_inscriptions) | **POST** /inscriptions | Fetch multiple inscriptions
[**get_block_inscriptions**](InscriptionsApi.md#get_block_inscriptions) | **GET** /inscriptions/block/{block_height} | Get inscriptions in a specific block
[**get_inscription**](InscriptionsApi.md#get_inscription) | **GET** /inscription/{inscription_id} | Get inscription info
[**get_latest_inscriptions**](InscriptionsApi.md#get_latest_inscriptions) | **GET** /inscriptions | Get latest inscriptions
[**get_latest_inscriptions_page**](InscriptionsApi.md#get_latest_inscriptions_page) | **GET** /inscriptions/{page} | Get latest inscriptions page

# **fetch_inscription_child**
> InlineResponse20017 fetch_inscription_child(inscription_id, child_index)

Get inscription child info

Retrieve information about a specific child of an inscription

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
api_instance = satstream_python_sdk.InscriptionsApi(satstream_python_sdk.ApiClient(configuration))
inscription_id = 'inscription_id_example' # str | Inscription ID
child_index = 56 # int | Child Index

try:
    # Get inscription child info
    api_response = api_instance.fetch_inscription_child(inscription_id, child_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->fetch_inscription_child: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inscription_id** | **str**| Inscription ID | 
 **child_index** | **int**| Child Index | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_inscriptions**
> InlineResponse20019 fetch_inscriptions(body)

Fetch multiple inscriptions

Retrieve information about multiple inscriptions

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
api_instance = satstream_python_sdk.InscriptionsApi(satstream_python_sdk.ApiClient(configuration))
body = ['body_example'] # list[str] | Inscription IDs

try:
    # Fetch multiple inscriptions
    api_response = api_instance.fetch_inscriptions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->fetch_inscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| Inscription IDs | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_inscriptions**
> InlineResponse20018 get_block_inscriptions(block_height)

Get inscriptions in a specific block

Retrieve all inscriptions in a specific block

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
api_instance = satstream_python_sdk.InscriptionsApi(satstream_python_sdk.ApiClient(configuration))
block_height = 56 # int | Block Height

try:
    # Get inscriptions in a specific block
    api_response = api_instance.get_block_inscriptions(block_height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_block_inscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_height** | **int**| Block Height | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inscription**
> InlineResponse20017 get_inscription(inscription_id)

Get inscription info

Get information about a specific inscription

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
api_instance = satstream_python_sdk.InscriptionsApi(satstream_python_sdk.ApiClient(configuration))
inscription_id = 'inscription_id_example' # str | Inscription ID

try:
    # Get inscription info
    api_response = api_instance.get_inscription(inscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_inscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inscription_id** | **str**| Inscription ID | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_inscriptions**
> InlineResponse20018 get_latest_inscriptions()

Get latest inscriptions

Retrieve the latest 100 inscriptions (first page)

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
api_instance = satstream_python_sdk.InscriptionsApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Get latest inscriptions
    api_response = api_instance.get_latest_inscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_latest_inscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_inscriptions_page**
> InlineResponse20018 get_latest_inscriptions_page(page)

Get latest inscriptions page

Retrieve a specific page of 100 inscriptions

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
api_instance = satstream_python_sdk.InscriptionsApi(satstream_python_sdk.ApiClient(configuration))
page = 56 # int | Page number

try:
    # Get latest inscriptions page
    api_response = api_instance.get_latest_inscriptions_page(page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_latest_inscriptions_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

