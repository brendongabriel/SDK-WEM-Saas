# coding: utf-8

"""
    WEM

    WEM Application API Documentation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ConversoDeFatoresDeEmissoApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def emissionsConversionFactorPatch(self, **kwargs):  # noqa: E501
        """Editar fatores de emissão  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.emissionsConversionFactorPatch(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.emissionsConversionFactorPatchHttp(**kwargs)  # noqa: E501
        else:
            (data) = self.emissionsConversionFactorPatchHttp(**kwargs)  # noqa: E501
            return data

    def emissionsConversionFactorPatchHttp(self, **kwargs):  # noqa: E501
        """Editar fatores de emissão  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.emissionsConversionFactorPatchHttp(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :return: object
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
                    " to method emissionsConversionFactorPatch" % key
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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/exchange/api/v1/emissions/conversion-factor', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def emissionsConversionFactorDeleteAll(self, plant_id, **kwargs):  # noqa: E501
        """Remover todos os fatores  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.emissionsConversionFactorDeleteAll(plant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str plant_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.emissionsConversionFactorDeleteAllHttp(plant_id, **kwargs)  # noqa: E501
        else:
            (data) = self.emissionsConversionFactorDeleteAllHttp(plant_id, **kwargs)  # noqa: E501
            return data

    def emissionsConversionFactorDeleteAllHttp(self, plant_id, **kwargs):  # noqa: E501
        """Remover todos os fatores  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.emissionsConversionFactorDeleteAllHttp(plant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str plant_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['plant_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method emissionsConversionFactorDeleteAll" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'plant_id' is set
        if ('plant_id' not in params or
                params['plant_id'] is None):
            raise ValueError("Missing the required parameter `plant_id` when calling `emissionsConversionFactorDeleteAll`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'plant_id' in params:
            path_params['plant_id'] = params['plant_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/exchange/api/v1/emissions/conversion-factor/plants/{plant_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def emissionsConversionFactorGet(self, plant_id, **kwargs):  # noqa: E501
        """Buscar fatores de emissão  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.emissionsConversionFactorGet(plant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str plant_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.emissionsConversionFactorGetHttp(plant_id, **kwargs)  # noqa: E501
        else:
            (data) = self.emissionsConversionFactorGetHttp(plant_id, **kwargs)  # noqa: E501
            return data

    def emissionsConversionFactorGetHttp(self, plant_id, **kwargs):  # noqa: E501
        """Buscar fatores de emissão  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.emissionsConversionFactorGetHttp(plant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str plant_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['plant_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method emissionsConversionFactorGet" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'plant_id' is set
        if ('plant_id' not in params or
                params['plant_id'] is None):
            raise ValueError("Missing the required parameter `plant_id` when calling `emissionsConversionFactorGet`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'plant_id' in params:
            path_params['plant_id'] = params['plant_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/exchange/api/v1/emissions/conversion-factor/plants/{plant_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)