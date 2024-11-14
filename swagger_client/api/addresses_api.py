# coding: utf-8

"""
    Satstream API

    Satstream API  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: team@satstream.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AddressesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_address_balance(self, address, **kwargs):  # noqa: E501
        """Get address balance  # noqa: E501

        Get the current balance of a Bitcoin address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_balance(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Bitcoin address (required)
        :return: ResponsesGetAddressBalance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_address_balance_with_http_info(address, **kwargs)  # noqa: E501
        else:
            (data) = self.get_address_balance_with_http_info(address, **kwargs)  # noqa: E501
            return data

    def get_address_balance_with_http_info(self, address, **kwargs):  # noqa: E501
        """Get address balance  # noqa: E501

        Get the current balance of a Bitcoin address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_balance_with_http_info(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Bitcoin address (required)
        :return: ResponsesGetAddressBalance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_address_balance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `get_address_balance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address' in params:
            path_params['address'] = params['address']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/addresses/{address}/balance', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsesGetAddressBalance',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_address_non_inscription_utxos(self, address, **kwargs):  # noqa: E501
        """Get address non-inscription UTXOs  # noqa: E501

        Get all non-inscription UTXOs for a Bitcoin address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_non_inscription_utxos(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Bitcoin address (required)
        :return: ResponsesGetAddressNonInscriptionUTXO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_address_non_inscription_utxos_with_http_info(address, **kwargs)  # noqa: E501
        else:
            (data) = self.get_address_non_inscription_utxos_with_http_info(address, **kwargs)  # noqa: E501
            return data

    def get_address_non_inscription_utxos_with_http_info(self, address, **kwargs):  # noqa: E501
        """Get address non-inscription UTXOs  # noqa: E501

        Get all non-inscription UTXOs for a Bitcoin address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_non_inscription_utxos_with_http_info(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Bitcoin address (required)
        :return: ResponsesGetAddressNonInscriptionUTXO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_address_non_inscription_utxos" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `get_address_non_inscription_utxos`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address' in params:
            path_params['address'] = params['address']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/addresses/{address}/utxos', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsesGetAddressNonInscriptionUTXO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_address_rune_balance(self, address, runeid, **kwargs):  # noqa: E501
        """Get address rune balance  # noqa: E501

        Get the balance of a specific rune for a Bitcoin address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_rune_balance(address, runeid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Bitcoin address (required)
        :param str runeid: Rune ID (required)
        :return: ResponsesGetAddressRuneBalance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_address_rune_balance_with_http_info(address, runeid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_address_rune_balance_with_http_info(address, runeid, **kwargs)  # noqa: E501
            return data

    def get_address_rune_balance_with_http_info(self, address, runeid, **kwargs):  # noqa: E501
        """Get address rune balance  # noqa: E501

        Get the balance of a specific rune for a Bitcoin address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_rune_balance_with_http_info(address, runeid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Bitcoin address (required)
        :param str runeid: Rune ID (required)
        :return: ResponsesGetAddressRuneBalance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address', 'runeid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_address_rune_balance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `get_address_rune_balance`")  # noqa: E501
        # verify the required parameter 'runeid' is set
        if ('runeid' not in params or
                params['runeid'] is None):
            raise ValueError("Missing the required parameter `runeid` when calling `get_address_rune_balance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address' in params:
            path_params['address'] = params['address']  # noqa: E501
        if 'runeid' in params:
            path_params['runeid'] = params['runeid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/addresses/{address}/runes/{runeid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsesGetAddressRuneBalance',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_address_runes_balance_list(self, address, **kwargs):  # noqa: E501
        """Get address runes balance list  # noqa: E501

        Get the balance of all runes for a Bitcoin address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_runes_balance_list(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Bitcoin address (required)
        :return: ResponsesGetAddressRunesBalanceList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_address_runes_balance_list_with_http_info(address, **kwargs)  # noqa: E501
        else:
            (data) = self.get_address_runes_balance_list_with_http_info(address, **kwargs)  # noqa: E501
            return data

    def get_address_runes_balance_list_with_http_info(self, address, **kwargs):  # noqa: E501
        """Get address runes balance list  # noqa: E501

        Get the balance of all runes for a Bitcoin address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_runes_balance_list_with_http_info(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Bitcoin address (required)
        :return: ResponsesGetAddressRunesBalanceList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_address_runes_balance_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `get_address_runes_balance_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address' in params:
            path_params['address'] = params['address']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/addresses/{address}/runes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsesGetAddressRunesBalanceList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_address_timeframe_balance(self, address, timeframe, **kwargs):  # noqa: E501
        """Get address timeframe balance  # noqa: E501

        Get the balance of a Bitcoin address for a specific timeframe  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_timeframe_balance(address, timeframe, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Bitcoin address (required)
        :param str timeframe: Timeframe (required)
        :param str token: Token
        :return: ResponsesGetAddressTimeframeBalance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_address_timeframe_balance_with_http_info(address, timeframe, **kwargs)  # noqa: E501
        else:
            (data) = self.get_address_timeframe_balance_with_http_info(address, timeframe, **kwargs)  # noqa: E501
            return data

    def get_address_timeframe_balance_with_http_info(self, address, timeframe, **kwargs):  # noqa: E501
        """Get address timeframe balance  # noqa: E501

        Get the balance of a Bitcoin address for a specific timeframe  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_timeframe_balance_with_http_info(address, timeframe, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Bitcoin address (required)
        :param str timeframe: Timeframe (required)
        :param str token: Token
        :return: ResponsesGetAddressTimeframeBalance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address', 'timeframe', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_address_timeframe_balance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `get_address_timeframe_balance`")  # noqa: E501
        # verify the required parameter 'timeframe' is set
        if ('timeframe' not in params or
                params['timeframe'] is None):
            raise ValueError("Missing the required parameter `timeframe` when calling `get_address_timeframe_balance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address' in params:
            path_params['address'] = params['address']  # noqa: E501

        query_params = []
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501
        if 'timeframe' in params:
            query_params.append(('timeframe', params['timeframe']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/addresses/{address}/balance/timeframe', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsesGetAddressTimeframeBalance',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
