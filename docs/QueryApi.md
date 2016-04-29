# wavefront_client.QueryApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chart**](QueryApi.md#chart) | **GET** /chart/api | Perform a charting query against Wavefront servers which returns the appropriate points in the specified time window and granularity
[**raw_query**](QueryApi.md#raw_query) | **GET** /chart/raw | Perform a raw data query against Wavefront servers which returns second granularity points grouped by tags


# **chart**
> QueryResult chart(q, s, g, n=n, e=e, p=p, i=i, auto_events=auto_events, summarization=summarization, list_mode=list_mode, strict=strict, include_obsolete_metrics=include_obsolete_metrics, sorted=sorted)

Perform a charting query against Wavefront servers which returns the appropriate points in the specified time window and granularity

Be aware that long time spans and small granularities can take a long time to calculate

### Example 
```python
import time
import wavefront_client
from wavefront_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
wavefront_client.configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# wavefront_client.configuration.api_key_prefix['X-AUTH-TOKEN'] = 'BEARER'

# create an instance of the API class
api_instance = wavefront_client.QueryApi()
q = 'q_example' # str | the query expression to execute
s = 's_example' # str | the start time of the query window
g = 'g_example' # str | the granularity of the points returned
n = 'n_example' # str | name used to identify the query (optional)
e = 'e_example' # str | the end time of the query window (null to use now) (optional)
p = 'p_example' # str | the maximum number of points to return (optional)
i = true # bool | whether series with only points that are outside of the query window will be returned (defaults to true) (optional)
auto_events = true # bool | whether events for sources included in the query will be automatically returned by the query (optional)
summarization = 'summarization_example' # str | summarization strategy to use when bucketing points together (optional)
list_mode = true # bool | retrieve events more optimally displayed for a list (optional)
strict = true # bool | do not return points outside the query window [q;s), defaults to false (optional)
include_obsolete_metrics = true # bool | include metrics that have not been reporting recently, defaults to false (optional)
sorted = false # bool | sorts the output so that returned series are in order, defaults to false (optional) (default to false)

try: 
    # Perform a charting query against Wavefront servers which returns the appropriate points in the specified time window and granularity
    api_response = api_instance.chart(q, s, g, n=n, e=e, p=p, i=i, auto_events=auto_events, summarization=summarization, list_mode=list_mode, strict=strict, include_obsolete_metrics=include_obsolete_metrics, sorted=sorted)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QueryApi->chart: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| the query expression to execute | 
 **s** | **str**| the start time of the query window | 
 **g** | **str**| the granularity of the points returned | 
 **n** | **str**| name used to identify the query | [optional] 
 **e** | **str**| the end time of the query window (null to use now) | [optional] 
 **p** | **str**| the maximum number of points to return | [optional] 
 **i** | **bool**| whether series with only points that are outside of the query window will be returned (defaults to true) | [optional] 
 **auto_events** | **bool**| whether events for sources included in the query will be automatically returned by the query | [optional] 
 **summarization** | **str**| summarization strategy to use when bucketing points together | [optional] 
 **list_mode** | **bool**| retrieve events more optimally displayed for a list | [optional] 
 **strict** | **bool**| do not return points outside the query window [q;s), defaults to false | [optional] 
 **include_obsolete_metrics** | **bool**| include metrics that have not been reporting recently, defaults to false | [optional] 
 **sorted** | **bool**| sorts the output so that returned series are in order, defaults to false | [optional] [default to false]

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-javascript; charset&#x3D;UTF-8, application/javascript; charset&#x3D;UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **raw_query**
> list[Timeseries] raw_query(metric, host=host, source=source, start_time=start_time, end_time=end_time)

Perform a raw data query against Wavefront servers which returns second granularity points grouped by tags

User can use this API to check if ingested points are as expected. Note that points ingested within a single second are averaged when returned.

### Example 
```python
import time
import wavefront_client
from wavefront_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
wavefront_client.configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# wavefront_client.configuration.api_key_prefix['X-AUTH-TOKEN'] = 'BEARER'

# create an instance of the API class
api_instance = wavefront_client.QueryApi()
metric = 'metric_example' # str | metric to query ingested points for (cannot contain wildcards)
host = 'host_example' # str | host to query ingested points for (cannot contain wildcards). host or source is equivalent, only one should be used. (optional)
source = 'source_example' # str | source to query ingested points for (cannot contain wildcards). host or source is equivalent, only one should be used. (optional)
start_time = 789 # int | start time in milliseconds (cannot be more than a day in the past) null to use an hour before endTime (optional)
end_time = 789 # int | end time in milliseconds (cannot be more than a day in the past) null to use now (optional)

try: 
    # Perform a raw data query against Wavefront servers which returns second granularity points grouped by tags
    api_response = api_instance.raw_query(metric, host=host, source=source, start_time=start_time, end_time=end_time)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QueryApi->raw_query: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric** | **str**| metric to query ingested points for (cannot contain wildcards) | 
 **host** | **str**| host to query ingested points for (cannot contain wildcards). host or source is equivalent, only one should be used. | [optional] 
 **source** | **str**| source to query ingested points for (cannot contain wildcards). host or source is equivalent, only one should be used. | [optional] 
 **start_time** | **int**| start time in milliseconds (cannot be more than a day in the past) null to use an hour before endTime | [optional] 
 **end_time** | **int**| end time in milliseconds (cannot be more than a day in the past) null to use now | [optional] 

### Return type

[**list[Timeseries]**](Timeseries.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

