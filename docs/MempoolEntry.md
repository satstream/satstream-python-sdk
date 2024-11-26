# MempoolEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ancestorcount** | **int** | Number of in-mempool ancestor transactions | [optional] 
**ancestorsize** | **int** | Virtual size of in-mempool ancestors | [optional] 
**bip125_replaceable** | **bool** | Whether this transaction is replaceable | [optional] 
**depends** | **list[str]** | Parent transaction IDs | [optional] 
**descendantcount** | **int** | Number of in-mempool descendant transactions | [optional] 
**descendantsize** | **int** | Virtual size of in-mempool descendants | [optional] 
**fees** | **AllOfMempoolEntryFees** | Fee information | [optional] 
**height** | **int** | Block height when transaction entered pool | [optional] 
**spentby** | **list[str]** | Child transaction IDs | [optional] 
**time** | **int** | Time transaction entered pool | [optional] 
**unbroadcast** | **bool** | Whether this transaction is currently unbroadcast | [optional] 
**vsize** | **int** | Virtual transaction size | [optional] 
**weight** | **int** | Transaction weight | [optional] 
**wtxid** | **str** | Hash of serialized transaction with witness data | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

