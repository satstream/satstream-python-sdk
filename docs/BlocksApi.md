# satstream_python_sdk.BlocksApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_block_count**](BlocksApi.md#get_block_count) | **GET** /blockcount | Get the height of the latest block
[**get_block_decoded**](BlocksApi.md#get_block_decoded) | **GET** /block/raw/{identifier}/decoded | Get block by hash or height (verbosity 2)
[**get_block_hash_by_height**](BlocksApi.md#get_block_hash_by_height) | **GET** /blockhash/{block_height} | Returns blockhash of specified block.
[**get_block_hex**](BlocksApi.md#get_block_hex) | **GET** /block/raw/{identifier}/hex | Get block by hash or height (verbosity 0)
[**get_block_info**](BlocksApi.md#get_block_info) | **GET** /block/{identifier} | Get block info by hash or height
[**get_block_prevout**](BlocksApi.md#get_block_prevout) | **GET** /block/raw/{identifier}/prevout | Get block by hash or height (verbosity 3)
[**get_block_stats**](BlocksApi.md#get_block_stats) | **POST** /block/stats | Get block stats
[**get_block_summary**](BlocksApi.md#get_block_summary) | **GET** /block/raw/{identifier}/summary | Get block by hash or height (verbosity 1)
[**get_blockchain_info**](BlocksApi.md#get_blockchain_info) | **GET** /blockchain/info | Get blockchain information
[**get_blocks**](BlocksApi.md#get_blocks) | **GET** /blocks | Returns the latest block height, last 100 block hashes, and featured inscriptions
[**get_latest_block_height**](BlocksApi.md#get_latest_block_height) | **GET** /blockheight | Returns the height of the latest block.
[**get_latest_blockhash**](BlocksApi.md#get_latest_blockhash) | **GET** /blockhash | Returns blockhash for the latest block.
[**get_latest_blocktime**](BlocksApi.md#get_latest_blocktime) | **GET** /blocktime | Get the timestamp of the latest block

# **get_block_count**
> InlineResponse2007 get_block_count()

Get the height of the latest block

Returns the height of the latest block

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
api_instance = satstream_python_sdk.BlocksApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Get the height of the latest block
    api_response = api_instance.get_block_count()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_block_count: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_decoded**
> InlineResponse200 get_block_decoded(identifier)

Get block by hash or height (verbosity 2)

Get block by hash or height as a decoded object

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
api_instance = satstream_python_sdk.BlocksApi(satstream_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Block hash or height

try:
    # Get block by hash or height (verbosity 2)
    api_response = api_instance.get_block_decoded(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_block_decoded: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Block hash or height | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_hash_by_height**
> InlineResponse2001 get_block_hash_by_height(block_height)

Returns blockhash of specified block.

Returns blockhash of specified block.

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
api_instance = satstream_python_sdk.BlocksApi(satstream_python_sdk.ApiClient(configuration))
block_height = 'block_height_example' # str | Block Height

try:
    # Returns blockhash of specified block.
    api_response = api_instance.get_block_hash_by_height(block_height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_block_hash_by_height: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_height** | **str**| Block Height | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_hex**
> InlineResponse2001 get_block_hex(identifier)

Get block by hash or height (verbosity 0)

Get block by hash or height as a raw hex string

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
api_instance = satstream_python_sdk.BlocksApi(satstream_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Block hash or height

try:
    # Get block by hash or height (verbosity 0)
    api_response = api_instance.get_block_hex(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_block_hex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Block hash or height | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_info**
> InlineResponse2005 get_block_info(identifier)

Get block info by hash or height

Get detailed information about a specific block by hash or height

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
api_instance = satstream_python_sdk.BlocksApi(satstream_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Block hash or height

try:
    # Get block info by hash or height
    api_response = api_instance.get_block_info(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_block_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Block hash or height | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_prevout**
> InlineResponse2002 get_block_prevout(identifier)

Get block by hash or height (verbosity 3)

Get block by hash or height with prevout information

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
api_instance = satstream_python_sdk.BlocksApi(satstream_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Block hash or height

try:
    # Get block by hash or height (verbosity 3)
    api_response = api_instance.get_block_prevout(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_block_prevout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Block hash or height | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_stats**
> InlineResponse2004 get_block_stats(body)

Get block stats

Computes per block statistics for a given window

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
api_instance = satstream_python_sdk.BlocksApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsGetBlockStatsRequest() # RequestsGetBlockStatsRequest | Block stats request parameters

try:
    # Get block stats
    api_response = api_instance.get_block_stats(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_block_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsGetBlockStatsRequest**](RequestsGetBlockStatsRequest.md)| Block stats request parameters | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_summary**
> InlineResponse2003 get_block_summary(identifier)

Get block by hash or height (verbosity 1)

Get block by hash or height as a summary object

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
api_instance = satstream_python_sdk.BlocksApi(satstream_python_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Block hash or height

try:
    # Get block by hash or height (verbosity 1)
    api_response = api_instance.get_block_summary(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_block_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Block hash or height | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blockchain_info**
> InlineResponse2006 get_blockchain_info()

Get blockchain information

Returns an object containing various state info regarding blockchain processing

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
api_instance = satstream_python_sdk.BlocksApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Get blockchain information
    api_response = api_instance.get_blockchain_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_blockchain_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blocks**
> InlineResponse2008 get_blocks()

Returns the latest block height, last 100 block hashes, and featured inscriptions

Returns the latest block height, last 100 block hashes, and featured inscriptions

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
api_instance = satstream_python_sdk.BlocksApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Returns the latest block height, last 100 block hashes, and featured inscriptions
    api_response = api_instance.get_blocks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_blocks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_block_height**
> InlineResponse2007 get_latest_block_height()

Returns the height of the latest block.

Returns the height of the latest block.

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
api_instance = satstream_python_sdk.BlocksApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Returns the height of the latest block.
    api_response = api_instance.get_latest_block_height()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_latest_block_height: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_blockhash**
> InlineResponse2001 get_latest_blockhash()

Returns blockhash for the latest block.

Returns blockhash for the latest block.

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
api_instance = satstream_python_sdk.BlocksApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Returns blockhash for the latest block.
    api_response = api_instance.get_latest_blockhash()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_latest_blockhash: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_blocktime**
> InlineResponse2007 get_latest_blocktime()

Get the timestamp of the latest block

Returns the UNIX timestamp of when the latest block was mined

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
api_instance = satstream_python_sdk.BlocksApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Get the timestamp of the latest block
    api_response = api_instance.get_latest_blocktime()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_latest_blocktime: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

