# wavefront_client.EventsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_ongoing_event**](EventsApi.md#close_ongoing_event) | **POST** /api/events/close | Close an event
[**create_new_event**](EventsApi.md#create_new_event) | **POST** /api/events | Create a new event
[**delete_event**](EventsApi.md#delete_event) | **DELETE** /api/events/{startTime}/{name} | Delete an event. Can only delete non-system events. System events include alert firings, error events, and maintenance windows


# **close_ongoing_event**
> ReportEvent close_ongoing_event(s, n, e=e)

Close an event

Method is idempotent. The closed event is returned.

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
api_instance = wavefront_client.EventsApi()
s = 789 # int | start time of the event to close in milliseconds
n = 'n_example' # str | name of the event to close
e = 789 # int | end time of the event to close (null will use current time) in milliseconds (optional)

try: 
    # Close an event
    api_response = api_instance.close_ongoing_event(s, n, e=e)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EventsApi->close_ongoing_event: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s** | **int**| start time of the event to close in milliseconds | 
 **n** | **str**| name of the event to close | 
 **e** | **int**| end time of the event to close (null will use current time) in milliseconds | [optional] 

### Return type

[**ReportEvent**](ReportEvent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_event**
> ReportEvent create_new_event(n, s=s, e=e, c=c, d=d, h=h, l=l, t=t)

Create a new event

The created event is returned.

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
api_instance = wavefront_client.EventsApi()
n = 'n_example' # str | name for the event
s = 789 # int | start time for the event in milliseconds (optional)
e = 789 # int | end time for the event in milliseconds (optional)
c = true # bool | flag for instantaneous event (optional)
d = 'd_example' # str | additional details for the event (optional)
h = ['h_example'] # list[str] | set of hosts affected by this event (optional)
l = 'l_example' # str | severity of the event (optional)
t = 't_example' # str | event type (optional)

try: 
    # Create a new event
    api_response = api_instance.create_new_event(n, s=s, e=e, c=c, d=d, h=h, l=l, t=t)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling EventsApi->create_new_event: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **n** | **str**| name for the event | 
 **s** | **int**| start time for the event in milliseconds | [optional] 
 **e** | **int**| end time for the event in milliseconds | [optional] 
 **c** | **bool**| flag for instantaneous event | [optional] 
 **d** | **str**| additional details for the event | [optional] 
 **h** | [**list[str]**](str.md)| set of hosts affected by this event | [optional] 
 **l** | **str**| severity of the event | [optional] 
 **t** | **str**| event type | [optional] 

### Return type

[**ReportEvent**](ReportEvent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event**
> delete_event(start_time, name)

Delete an event. Can only delete non-system events. System events include alert firings, error events, and maintenance windows



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
api_instance = wavefront_client.EventsApi()
start_time = 789 # int | start time of the event to delete in milliseconds
name = 'name_example' # str | name of the event

try: 
    # Delete an event. Can only delete non-system events. System events include alert firings, error events, and maintenance windows
    api_instance.delete_event(start_time, name)
except ApiException as e:
    print "Exception when calling EventsApi->delete_event: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| start time of the event to delete in milliseconds | 
 **name** | **str**| name of the event | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

