# coding: utf-8

"""
    Wavefront REST API Documentation

    <p>The REST API enables you to interact with the Wavefront service by using standard REST API tools. You can use the REST API to automate commonly executed operations, for example to tag sources automatically.</p><p>When you make REST API calls outside the REST API documentation UI, to authenticate to the service, you must use an API token associated with a user account or a service account. For information on how to get the API token and examples, see <a href=\"http://docs.wavefront.com/using_wavefront_api.html\">Use the Wavefront REST API.</a></p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from wavefront_api_client.api_client import ApiClient


class IngestionSpyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def spy_on_delta_counters(self, **kwargs):  # noqa: E501
        """Gets new delta counters that are added to existing time series.  # noqa: E501

        Try it Out button won't work in this case, as it's a streaming API. Endpoint: https://.wavefront.com/api/spy/deltas.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spy_on_delta_counters(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str counter: List a delta counter only if its name starts with the specified case-sensitive prefix.  E.g., counter=orderShirt matches counters named orderShirt and orderShirts, but not OrderShirts.
        :param str host: List a delta counter only if the name of its source starts with the specified case-sensitive prefix.
        :param list[str] counter_tag_key: List a delta counter only if it has the specified tag key. Add this parameter multiple times to specify multiple tags, e.g. counterTagKey=cluster&counterTagKey=shard  put cluster in the first line, put shard in the second line as values
        :param float sampling:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.spy_on_delta_counters_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.spy_on_delta_counters_with_http_info(**kwargs)  # noqa: E501
            return data

    def spy_on_delta_counters_with_http_info(self, **kwargs):  # noqa: E501
        """Gets new delta counters that are added to existing time series.  # noqa: E501

        Try it Out button won't work in this case, as it's a streaming API. Endpoint: https://.wavefront.com/api/spy/deltas.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spy_on_delta_counters_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str counter: List a delta counter only if its name starts with the specified case-sensitive prefix.  E.g., counter=orderShirt matches counters named orderShirt and orderShirts, but not OrderShirts.
        :param str host: List a delta counter only if the name of its source starts with the specified case-sensitive prefix.
        :param list[str] counter_tag_key: List a delta counter only if it has the specified tag key. Add this parameter multiple times to specify multiple tags, e.g. counterTagKey=cluster&counterTagKey=shard  put cluster in the first line, put shard in the second line as values
        :param float sampling:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['counter', 'host', 'counter_tag_key', 'sampling']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method spy_on_delta_counters" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'counter' in params:
            query_params.append(('counter', params['counter']))  # noqa: E501
        if 'host' in params:
            query_params.append(('host', params['host']))  # noqa: E501
        if 'counter_tag_key' in params:
            query_params.append(('counterTagKey', params['counter_tag_key']))  # noqa: E501
            collection_formats['counterTagKey'] = 'multi'  # noqa: E501
        if 'sampling' in params:
            query_params.append(('sampling', params['sampling']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/spy/deltas', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def spy_on_ephemeral_points(self, **kwargs):  # noqa: E501
        """Gets a sampling of new ephemeral metric data points that are added to existing time series.  # noqa: E501

        Try it Out button won't work in this case, as it's a streaming API.  Endpoint: https://<cluster>.wavefront.com/api/spy/ephemeral.   Details usage can be find at: https://docs.wavefront.com/wavefront_monitoring_spy.html#get-ingested-metric-points-with-spy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spy_on_ephemeral_points(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str metric: List a point only if its metric name starts with the specified case-sensitive prefix. E.g., metric=Cust matches metrics named Customer, Customers, Customer.alerts, but not customer.
        :param str host: List a point only if its source name starts with the specified case-sensitive prefix.
        :param list[str] point_tag_key: List a point only if it has the specified point tag key. Add this parameter multiple times to specify multiple point tags, e.g., pointTagKey=env&pointTagKey=datacenter  put env in the first line and datacenter in the second line as values
        :param float sampling: goes from 0 to 1 with 0.01 being 1%
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.spy_on_ephemeral_points_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.spy_on_ephemeral_points_with_http_info(**kwargs)  # noqa: E501
            return data

    def spy_on_ephemeral_points_with_http_info(self, **kwargs):  # noqa: E501
        """Gets a sampling of new ephemeral metric data points that are added to existing time series.  # noqa: E501

        Try it Out button won't work in this case, as it's a streaming API.  Endpoint: https://<cluster>.wavefront.com/api/spy/ephemeral.   Details usage can be find at: https://docs.wavefront.com/wavefront_monitoring_spy.html#get-ingested-metric-points-with-spy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spy_on_ephemeral_points_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str metric: List a point only if its metric name starts with the specified case-sensitive prefix. E.g., metric=Cust matches metrics named Customer, Customers, Customer.alerts, but not customer.
        :param str host: List a point only if its source name starts with the specified case-sensitive prefix.
        :param list[str] point_tag_key: List a point only if it has the specified point tag key. Add this parameter multiple times to specify multiple point tags, e.g., pointTagKey=env&pointTagKey=datacenter  put env in the first line and datacenter in the second line as values
        :param float sampling: goes from 0 to 1 with 0.01 being 1%
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['metric', 'host', 'point_tag_key', 'sampling']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method spy_on_ephemeral_points" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'metric' in params:
            query_params.append(('metric', params['metric']))  # noqa: E501
        if 'host' in params:
            query_params.append(('host', params['host']))  # noqa: E501
        if 'point_tag_key' in params:
            query_params.append(('pointTagKey', params['point_tag_key']))  # noqa: E501
            collection_formats['pointTagKey'] = 'multi'  # noqa: E501
        if 'sampling' in params:
            query_params.append(('sampling', params['sampling']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/spy/ephemeral', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def spy_on_histograms(self, **kwargs):  # noqa: E501
        """Gets new histograms that are added to existing time series.  # noqa: E501

        Try it Out button won't work in this case, as it's a streaming API. Endpoint: https://.wavefront.com/api/spy/histograms  .   Details usage can be find at: https://docs.wavefront.com/wavefront_monitoring_spy.html#get-ingested-histograms-with-spy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spy_on_histograms(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str histogram: List a histogram only if its name starts with the specified case-sensitive prefix. E.g., histogram=orderShirt matches histograms named orderShirt and orderShirts, but not OrderShirts.
        :param str host: List a histogram only if the name of its source starts with the specified case-sensitive prefix.
        :param list[str] histogram_tag_key: List a histogram only if it has the specified tag key. Add this parameter multiple times to specify multiple tags, e.g. histogramTagKey=cluster&histogramTagKey=shard  put cluster in the first line, put shard in the second line as values
        :param float sampling:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.spy_on_histograms_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.spy_on_histograms_with_http_info(**kwargs)  # noqa: E501
            return data

    def spy_on_histograms_with_http_info(self, **kwargs):  # noqa: E501
        """Gets new histograms that are added to existing time series.  # noqa: E501

        Try it Out button won't work in this case, as it's a streaming API. Endpoint: https://.wavefront.com/api/spy/histograms  .   Details usage can be find at: https://docs.wavefront.com/wavefront_monitoring_spy.html#get-ingested-histograms-with-spy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spy_on_histograms_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str histogram: List a histogram only if its name starts with the specified case-sensitive prefix. E.g., histogram=orderShirt matches histograms named orderShirt and orderShirts, but not OrderShirts.
        :param str host: List a histogram only if the name of its source starts with the specified case-sensitive prefix.
        :param list[str] histogram_tag_key: List a histogram only if it has the specified tag key. Add this parameter multiple times to specify multiple tags, e.g. histogramTagKey=cluster&histogramTagKey=shard  put cluster in the first line, put shard in the second line as values
        :param float sampling:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['histogram', 'host', 'histogram_tag_key', 'sampling']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method spy_on_histograms" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'histogram' in params:
            query_params.append(('histogram', params['histogram']))  # noqa: E501
        if 'host' in params:
            query_params.append(('host', params['host']))  # noqa: E501
        if 'histogram_tag_key' in params:
            query_params.append(('histogramTagKey', params['histogram_tag_key']))  # noqa: E501
            collection_formats['histogramTagKey'] = 'multi'  # noqa: E501
        if 'sampling' in params:
            query_params.append(('sampling', params['sampling']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/spy/histograms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def spy_on_id_creations(self, **kwargs):  # noqa: E501
        """Gets newly allocated IDs that correspond to new metric names, source names, point tags, or span tags. A new ID generally indicates that a new time series has been introduced.  # noqa: E501

        Try it Out button won't work in this case, as it's a streaming API.  Endpoint: https://<cluster>.wavefront.com/api/spy/ids.   Details usage can be find at: https://docs.wavefront.com/wavefront_monitoring_spy.html#get-new-id-assignments-with-spy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spy_on_id_creations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: Type of new items you want to see ID assignments for: METRIC - Metric names SPAN - Span names HOST - Source names STRING - Point tags or span tags, represented as a single string containing a unique key-value pair, e.g. env=prod, env=dev, etc.
        :param str body: Case-sensitive prefix for the items that you are interested in.
        :param float sampling: goes from 0 to 1 with 0.01 being 1%
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.spy_on_id_creations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.spy_on_id_creations_with_http_info(**kwargs)  # noqa: E501
            return data

    def spy_on_id_creations_with_http_info(self, **kwargs):  # noqa: E501
        """Gets newly allocated IDs that correspond to new metric names, source names, point tags, or span tags. A new ID generally indicates that a new time series has been introduced.  # noqa: E501

        Try it Out button won't work in this case, as it's a streaming API.  Endpoint: https://<cluster>.wavefront.com/api/spy/ids.   Details usage can be find at: https://docs.wavefront.com/wavefront_monitoring_spy.html#get-new-id-assignments-with-spy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spy_on_id_creations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: Type of new items you want to see ID assignments for: METRIC - Metric names SPAN - Span names HOST - Source names STRING - Point tags or span tags, represented as a single string containing a unique key-value pair, e.g. env=prod, env=dev, etc.
        :param str body: Case-sensitive prefix for the items that you are interested in.
        :param float sampling: goes from 0 to 1 with 0.01 being 1%
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type', 'body', 'sampling']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method spy_on_id_creations" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'sampling' in params:
            query_params.append(('sampling', params['sampling']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/spy/ids', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def spy_on_points(self, **kwargs):  # noqa: E501
        """Gets a sampling of new metric data points that are added to existing time series.  # noqa: E501

        Try it Out button won't work in this case, as it's a streaming API.  Endpoint: https://<cluster>.wavefront.com/api/spy/points.   Details usage can be find at: https://docs.wavefront.com/wavefront_monitoring_spy.html#get-ingested-metric-points-with-spy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spy_on_points(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str metric: List a point only if its metric name starts with the specified case-sensitive prefix. E.g., metric=Cust matches metrics named Customer, Customers, Customer.alerts, but not customer.
        :param str host: List a point only if its source name starts with the specified case-sensitive prefix.
        :param list[str] point_tag_key: List a point only if it has the specified point tag key. Add this parameter multiple times to specify multiple point tags, e.g., pointTagKey=env&pointTagKey=datacenter  put env in the first line and datacenter in the second line as values
        :param float sampling: goes from 0 to 1 with 0.01 being 1%
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.spy_on_points_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.spy_on_points_with_http_info(**kwargs)  # noqa: E501
            return data

    def spy_on_points_with_http_info(self, **kwargs):  # noqa: E501
        """Gets a sampling of new metric data points that are added to existing time series.  # noqa: E501

        Try it Out button won't work in this case, as it's a streaming API.  Endpoint: https://<cluster>.wavefront.com/api/spy/points.   Details usage can be find at: https://docs.wavefront.com/wavefront_monitoring_spy.html#get-ingested-metric-points-with-spy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spy_on_points_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str metric: List a point only if its metric name starts with the specified case-sensitive prefix. E.g., metric=Cust matches metrics named Customer, Customers, Customer.alerts, but not customer.
        :param str host: List a point only if its source name starts with the specified case-sensitive prefix.
        :param list[str] point_tag_key: List a point only if it has the specified point tag key. Add this parameter multiple times to specify multiple point tags, e.g., pointTagKey=env&pointTagKey=datacenter  put env in the first line and datacenter in the second line as values
        :param float sampling: goes from 0 to 1 with 0.01 being 1%
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['metric', 'host', 'point_tag_key', 'sampling']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method spy_on_points" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'metric' in params:
            query_params.append(('metric', params['metric']))  # noqa: E501
        if 'host' in params:
            query_params.append(('host', params['host']))  # noqa: E501
        if 'point_tag_key' in params:
            query_params.append(('pointTagKey', params['point_tag_key']))  # noqa: E501
            collection_formats['pointTagKey'] = 'multi'  # noqa: E501
        if 'sampling' in params:
            query_params.append(('sampling', params['sampling']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/spy/points', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def spy_on_spans(self, **kwargs):  # noqa: E501
        """Gets new spans with existing source names and span tags.  # noqa: E501

        Try it Out button won't work in this case, as it's a streaming API.   Endpoint: https://<cluster>.wavefront.com/api/spy/spans   Details usage can be find at: https://docs.wavefron.com/wavefront_monitoring_spy.html#get-ingested-spans-with-spy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spy_on_spans(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: List a span only if its operation name starts with the specified case-sensitive prefix. E.g., name=orderShirt matches spans named orderShirt and orderShirts, but not OrderShirts.
        :param str host: List a span only if the name of its source starts with the specified case-sensitive prefix.
        :param list[str] span_tag_key: List a span only if it has the specified span tag key. Add this parameter multiple times to specify multiple span tags, e.g. spanTagKey=cluster&spanTagKey=shard
        :param float sampling: goes from 0 to 1 with 0.01 being 1%
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.spy_on_spans_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.spy_on_spans_with_http_info(**kwargs)  # noqa: E501
            return data

    def spy_on_spans_with_http_info(self, **kwargs):  # noqa: E501
        """Gets new spans with existing source names and span tags.  # noqa: E501

        Try it Out button won't work in this case, as it's a streaming API.   Endpoint: https://<cluster>.wavefront.com/api/spy/spans   Details usage can be find at: https://docs.wavefron.com/wavefront_monitoring_spy.html#get-ingested-spans-with-spy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spy_on_spans_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: List a span only if its operation name starts with the specified case-sensitive prefix. E.g., name=orderShirt matches spans named orderShirt and orderShirts, but not OrderShirts.
        :param str host: List a span only if the name of its source starts with the specified case-sensitive prefix.
        :param list[str] span_tag_key: List a span only if it has the specified span tag key. Add this parameter multiple times to specify multiple span tags, e.g. spanTagKey=cluster&spanTagKey=shard
        :param float sampling: goes from 0 to 1 with 0.01 being 1%
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'host', 'span_tag_key', 'sampling']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method spy_on_spans" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'host' in params:
            query_params.append(('host', params['host']))  # noqa: E501
        if 'span_tag_key' in params:
            query_params.append(('spanTagKey', params['span_tag_key']))  # noqa: E501
            collection_formats['spanTagKey'] = 'multi'  # noqa: E501
        if 'sampling' in params:
            query_params.append(('sampling', params['sampling']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/spy/spans', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
