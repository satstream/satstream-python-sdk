# satstream_python_sdk.PSBTsApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_psbt**](PSBTsApi.md#analyze_psbt) | **POST** /psbt/analyze | Analyze PSBT
[**combine_psbt**](PSBTsApi.md#combine_psbt) | **POST** /psbt/combine | Combine PSBTs
[**create_psbt**](PSBTsApi.md#create_psbt) | **POST** /psbt/create | Create PSBT
[**decode_psbt**](PSBTsApi.md#decode_psbt) | **POST** /psbt/decode | Decode PSBT
[**join_psbts**](PSBTsApi.md#join_psbts) | **POST** /psbt/join | Join PSBTs

# **analyze_psbt**
> InlineResponse20024 analyze_psbt(body)

Analyze PSBT

Analyzes and provides information about the current status of a PSBT and its inputs

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
api_instance = satstream_python_sdk.PSBTsApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsAnalyzePSBTRequest() # RequestsAnalyzePSBTRequest | PSBT to analyze

try:
    # Analyze PSBT
    api_response = api_instance.analyze_psbt(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSBTsApi->analyze_psbt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsAnalyzePSBTRequest**](RequestsAnalyzePSBTRequest.md)| PSBT to analyze | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **combine_psbt**
> InlineResponse2001 combine_psbt(body)

Combine PSBTs

Combines multiple partially signed Bitcoin transactions into one transaction

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
api_instance = satstream_python_sdk.PSBTsApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsCombinePSBTRequest() # RequestsCombinePSBTRequest | Array of PSBTs to combine

try:
    # Combine PSBTs
    api_response = api_instance.combine_psbt(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSBTsApi->combine_psbt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsCombinePSBTRequest**](RequestsCombinePSBTRequest.md)| Array of PSBTs to combine | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_psbt**
> InlineResponse2001 create_psbt(body)

Create PSBT

Creates a transaction in the Partially Signed Transaction format. Implements the Creator role.

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
api_instance = satstream_python_sdk.PSBTsApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsCreatePSBTRequest() # RequestsCreatePSBTRequest | Transaction parameters

try:
    # Create PSBT
    api_response = api_instance.create_psbt(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSBTsApi->create_psbt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsCreatePSBTRequest**](RequestsCreatePSBTRequest.md)| Transaction parameters | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decode_psbt**
> InlineResponse20025 decode_psbt(body)

Decode PSBT

Return a JSON object representing the serialized, base64-encoded partially signed Bitcoin transaction.

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
api_instance = satstream_python_sdk.PSBTsApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsAnalyzePSBTRequest() # RequestsAnalyzePSBTRequest | PSBT to decode

try:
    # Decode PSBT
    api_response = api_instance.decode_psbt(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSBTsApi->decode_psbt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsAnalyzePSBTRequest**](RequestsAnalyzePSBTRequest.md)| PSBT to decode | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_psbts**
> InlineResponse2001 join_psbts(body)

Join PSBTs

Joins multiple distinct PSBTs with different inputs and outputs into one PSBT

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
api_instance = satstream_python_sdk.PSBTsApi(satstream_python_sdk.ApiClient(configuration))
body = satstream_python_sdk.RequestsJoinPSBTsRequest() # RequestsJoinPSBTsRequest | PSBTs to join

try:
    # Join PSBTs
    api_response = api_instance.join_psbts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSBTsApi->join_psbts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestsJoinPSBTsRequest**](RequestsJoinPSBTsRequest.md)| PSBTs to join | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

