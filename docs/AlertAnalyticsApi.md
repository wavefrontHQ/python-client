# wavefront_api_client.AlertAnalyticsApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_global_alert_analytics**](AlertAnalyticsApi.md#get_global_alert_analytics) | **GET** /api/v2/alert/analytics/global | Get Global Alert Analytics for a customer


# **get_global_alert_analytics**
> ResponseContainerGlobalAlertAnalytic get_global_alert_analytics(start, end=end)

Get Global Alert Analytics for a customer



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
end = 789 # int | End time in epoch seconds (optional)

try:
    # Get Global Alert Analytics for a customer
    api_response = api_instance.get_global_alert_analytics(start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertAnalyticsApi->get_global_alert_analytics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Start time in epoch seconds | 
 **end** | **int**| End time in epoch seconds | [optional] 

### Return type

[**ResponseContainerGlobalAlertAnalytic**](ResponseContainerGlobalAlertAnalytic.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

