# CreatePSBTRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | [**list[CreatePSBTInput]**](CreatePSBTInput.md) | The inputs for the transaction | 
**locktime** | **int** | Raw locktime. Non-0 value also locktime-activates inputs | [optional] 
**outputs** | [**list[CreatePSBTOutput]**](CreatePSBTOutput.md) | The outputs for the transaction (each address can only appear once) | 
**replaceable** | **bool** | Marks this transaction as BIP125-replaceable | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

