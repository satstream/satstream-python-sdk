# satstream_python_sdk.MempoolApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mempool_ancestors**](MempoolApi.md#get_mempool_ancestors) | **POST** /mempool/ancestors | Get mempool ancestors
[**get_mempool_descendants**](MempoolApi.md#get_mempool_descendants) | **POST** /mempool/descendants | Get mempool descendants
[**get_mempool_info**](MempoolApi.md#get_mempool_info) | **GET** /mempool/info | Get mempool information
[**get_raw_mempool**](MempoolApi.md#get_raw_mempool) | **POST** /mempool/raw | Get raw mempool
[**test_mempool_accept**](MempoolApi.md#test_mempool_accept) | **POST** /mempool/test-accept | Test mempool accept

# **get_mempool_ancestors**
> InlineResponse20020 get_mempool_ancestors(body)

Get mempool ancestors

Returns all in-mempool ancestors for a transaction in the mempool

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
api_instance = satstream_python_sdk.MempoolApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsGetMempoolAncestorsRequest() # RequestsGetMempoolAncestorsRequest | Mempool ancestors request parameters

try:
    # Get mempool ancestors
    api_response = api_instance.get_mempool_ancestors(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MempoolApi->get_mempool_ancestors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsGetMempoolAncestorsRequest**](RequestsGetMempoolAncestorsRequest.md)| Mempool ancestors request parameters | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mempool_descendants**
> InlineResponse20021 get_mempool_descendants(body)

Get mempool descendants

Returns all in-mempool descendants for a transaction in the mempool

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
api_instance = satstream_python_sdk.MempoolApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsGetMempoolDescendantsRequest() # RequestsGetMempoolDescendantsRequest | Mempool descendants request parameters

try:
    # Get mempool descendants
    api_response = api_instance.get_mempool_descendants(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MempoolApi->get_mempool_descendants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsGetMempoolDescendantsRequest**](RequestsGetMempoolDescendantsRequest.md)| Mempool descendants request parameters | 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mempool_info**
> InlineResponse20022 get_mempool_info()

Get mempool information

Returns details on the active state of the TX memory pool

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
api_instance = satstream_python_sdk.MempoolApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Get mempool information
    api_response = api_instance.get_mempool_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MempoolApi->get_mempool_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_mempool**
> InlineResponse20023 get_raw_mempool(body)

Get raw mempool

Returns all transaction ids in memory pool

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
api_instance = satstream_python_sdk.MempoolApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsGetRawMempoolRequest() # RequestsGetRawMempoolRequest | Raw mempool request parameters

try:
    # Get raw mempool
    api_response = api_instance.get_raw_mempool(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MempoolApi->get_raw_mempool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsGetRawMempoolRequest**](RequestsGetRawMempoolRequest.md)| Raw mempool request parameters | 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_mempool_accept**
> InlineResponse20024 test_mempool_accept(body)

Test mempool accept

Tests whether raw transactions would be accepted by mempool

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
api_instance = satstream_python_sdk.MempoolApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsTestMempoolAcceptRequest() # RequestsTestMempoolAcceptRequest | Raw transactions to test

try:
    # Test mempool accept
    api_response = api_instance.test_mempool_accept(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MempoolApi->test_mempool_accept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsTestMempoolAcceptRequest**](RequestsTestMempoolAcceptRequest.md)| Raw transactions to test | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

