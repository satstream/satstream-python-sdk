# ValidateAddressResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The bitcoin address validated | [optional] 
**error** | **str** | Error message, if any | [optional] 
**error_locations** | **list[int]** | Indices of likely error locations | [optional] 
**isscript** | **bool** | If the key is a script | [optional] 
**isvalid** | **bool** | If the address is valid or not | [optional] 
**iswitness** | **bool** | If the address is a witness address | [optional] 
**script_pub_key** | **str** | The hex-encoded scriptPubKey | [optional] 
**witness_program** | **str** | The hex value of the witness program | [optional] 
**witness_version** | **int** | The version number of the witness program | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

