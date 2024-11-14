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


class BlocksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_block_by_hash(self, hash, **kwargs):  # noqa: E501
        """Get block by hash  # noqa: E501

        Get information about a specific block by its hash  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_block_by_hash(hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hash: Block hash (required)
        :return: ResponsesGetBlockByHash
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_block_by_hash_with_http_info(hash, **kwargs)  # noqa: E501
        else:
            (data) = self.get_block_by_hash_with_http_info(hash, **kwargs)  # noqa: E501
            return data

    def get_block_by_hash_with_http_info(self, hash, **kwargs):  # noqa: E501
        """Get block by hash  # noqa: E501

        Get information about a specific block by its hash  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_block_by_hash_with_http_info(hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hash: Block hash (required)
        :return: ResponsesGetBlockByHash
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hash']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_block_by_hash" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hash' is set
        if ('hash' not in params or
                params['hash'] is None):
            raise ValueError("Missing the required parameter `hash` when calling `get_block_by_hash`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'hash' in params:
            path_params['hash'] = params['hash']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/blocks/hash/{hash}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsesGetBlockByHash',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_block_info(self, height, **kwargs):  # noqa: E501
        """Get block info  # noqa: E501

        Get information about a specific block by height  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_block_info(height, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int height: Block height (required)
        :return: ResponsesGetBlockInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_block_info_with_http_info(height, **kwargs)  # noqa: E501
        else:
            (data) = self.get_block_info_with_http_info(height, **kwargs)  # noqa: E501
            return data

    def get_block_info_with_http_info(self, height, **kwargs):  # noqa: E501
        """Get block info  # noqa: E501

        Get information about a specific block by height  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_block_info_with_http_info(height, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int height: Block height (required)
        :return: ResponsesGetBlockInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['height']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_block_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'height' is set
        if ('height' not in params or
                params['height'] is None):
            raise ValueError("Missing the required parameter `height` when calling `get_block_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'height' in params:
            path_params['height'] = params['height']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/blocks/{height}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsesGetBlockInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_block_transactions(self, height, **kwargs):  # noqa: E501
        """Get block transactions  # noqa: E501

        Get transactions for a specific block height  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_block_transactions(height, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int height: Block height (required)
        :return: ResponsesGetBlockTransactions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_block_transactions_with_http_info(height, **kwargs)  # noqa: E501
        else:
            (data) = self.get_block_transactions_with_http_info(height, **kwargs)  # noqa: E501
            return data

    def get_block_transactions_with_http_info(self, height, **kwargs):  # noqa: E501
        """Get block transactions  # noqa: E501

        Get transactions for a specific block height  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_block_transactions_with_http_info(height, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int height: Block height (required)
        :return: ResponsesGetBlockTransactions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['height']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_block_transactions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'height' is set
        if ('height' not in params or
                params['height'] is None):
            raise ValueError("Missing the required parameter `height` when calling `get_block_transactions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'height' in params:
            path_params['height'] = params['height']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/blocks/{height}/transactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsesGetBlockTransactions',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_current_block_height(self, **kwargs):  # noqa: E501
        """Get current block height  # noqa: E501

        Get the current block height of the Bitcoin blockchain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_block_height(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ResponsesGetBlockHeight
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_current_block_height_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_current_block_height_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_current_block_height_with_http_info(self, **kwargs):  # noqa: E501
        """Get current block height  # noqa: E501

        Get the current block height of the Bitcoin blockchain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_current_block_height_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ResponsesGetBlockHeight
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_current_block_height" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/blocks/current-height', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsesGetBlockHeight',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
