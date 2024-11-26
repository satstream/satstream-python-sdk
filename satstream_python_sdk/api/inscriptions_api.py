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


class InscriptionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def fetch_inscription_child(self, inscription_id, child_index, **kwargs):  # noqa: E501
        """Get inscription child info  # noqa: E501

        Retrieve information about a specific child of an inscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_inscription_child(inscription_id, child_index, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inscription_id: Inscription ID (required)
        :param int child_index: Child Index (required)
        :return: InlineResponse20017
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_inscription_child_with_http_info(inscription_id, child_index, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_inscription_child_with_http_info(inscription_id, child_index, **kwargs)  # noqa: E501
            return data

    def fetch_inscription_child_with_http_info(self, inscription_id, child_index, **kwargs):  # noqa: E501
        """Get inscription child info  # noqa: E501

        Retrieve information about a specific child of an inscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_inscription_child_with_http_info(inscription_id, child_index, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inscription_id: Inscription ID (required)
        :param int child_index: Child Index (required)
        :return: InlineResponse20017
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['inscription_id', 'child_index']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_inscription_child" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'inscription_id' is set
        if ('inscription_id' not in params or
                params['inscription_id'] is None):
            raise ValueError("Missing the required parameter `inscription_id` when calling `fetch_inscription_child`")  # noqa: E501
        # verify the required parameter 'child_index' is set
        if ('child_index' not in params or
                params['child_index'] is None):
            raise ValueError("Missing the required parameter `child_index` when calling `fetch_inscription_child`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inscription_id' in params:
            path_params['inscription_id'] = params['inscription_id']  # noqa: E501
        if 'child_index' in params:
            path_params['child_index'] = params['child_index']  # noqa: E501

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
            '/inscription/{inscription_id}/{child_index}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20017',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_inscriptions(self, body, **kwargs):  # noqa: E501
        """Fetch multiple inscriptions  # noqa: E501

        Retrieve information about multiple inscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_inscriptions(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: Inscription IDs (required)
        :return: InlineResponse20019
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_inscriptions_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.fetch_inscriptions_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def fetch_inscriptions_with_http_info(self, body, **kwargs):  # noqa: E501
        """Fetch multiple inscriptions  # noqa: E501

        Retrieve information about multiple inscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_inscriptions_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: Inscription IDs (required)
        :return: InlineResponse20019
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
                    " to method fetch_inscriptions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `fetch_inscriptions`")  # noqa: E501

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
            '/inscriptions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20019',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_block_inscriptions(self, block_height, **kwargs):  # noqa: E501
        """Get inscriptions in a specific block  # noqa: E501

        Retrieve all inscriptions in a specific block  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_block_inscriptions(block_height, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int block_height: Block Height (required)
        :return: InlineResponse20018
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_block_inscriptions_with_http_info(block_height, **kwargs)  # noqa: E501
        else:
            (data) = self.get_block_inscriptions_with_http_info(block_height, **kwargs)  # noqa: E501
            return data

    def get_block_inscriptions_with_http_info(self, block_height, **kwargs):  # noqa: E501
        """Get inscriptions in a specific block  # noqa: E501

        Retrieve all inscriptions in a specific block  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_block_inscriptions_with_http_info(block_height, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int block_height: Block Height (required)
        :return: InlineResponse20018
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['block_height']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_block_inscriptions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'block_height' is set
        if ('block_height' not in params or
                params['block_height'] is None):
            raise ValueError("Missing the required parameter `block_height` when calling `get_block_inscriptions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'block_height' in params:
            path_params['block_height'] = params['block_height']  # noqa: E501

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
            '/inscriptions/block/{block_height}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_inscription(self, inscription_id, **kwargs):  # noqa: E501
        """Get inscription info  # noqa: E501

        Get information about a specific inscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_inscription(inscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inscription_id: Inscription ID (required)
        :return: InlineResponse20017
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_inscription_with_http_info(inscription_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_inscription_with_http_info(inscription_id, **kwargs)  # noqa: E501
            return data

    def get_inscription_with_http_info(self, inscription_id, **kwargs):  # noqa: E501
        """Get inscription info  # noqa: E501

        Get information about a specific inscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_inscription_with_http_info(inscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inscription_id: Inscription ID (required)
        :return: InlineResponse20017
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['inscription_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_inscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'inscription_id' is set
        if ('inscription_id' not in params or
                params['inscription_id'] is None):
            raise ValueError("Missing the required parameter `inscription_id` when calling `get_inscription`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inscription_id' in params:
            path_params['inscription_id'] = params['inscription_id']  # noqa: E501

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
            '/inscription/{inscription_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20017',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_latest_inscriptions(self, **kwargs):  # noqa: E501
        """Get latest inscriptions  # noqa: E501

        Retrieve the latest 100 inscriptions (first page)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_latest_inscriptions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20018
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_latest_inscriptions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_latest_inscriptions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_latest_inscriptions_with_http_info(self, **kwargs):  # noqa: E501
        """Get latest inscriptions  # noqa: E501

        Retrieve the latest 100 inscriptions (first page)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_latest_inscriptions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20018
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
                    " to method get_latest_inscriptions" % key
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
            '/inscriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_latest_inscriptions_page(self, page, **kwargs):  # noqa: E501
        """Get latest inscriptions page  # noqa: E501

        Retrieve a specific page of 100 inscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_latest_inscriptions_page(page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page number (required)
        :return: InlineResponse20018
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_latest_inscriptions_page_with_http_info(page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_latest_inscriptions_page_with_http_info(page, **kwargs)  # noqa: E501
            return data

    def get_latest_inscriptions_page_with_http_info(self, page, **kwargs):  # noqa: E501
        """Get latest inscriptions page  # noqa: E501

        Retrieve a specific page of 100 inscriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_latest_inscriptions_page_with_http_info(page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page number (required)
        :return: InlineResponse20018
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_latest_inscriptions_page" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_latest_inscriptions_page`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'page' in params:
            path_params['page'] = params['page']  # noqa: E501

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
            '/inscriptions/{page}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20018',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)