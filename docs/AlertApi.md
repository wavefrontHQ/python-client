# wavefront_api_client.AlertApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_alert_tag**](AlertApi.md#add_alert_tag) | **PUT** /api/v2/alert/{id}/tag/{tagValue} | Add a tag to a specific alert
[**create_alert**](AlertApi.md#create_alert) | **POST** /api/v2/alert | Create a specific alert
[**delete_alert**](AlertApi.md#delete_alert) | **DELETE** /api/v2/alert/{id} | Delete a specific alert
[**get_alert**](AlertApi.md#get_alert) | **GET** /api/v2/alert/{id} | Get a specific alert
[**get_alert_history**](AlertApi.md#get_alert_history) | **GET** /api/v2/alert/{id}/history | Get the version history of a specific alert
[**get_alert_tags**](AlertApi.md#get_alert_tags) | **GET** /api/v2/alert/{id}/tag | Get all tags associated with a specific alert
[**get_alert_version**](AlertApi.md#get_alert_version) | **GET** /api/v2/alert/{id}/history/{version} | Get a specific historical version of a specific alert
[**get_alerts_summary**](AlertApi.md#get_alerts_summary) | **GET** /api/v2/alert/summary | Count alerts of various statuses for a customer
[**get_all_alert**](AlertApi.md#get_all_alert) | **GET** /api/v2/alert | Get all alerts for a customer
[**remove_alert_tag**](AlertApi.md#remove_alert_tag) | **DELETE** /api/v2/alert/{id}/tag/{tagValue} | Remove a tag from a specific alert
[**set_alert_tags**](AlertApi.md#set_alert_tags) | **POST** /api/v2/alert/{id}/tag | Set all tags associated with a specific alert
[**snooze_alert**](AlertApi.md#snooze_alert) | **POST** /api/v2/alert/{id}/snooze | Snooze a specific alert for some number of seconds
[**undelete_alert**](AlertApi.md#undelete_alert) | **POST** /api/v2/alert/{id}/undelete | Undelete a specific alert
[**unsnooze_alert**](AlertApi.md#unsnooze_alert) | **POST** /api/v2/alert/{id}/unsnooze | Unsnooze a specific alert
[**update_alert**](AlertApi.md#update_alert) | **PUT** /api/v2/alert/{id} | Update a specific alert


# **add_alert_tag**
> ResponseContainer add_alert_tag(id, tag_value)

Add a tag to a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
tag_value = 'tag_value_example' # str | 

try:
    # Add a tag to a specific alert
    api_response = api_instance.add_alert_tag(id, tag_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->add_alert_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tag_value** | **str**|  | 

### Return type

[**ResponseContainer**](ResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_alert**
> ResponseContainerAlert create_alert(body=body)

Create a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.Alert() # Alert | Example Body:  <pre>{   \"name\": \"Alert Name\",   \"target\": \"user@example.com\",   \"condition\": \"ts(~sample.cpu.loadavg.1m) > 1\",   \"displayExpression\": \"ts(~sample.cpu.loadavg.1m)\",   \"minutes\": 5,   \"resolveAfterMinutes\": 2,   \"severity\": \"INFO\",   \"additionalInformation\": \"Additional Info\" }</pre> (optional)

try:
    # Create a specific alert
    api_response = api_instance.create_alert(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->create_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Alert**](Alert.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;Alert Name\&quot;,   \&quot;target\&quot;: \&quot;user@example.com\&quot;,   \&quot;condition\&quot;: \&quot;ts(~sample.cpu.loadavg.1m) &gt; 1\&quot;,   \&quot;displayExpression\&quot;: \&quot;ts(~sample.cpu.loadavg.1m)\&quot;,   \&quot;minutes\&quot;: 5,   \&quot;resolveAfterMinutes\&quot;: 2,   \&quot;severity\&quot;: \&quot;INFO\&quot;,   \&quot;additionalInformation\&quot;: \&quot;Additional Info\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert**
> ResponseContainerAlert delete_alert(id)

Delete a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a specific alert
    api_response = api_instance.delete_alert(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->delete_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert**
> ResponseContainerAlert get_alert(id)

Get a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific alert
    api_response = api_instance.get_alert(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_history**
> ResponseContainerHistoryResponse get_alert_history(id, offset=offset, limit=limit)

Get the version history of a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get the version history of a specific alert
    api_response = api_instance.get_alert_history(id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_alert_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerHistoryResponse**](ResponseContainerHistoryResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_tags**
> ResponseContainerTagsResponse get_alert_tags(id)

Get all tags associated with a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get all tags associated with a specific alert
    api_response = api_instance.get_alert_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_alert_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerTagsResponse**](ResponseContainerTagsResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_version**
> ResponseContainerAlert get_alert_version(id, version)

Get a specific historical version of a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
version = 789 # int | 

try:
    # Get a specific historical version of a specific alert
    api_response = api_instance.get_alert_version(id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_alert_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **version** | **int**|  | 

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts_summary**
> ResponseContainerMapStringInteger get_alerts_summary()

Count alerts of various statuses for a customer



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))

try:
    # Count alerts of various statuses for a customer
    api_response = api_instance.get_alerts_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_alerts_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseContainerMapStringInteger**](ResponseContainerMapStringInteger.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_alert**
> ResponseContainerPagedAlert get_all_alert(offset=offset, limit=limit)

Get all alerts for a customer



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all alerts for a customer
    api_response = api_instance.get_all_alert(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_all_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedAlert**](ResponseContainerPagedAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_alert_tag**
> ResponseContainer remove_alert_tag(id, tag_value)

Remove a tag from a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
tag_value = 'tag_value_example' # str | 

try:
    # Remove a tag from a specific alert
    api_response = api_instance.remove_alert_tag(id, tag_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->remove_alert_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tag_value** | **str**|  | 

### Return type

[**ResponseContainer**](ResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_alert_tags**
> ResponseContainer set_alert_tags(id, body=body)

Set all tags associated with a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = [wavefront_api_client.list[str]()] # list[str] |  (optional)

try:
    # Set all tags associated with a specific alert
    api_response = api_instance.set_alert_tags(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->set_alert_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **list[str]**|  | [optional] 

### Return type

[**ResponseContainer**](ResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snooze_alert**
> ResponseContainerAlert snooze_alert(id, seconds=seconds)

Snooze a specific alert for some number of seconds



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
seconds = 789 # int |  (optional)

try:
    # Snooze a specific alert for some number of seconds
    api_response = api_instance.snooze_alert(id, seconds=seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->snooze_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **seconds** | **int**|  | [optional] 

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undelete_alert**
> ResponseContainerAlert undelete_alert(id)

Undelete a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Undelete a specific alert
    api_response = api_instance.undelete_alert(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->undelete_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsnooze_alert**
> ResponseContainerAlert unsnooze_alert(id)

Unsnooze a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Unsnooze a specific alert
    api_response = api_instance.unsnooze_alert(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->unsnooze_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert**
> ResponseContainerAlert update_alert(id, body=body)

Update a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.Alert() # Alert | Example Body:  <pre>{   \"id\": \"1459375928549\",   \"name\": \"Alert Name\",   \"target\": \"user@example.com\",   \"condition\": \"ts(~sample.cpu.loadavg.1m) > 1\",   \"displayExpression\": \"ts(~sample.cpu.loadavg.1m)\",   \"minutes\": 5,   \"resolveAfterMinutes\": 2,   \"severity\": \"INFO\",   \"additionalInformation\": \"Additional Info\" }</pre> (optional)

try:
    # Update a specific alert
    api_response = api_instance.update_alert(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->update_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Alert**](Alert.md)| Example Body:  &lt;pre&gt;{   \&quot;id\&quot;: \&quot;1459375928549\&quot;,   \&quot;name\&quot;: \&quot;Alert Name\&quot;,   \&quot;target\&quot;: \&quot;user@example.com\&quot;,   \&quot;condition\&quot;: \&quot;ts(~sample.cpu.loadavg.1m) &gt; 1\&quot;,   \&quot;displayExpression\&quot;: \&quot;ts(~sample.cpu.loadavg.1m)\&quot;,   \&quot;minutes\&quot;: 5,   \&quot;resolveAfterMinutes\&quot;: 2,   \&quot;severity\&quot;: \&quot;INFO\&quot;,   \&quot;additionalInformation\&quot;: \&quot;Additional Info\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

