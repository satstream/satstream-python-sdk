# satstream_python_sdk.AddressesApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_address**](AddressesApi.md#get_address) | **GET** /address/{address} | Get address info
[**get_address_balance**](AddressesApi.md#get_address_balance) | **GET** /address/{address}/balance | Get address balance
[**get_address_deltas**](AddressesApi.md#get_address_deltas) | **GET** /address/{address}/deltas | Get address deltas
[**get_address_rune_deltas**](AddressesApi.md#get_address_rune_deltas) | **GET** /address/{address}/deltas/runes | Get address rune deltas
[**get_address_utxos**](AddressesApi.md#get_address_utxos) | **GET** /address/{address}/outputs | Get UTXOs for an address
[**validate_address**](AddressesApi.md#validate_address) | **GET** /address/{address}/validate | Validate address

# **get_address**
> GetAddressResponse get_address(address)

Get address info

Get detailed information about a specific address

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
api_instance = satstream_python_sdk.AddressesApi(satstream_python_sdk.ApiClient(configuration))
address = 'address_example' # str | Address

try:
    # Get address info
    api_response = api_instance.get_address(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address | 

### Return type

[**GetAddressResponse**](GetAddressResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_balance**
> GetAddressBalanceResponse get_address_balance(address)

Get address balance

Get the total BTC balance of an address by summing all its deltas

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
api_instance = satstream_python_sdk.AddressesApi(satstream_python_sdk.ApiClient(configuration))
address = 'address_example' # str | Address

try:
    # Get address balance
    api_response = api_instance.get_address_balance(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_address_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address | 

### Return type

[**GetAddressBalanceResponse**](GetAddressBalanceResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_deltas**
> GetAddressDeltasResponse get_address_deltas(address, page_size=page_size, start_height=start_height, end_height=end_height, cursor=cursor)

Get address deltas

Get deltas for a specific address with pagination

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
api_instance = satstream_python_sdk.AddressesApi(satstream_python_sdk.ApiClient(configuration))
address = 'address_example' # str | Address
page_size = 56 # int | Number of results per page (default: 100, max: 1000) (optional)
start_height = 56 # int | Start block height (optional)
end_height = 56 # int | End block height (optional)
cursor = 'cursor_example' # str | Base64 encoded cursor for pagination (optional)

try:
    # Get address deltas
    api_response = api_instance.get_address_deltas(address, page_size=page_size, start_height=start_height, end_height=end_height, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_address_deltas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address | 
 **page_size** | **int**| Number of results per page (default: 100, max: 1000) | [optional] 
 **start_height** | **int**| Start block height | [optional] 
 **end_height** | **int**| End block height | [optional] 
 **cursor** | **str**| Base64 encoded cursor for pagination | [optional] 

### Return type

[**GetAddressDeltasResponse**](GetAddressDeltasResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_rune_deltas**
> GetAddressRuneDeltasResponse get_address_rune_deltas(address, page_size=page_size, start_height=start_height, end_height=end_height, cursor=cursor)

Get address rune deltas

Get rune deltas for a specific address with pagination

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
api_instance = satstream_python_sdk.AddressesApi(satstream_python_sdk.ApiClient(configuration))
address = 'address_example' # str | Address
page_size = 56 # int | Number of results per page (default: 100, max: 1000) (optional)
start_height = 56 # int | Start block height (optional)
end_height = 56 # int | End block height (optional)
cursor = 'cursor_example' # str | Cursor for pagination (optional)

try:
    # Get address rune deltas
    api_response = api_instance.get_address_rune_deltas(address, page_size=page_size, start_height=start_height, end_height=end_height, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_address_rune_deltas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address | 
 **page_size** | **int**| Number of results per page (default: 100, max: 1000) | [optional] 
 **start_height** | **int**| Start block height | [optional] 
 **end_height** | **int**| End block height | [optional] 
 **cursor** | **str**| Cursor for pagination | [optional] 

### Return type

[**GetAddressRuneDeltasResponse**](GetAddressRuneDeltasResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_utxos**
> GetAddressUTXOsResponse get_address_utxos(address, type=type)

Get UTXOs for an address

Retrieve UTXOs held by a specific address with optional type filtering

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
api_instance = satstream_python_sdk.AddressesApi(satstream_python_sdk.ApiClient(configuration))
address = 'address_example' # str | Address
type = 'type_example' # str | UTXO Type (optional)

try:
    # Get UTXOs for an address
    api_response = api_instance.get_address_utxos(address, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_address_utxos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address | 
 **type** | **str**| UTXO Type | [optional] 

### Return type

[**GetAddressUTXOsResponse**](GetAddressUTXOsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_address**
> ValidateAddressResponse validate_address(address)

Validate address

Returns information about the given Bitcoin address

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
api_instance = satstream_python_sdk.AddressesApi(satstream_python_sdk.ApiClient(configuration))
address = 'address_example' # str | Bitcoin address to validate

try:
    # Validate address
    api_response = api_instance.validate_address(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->validate_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Bitcoin address to validate | 

### Return type

[**ValidateAddressResponse**](ValidateAddressResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

