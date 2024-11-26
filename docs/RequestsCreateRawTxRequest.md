# RequestsCreateRawTxRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | [**list[RequestsCreateRawTxInput]**](RequestsCreateRawTxInput.md) | The inputs for the transaction | 
**locktime** | **int** | Raw locktime. Non-0 value also locktime-activates inputs Optional, defaults to 0 | [optional] 
**outputs** | [**list[RequestsCreateRawTxOutput]**](RequestsCreateRawTxOutput.md) | The outputs for the transaction Each address can only appear once and there can only be one &#x27;data&#x27; object | 
**replaceable** | **bool** | Marks this transaction as BIP125-replaceable Allows this transaction to be replaced by a transaction with higher fees If provided, it is an error if explicit sequence numbers are incompatible Optional, defaults to true | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

