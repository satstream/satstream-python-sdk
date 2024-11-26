# DecodedPSBT

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | **float** | The transaction fee paid if all UTXOs slots are filled | [optional] 
**inputs** | [**list[DecodedPSBTInput]**](DecodedPSBTInput.md) | Array of inputs | [optional] 
**outputs** | [**list[DecodedPSBTOutput]**](DecodedPSBTOutput.md) | Array of outputs | [optional] 
**tx** | **AllOfDecodedPSBTTx** | The decoded network-serialized unsigned transaction | [optional] 
**unknown** | **AllOfDecodedPSBTUnknown** | The unknown global fields | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

