# wavefront_client.MaintenanceWindowApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close**](MaintenanceWindowApi.md#close) | **POST** /api/alert/maintenancewindow/{id}/close | Close a currently active maintenance window
[**create_from_parts**](MaintenanceWindowApi.md#create_from_parts) | **POST** /api/alert/maintenancewindow/create | Create a new maintenance window
[**delete**](MaintenanceWindowApi.md#delete) | **DELETE** /api/alert/maintenancewindow/{id} | Delete a specific maintenance window
[**extend**](MaintenanceWindowApi.md#extend) | **POST** /api/alert/maintenancewindow/{id}/extend | Extend a currently active maintenance window by specified number of seconds
[**get_all**](MaintenanceWindowApi.md#get_all) | **GET** /api/alert/maintenancewindow/all | Get a list of every maintenance window
[**get_summary**](MaintenanceWindowApi.md#get_summary) | **GET** /api/alert/maintenancewindow/summary | Get a filtered list of maintenance windows
[**update_from_parts**](MaintenanceWindowApi.md#update_from_parts) | **POST** /api/alert/maintenancewindow/{id} | Update a maintenance window


# **close**
> close(id)

Close a currently active maintenance window



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
api_instance = wavefront_client.MaintenanceWindowApi()
id = 789 # int | Id of the maintenance window to close

try: 
    # Close a currently active maintenance window
    api_instance.close(id)
except ApiException as e:
    print "Exception when calling MaintenanceWindowApi->close: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the maintenance window to close | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_from_parts**
> MaintenanceWindow create_from_parts(title=title, start_time_seconds=start_time_seconds, end_time_seconds=end_time_seconds, reason=reason, alert_tags=alert_tags, host_names=host_names, host_tags=host_tags)

Create a new maintenance window



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
api_instance = wavefront_client.MaintenanceWindowApi()
title = 'title_example' # str | Title text (optional)
start_time_seconds = 789 # int | Time in seconds that this maintenance window should start (optional)
end_time_seconds = 789 # int | Time in seconds that this maintenance window should end (optional)
reason = 'reason_example' # str | Description of the purpose of this maintenance window (optional)
alert_tags = 'alert_tags_example' # str | Comma separated list of the shared alert tags that should match this maintenance window (optional)
host_names = 'host_names_example' # str | Comma separated list of the host names that should match this maintenance window (optional)
host_tags = 'host_tags_example' # str | Comma separated list of the host tags that should match this maintenance window (optional)

try: 
    # Create a new maintenance window
    api_response = api_instance.create_from_parts(title=title, start_time_seconds=start_time_seconds, end_time_seconds=end_time_seconds, reason=reason, alert_tags=alert_tags, host_names=host_names, host_tags=host_tags)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MaintenanceWindowApi->create_from_parts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| Title text | [optional] 
 **start_time_seconds** | **int**| Time in seconds that this maintenance window should start | [optional] 
 **end_time_seconds** | **int**| Time in seconds that this maintenance window should end | [optional] 
 **reason** | **str**| Description of the purpose of this maintenance window | [optional] 
 **alert_tags** | **str**| Comma separated list of the shared alert tags that should match this maintenance window | [optional] 
 **host_names** | **str**| Comma separated list of the host names that should match this maintenance window | [optional] 
 **host_tags** | **str**| Comma separated list of the host tags that should match this maintenance window | [optional] 

### Return type

[**MaintenanceWindow**](MaintenanceWindow.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(id)

Delete a specific maintenance window



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
api_instance = wavefront_client.MaintenanceWindowApi()
id = 789 # int | Id of the maintenance window to delete

try: 
    # Delete a specific maintenance window
    api_instance.delete(id)
except ApiException as e:
    print "Exception when calling MaintenanceWindowApi->delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the maintenance window to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extend**
> extend(id, seconds=seconds)

Extend a currently active maintenance window by specified number of seconds



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
api_instance = wavefront_client.MaintenanceWindowApi()
id = 789 # int | Id of the maintenance window to extend
seconds = 789 # int | Additional number of seconds that this maintenance window should stay open for (optional)

try: 
    # Extend a currently active maintenance window by specified number of seconds
    api_instance.extend(id, seconds=seconds)
except ApiException as e:
    print "Exception when calling MaintenanceWindowApi->extend: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the maintenance window to extend | 
 **seconds** | **int**| Additional number of seconds that this maintenance window should stay open for | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> list[MaintenanceWindow] get_all()

Get a list of every maintenance window



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
api_instance = wavefront_client.MaintenanceWindowApi()

try: 
    # Get a list of every maintenance window
    api_response = api_instance.get_all()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MaintenanceWindowApi->get_all: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MaintenanceWindow]**](MaintenanceWindow.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary**
> SummaryOfMaintenanceWindows get_summary()

Get a filtered list of maintenance windows



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
api_instance = wavefront_client.MaintenanceWindowApi()

try: 
    # Get a filtered list of maintenance windows
    api_response = api_instance.get_summary()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MaintenanceWindowApi->get_summary: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SummaryOfMaintenanceWindows**](SummaryOfMaintenanceWindows.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_from_parts**
> update_from_parts(id, title=title, start_time_seconds=start_time_seconds, end_time_seconds=end_time_seconds, reason=reason, alert_tags=alert_tags, host_names=host_names, host_tags=host_tags)

Update a maintenance window



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
api_instance = wavefront_client.MaintenanceWindowApi()
id = 789 # int | Id of the maintenance window to edit
title = 'title_example' # str | Title text (optional)
start_time_seconds = 789 # int | Time in seconds that this maintenance window should start (optional)
end_time_seconds = 789 # int | Time in seconds that this maintenance window should end (optional)
reason = 'reason_example' # str | Description of the purpose of this maintenance window (optional)
alert_tags = 'alert_tags_example' # str | Comma separated list of the shared alert tags that should match this maintenance window (optional)
host_names = 'host_names_example' # str | Comma separated list of the host names that should match this maintenance window (optional)
host_tags = 'host_tags_example' # str | Comma separated list of the host tags that should match this maintenance window (optional)

try: 
    # Update a maintenance window
    api_instance.update_from_parts(id, title=title, start_time_seconds=start_time_seconds, end_time_seconds=end_time_seconds, reason=reason, alert_tags=alert_tags, host_names=host_names, host_tags=host_tags)
except ApiException as e:
    print "Exception when calling MaintenanceWindowApi->update_from_parts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the maintenance window to edit | 
 **title** | **str**| Title text | [optional] 
 **start_time_seconds** | **int**| Time in seconds that this maintenance window should start | [optional] 
 **end_time_seconds** | **int**| Time in seconds that this maintenance window should end | [optional] 
 **reason** | **str**| Description of the purpose of this maintenance window | [optional] 
 **alert_tags** | **str**| Comma separated list of the shared alert tags that should match this maintenance window | [optional] 
 **host_names** | **str**| Comma separated list of the host names that should match this maintenance window | [optional] 
 **host_tags** | **str**| Comma separated list of the host tags that should match this maintenance window | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

