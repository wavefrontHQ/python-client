# wavefront_api_client.MonitoredApplicationApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_applications**](MonitoredApplicationApi.md#get_all_applications) | **GET** /api/v2/monitoredapplication | Get all monitored applications
[**get_application**](MonitoredApplicationApi.md#get_application) | **GET** /api/v2/monitoredapplication/{application} | Get a specific application
[**update_service**](MonitoredApplicationApi.md#update_service) | **PUT** /api/v2/monitoredapplication/{application} | Update a specific service


# **get_all_applications**
> ResponseContainerPagedMonitoredApplicationDTO get_all_applications(offset=offset, limit=limit)

Get all monitored applications



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
api_instance = wavefront_api_client.MonitoredApplicationApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all monitored applications
    api_response = api_instance.get_all_applications(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredApplicationApi->get_all_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedMonitoredApplicationDTO**](ResponseContainerPagedMonitoredApplicationDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application**
> ResponseContainerMonitoredApplicationDTO get_application(application)

Get a specific application



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
api_instance = wavefront_api_client.MonitoredApplicationApi(wavefront_api_client.ApiClient(configuration))
application = 'application_example' # str | 

try:
    # Get a specific application
    api_response = api_instance.get_application(application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredApplicationApi->get_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**|  | 

### Return type

[**ResponseContainerMonitoredApplicationDTO**](ResponseContainerMonitoredApplicationDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service**
> ResponseContainerMonitoredApplicationDTO update_service(application, body=body)

Update a specific service



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
api_instance = wavefront_api_client.MonitoredApplicationApi(wavefront_api_client.ApiClient(configuration))
application = 'application_example' # str | 
body = wavefront_api_client.MonitoredApplicationDTO() # MonitoredApplicationDTO | Example Body:  <pre>{   \"application\": \"beachshirts\",   \"satisfiedLatencyMillis\": \"100000\",   \"hidden\": \"false\" }</pre> (optional)

try:
    # Update a specific service
    api_response = api_instance.update_service(application, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredApplicationApi->update_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**|  | 
 **body** | [**MonitoredApplicationDTO**](MonitoredApplicationDTO.md)| Example Body:  &lt;pre&gt;{   \&quot;application\&quot;: \&quot;beachshirts\&quot;,   \&quot;satisfiedLatencyMillis\&quot;: \&quot;100000\&quot;,   \&quot;hidden\&quot;: \&quot;false\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerMonitoredApplicationDTO**](ResponseContainerMonitoredApplicationDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

