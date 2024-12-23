# DecodedPSBTInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bip32_derivs** | [**dict(str, Bip32Deriv)**](Bip32Deriv.md) | The BIP32 derivation paths | [optional] 
**final_scriptsig** | **AllOfDecodedPSBTInputFinalScriptsig** | The final script sig | [optional] 
**final_scriptwitness** | **list[str]** | The final script witness | [optional] 
**non_witness_utxo** | **AllOfDecodedPSBTInputNonWitnessUtxo** | Decoded network transaction for non-witness UTXOs | [optional] 
**partial_signatures** | **dict(str, str)** | The public key and signature pairs | [optional] 
**redeem_script** | **AllOfDecodedPSBTInputRedeemScript** | The redeem script | [optional] 
**sighash** | **str** | The sighash type to be used | [optional] 
**unknown** | **AllOfDecodedPSBTInputUnknown** | Unknown fields | [optional] 
**witness_script** | **AllOfDecodedPSBTInputWitnessScript** | The witness script | [optional] 
**witness_utxo** | **AllOfDecodedPSBTInputWitnessUtxo** | Transaction output for witness UTXOs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

