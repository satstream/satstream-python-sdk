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

from satstream_python_sdk.api_client import ApiClient


class AddressesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_address(self, address, **kwargs):  # noqa: E501
        """Get address info  # noqa: E501

        Get detailed information about a specific address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Address (required)
        :return: GetAddressResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_address_with_http_info(address, **kwargs)  # noqa: E501
        else:
            (data) = self.get_address_with_http_info(address, **kwargs)  # noqa: E501
            return data

    def get_address_with_http_info(self, address, **kwargs):  # noqa: E501
        """Get address info  # noqa: E501

        Get detailed information about a specific address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_with_http_info(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Address (required)
        :return: GetAddressResponse
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
                    " to method get_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `get_address`")  # noqa: E501

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
            '/address/{address}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAddressResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_address_deltas(self, address, **kwargs):  # noqa: E501
        """Get address deltas  # noqa: E501

        Get deltas for a specific address with pagination  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_deltas(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Address (required)
        :param int page_size: Number of results per page (default: 100, max: 1000)
        :param int start_height: Start block height
        :param int end_height: End block height
        :param str cursor: Base64 encoded cursor for pagination
        :return: GetAddressDeltasResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_address_deltas_with_http_info(address, **kwargs)  # noqa: E501
        else:
            (data) = self.get_address_deltas_with_http_info(address, **kwargs)  # noqa: E501
            return data

    def get_address_deltas_with_http_info(self, address, **kwargs):  # noqa: E501
        """Get address deltas  # noqa: E501

        Get deltas for a specific address with pagination  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_deltas_with_http_info(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Address (required)
        :param int page_size: Number of results per page (default: 100, max: 1000)
        :param int start_height: Start block height
        :param int end_height: End block height
        :param str cursor: Base64 encoded cursor for pagination
        :return: GetAddressDeltasResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address', 'page_size', 'start_height', 'end_height', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_address_deltas" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `get_address_deltas`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address' in params:
            path_params['address'] = params['address']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'start_height' in params:
            query_params.append(('start_height', params['start_height']))  # noqa: E501
        if 'end_height' in params:
            query_params.append(('end_height', params['end_height']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

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
            '/address/{address}/deltas', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAddressDeltasResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_address_rune_deltas(self, address, **kwargs):  # noqa: E501
        """Get address rune deltas  # noqa: E501

        Get rune deltas for a specific address with pagination  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_rune_deltas(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Address (required)
        :param int page_size: Number of results per page (default: 100, max: 1000)
        :param int start_height: Start block height
        :param int end_height: End block height
        :param str cursor: Cursor for pagination
        :return: GetAddressRuneDeltasResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_address_rune_deltas_with_http_info(address, **kwargs)  # noqa: E501
        else:
            (data) = self.get_address_rune_deltas_with_http_info(address, **kwargs)  # noqa: E501
            return data

    def get_address_rune_deltas_with_http_info(self, address, **kwargs):  # noqa: E501
        """Get address rune deltas  # noqa: E501

        Get rune deltas for a specific address with pagination  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_rune_deltas_with_http_info(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Address (required)
        :param int page_size: Number of results per page (default: 100, max: 1000)
        :param int start_height: Start block height
        :param int end_height: End block height
        :param str cursor: Cursor for pagination
        :return: GetAddressRuneDeltasResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address', 'page_size', 'start_height', 'end_height', 'cursor']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_address_rune_deltas" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `get_address_rune_deltas`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address' in params:
            path_params['address'] = params['address']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'start_height' in params:
            query_params.append(('start_height', params['start_height']))  # noqa: E501
        if 'end_height' in params:
            query_params.append(('end_height', params['end_height']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501

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
            '/address/{address}/deltas/runes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAddressRuneDeltasResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_address_utxos(self, address, **kwargs):  # noqa: E501
        """Get UTXOs for an address  # noqa: E501

        Retrieve UTXOs held by a specific address with optional type filtering  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_utxos(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Address (required)
        :param str type: UTXO Type
        :return: GetAddressUTXOsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_address_utxos_with_http_info(address, **kwargs)  # noqa: E501
        else:
            (data) = self.get_address_utxos_with_http_info(address, **kwargs)  # noqa: E501
            return data

    def get_address_utxos_with_http_info(self, address, **kwargs):  # noqa: E501
        """Get UTXOs for an address  # noqa: E501

        Retrieve UTXOs held by a specific address with optional type filtering  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_address_utxos_with_http_info(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Address (required)
        :param str type: UTXO Type
        :return: GetAddressUTXOsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_address_utxos" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `get_address_utxos`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address' in params:
            path_params['address'] = params['address']  # noqa: E501

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

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
            '/address/{address}/outputs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAddressUTXOsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def validate_address(self, address, **kwargs):  # noqa: E501
        """Validate address  # noqa: E501

        Returns information about the given Bitcoin address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_address(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Bitcoin address to validate (required)
        :return: ValidateAddressResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.validate_address_with_http_info(address, **kwargs)  # noqa: E501
        else:
            (data) = self.validate_address_with_http_info(address, **kwargs)  # noqa: E501
            return data

    def validate_address_with_http_info(self, address, **kwargs):  # noqa: E501
        """Validate address  # noqa: E501

        Returns information about the given Bitcoin address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_address_with_http_info(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: Bitcoin address to validate (required)
        :return: ValidateAddressResponse
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
                    " to method validate_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `validate_address`")  # noqa: E501

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
            '/address/{address}/validate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ValidateAddressResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
