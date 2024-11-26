# satstream_python_sdk.InscriptionsApi

All URIs are relative to *https://api.satstream.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**decode_tx**](InscriptionsApi.md#decode_tx) | **GET** /decode/{txid} | Decode a transaction
[**fetch_inscription_child**](InscriptionsApi.md#fetch_inscription_child) | **GET** /inscription/{inscription_id}/child/{child_index} | Get inscription child info
[**fetch_inscriptions**](InscriptionsApi.md#fetch_inscriptions) | **POST** /inscriptions | Fetch multiple inscriptions
[**get_address**](InscriptionsApi.md#get_address) | **GET** /address/{address} | Get address info
[**get_address_utxos**](InscriptionsApi.md#get_address_utxos) | **GET** /address/{address}/outputs | Get UTXOs for an address
[**get_block_by_height**](InscriptionsApi.md#get_block_by_height) | **GET** /block/height/{block_height} | Get block info by height
[**get_block_count**](InscriptionsApi.md#get_block_count) | **GET** /blockcount | Get the height of the latest block
[**get_block_hash_by_height**](InscriptionsApi.md#get_block_hash_by_height) | **GET** /blockhash/{block_height} | Returns blockhash of specified block.
[**get_block_inscriptions**](InscriptionsApi.md#get_block_inscriptions) | **GET** /inscriptions/block/{block_height} | Get inscriptions in a specific block
[**get_blocks**](InscriptionsApi.md#get_blocks) | **GET** /blocks | Returns the latest block height, last 100 block hashes, and featured inscriptions
[**get_inscription**](InscriptionsApi.md#get_inscription) | **GET** /inscription/{inscription_id} | Get inscription info
[**get_latest_block_height**](InscriptionsApi.md#get_latest_block_height) | **GET** /latestblockheight | Returns the height of the latest block.
[**get_latest_blockhash**](InscriptionsApi.md#get_latest_blockhash) | **GET** /latestblockhash | Returns blockhash for the latest block.
[**get_latest_blocktime**](InscriptionsApi.md#get_latest_blocktime) | **GET** /blocktime | Get the timestamp of the latest block
[**get_latest_inscriptions**](InscriptionsApi.md#get_latest_inscriptions) | **GET** /inscriptions/latest | Get latest inscriptions
[**get_latest_inscriptions_page**](InscriptionsApi.md#get_latest_inscriptions_page) | **GET** /inscriptions/page/{page} | Get latest inscriptions page
[**get_latest_runes**](InscriptionsApi.md#get_latest_runes) | **GET** /runes/latest | Get latest runes
[**get_latest_runes_page**](InscriptionsApi.md#get_latest_runes_page) | **GET** /runes/page/{page} | Get latest runes page
[**get_output_by_outpoint**](InscriptionsApi.md#get_output_by_outpoint) | **GET** /output/outpoint/{outpoint} | Get output info by outpoint
[**get_outputs**](InscriptionsApi.md#get_outputs) | **POST** /outputs | Get multiple outputs
[**get_rune**](InscriptionsApi.md#get_rune) | **GET** /rune/{rune_name} | Get rune info
[**get_satoshi**](InscriptionsApi.md#get_satoshi) | **GET** /sat/{number} | Get satoshi info
[**get_status**](InscriptionsApi.md#get_status) | **GET** /status | Get server status
[**get_transaction**](InscriptionsApi.md#get_transaction) | **GET** /tx/{txid} | Get transaction info

# **decode_tx**
> GithubComSatstreamSsApiServerApiTransactionResponsesDecodeResponse decode_tx(txid)

Decode a transaction

Decodes a transaction and returns its inscriptions and runestone data

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
txid = 'txid_example' # str | Transaction ID

try:
    # Decode a transaction
    api_response = api_instance.decode_tx(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->decode_tx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Transaction ID | 

### Return type

[**GithubComSatstreamSsApiServerApiTransactionResponsesDecodeResponse**](GithubComSatstreamSsApiServerApiTransactionResponsesDecodeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_inscription_child**
> GithubComSatstreamSsApiServerApiInscriptionResponsesInscriptionResponse fetch_inscription_child(inscription_id, child_index)

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

[**GithubComSatstreamSsApiServerApiInscriptionResponsesInscriptionResponse**](GithubComSatstreamSsApiServerApiInscriptionResponsesInscriptionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_inscriptions**
> list[GithubComSatstreamSsApiServerApiInscriptionResponsesInscriptionResponse] fetch_inscriptions(body)

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

[**list[GithubComSatstreamSsApiServerApiInscriptionResponsesInscriptionResponse]**](GithubComSatstreamSsApiServerApiInscriptionResponsesInscriptionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address**
> GithubComSatstreamSsApiServerApiAddressResponsesAddressResponse get_address(address)

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
api_instance = satstream_python_sdk.InscriptionsApi(satstream_python_sdk.ApiClient(configuration))
address = 'address_example' # str | Address

try:
    # Get address info
    api_response = api_instance.get_address(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address | 

### Return type

[**GithubComSatstreamSsApiServerApiAddressResponsesAddressResponse**](GithubComSatstreamSsApiServerApiAddressResponsesAddressResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_utxos**
> list[GithubComSatstreamSsApiServerApiAddressResponsesOutputResponse] get_address_utxos(address, type=type)

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
api_instance = satstream_python_sdk.InscriptionsApi(satstream_python_sdk.ApiClient(configuration))
address = 'address_example' # str | Address
type = 'type_example' # str | UTXO Type (optional)

try:
    # Get UTXOs for an address
    api_response = api_instance.get_address_utxos(address, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_address_utxos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address | 
 **type** | **str**| UTXO Type | [optional] 

### Return type

[**list[GithubComSatstreamSsApiServerApiAddressResponsesOutputResponse]**](GithubComSatstreamSsApiServerApiAddressResponsesOutputResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_by_height**
> GithubComSatstreamSsApiServerApiBlockResponsesBlockResponse get_block_by_height(block_height)

Get block info by height

Get detailed information about a specific block by height

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
block_height = 'block_height_example' # str | Block Height

try:
    # Get block info by height
    api_response = api_instance.get_block_by_height(block_height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_block_by_height: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_height** | **str**| Block Height | 

### Return type

[**GithubComSatstreamSsApiServerApiBlockResponsesBlockResponse**](GithubComSatstreamSsApiServerApiBlockResponsesBlockResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_count**
> GithubComSatstreamSsApiServerApiBlockResponsesBlockCountResponse get_block_count()

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
api_instance = satstream_python_sdk.InscriptionsApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Get the height of the latest block
    api_response = api_instance.get_block_count()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_block_count: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GithubComSatstreamSsApiServerApiBlockResponsesBlockCountResponse**](GithubComSatstreamSsApiServerApiBlockResponsesBlockCountResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_hash_by_height**
> GithubComSatstreamSsApiServerApiBlockResponsesBlockHashResponse get_block_hash_by_height(block_height)

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
api_instance = satstream_python_sdk.InscriptionsApi(satstream_python_sdk.ApiClient(configuration))
block_height = 'block_height_example' # str | Block Height

try:
    # Returns blockhash of specified block.
    api_response = api_instance.get_block_hash_by_height(block_height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_block_hash_by_height: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_height** | **str**| Block Height | 

### Return type

[**GithubComSatstreamSsApiServerApiBlockResponsesBlockHashResponse**](GithubComSatstreamSsApiServerApiBlockResponsesBlockHashResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_inscriptions**
> GithubComSatstreamSsApiServerApiInscriptionResponsesLatestInscriptionsResponse get_block_inscriptions(block_height)

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

[**GithubComSatstreamSsApiServerApiInscriptionResponsesLatestInscriptionsResponse**](GithubComSatstreamSsApiServerApiInscriptionResponsesLatestInscriptionsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blocks**
> GithubComSatstreamSsApiServerApiBlockResponsesBlocksResponse get_blocks()

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
api_instance = satstream_python_sdk.InscriptionsApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Returns the latest block height, last 100 block hashes, and featured inscriptions
    api_response = api_instance.get_blocks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_blocks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GithubComSatstreamSsApiServerApiBlockResponsesBlocksResponse**](GithubComSatstreamSsApiServerApiBlockResponsesBlocksResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inscription**
> GithubComSatstreamSsApiServerApiInscriptionResponsesInscriptionResponse get_inscription(inscription_id)

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

[**GithubComSatstreamSsApiServerApiInscriptionResponsesInscriptionResponse**](GithubComSatstreamSsApiServerApiInscriptionResponsesInscriptionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_block_height**
> ResponsesLatestBlockHeightResponse get_latest_block_height()

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
api_instance = satstream_python_sdk.InscriptionsApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Returns the height of the latest block.
    api_response = api_instance.get_latest_block_height()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_latest_block_height: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponsesLatestBlockHeightResponse**](ResponsesLatestBlockHeightResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_blockhash**
> ResponsesLatestBlockHashResponse get_latest_blockhash()

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
api_instance = satstream_python_sdk.InscriptionsApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Returns blockhash for the latest block.
    api_response = api_instance.get_latest_blockhash()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_latest_blockhash: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponsesLatestBlockHashResponse**](ResponsesLatestBlockHashResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_blocktime**
> ResponsesLatestBlockTimeResponse get_latest_blocktime()

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
api_instance = satstream_python_sdk.InscriptionsApi(satstream_python_sdk.ApiClient(configuration))

try:
    # Get the timestamp of the latest block
    api_response = api_instance.get_latest_blocktime()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_latest_blocktime: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponsesLatestBlockTimeResponse**](ResponsesLatestBlockTimeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_inscriptions**
> GithubComSatstreamSsApiServerApiInscriptionResponsesLatestInscriptionsResponse get_latest_inscriptions()

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

[**GithubComSatstreamSsApiServerApiInscriptionResponsesLatestInscriptionsResponse**](GithubComSatstreamSsApiServerApiInscriptionResponsesLatestInscriptionsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_inscriptions_page**
> GithubComSatstreamSsApiServerApiInscriptionResponsesLatestInscriptionsResponse get_latest_inscriptions_page(page)

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

[**GithubComSatstreamSsApiServerApiInscriptionResponsesLatestInscriptionsResponse**](GithubComSatstreamSsApiServerApiInscriptionResponsesLatestInscriptionsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_runes**
> GithubComSatstreamSsApiServerApiRuneResponsesRunesListResponse get_latest_runes()

Get latest runes

Retrieve information about the last 100 inscribed runes (first page)

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
    # Get latest runes
    api_response = api_instance.get_latest_runes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_latest_runes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GithubComSatstreamSsApiServerApiRuneResponsesRunesListResponse**](GithubComSatstreamSsApiServerApiRuneResponsesRunesListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_runes_page**
> GithubComSatstreamSsApiServerApiRuneResponsesRunesListResponse get_latest_runes_page(page)

Get latest runes page

Retrieve a specific page of 100 inscribed runes

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
    # Get latest runes page
    api_response = api_instance.get_latest_runes_page(page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_latest_runes_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | 

### Return type

[**GithubComSatstreamSsApiServerApiRuneResponsesRunesListResponse**](GithubComSatstreamSsApiServerApiRuneResponsesRunesListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_output_by_outpoint**
> ResponsesGetOutputByOutpointResponse get_output_by_outpoint(outpoint)

Get output info by outpoint

Retrieve information about a specific UTXO using outpoint string

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
outpoint = 'outpoint_example' # str | Outpoint

try:
    # Get output info by outpoint
    api_response = api_instance.get_output_by_outpoint(outpoint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_output_by_outpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outpoint** | **str**| Outpoint | 

### Return type

[**ResponsesGetOutputByOutpointResponse**](ResponsesGetOutputByOutpointResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outputs**
> list[ResponsesGetOutputsResponse] get_outputs(body)

Get multiple outputs

Retrieve information about multiple UTXOs

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
body = ['body_example'] # list[str] | Outpoints

try:
    # Get multiple outputs
    api_response = api_instance.get_outputs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_outputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| Outpoints | 

### Return type

[**list[ResponsesGetOutputsResponse]**](ResponsesGetOutputsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rune**
> GithubComSatstreamSsApiServerApiRuneResponsesRuneResponse get_rune(rune_name)

Get rune info

Retrieve information about a specific rune

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
rune_name = 'rune_name_example' # str | Rune Name

try:
    # Get rune info
    api_response = api_instance.get_rune(rune_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_rune: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rune_name** | **str**| Rune Name | 

### Return type

[**GithubComSatstreamSsApiServerApiRuneResponsesRuneResponse**](GithubComSatstreamSsApiServerApiRuneResponsesRuneResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_satoshi**
> GithubComSatstreamSsApiServerApiSatoshiResponsesSatoshiResponse get_satoshi(number)

Get satoshi info

Retrieve information about a specific satoshi

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
number = 56 # int | Satoshi Number

try:
    # Get satoshi info
    api_response = api_instance.get_satoshi(number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_satoshi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **int**| Satoshi Number | 

### Return type

[**GithubComSatstreamSsApiServerApiSatoshiResponsesSatoshiResponse**](GithubComSatstreamSsApiServerApiSatoshiResponsesSatoshiResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> GithubComSatstreamSsApiServerApiStatusResponsesStatusResponse get_status()

Get server status

Retrieve information about the server installation and index

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
    # Get server status
    api_response = api_instance.get_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GithubComSatstreamSsApiServerApiStatusResponsesStatusResponse**](GithubComSatstreamSsApiServerApiStatusResponsesStatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse get_transaction(txid)

Get transaction info

Retrieve information about a specific transaction

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
txid = 'txid_example' # str | Transaction ID

try:
    # Get transaction info
    api_response = api_instance.get_transaction(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InscriptionsApi->get_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Transaction ID | 

### Return type

[**GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse**](GithubComSatstreamSsApiServerApiTransactionResponsesTransactionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

