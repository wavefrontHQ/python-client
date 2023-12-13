# wavefront_api_client.AlertAnalyticsApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_no_target_alert_summary_details**](AlertAnalyticsApi.md#get_active_no_target_alert_summary_details) | **GET** /api/v2/alert/analytics/summary/alerts/noTarget | Get Active No Target Alert Summary for a customer
[**get_alert_analytics_errors_summary**](AlertAnalyticsApi.md#get_alert_analytics_errors_summary) | **GET** /api/v2/alert/analytics/summary/errors | Get Alert Analytics errors summary
[**get_alert_analytics_summary**](AlertAnalyticsApi.md#get_alert_analytics_summary) | **GET** /api/v2/alert/analytics/summary | Get Alert Analytics Summary for a customer
[**get_failed_alert_summary_details**](AlertAnalyticsApi.md#get_failed_alert_summary_details) | **GET** /api/v2/alert/analytics/summary/alerts/failed | Get Failed Alert Summary Details for a customer
[**get_no_data_alert_summary_details**](AlertAnalyticsApi.md#get_no_data_alert_summary_details) | **GET** /api/v2/alert/analytics/summary/alerts/noData | Get No Data Alert Summary for a customer


# **get_active_no_target_alert_summary_details**
> ResponseContainerPagedAlertAnalyticsSummaryDetail get_active_no_target_alert_summary_details(start, end=end, offset=offset, limit=limit)

Get Active No Target Alert Summary for a customer



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
api_instance = wavefront_api_client.AlertAnalyticsApi(wavefront_api_client.ApiClient(configuration))
start = 789 # int | Start time in epoch seconds
end = 789 # int | End time in epoch seconds, null to use now (optional)
offset = 0 # int | offset for records (optional) (default to 0)
limit = 50 # int | Number of records (optional) (default to 50)

try:
    # Get Active No Target Alert Summary for a customer
    api_response = api_instance.get_active_no_target_alert_summary_details(start, end=end, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertAnalyticsApi->get_active_no_target_alert_summary_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Start time in epoch seconds | 
 **end** | **int**| End time in epoch seconds, null to use now | [optional] 
 **offset** | **int**| offset for records | [optional] [default to 0]
 **limit** | **int**| Number of records | [optional] [default to 50]

### Return type

[**ResponseContainerPagedAlertAnalyticsSummaryDetail**](ResponseContainerPagedAlertAnalyticsSummaryDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_analytics_errors_summary**
> ResponseContainerListAlertErrorGroupInfo get_alert_analytics_errors_summary(start, end=end)

Get Alert Analytics errors summary



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
api_instance = wavefront_api_client.AlertAnalyticsApi(wavefront_api_client.ApiClient(configuration))
start = 789 # int | Start time in epoch seconds
end = 789 # int | End time in epoch seconds, null to use now (optional)

try:
    # Get Alert Analytics errors summary
    api_response = api_instance.get_alert_analytics_errors_summary(start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertAnalyticsApi->get_alert_analytics_errors_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Start time in epoch seconds | 
 **end** | **int**| End time in epoch seconds, null to use now | [optional] 

### Return type

[**ResponseContainerListAlertErrorGroupInfo**](ResponseContainerListAlertErrorGroupInfo.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_analytics_summary**
> ResponseContainerAlertAnalyticsSummary get_alert_analytics_summary(start, end=end)

Get Alert Analytics Summary for a customer



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
api_instance = wavefront_api_client.AlertAnalyticsApi(wavefront_api_client.ApiClient(configuration))
start = 789 # int | Start time in epoch seconds
end = 789 # int | End time in epoch seconds, null to use now (optional)

try:
    # Get Alert Analytics Summary for a customer
    api_response = api_instance.get_alert_analytics_summary(start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertAnalyticsApi->get_alert_analytics_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Start time in epoch seconds | 
 **end** | **int**| End time in epoch seconds, null to use now | [optional] 

### Return type

[**ResponseContainerAlertAnalyticsSummary**](ResponseContainerAlertAnalyticsSummary.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_failed_alert_summary_details**
> ResponseContainerPagedAlertAnalyticsSummaryDetail get_failed_alert_summary_details(start, end=end, offset=offset, limit=limit)

Get Failed Alert Summary Details for a customer



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
api_instance = wavefront_api_client.AlertAnalyticsApi(wavefront_api_client.ApiClient(configuration))
start = 789 # int | Start time in epoch seconds
end = 789 # int | End time in epoch seconds, null to use now (optional)
offset = 0 # int | offset for records (optional) (default to 0)
limit = 50 # int | Number of records (optional) (default to 50)

try:
    # Get Failed Alert Summary Details for a customer
    api_response = api_instance.get_failed_alert_summary_details(start, end=end, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertAnalyticsApi->get_failed_alert_summary_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Start time in epoch seconds | 
 **end** | **int**| End time in epoch seconds, null to use now | [optional] 
 **offset** | **int**| offset for records | [optional] [default to 0]
 **limit** | **int**| Number of records | [optional] [default to 50]

### Return type

[**ResponseContainerPagedAlertAnalyticsSummaryDetail**](ResponseContainerPagedAlertAnalyticsSummaryDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_no_data_alert_summary_details**
> ResponseContainerPagedAlertAnalyticsSummaryDetail get_no_data_alert_summary_details(start, end=end, offset=offset, limit=limit)

Get No Data Alert Summary for a customer



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
api_instance = wavefront_api_client.AlertAnalyticsApi(wavefront_api_client.ApiClient(configuration))
start = 789 # int | Start time in epoch seconds
end = 789 # int | End time in epoch seconds, null to use now (optional)
offset = 0 # int | offset for records (optional) (default to 0)
limit = 50 # int | Number of records (optional) (default to 50)

try:
    # Get No Data Alert Summary for a customer
    api_response = api_instance.get_no_data_alert_summary_details(start, end=end, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertAnalyticsApi->get_no_data_alert_summary_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Start time in epoch seconds | 
 **end** | **int**| End time in epoch seconds, null to use now | [optional] 
 **offset** | **int**| offset for records | [optional] [default to 0]
 **limit** | **int**| Number of records | [optional] [default to 50]

### Return type

[**ResponseContainerPagedAlertAnalyticsSummaryDetail**](ResponseContainerPagedAlertAnalyticsSummaryDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

