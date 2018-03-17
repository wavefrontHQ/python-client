# wavefront_api_client.QueryApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_api**](QueryApi.md#query_api) | **GET** /api/v2/chart/api | Perform a charting query against Wavefront servers that returns the appropriate points in the specified time window and granularity
[**query_raw**](QueryApi.md#query_raw) | **GET** /api/v2/chart/raw | Perform a raw data query against Wavefront servers that returns second granularity points grouped by tags


# **query_api**
> QueryResult query_api(q, s, g, n=n, e=e, p=p, i=i, auto_events=auto_events, summarization=summarization, list_mode=list_mode, strict=strict, include_obsolete_metrics=include_obsolete_metrics, sorted=sorted)

Perform a charting query against Wavefront servers that returns the appropriate points in the specified time window and granularity

Long time spans and small granularities can take a long time to calculate

### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.QueryApi(wavefront_api_client.ApiClient(configuration))
q = 'q_example' # str | the query expression to execute
s = 's_example' # str | the start time of the query window in epoch milliseconds
g = 'g_example' # str | the granularity of the points returned
n = 'n_example' # str | name used to identify the query (optional)
e = 'e_example' # str | the end time of the query window in epoch milliseconds (null to use now) (optional)
p = 'p_example' # str | the approximate maximum number of points to return (may not limit number of points exactly) (optional)
i = true # bool | whether series with only points that are outside of the query window will be returned (defaults to true) (optional)
auto_events = true # bool | whether events for sources included in the query will be automatically returned by the query (optional)
summarization = 'summarization_example' # str | summarization strategy to use when bucketing points together (optional)
list_mode = true # bool | retrieve events more optimally displayed for a list (optional)
strict = true # bool | do not return points outside the query window [s;e), defaults to false (optional)
include_obsolete_metrics = true # bool | include metrics that have not been reporting recently, defaults to false (optional)
sorted = false # bool | sorts the output so that returned series are in order, defaults to false (optional) (default to false)

try:
    # Perform a charting query against Wavefront servers that returns the appropriate points in the specified time window and granularity
    api_response = api_instance.query_api(q, s, g, n=n, e=e, p=p, i=i, auto_events=auto_events, summarization=summarization, list_mode=list_mode, strict=strict, include_obsolete_metrics=include_obsolete_metrics, sorted=sorted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->query_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| the query expression to execute | 
 **s** | **str**| the start time of the query window in epoch milliseconds | 
 **g** | **str**| the granularity of the points returned | 
 **n** | **str**| name used to identify the query | [optional] 
 **e** | **str**| the end time of the query window in epoch milliseconds (null to use now) | [optional] 
 **p** | **str**| the approximate maximum number of points to return (may not limit number of points exactly) | [optional] 
 **i** | **bool**| whether series with only points that are outside of the query window will be returned (defaults to true) | [optional] 
 **auto_events** | **bool**| whether events for sources included in the query will be automatically returned by the query | [optional] 
 **summarization** | **str**| summarization strategy to use when bucketing points together | [optional] 
 **list_mode** | **bool**| retrieve events more optimally displayed for a list | [optional] 
 **strict** | **bool**| do not return points outside the query window [s;e), defaults to false | [optional] 
 **include_obsolete_metrics** | **bool**| include metrics that have not been reporting recently, defaults to false | [optional] 
 **sorted** | **bool**| sorts the output so that returned series are in order, defaults to false | [optional] [default to false]

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-javascript; charset=UTF-8, application/javascript; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_raw**
> list[RawTimeseries] query_raw(metric, host=host, source=source, start_time=start_time, end_time=end_time)

Perform a raw data query against Wavefront servers that returns second granularity points grouped by tags

An API to check if ingested points are as expected.  Points ingested within a single second are averaged when returned.

### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.QueryApi(wavefront_api_client.ApiClient(configuration))
metric = 'metric_example' # str | metric to query ingested points for (cannot contain wildcards)
host = 'host_example' # str | host to query ingested points for (cannot contain wildcards). host or source is equivalent, only one should be used. (optional)
source = 'source_example' # str | source to query ingested points for (cannot contain wildcards). host or source is equivalent, only one should be used. (optional)
start_time = 789 # int | start time in epoch milliseconds (cannot be more than a day in the past) null to use an hour before endTime (optional)
end_time = 789 # int | end time in epoch milliseconds (cannot be more than a day in the past) null to use now (optional)

try:
    # Perform a raw data query against Wavefront servers that returns second granularity points grouped by tags
    api_response = api_instance.query_raw(metric, host=host, source=source, start_time=start_time, end_time=end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->query_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric** | **str**| metric to query ingested points for (cannot contain wildcards) | 
 **host** | **str**| host to query ingested points for (cannot contain wildcards). host or source is equivalent, only one should be used. | [optional] 
 **source** | **str**| source to query ingested points for (cannot contain wildcards). host or source is equivalent, only one should be used. | [optional] 
 **start_time** | **int**| start time in epoch milliseconds (cannot be more than a day in the past) null to use an hour before endTime | [optional] 
 **end_time** | **int**| end time in epoch milliseconds (cannot be more than a day in the past) null to use now | [optional] 

### Return type

[**list[RawTimeseries]**](RawTimeseries.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

