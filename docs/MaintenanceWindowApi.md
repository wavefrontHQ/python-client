# wavefront_api_client.MaintenanceWindowApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_maintenance_window**](MaintenanceWindowApi.md#create_maintenance_window) | **POST** /api/v2/maintenancewindow | Create a maintenance window
[**delete_maintenance_window**](MaintenanceWindowApi.md#delete_maintenance_window) | **DELETE** /api/v2/maintenancewindow/{id} | Delete a specific maintenance window
[**get_all_maintenance_window**](MaintenanceWindowApi.md#get_all_maintenance_window) | **GET** /api/v2/maintenancewindow | Get all maintenance windows for a customer
[**get_maintenance_window**](MaintenanceWindowApi.md#get_maintenance_window) | **GET** /api/v2/maintenancewindow/{id} | Get a specific maintenance window
[**update_maintenance_window**](MaintenanceWindowApi.md#update_maintenance_window) | **PUT** /api/v2/maintenancewindow/{id} | Update a specific maintenance window


# **create_maintenance_window**
> ResponseContainerMaintenanceWindow create_maintenance_window(body=body)

Create a maintenance window



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
api_instance = wavefront_api_client.MaintenanceWindowApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.MaintenanceWindow() # MaintenanceWindow | Example Body:  <pre>{   \"reason\": \"MW Reason\",   \"title\": \"MW Title\",   \"startTimeInSeconds\": 1483228800,   \"endTimeInSeconds\": 1483232400,   \"relevantCustomerTags\": [     \"alertId1\"   ],   \"relevantHostTags\": [     \"sourceTag1\"   ] }</pre> (optional)

try:
    # Create a maintenance window
    api_response = api_instance.create_maintenance_window(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceWindowApi->create_maintenance_window: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MaintenanceWindow**](MaintenanceWindow.md)| Example Body:  &lt;pre&gt;{   \&quot;reason\&quot;: \&quot;MW Reason\&quot;,   \&quot;title\&quot;: \&quot;MW Title\&quot;,   \&quot;startTimeInSeconds\&quot;: 1483228800,   \&quot;endTimeInSeconds\&quot;: 1483232400,   \&quot;relevantCustomerTags\&quot;: [     \&quot;alertId1\&quot;   ],   \&quot;relevantHostTags\&quot;: [     \&quot;sourceTag1\&quot;   ] }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerMaintenanceWindow**](ResponseContainerMaintenanceWindow.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_maintenance_window**
> ResponseContainerMaintenanceWindow delete_maintenance_window(id)

Delete a specific maintenance window



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
api_instance = wavefront_api_client.MaintenanceWindowApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a specific maintenance window
    api_response = api_instance.delete_maintenance_window(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceWindowApi->delete_maintenance_window: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerMaintenanceWindow**](ResponseContainerMaintenanceWindow.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_maintenance_window**
> ResponseContainerPagedMaintenanceWindow get_all_maintenance_window(offset=offset, limit=limit)

Get all maintenance windows for a customer



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
api_instance = wavefront_api_client.MaintenanceWindowApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all maintenance windows for a customer
    api_response = api_instance.get_all_maintenance_window(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceWindowApi->get_all_maintenance_window: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedMaintenanceWindow**](ResponseContainerPagedMaintenanceWindow.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_maintenance_window**
> ResponseContainerMaintenanceWindow get_maintenance_window(id)

Get a specific maintenance window



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
api_instance = wavefront_api_client.MaintenanceWindowApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific maintenance window
    api_response = api_instance.get_maintenance_window(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceWindowApi->get_maintenance_window: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerMaintenanceWindow**](ResponseContainerMaintenanceWindow.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_maintenance_window**
> ResponseContainerMaintenanceWindow update_maintenance_window(id, body=body)

Update a specific maintenance window



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
api_instance = wavefront_api_client.MaintenanceWindowApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.MaintenanceWindow() # MaintenanceWindow | Example Body:  <pre>{   \"reason\": \"MW Reason\",   \"title\": \"MW Title\",   \"startTimeInSeconds\": 1483228800,   \"endTimeInSeconds\": 1483232400,   \"relevantCustomerTags\": [     \"alertId1\"   ],   \"relevantHostTags\": [     \"sourceTag1\"   ] }</pre> (optional)

try:
    # Update a specific maintenance window
    api_response = api_instance.update_maintenance_window(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceWindowApi->update_maintenance_window: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**MaintenanceWindow**](MaintenanceWindow.md)| Example Body:  &lt;pre&gt;{   \&quot;reason\&quot;: \&quot;MW Reason\&quot;,   \&quot;title\&quot;: \&quot;MW Title\&quot;,   \&quot;startTimeInSeconds\&quot;: 1483228800,   \&quot;endTimeInSeconds\&quot;: 1483232400,   \&quot;relevantCustomerTags\&quot;: [     \&quot;alertId1\&quot;   ],   \&quot;relevantHostTags\&quot;: [     \&quot;sourceTag1\&quot;   ] }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerMaintenanceWindow**](ResponseContainerMaintenanceWindow.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

