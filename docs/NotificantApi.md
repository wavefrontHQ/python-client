# wavefront_api_client.NotificantApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notificant**](NotificantApi.md#create_notificant) | **POST** /api/v2/notificant | Create a notification target
[**delete_notificant**](NotificantApi.md#delete_notificant) | **DELETE** /api/v2/notificant/{id} | Delete a specific notification target
[**get_all_notificants**](NotificantApi.md#get_all_notificants) | **GET** /api/v2/notificant | Get all notification targets for a customer
[**get_notificant**](NotificantApi.md#get_notificant) | **GET** /api/v2/notificant/{id} | Get a specific notification target
[**test_notificant**](NotificantApi.md#test_notificant) | **POST** /api/v2/notificant/test/{id} | Test a specific notification target
[**update_notificant**](NotificantApi.md#update_notificant) | **PUT** /api/v2/notificant/{id} | Update a specific notification target


# **create_notificant**
> ResponseContainerNotificant create_notificant(body=body)

Create a notification target



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
api_instance = wavefront_api_client.NotificantApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.Notificant() # Notificant | Example Body:  <pre>{   \"description\": \"Notificant Description\",   \"template\": \"POST Body -- Mustache syntax\",   \"title\": \"Email title\",   \"triggers\": [     \"ALERT_OPENED\"   ],   \"method\": \"EMAIL\",   \"recipient\": \"value@example.com\",   \"emailSubject\": \"Email subject cannot contain new line\" }</pre> (optional)

try:
    # Create a notification target
    api_response = api_instance.create_notificant(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificantApi->create_notificant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Notificant**](Notificant.md)| Example Body:  &lt;pre&gt;{   \&quot;description\&quot;: \&quot;Notificant Description\&quot;,   \&quot;template\&quot;: \&quot;POST Body -- Mustache syntax\&quot;,   \&quot;title\&quot;: \&quot;Email title\&quot;,   \&quot;triggers\&quot;: [     \&quot;ALERT_OPENED\&quot;   ],   \&quot;method\&quot;: \&quot;EMAIL\&quot;,   \&quot;recipient\&quot;: \&quot;value@example.com\&quot;,   \&quot;emailSubject\&quot;: \&quot;Email subject cannot contain new line\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerNotificant**](ResponseContainerNotificant.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notificant**
> ResponseContainerNotificant delete_notificant(id)

Delete a specific notification target



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
api_instance = wavefront_api_client.NotificantApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a specific notification target
    api_response = api_instance.delete_notificant(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificantApi->delete_notificant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerNotificant**](ResponseContainerNotificant.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_notificants**
> ResponseContainerPagedNotificant get_all_notificants(offset=offset, limit=limit)

Get all notification targets for a customer



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
api_instance = wavefront_api_client.NotificantApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all notification targets for a customer
    api_response = api_instance.get_all_notificants(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificantApi->get_all_notificants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedNotificant**](ResponseContainerPagedNotificant.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notificant**
> ResponseContainerNotificant get_notificant(id)

Get a specific notification target



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
api_instance = wavefront_api_client.NotificantApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific notification target
    api_response = api_instance.get_notificant(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificantApi->get_notificant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerNotificant**](ResponseContainerNotificant.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_notificant**
> ResponseContainerNotificant test_notificant(id)

Test a specific notification target



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
api_instance = wavefront_api_client.NotificantApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Test a specific notification target
    api_response = api_instance.test_notificant(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificantApi->test_notificant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerNotificant**](ResponseContainerNotificant.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notificant**
> ResponseContainerNotificant update_notificant(id, body=body)

Update a specific notification target



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
api_instance = wavefront_api_client.NotificantApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.Notificant() # Notificant | Example Body:  <pre>{   \"description\": \"Notificant Description\",   \"template\": \"POST Body -- Mustache syntax\",   \"title\": \"Email title\",   \"triggers\": [     \"ALERT_OPENED\"   ],   \"method\": \"EMAIL\",   \"recipient\": \"value@example.com\",   \"emailSubject\": \"Email subject cannot contain new line\" }</pre> (optional)

try:
    # Update a specific notification target
    api_response = api_instance.update_notificant(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificantApi->update_notificant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Notificant**](Notificant.md)| Example Body:  &lt;pre&gt;{   \&quot;description\&quot;: \&quot;Notificant Description\&quot;,   \&quot;template\&quot;: \&quot;POST Body -- Mustache syntax\&quot;,   \&quot;title\&quot;: \&quot;Email title\&quot;,   \&quot;triggers\&quot;: [     \&quot;ALERT_OPENED\&quot;   ],   \&quot;method\&quot;: \&quot;EMAIL\&quot;,   \&quot;recipient\&quot;: \&quot;value@example.com\&quot;,   \&quot;emailSubject\&quot;: \&quot;Email subject cannot contain new line\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerNotificant**](ResponseContainerNotificant.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

