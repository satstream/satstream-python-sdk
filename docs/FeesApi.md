# satstream_python_sdk.FeesApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**estimate_raw_fee**](FeesApi.md#estimate_raw_fee) | **POST** /fee/estimate-raw | Estimate Raw Fee
[**estimate_smart_fee**](FeesApi.md#estimate_smart_fee) | **POST** /fee/estimate-smart | Estimate smart fee

# **estimate_raw_fee**
> InlineResponse20015 estimate_raw_fee(body)

Estimate Raw Fee

Estimates the approximate fee per kilobyte needed for a transaction to begin confirmation within conf_target blocks if possible.

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
api_instance = satstream_python_sdk.FeesApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsEstimateRawFeeRequest() # RequestsEstimateRawFeeRequest | Fee estimation parameters

try:
    # Estimate Raw Fee
    api_response = api_instance.estimate_raw_fee(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->estimate_raw_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsEstimateRawFeeRequest**](RequestsEstimateRawFeeRequest.md)| Fee estimation parameters | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **estimate_smart_fee**
> InlineResponse20016 estimate_smart_fee(body)

Estimate smart fee

Estimates the approximate fee per kilobyte needed for a transaction to begin confirmation within conf_target blocks

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
api_instance = satstream_python_sdk.FeesApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsEstimateSmartFeeRequest() # RequestsEstimateSmartFeeRequest | Fee estimation parameters

try:
    # Estimate smart fee
    api_response = api_instance.estimate_smart_fee(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->estimate_smart_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsEstimateSmartFeeRequest**](RequestsEstimateSmartFeeRequest.md)| Fee estimation parameters | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

