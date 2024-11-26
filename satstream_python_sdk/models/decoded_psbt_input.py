# coding: utf-8

"""
    Satstream API

    Satstream API  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: team@satstream.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DecodedPSBTInput(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bip32_derivs': 'dict(str, Bip32Deriv)',
        'final_scriptsig': 'AllOfDecodedPSBTInputFinalScriptsig',
        'final_scriptwitness': 'list[str]',
        'non_witness_utxo': 'AllOfDecodedPSBTInputNonWitnessUtxo',
        'partial_signatures': 'dict(str, str)',
        'redeem_script': 'AllOfDecodedPSBTInputRedeemScript',
        'sighash': 'str',
        'unknown': 'AllOfDecodedPSBTInputUnknown',
        'witness_script': 'AllOfDecodedPSBTInputWitnessScript',
        'witness_utxo': 'AllOfDecodedPSBTInputWitnessUtxo'
    }

    attribute_map = {
        'bip32_derivs': 'bip32_derivs',
        'final_scriptsig': 'final_scriptsig',
        'final_scriptwitness': 'final_scriptwitness',
        'non_witness_utxo': 'non_witness_utxo',
        'partial_signatures': 'partial_signatures',
        'redeem_script': 'redeem_script',
        'sighash': 'sighash',
        'unknown': 'unknown',
        'witness_script': 'witness_script',
        'witness_utxo': 'witness_utxo'
    }

    def __init__(self, bip32_derivs=None, final_scriptsig=None, final_scriptwitness=None, non_witness_utxo=None, partial_signatures=None, redeem_script=None, sighash=None, unknown=None, witness_script=None, witness_utxo=None):  # noqa: E501
        """DecodedPSBTInput - a model defined in Swagger"""  # noqa: E501
        self._bip32_derivs = None
        self._final_scriptsig = None
        self._final_scriptwitness = None
        self._non_witness_utxo = None
        self._partial_signatures = None
        self._redeem_script = None
        self._sighash = None
        self._unknown = None
        self._witness_script = None
        self._witness_utxo = None
        self.discriminator = None
        if bip32_derivs is not None:
            self.bip32_derivs = bip32_derivs
        if final_scriptsig is not None:
            self.final_scriptsig = final_scriptsig
        if final_scriptwitness is not None:
            self.final_scriptwitness = final_scriptwitness
        if non_witness_utxo is not None:
            self.non_witness_utxo = non_witness_utxo
        if partial_signatures is not None:
            self.partial_signatures = partial_signatures
        if redeem_script is not None:
            self.redeem_script = redeem_script
        if sighash is not None:
            self.sighash = sighash
        if unknown is not None:
            self.unknown = unknown
        if witness_script is not None:
            self.witness_script = witness_script
        if witness_utxo is not None:
            self.witness_utxo = witness_utxo

    @property
    def bip32_derivs(self):
        """Gets the bip32_derivs of this DecodedPSBTInput.  # noqa: E501

        The BIP32 derivation paths  # noqa: E501

        :return: The bip32_derivs of this DecodedPSBTInput.  # noqa: E501
        :rtype: dict(str, Bip32Deriv)
        """
        return self._bip32_derivs

    @bip32_derivs.setter
    def bip32_derivs(self, bip32_derivs):
        """Sets the bip32_derivs of this DecodedPSBTInput.

        The BIP32 derivation paths  # noqa: E501

        :param bip32_derivs: The bip32_derivs of this DecodedPSBTInput.  # noqa: E501
        :type: dict(str, Bip32Deriv)
        """

        self._bip32_derivs = bip32_derivs

    @property
    def final_scriptsig(self):
        """Gets the final_scriptsig of this DecodedPSBTInput.  # noqa: E501

        The final script sig  # noqa: E501

        :return: The final_scriptsig of this DecodedPSBTInput.  # noqa: E501
        :rtype: AllOfDecodedPSBTInputFinalScriptsig
        """
        return self._final_scriptsig

    @final_scriptsig.setter
    def final_scriptsig(self, final_scriptsig):
        """Sets the final_scriptsig of this DecodedPSBTInput.

        The final script sig  # noqa: E501

        :param final_scriptsig: The final_scriptsig of this DecodedPSBTInput.  # noqa: E501
        :type: AllOfDecodedPSBTInputFinalScriptsig
        """

        self._final_scriptsig = final_scriptsig

    @property
    def final_scriptwitness(self):
        """Gets the final_scriptwitness of this DecodedPSBTInput.  # noqa: E501

        The final script witness  # noqa: E501

        :return: The final_scriptwitness of this DecodedPSBTInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._final_scriptwitness

    @final_scriptwitness.setter
    def final_scriptwitness(self, final_scriptwitness):
        """Sets the final_scriptwitness of this DecodedPSBTInput.

        The final script witness  # noqa: E501

        :param final_scriptwitness: The final_scriptwitness of this DecodedPSBTInput.  # noqa: E501
        :type: list[str]
        """

        self._final_scriptwitness = final_scriptwitness

    @property
    def non_witness_utxo(self):
        """Gets the non_witness_utxo of this DecodedPSBTInput.  # noqa: E501

        Decoded network transaction for non-witness UTXOs  # noqa: E501

        :return: The non_witness_utxo of this DecodedPSBTInput.  # noqa: E501
        :rtype: AllOfDecodedPSBTInputNonWitnessUtxo
        """
        return self._non_witness_utxo

    @non_witness_utxo.setter
    def non_witness_utxo(self, non_witness_utxo):
        """Sets the non_witness_utxo of this DecodedPSBTInput.

        Decoded network transaction for non-witness UTXOs  # noqa: E501

        :param non_witness_utxo: The non_witness_utxo of this DecodedPSBTInput.  # noqa: E501
        :type: AllOfDecodedPSBTInputNonWitnessUtxo
        """

        self._non_witness_utxo = non_witness_utxo

    @property
    def partial_signatures(self):
        """Gets the partial_signatures of this DecodedPSBTInput.  # noqa: E501

        The public key and signature pairs  # noqa: E501

        :return: The partial_signatures of this DecodedPSBTInput.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._partial_signatures

    @partial_signatures.setter
    def partial_signatures(self, partial_signatures):
        """Sets the partial_signatures of this DecodedPSBTInput.

        The public key and signature pairs  # noqa: E501

        :param partial_signatures: The partial_signatures of this DecodedPSBTInput.  # noqa: E501
        :type: dict(str, str)
        """

        self._partial_signatures = partial_signatures

    @property
    def redeem_script(self):
        """Gets the redeem_script of this DecodedPSBTInput.  # noqa: E501

        The redeem script  # noqa: E501

        :return: The redeem_script of this DecodedPSBTInput.  # noqa: E501
        :rtype: AllOfDecodedPSBTInputRedeemScript
        """
        return self._redeem_script

    @redeem_script.setter
    def redeem_script(self, redeem_script):
        """Sets the redeem_script of this DecodedPSBTInput.

        The redeem script  # noqa: E501

        :param redeem_script: The redeem_script of this DecodedPSBTInput.  # noqa: E501
        :type: AllOfDecodedPSBTInputRedeemScript
        """

        self._redeem_script = redeem_script

    @property
    def sighash(self):
        """Gets the sighash of this DecodedPSBTInput.  # noqa: E501

        The sighash type to be used  # noqa: E501

        :return: The sighash of this DecodedPSBTInput.  # noqa: E501
        :rtype: str
        """
        return self._sighash

    @sighash.setter
    def sighash(self, sighash):
        """Sets the sighash of this DecodedPSBTInput.

        The sighash type to be used  # noqa: E501

        :param sighash: The sighash of this DecodedPSBTInput.  # noqa: E501
        :type: str
        """

        self._sighash = sighash

    @property
    def unknown(self):
        """Gets the unknown of this DecodedPSBTInput.  # noqa: E501

        Unknown fields  # noqa: E501

        :return: The unknown of this DecodedPSBTInput.  # noqa: E501
        :rtype: AllOfDecodedPSBTInputUnknown
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        """Sets the unknown of this DecodedPSBTInput.

        Unknown fields  # noqa: E501

        :param unknown: The unknown of this DecodedPSBTInput.  # noqa: E501
        :type: AllOfDecodedPSBTInputUnknown
        """

        self._unknown = unknown

    @property
    def witness_script(self):
        """Gets the witness_script of this DecodedPSBTInput.  # noqa: E501

        The witness script  # noqa: E501

        :return: The witness_script of this DecodedPSBTInput.  # noqa: E501
        :rtype: AllOfDecodedPSBTInputWitnessScript
        """
        return self._witness_script

    @witness_script.setter
    def witness_script(self, witness_script):
        """Sets the witness_script of this DecodedPSBTInput.

        The witness script  # noqa: E501

        :param witness_script: The witness_script of this DecodedPSBTInput.  # noqa: E501
        :type: AllOfDecodedPSBTInputWitnessScript
        """

        self._witness_script = witness_script

    @property
    def witness_utxo(self):
        """Gets the witness_utxo of this DecodedPSBTInput.  # noqa: E501

        Transaction output for witness UTXOs  # noqa: E501

        :return: The witness_utxo of this DecodedPSBTInput.  # noqa: E501
        :rtype: AllOfDecodedPSBTInputWitnessUtxo
        """
        return self._witness_utxo

    @witness_utxo.setter
    def witness_utxo(self, witness_utxo):
        """Sets the witness_utxo of this DecodedPSBTInput.

        Transaction output for witness UTXOs  # noqa: E501

        :param witness_utxo: The witness_utxo of this DecodedPSBTInput.  # noqa: E501
        :type: AllOfDecodedPSBTInputWitnessUtxo
        """

        self._witness_utxo = witness_utxo

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DecodedPSBTInput, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DecodedPSBTInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
