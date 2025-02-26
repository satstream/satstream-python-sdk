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


class MempoolApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_mempool_ancestors(self, body, **kwargs):  # noqa: E501
        """Get mempool ancestors  # noqa: E501

        Returns all in-mempool ancestors for a transaction in the mempool  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mempool_ancestors(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetMempoolAncestorsRequest body: Mempool ancestors request parameters (required)
        :return: GetMempoolAncestorsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_mempool_ancestors_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.get_mempool_ancestors_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def get_mempool_ancestors_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get mempool ancestors  # noqa: E501

        Returns all in-mempool ancestors for a transaction in the mempool  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mempool_ancestors_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetMempoolAncestorsRequest body: Mempool ancestors request parameters (required)
        :return: GetMempoolAncestorsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_mempool_ancestors" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `get_mempool_ancestors`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/mempool/ancestors', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetMempoolAncestorsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_mempool_descendants(self, body, **kwargs):  # noqa: E501
        """Get mempool descendants  # noqa: E501

        Returns all in-mempool descendants for a transaction in the mempool  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mempool_descendants(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetMempoolDescendantsRequest body: Mempool descendants request parameters (required)
        :return: GetMempoolDescendantsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_mempool_descendants_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.get_mempool_descendants_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def get_mempool_descendants_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get mempool descendants  # noqa: E501

        Returns all in-mempool descendants for a transaction in the mempool  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mempool_descendants_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetMempoolDescendantsRequest body: Mempool descendants request parameters (required)
        :return: GetMempoolDescendantsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_mempool_descendants" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `get_mempool_descendants`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/mempool/descendants', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetMempoolDescendantsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_mempool_info(self, **kwargs):  # noqa: E501
        """Get mempool information  # noqa: E501

        Returns details on the active state of the TX memory pool  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mempool_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetMempoolInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_mempool_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_mempool_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_mempool_info_with_http_info(self, **kwargs):  # noqa: E501
        """Get mempool information  # noqa: E501

        Returns details on the active state of the TX memory pool  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mempool_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GetMempoolInfoResponse
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
                    " to method get_mempool_info" % key
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
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/mempool/info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetMempoolInfoResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_raw_mempool(self, body, **kwargs):  # noqa: E501
        """Get raw mempool  # noqa: E501

        Returns all transaction ids in memory pool  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_raw_mempool(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetRawMempoolRequest body: Raw mempool request parameters (required)
        :return: GetRawMempoolResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_raw_mempool_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.get_raw_mempool_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def get_raw_mempool_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get raw mempool  # noqa: E501

        Returns all transaction ids in memory pool  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_raw_mempool_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetRawMempoolRequest body: Raw mempool request parameters (required)
        :return: GetRawMempoolResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_raw_mempool" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `get_raw_mempool`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/mempool/raw', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetRawMempoolResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def test_mempool_accept(self, body, **kwargs):  # noqa: E501
        """Test mempool accept  # noqa: E501

        Tests whether raw transactions would be accepted by mempool  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.test_mempool_accept(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TestMempoolAcceptRequest body: Raw transactions to test (required)
        :return: TestMempoolAcceptResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.test_mempool_accept_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.test_mempool_accept_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def test_mempool_accept_with_http_info(self, body, **kwargs):  # noqa: E501
        """Test mempool accept  # noqa: E501

        Tests whether raw transactions would be accepted by mempool  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.test_mempool_accept_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TestMempoolAcceptRequest body: Raw transactions to test (required)
        :return: TestMempoolAcceptResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method test_mempool_accept" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `test_mempool_accept`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/mempool/test-accept', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TestMempoolAcceptResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
