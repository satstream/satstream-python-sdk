# satstream_python_sdk.AddressesApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_address**](AddressesApi.md#get_address) | **GET** /address/{address} | Get address info
[**get_address_utxos**](AddressesApi.md#get_address_utxos) | **GET** /address/{address}/outputs | Get UTXOs for an address
[**validate_address**](AddressesApi.md#validate_address) | **GET** /address/{address}/validate | Validate address
[**verify_message**](AddressesApi.md#verify_message) | **POST** /address/verify-message | Verify message

# **get_address**
> InlineResponse2001 get_address(address)

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

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_utxos**
> InlineResponse2002 get_address_utxos(address, type=type)

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

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_address**
> InlineResponse2003 validate_address(address)

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

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_message**
> InlineResponse200 verify_message(body)

Verify message

Verifies a signed message

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
body = satstream_python_sdk.RequestsVerifyMessageRequest() # RequestsVerifyMessageRequest | Message verification parameters

try:
    # Verify message
    api_response = api_instance.verify_message(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->verify_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsVerifyMessageRequest**](RequestsVerifyMessageRequest.md)| Message verification parameters | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

