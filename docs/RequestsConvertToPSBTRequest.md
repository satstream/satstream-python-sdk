# RequestsConvertToPSBTRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hexstring** | **str** | The hex string of a raw transaction | 
**is_witness** | **bool** | Whether the transaction hex is a serialized witness transaction. If not provided, heuristic tests will be used in decoding. If true, only witness deserialization will be tried. If false, only non-witness deserialization will be tried. This boolean should reflect whether the transaction has inputs (e.g. fully valid, or on-chain transactions), if known by the caller. Optional, defaults to heuristic tests if not provided. | [optional] 
**permit_sigdata** | **bool** | If true, any signatures in the input will be discarded and conversion will continue. If false, RPC will fail if any signatures are present. Optional, defaults to false if not provided. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

