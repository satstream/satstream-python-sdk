# satstream-python-sdk.AddressesApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_address_balance**](AddressesApi.md#get_address_balance) | **GET** /addresses/{address}/balance | Get address balance
[**get_address_non_inscription_utxos**](AddressesApi.md#get_address_non_inscription_utxos) | **GET** /addresses/{address}/utxos | Get address non-inscription UTXOs
[**get_address_rune_balance**](AddressesApi.md#get_address_rune_balance) | **GET** /addresses/{address}/runes/{runeid} | Get address rune balance
[**get_address_runes_balance_list**](AddressesApi.md#get_address_runes_balance_list) | **GET** /addresses/{address}/runes | Get address runes balance list
[**get_address_timeframe_balance**](AddressesApi.md#get_address_timeframe_balance) | **GET** /addresses/{address}/balance/timeframe | Get address timeframe balance

# **get_address_balance**
> ResponsesGetAddressBalance get_address_balance(address)

Get address balance

Get the current balance of a Bitcoin address

### Example
```python
from __future__ import print_function
import time
import satstream-python-sdk
from satstream-python-sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = satstream-python-sdk.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = satstream-python-sdk.AddressesApi(satstream-python-sdk.ApiClient(configuration))
address = 'address_example' # str | Bitcoin address

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
 **address** | **str**| Bitcoin address | 

### Return type

[**ResponsesGetAddressBalance**](ResponsesGetAddressBalance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_non_inscription_utxos**
> ResponsesGetAddressNonInscriptionUTXO get_address_non_inscription_utxos(address)

Get address non-inscription UTXOs

Get all non-inscription UTXOs for a Bitcoin address

### Example
```python
from __future__ import print_function
import time
import satstream-python-sdk
from satstream-python-sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = satstream-python-sdk.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = satstream-python-sdk.AddressesApi(satstream-python-sdk.ApiClient(configuration))
address = 'address_example' # str | Bitcoin address

try:
    # Get address non-inscription UTXOs
    api_response = api_instance.get_address_non_inscription_utxos(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_address_non_inscription_utxos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Bitcoin address | 

### Return type

[**ResponsesGetAddressNonInscriptionUTXO**](ResponsesGetAddressNonInscriptionUTXO.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_rune_balance**
> ResponsesGetAddressRuneBalance get_address_rune_balance(address, runeid)

Get address rune balance

Get the balance of a specific rune for a Bitcoin address

### Example
```python
from __future__ import print_function
import time
import satstream-python-sdk
from satstream-python-sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = satstream-python-sdk.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = satstream-python-sdk.AddressesApi(satstream-python-sdk.ApiClient(configuration))
address = 'address_example' # str | Bitcoin address
runeid = 'runeid_example' # str | Rune ID

try:
    # Get address rune balance
    api_response = api_instance.get_address_rune_balance(address, runeid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_address_rune_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Bitcoin address | 
 **runeid** | **str**| Rune ID | 

### Return type

[**ResponsesGetAddressRuneBalance**](ResponsesGetAddressRuneBalance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_runes_balance_list**
> ResponsesGetAddressRunesBalanceList get_address_runes_balance_list(address)

Get address runes balance list

Get the balance of all runes for a Bitcoin address

### Example
```python
from __future__ import print_function
import time
import satstream-python-sdk
from satstream-python-sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = satstream-python-sdk.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = satstream-python-sdk.AddressesApi(satstream-python-sdk.ApiClient(configuration))
address = 'address_example' # str | Bitcoin address

try:
    # Get address runes balance list
    api_response = api_instance.get_address_runes_balance_list(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_address_runes_balance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Bitcoin address | 

### Return type

[**ResponsesGetAddressRunesBalanceList**](ResponsesGetAddressRunesBalanceList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_timeframe_balance**
> ResponsesGetAddressTimeframeBalance get_address_timeframe_balance(address, timeframe, token=token)

Get address timeframe balance

Get the balance of a Bitcoin address for a specific timeframe

### Example
```python
from __future__ import print_function
import time
import satstream-python-sdk
from satstream-python-sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = satstream-python-sdk.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = satstream-python-sdk.AddressesApi(satstream-python-sdk.ApiClient(configuration))
address = 'address_example' # str | Bitcoin address
timeframe = 'timeframe_example' # str | Timeframe
token = 'token_example' # str | Token (optional)

try:
    # Get address timeframe balance
    api_response = api_instance.get_address_timeframe_balance(address, timeframe, token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_address_timeframe_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Bitcoin address | 
 **timeframe** | **str**| Timeframe | 
 **token** | **str**| Token | [optional] 

### Return type

[**ResponsesGetAddressTimeframeBalance**](ResponsesGetAddressTimeframeBalance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

