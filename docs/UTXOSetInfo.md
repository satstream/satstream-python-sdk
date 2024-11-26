# UTXOSetInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bestblock** | **str** | The hash of the block at which these statistics are calculated | [optional] 
**block_info** | **AllOfUTXOSetInfoBlockInfo** | Info on amounts in the block at this height | [optional] 
**bogosize** | **int** | Database-independent metric indicating the UTXO set size | [optional] 
**disk_size** | **int** | The estimated size of the chainstate on disk | [optional] 
**hash_serialized_2** | **str** | The serialized hash (only for hash_serialized_2) | [optional] 
**height** | **int** | The block height of the returned statistics | [optional] 
**muhash** | **str** | The serialized hash (only for muhash) | [optional] 
**total_amount** | **float** | The total amount of coins in the UTXO set | [optional] 
**total_unspendable_amount** | **float** | Total amount permanently excluded from UTXO set | [optional] 
**transactions** | **int** | The number of transactions with unspent outputs | [optional] 
**txouts** | **int** | The number of unspent transaction outputs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

