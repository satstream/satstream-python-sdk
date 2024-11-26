# BlockStats

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avgfee** | **float** | Average fee in the block | [optional] 
**avgfeerate** | **float** | Average feerate (in satoshis per virtual byte) | [optional] 
**avgtxsize** | **float** | Average transaction size | [optional] 
**blockhash** | **str** | The block hash (to check for potential reorgs) | [optional] 
**feerate_percentiles** | **list[float]** | Feerates at the 10th, 25th, 50th, 75th, and 90th percentile | [optional] 
**height** | **int** | The height of the block | [optional] 
**ins** | **int** | The number of inputs (excluding coinbase) | [optional] 
**maxfee** | **float** | Maximum fee in the block | [optional] 
**maxfeerate** | **float** | Maximum feerate (in satoshis per virtual byte) | [optional] 
**maxtxsize** | **int** | Maximum transaction size | [optional] 
**medianfee** | **float** | Truncated median fee in the block | [optional] 
**mediantime** | **int** | The block median time past | [optional] 
**mediantxsize** | **int** | Truncated median transaction size | [optional] 
**minfee** | **float** | Minimum fee in the block | [optional] 
**minfeerate** | **float** | Minimum feerate (in satoshis per virtual byte) | [optional] 
**mintxsize** | **int** | Minimum transaction size | [optional] 
**outs** | **int** | The number of outputs | [optional] 
**subsidy** | **float** | The block subsidy | [optional] 
**swtotal_size** | **int** | Total size of all segwit transactions | [optional] 
**swtotal_weight** | **int** | Total weight of all segwit transactions | [optional] 
**swtxs** | **int** | The number of segwit transactions | [optional] 
**time** | **int** | The block time | [optional] 
**total_out** | **float** | Total amount in all outputs | [optional] 
**total_size** | **int** | Total size of all non-coinbase transactions | [optional] 
**total_weight** | **int** | Total weight of all non-coinbase transactions | [optional] 
**totalfee** | **float** | The fee total | [optional] 
**txs** | **int** | The number of transactions (excluding coinbase) | [optional] 
**utxo_increase** | **int** | The increase/decrease in the number of unspent outputs | [optional] 
**utxo_size_inc** | **int** | The increase/decrease in size for the utxo index | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

