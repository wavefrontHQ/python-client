# wavefront_api_client.AnomalyApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_anomalies**](AnomalyApi.md#get_all_anomalies) | **GET** /api/v2/anomaly | Get all anomalies for a customer during a time interval
[**get_anomalies_for_chart_and_param_hash**](AnomalyApi.md#get_anomalies_for_chart_and_param_hash) | **GET** /api/v2/anomaly/{dashboardId}/chart/{chartHash}/{paramHash} | Get all anomalies for a chart with a set of dashboard parameters during a time interval
[**get_chart_anomalies**](AnomalyApi.md#get_chart_anomalies) | **GET** /api/v2/anomaly/{dashboardId} | Get all anomalies for a dashboard that does not have any dashboard parameters during a time interval
[**get_chart_anomalies_0**](AnomalyApi.md#get_chart_anomalies_0) | **GET** /api/v2/anomaly/{dashboardId}/chart/{chartHash} | Get all anomalies for a chart during a time interval
[**get_dashboard_anomalies**](AnomalyApi.md#get_dashboard_anomalies) | **GET** /api/v2/anomaly/{dashboardId}/{paramHash} | Get all anomalies for a dashboard with a particular set of dashboard parameters as identified by paramHash, during a time interval
[**get_related_anomalies**](AnomalyApi.md#get_related_anomalies) | **GET** /api/v2/anomaly/{eventId}/anomalies | Get all related anomalies for a firing event with a time span


# **get_all_anomalies**
> ResponseContainerPagedAnomaly get_all_anomalies(start_ms=start_ms, end_ms=end_ms, offset=offset, limit=limit)

Get all anomalies for a customer during a time interval



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
api_instance = wavefront_api_client.AnomalyApi(wavefront_api_client.ApiClient(configuration))
start_ms = 789 # int |  (optional)
end_ms = 789 # int |  (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 1000 # int |  (optional) (default to 1000)

try:
    # Get all anomalies for a customer during a time interval
    api_response = api_instance.get_all_anomalies(start_ms=start_ms, end_ms=end_ms, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnomalyApi->get_all_anomalies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_ms** | **int**|  | [optional] 
 **end_ms** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 1000]

### Return type

[**ResponseContainerPagedAnomaly**](ResponseContainerPagedAnomaly.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anomalies_for_chart_and_param_hash**
> ResponseContainerPagedAnomaly get_anomalies_for_chart_and_param_hash(dashboard_id, chart_hash, param_hash, start_ms=start_ms, end_ms=end_ms, offset=offset, limit=limit)

Get all anomalies for a chart with a set of dashboard parameters during a time interval



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
api_instance = wavefront_api_client.AnomalyApi(wavefront_api_client.ApiClient(configuration))
dashboard_id = 'dashboard_id_example' # str | 
chart_hash = 'chart_hash_example' # str | 
param_hash = 'param_hash_example' # str | 
start_ms = 789 # int |  (optional)
end_ms = 789 # int |  (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 1000 # int |  (optional) (default to 1000)

try:
    # Get all anomalies for a chart with a set of dashboard parameters during a time interval
    api_response = api_instance.get_anomalies_for_chart_and_param_hash(dashboard_id, chart_hash, param_hash, start_ms=start_ms, end_ms=end_ms, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnomalyApi->get_anomalies_for_chart_and_param_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**|  | 
 **chart_hash** | **str**|  | 
 **param_hash** | **str**|  | 
 **start_ms** | **int**|  | [optional] 
 **end_ms** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 1000]

### Return type

[**ResponseContainerPagedAnomaly**](ResponseContainerPagedAnomaly.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chart_anomalies**
> ResponseContainerPagedAnomaly get_chart_anomalies(dashboard_id, start_ms=start_ms, end_ms=end_ms, offset=offset, limit=limit)

Get all anomalies for a dashboard that does not have any dashboard parameters during a time interval



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
api_instance = wavefront_api_client.AnomalyApi(wavefront_api_client.ApiClient(configuration))
dashboard_id = 'dashboard_id_example' # str | 
start_ms = 789 # int |  (optional)
end_ms = 789 # int |  (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 1000 # int |  (optional) (default to 1000)

try:
    # Get all anomalies for a dashboard that does not have any dashboard parameters during a time interval
    api_response = api_instance.get_chart_anomalies(dashboard_id, start_ms=start_ms, end_ms=end_ms, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnomalyApi->get_chart_anomalies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**|  | 
 **start_ms** | **int**|  | [optional] 
 **end_ms** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 1000]

### Return type

[**ResponseContainerPagedAnomaly**](ResponseContainerPagedAnomaly.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chart_anomalies_0**
> ResponseContainerPagedAnomaly get_chart_anomalies_0(dashboard_id, chart_hash, start_ms=start_ms, end_ms=end_ms, offset=offset, limit=limit)

Get all anomalies for a chart during a time interval



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
api_instance = wavefront_api_client.AnomalyApi(wavefront_api_client.ApiClient(configuration))
dashboard_id = 'dashboard_id_example' # str | 
chart_hash = 'chart_hash_example' # str | 
start_ms = 789 # int |  (optional)
end_ms = 789 # int |  (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 1000 # int |  (optional) (default to 1000)

try:
    # Get all anomalies for a chart during a time interval
    api_response = api_instance.get_chart_anomalies_0(dashboard_id, chart_hash, start_ms=start_ms, end_ms=end_ms, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnomalyApi->get_chart_anomalies_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**|  | 
 **chart_hash** | **str**|  | 
 **start_ms** | **int**|  | [optional] 
 **end_ms** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 1000]

### Return type

[**ResponseContainerPagedAnomaly**](ResponseContainerPagedAnomaly.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_anomalies**
> ResponseContainerPagedAnomaly get_dashboard_anomalies(dashboard_id, param_hash, start_ms=start_ms, end_ms=end_ms, offset=offset, limit=limit)

Get all anomalies for a dashboard with a particular set of dashboard parameters as identified by paramHash, during a time interval



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
api_instance = wavefront_api_client.AnomalyApi(wavefront_api_client.ApiClient(configuration))
dashboard_id = 'dashboard_id_example' # str | 
param_hash = 'param_hash_example' # str | 
start_ms = 789 # int |  (optional)
end_ms = 789 # int |  (optional)
offset = 0 # int |  (optional) (default to 0)
limit = 1000 # int |  (optional) (default to 1000)

try:
    # Get all anomalies for a dashboard with a particular set of dashboard parameters as identified by paramHash, during a time interval
    api_response = api_instance.get_dashboard_anomalies(dashboard_id, param_hash, start_ms=start_ms, end_ms=end_ms, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnomalyApi->get_dashboard_anomalies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**|  | 
 **param_hash** | **str**|  | 
 **start_ms** | **int**|  | [optional] 
 **end_ms** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 1000]

### Return type

[**ResponseContainerPagedAnomaly**](ResponseContainerPagedAnomaly.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_related_anomalies**
> ResponseContainerPagedAnomaly get_related_anomalies(event_id, rendering_method=rendering_method, is_overlapped=is_overlapped, limit=limit)

Get all related anomalies for a firing event with a time span



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
api_instance = wavefront_api_client.AnomalyApi(wavefront_api_client.ApiClient(configuration))
event_id = 'event_id_example' # str | 
rendering_method = 'rendering_method_example' # str |  (optional)
is_overlapped = false # bool |  (optional) (default to false)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all related anomalies for a firing event with a time span
    api_response = api_instance.get_related_anomalies(event_id, rendering_method=rendering_method, is_overlapped=is_overlapped, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnomalyApi->get_related_anomalies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 
 **rendering_method** | **str**|  | [optional] 
 **is_overlapped** | **bool**|  | [optional] [default to false]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedAnomaly**](ResponseContainerPagedAnomaly.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

