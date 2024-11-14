# swagger_client.FeesApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_recommended_fees**](FeesApi.md#get_recommended_fees) | **GET** /fees | Get recommended fees

# **get_recommended_fees**
> ResponsesGetFees get_recommended_fees()

Get recommended fees

Get recommended fees for Bitcoin transactions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeesApi()

try:
    # Get recommended fees
    api_response = api_instance.get_recommended_fees()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeesApi->get_recommended_fees: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponsesGetFees**](ResponsesGetFees.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

