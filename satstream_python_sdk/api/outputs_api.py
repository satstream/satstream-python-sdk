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


class OutputsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_output_by_outpoint(self, outpoint, **kwargs):  # noqa: E501
        """Get output info by outpoint  # noqa: E501

        Retrieve information about a specific UTXO using outpoint string  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_output_by_outpoint(outpoint, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str outpoint: Outpoint (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_output_by_outpoint_with_http_info(outpoint, **kwargs)  # noqa: E501
        else:
            (data) = self.get_output_by_outpoint_with_http_info(outpoint, **kwargs)  # noqa: E501
            return data

    def get_output_by_outpoint_with_http_info(self, outpoint, **kwargs):  # noqa: E501
        """Get output info by outpoint  # noqa: E501

        Retrieve information about a specific UTXO using outpoint string  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_output_by_outpoint_with_http_info(outpoint, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str outpoint: Outpoint (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['outpoint']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_output_by_outpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'outpoint' is set
        if ('outpoint' not in params or
                params['outpoint'] is None):
            raise ValueError("Missing the required parameter `outpoint` when calling `get_output_by_outpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'outpoint' in params:
            path_params['outpoint'] = params['outpoint']  # noqa: E501

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
            '/output/{outpoint}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_outputs(self, body, **kwargs):  # noqa: E501
        """Get multiple outputs  # noqa: E501

        Retrieve information about multiple UTXOs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_outputs(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: Outpoints (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_outputs_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.get_outputs_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def get_outputs_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get multiple outputs  # noqa: E501

        Retrieve information about multiple UTXOs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_outputs_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: Outpoints (required)
        :return: InlineResponse2001
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
                    " to method get_outputs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `get_outputs`")  # noqa: E501

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
            '/outputs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
