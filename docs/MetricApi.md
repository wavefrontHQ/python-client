# wavefront_api_client.MetricApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metric_details**](MetricApi.md#get_metric_details) | **GET** /api/v2/chart/metric/detail | Get more details on a metric, including reporting sources and approximate last time reported


# **get_metric_details**
> MetricDetailsResponse get_metric_details(m, l=l, c=c, h=h)

Get more details on a metric, including reporting sources and approximate last time reported



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
api_instance = wavefront_api_client.MetricApi(wavefront_api_client.ApiClient(configuration))
m = 'm_example' # str | Metric name
l = 56 # int | limit (optional)
c = 'c_example' # str | cursor value to continue if the number of results exceeds 1000 (optional)
h = ['h_example'] # list[str] | glob pattern for sources to include in the query result (optional)

try:
    # Get more details on a metric, including reporting sources and approximate last time reported
    api_response = api_instance.get_metric_details(m, l=l, c=c, h=h)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricApi->get_metric_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **m** | **str**| Metric name | 
 **l** | **int**| limit | [optional] 
 **c** | **str**| cursor value to continue if the number of results exceeds 1000 | [optional] 
 **h** | [**list[str]**](str.md)| glob pattern for sources to include in the query result | [optional] 

### Return type

[**MetricDetailsResponse**](MetricDetailsResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-javascript, application/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

