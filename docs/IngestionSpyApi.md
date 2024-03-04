# wavefront_api_client.IngestionSpyApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spy_on_delta_counters**](IngestionSpyApi.md#spy_on_delta_counters) | **GET** /api/spy/deltas | Gets new delta counters that are added to existing time series.
[**spy_on_ephemeral_points**](IngestionSpyApi.md#spy_on_ephemeral_points) | **GET** /api/spy/ephemeral | Gets a sampling of new ephemeral metric data points that are added to existing time series.
[**spy_on_histograms**](IngestionSpyApi.md#spy_on_histograms) | **GET** /api/spy/histograms | Gets new histograms that are added to existing time series.
[**spy_on_id_creations**](IngestionSpyApi.md#spy_on_id_creations) | **GET** /api/spy/ids | Gets newly allocated IDs that correspond to new metric names, source names, point tags, or span tags. A new ID generally indicates that a new time series has been introduced.
[**spy_on_points**](IngestionSpyApi.md#spy_on_points) | **GET** /api/spy/points | Gets a sampling of new metric data points that are added to existing time series.
[**spy_on_spans**](IngestionSpyApi.md#spy_on_spans) | **GET** /api/spy/spans | Gets new spans with existing source names and span tags.


# **spy_on_delta_counters**
> spy_on_delta_counters(counter=counter, host=host, counter_tag_key=counter_tag_key, sampling=sampling)

Gets new delta counters that are added to existing time series.

Try it Out button won't work in this case, as it's a streaming API. Endpoint: https://.wavefront.com/api/spy/deltas.  

### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wavefront_api_client.IngestionSpyApi()
counter = 'counter_example' # str | List a delta counter only if its name starts with the specified case-sensitive prefix.  E.g., counter=orderShirt matches counters named orderShirt and orderShirts, but not OrderShirts. (optional)
host = 'host_example' # str | List a delta counter only if the name of its source starts with the specified case-sensitive prefix. (optional)
counter_tag_key = ['counter_tag_key_example'] # list[str] | List a delta counter only if it has the specified tag key. Add this parameter multiple times to specify multiple tags, e.g. counterTagKey=cluster&counterTagKey=shard  put cluster in the first line, put shard in the second line as values (optional)
sampling = 0.01 # float |  (optional) (default to 0.01)

try:
    # Gets new delta counters that are added to existing time series.
    api_instance.spy_on_delta_counters(counter=counter, host=host, counter_tag_key=counter_tag_key, sampling=sampling)
except ApiException as e:
    print("Exception when calling IngestionSpyApi->spy_on_delta_counters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **counter** | **str**| List a delta counter only if its name starts with the specified case-sensitive prefix.  E.g., counter&#x3D;orderShirt matches counters named orderShirt and orderShirts, but not OrderShirts. | [optional] 
 **host** | **str**| List a delta counter only if the name of its source starts with the specified case-sensitive prefix. | [optional] 
 **counter_tag_key** | [**list[str]**](str.md)| List a delta counter only if it has the specified tag key. Add this parameter multiple times to specify multiple tags, e.g. counterTagKey&#x3D;cluster&amp;counterTagKey&#x3D;shard  put cluster in the first line, put shard in the second line as values | [optional] 
 **sampling** | **float**|  | [optional] [default to 0.01]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spy_on_ephemeral_points**
> spy_on_ephemeral_points(metric=metric, host=host, point_tag_key=point_tag_key, sampling=sampling)

Gets a sampling of new ephemeral metric data points that are added to existing time series.

Try it Out button won't work in this case, as it's a streaming API.  Endpoint: https://<cluster>.wavefront.com/api/spy/ephemeral.   Details usage can be find at: https://docs.wavefront.com/wavefront_monitoring_spy.html#get-ingested-metric-points-with-spy

### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wavefront_api_client.IngestionSpyApi()
metric = 'metric_example' # str | List a point only if its metric name starts with the specified case-sensitive prefix. E.g., metric=Cust matches metrics named Customer, Customers, Customer.alerts, but not customer. (optional)
host = 'host_example' # str | List a point only if its source name starts with the specified case-sensitive prefix. (optional)
point_tag_key = ['point_tag_key_example'] # list[str] | List a point only if it has the specified point tag key. Add this parameter multiple times to specify multiple point tags, e.g., pointTagKey=env&pointTagKey=datacenter  put env in the first line and datacenter in the second line as values (optional)
sampling = 0.01 # float | goes from 0 to 1 with 0.01 being 1% (optional) (default to 0.01)

try:
    # Gets a sampling of new ephemeral metric data points that are added to existing time series.
    api_instance.spy_on_ephemeral_points(metric=metric, host=host, point_tag_key=point_tag_key, sampling=sampling)
except ApiException as e:
    print("Exception when calling IngestionSpyApi->spy_on_ephemeral_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric** | **str**| List a point only if its metric name starts with the specified case-sensitive prefix. E.g., metric&#x3D;Cust matches metrics named Customer, Customers, Customer.alerts, but not customer. | [optional] 
 **host** | **str**| List a point only if its source name starts with the specified case-sensitive prefix. | [optional] 
 **point_tag_key** | [**list[str]**](str.md)| List a point only if it has the specified point tag key. Add this parameter multiple times to specify multiple point tags, e.g., pointTagKey&#x3D;env&amp;pointTagKey&#x3D;datacenter  put env in the first line and datacenter in the second line as values | [optional] 
 **sampling** | **float**| goes from 0 to 1 with 0.01 being 1% | [optional] [default to 0.01]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spy_on_histograms**
> spy_on_histograms(histogram=histogram, host=host, histogram_tag_key=histogram_tag_key, sampling=sampling)

Gets new histograms that are added to existing time series.

Try it Out button won't work in this case, as it's a streaming API. Endpoint: https://.wavefront.com/api/spy/histograms  .   Details usage can be find at: https://docs.wavefront.com/wavefront_monitoring_spy.html#get-ingested-histograms-with-spy

### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wavefront_api_client.IngestionSpyApi()
histogram = 'histogram_example' # str | List a histogram only if its name starts with the specified case-sensitive prefix. E.g., histogram=orderShirt matches histograms named orderShirt and orderShirts, but not OrderShirts. (optional)
host = 'host_example' # str | List a histogram only if the name of its source starts with the specified case-sensitive prefix. (optional)
histogram_tag_key = ['histogram_tag_key_example'] # list[str] | List a histogram only if it has the specified tag key. Add this parameter multiple times to specify multiple tags, e.g. histogramTagKey=cluster&histogramTagKey=shard  put cluster in the first line, put shard in the second line as values (optional)
sampling = 0.01 # float |  (optional) (default to 0.01)

try:
    # Gets new histograms that are added to existing time series.
    api_instance.spy_on_histograms(histogram=histogram, host=host, histogram_tag_key=histogram_tag_key, sampling=sampling)
except ApiException as e:
    print("Exception when calling IngestionSpyApi->spy_on_histograms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **histogram** | **str**| List a histogram only if its name starts with the specified case-sensitive prefix. E.g., histogram&#x3D;orderShirt matches histograms named orderShirt and orderShirts, but not OrderShirts. | [optional] 
 **host** | **str**| List a histogram only if the name of its source starts with the specified case-sensitive prefix. | [optional] 
 **histogram_tag_key** | [**list[str]**](str.md)| List a histogram only if it has the specified tag key. Add this parameter multiple times to specify multiple tags, e.g. histogramTagKey&#x3D;cluster&amp;histogramTagKey&#x3D;shard  put cluster in the first line, put shard in the second line as values | [optional] 
 **sampling** | **float**|  | [optional] [default to 0.01]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spy_on_id_creations**
> spy_on_id_creations(type=type, body=body, sampling=sampling)

Gets newly allocated IDs that correspond to new metric names, source names, point tags, or span tags. A new ID generally indicates that a new time series has been introduced.

Try it Out button won't work in this case, as it's a streaming API.  Endpoint: https://<cluster>.wavefront.com/api/spy/ids.   Details usage can be find at: https://docs.wavefront.com/wavefront_monitoring_spy.html#get-new-id-assignments-with-spy

### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wavefront_api_client.IngestionSpyApi()
type = 'type_example' # str | Type of new items you want to see ID assignments for: METRIC - Metric names SPAN - Span names HOST - Source names STRING - Point tags or span tags, represented as a single string containing a unique key-value pair, e.g. env=prod, env=dev, etc. (optional)
body = 'body_example' # str | Case-sensitive prefix for the items that you are interested in. (optional)
sampling = 0.01 # float | goes from 0 to 1 with 0.01 being 1% (optional) (default to 0.01)

try:
    # Gets newly allocated IDs that correspond to new metric names, source names, point tags, or span tags. A new ID generally indicates that a new time series has been introduced.
    api_instance.spy_on_id_creations(type=type, body=body, sampling=sampling)
except ApiException as e:
    print("Exception when calling IngestionSpyApi->spy_on_id_creations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of new items you want to see ID assignments for: METRIC - Metric names SPAN - Span names HOST - Source names STRING - Point tags or span tags, represented as a single string containing a unique key-value pair, e.g. env&#x3D;prod, env&#x3D;dev, etc. | [optional] 
 **body** | **str**| Case-sensitive prefix for the items that you are interested in. | [optional] 
 **sampling** | **float**| goes from 0 to 1 with 0.01 being 1% | [optional] [default to 0.01]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spy_on_points**
> spy_on_points(metric=metric, host=host, point_tag_key=point_tag_key, sampling=sampling)

Gets a sampling of new metric data points that are added to existing time series.

Try it Out button won't work in this case, as it's a streaming API.  Endpoint: https://<cluster>.wavefront.com/api/spy/points.   Details usage can be find at: https://docs.wavefront.com/wavefront_monitoring_spy.html#get-ingested-metric-points-with-spy

### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wavefront_api_client.IngestionSpyApi()
metric = 'metric_example' # str | List a point only if its metric name starts with the specified case-sensitive prefix. E.g., metric=Cust matches metrics named Customer, Customers, Customer.alerts, but not customer. (optional)
host = 'host_example' # str | List a point only if its source name starts with the specified case-sensitive prefix. (optional)
point_tag_key = ['point_tag_key_example'] # list[str] | List a point only if it has the specified point tag key. Add this parameter multiple times to specify multiple point tags, e.g., pointTagKey=env&pointTagKey=datacenter  put env in the first line and datacenter in the second line as values (optional)
sampling = 0.01 # float | goes from 0 to 1 with 0.01 being 1% (optional) (default to 0.01)

try:
    # Gets a sampling of new metric data points that are added to existing time series.
    api_instance.spy_on_points(metric=metric, host=host, point_tag_key=point_tag_key, sampling=sampling)
except ApiException as e:
    print("Exception when calling IngestionSpyApi->spy_on_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric** | **str**| List a point only if its metric name starts with the specified case-sensitive prefix. E.g., metric&#x3D;Cust matches metrics named Customer, Customers, Customer.alerts, but not customer. | [optional] 
 **host** | **str**| List a point only if its source name starts with the specified case-sensitive prefix. | [optional] 
 **point_tag_key** | [**list[str]**](str.md)| List a point only if it has the specified point tag key. Add this parameter multiple times to specify multiple point tags, e.g., pointTagKey&#x3D;env&amp;pointTagKey&#x3D;datacenter  put env in the first line and datacenter in the second line as values | [optional] 
 **sampling** | **float**| goes from 0 to 1 with 0.01 being 1% | [optional] [default to 0.01]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spy_on_spans**
> spy_on_spans(name=name, host=host, span_tag_key=span_tag_key, sampling=sampling)

Gets new spans with existing source names and span tags.

Try it Out button won't work in this case, as it's a streaming API.   Endpoint: https://<cluster>.wavefront.com/api/spy/spans   Details usage can be find at: https://docs.wavefron.com/wavefront_monitoring_spy.html#get-ingested-spans-with-spy

### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = wavefront_api_client.IngestionSpyApi()
name = 'name_example' # str | List a span only if its operation name starts with the specified case-sensitive prefix. E.g., name=orderShirt matches spans named orderShirt and orderShirts, but not OrderShirts. (optional)
host = 'host_example' # str | List a span only if the name of its source starts with the specified case-sensitive prefix. (optional)
span_tag_key = ['span_tag_key_example'] # list[str] | List a span only if it has the specified span tag key. Add this parameter multiple times to specify multiple span tags, e.g. spanTagKey=cluster&spanTagKey=shard (optional)
sampling = 0.01 # float | goes from 0 to 1 with 0.01 being 1% (optional) (default to 0.01)

try:
    # Gets new spans with existing source names and span tags.
    api_instance.spy_on_spans(name=name, host=host, span_tag_key=span_tag_key, sampling=sampling)
except ApiException as e:
    print("Exception when calling IngestionSpyApi->spy_on_spans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| List a span only if its operation name starts with the specified case-sensitive prefix. E.g., name&#x3D;orderShirt matches spans named orderShirt and orderShirts, but not OrderShirts. | [optional] 
 **host** | **str**| List a span only if the name of its source starts with the specified case-sensitive prefix. | [optional] 
 **span_tag_key** | [**list[str]**](str.md)| List a span only if it has the specified span tag key. Add this parameter multiple times to specify multiple span tags, e.g. spanTagKey&#x3D;cluster&amp;spanTagKey&#x3D;shard | [optional] 
 **sampling** | **float**| goes from 0 to 1 with 0.01 being 1% | [optional] [default to 0.01]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

