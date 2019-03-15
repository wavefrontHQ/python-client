# wavefront_api_client.DashboardApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_access**](DashboardApi.md#add_access) | **POST** /api/v2/dashboard/acl/add | Adds the specified ids to the given dashboards&#39; ACL
[**add_dashboard_tag**](DashboardApi.md#add_dashboard_tag) | **PUT** /api/v2/dashboard/{id}/tag/{tagValue} | Add a tag to a specific dashboard
[**create_dashboard**](DashboardApi.md#create_dashboard) | **POST** /api/v2/dashboard | Create a specific dashboard
[**delete_dashboard**](DashboardApi.md#delete_dashboard) | **DELETE** /api/v2/dashboard/{id} | Delete a specific dashboard
[**favorite_dashboard**](DashboardApi.md#favorite_dashboard) | **POST** /api/v2/dashboard/{id}/favorite | Mark a dashboard as favorite
[**get_access_control_list**](DashboardApi.md#get_access_control_list) | **GET** /api/v2/dashboard/acl | Get list of Access Control Lists for the specified dashboards
[**get_all_dashboard**](DashboardApi.md#get_all_dashboard) | **GET** /api/v2/dashboard | Get all dashboards for a customer
[**get_dashboard**](DashboardApi.md#get_dashboard) | **GET** /api/v2/dashboard/{id} | Get a specific dashboard
[**get_dashboard_history**](DashboardApi.md#get_dashboard_history) | **GET** /api/v2/dashboard/{id}/history | Get the version history of a specific dashboard
[**get_dashboard_tags**](DashboardApi.md#get_dashboard_tags) | **GET** /api/v2/dashboard/{id}/tag | Get all tags associated with a specific dashboard
[**get_dashboard_version**](DashboardApi.md#get_dashboard_version) | **GET** /api/v2/dashboard/{id}/history/{version} | Get a specific version of a specific dashboard
[**remove_access**](DashboardApi.md#remove_access) | **POST** /api/v2/dashboard/acl/remove | Removes the specified ids from the given dashboards&#39; ACL
[**remove_dashboard_tag**](DashboardApi.md#remove_dashboard_tag) | **DELETE** /api/v2/dashboard/{id}/tag/{tagValue} | Remove a tag from a specific dashboard
[**set_acl**](DashboardApi.md#set_acl) | **PUT** /api/v2/dashboard/acl/set | Set ACL for the specified dashboards
[**set_dashboard_tags**](DashboardApi.md#set_dashboard_tags) | **POST** /api/v2/dashboard/{id}/tag | Set all tags associated with a specific dashboard
[**undelete_dashboard**](DashboardApi.md#undelete_dashboard) | **POST** /api/v2/dashboard/{id}/undelete | Undelete a specific dashboard
[**unfavorite_dashboard**](DashboardApi.md#unfavorite_dashboard) | **POST** /api/v2/dashboard/{id}/unfavorite | Unmark a dashboard as favorite
[**update_dashboard**](DashboardApi.md#update_dashboard) | **PUT** /api/v2/dashboard/{id} | Update a specific dashboard


# **add_access**
> add_access(body=body)

Adds the specified ids to the given dashboards' ACL



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
api_instance = wavefront_api_client.DashboardApi(wavefront_api_client.ApiClient(configuration))
body = [wavefront_api_client.ACL()] # list[ACL] |  (optional)

try:
    # Adds the specified ids to the given dashboards' ACL
    api_instance.add_access(body=body)
except ApiException as e:
    print("Exception when calling DashboardApi->add_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ACL]**](ACL.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dashboard_tag**
> ResponseContainer add_dashboard_tag(id, tag_value)

Add a tag to a specific dashboard



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
api_instance = wavefront_api_client.DashboardApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
tag_value = 'tag_value_example' # str | 

try:
    # Add a tag to a specific dashboard
    api_response = api_instance.add_dashboard_tag(id, tag_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->add_dashboard_tag: %s\n" % e)
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

# **create_dashboard**
> ResponseContainerDashboard create_dashboard(body=body)

Create a specific dashboard



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
api_instance = wavefront_api_client.DashboardApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.Dashboard() # Dashboard | Example Body:  <pre>{   \"name\": \"Dashboard API example\",   \"id\": \"api-example\",   \"url\": \"api-example\",   \"description\": \"Dashboard Description\",   \"sections\": [     {       \"name\": \"Section 1\",       \"rows\": [         {           \"charts\": [             {               \"name\": \"Chart 1\",               \"description\": \"description1\",               \"sources\": [                 {                   \"name\": \"Source1\",                   \"query\": \"ts()\"                 }               ]             }           ]         }       ]     }   ] }</pre> (optional)

try:
    # Create a specific dashboard
    api_response = api_instance.create_dashboard(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->create_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dashboard**](Dashboard.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;Dashboard API example\&quot;,   \&quot;id\&quot;: \&quot;api-example\&quot;,   \&quot;url\&quot;: \&quot;api-example\&quot;,   \&quot;description\&quot;: \&quot;Dashboard Description\&quot;,   \&quot;sections\&quot;: [     {       \&quot;name\&quot;: \&quot;Section 1\&quot;,       \&quot;rows\&quot;: [         {           \&quot;charts\&quot;: [             {               \&quot;name\&quot;: \&quot;Chart 1\&quot;,               \&quot;description\&quot;: \&quot;description1\&quot;,               \&quot;sources\&quot;: [                 {                   \&quot;name\&quot;: \&quot;Source1\&quot;,                   \&quot;query\&quot;: \&quot;ts()\&quot;                 }               ]             }           ]         }       ]     }   ] }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerDashboard**](ResponseContainerDashboard.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard**
> ResponseContainerDashboard delete_dashboard(id)

Delete a specific dashboard



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
api_instance = wavefront_api_client.DashboardApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a specific dashboard
    api_response = api_instance.delete_dashboard(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->delete_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerDashboard**](ResponseContainerDashboard.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **favorite_dashboard**
> ResponseContainer favorite_dashboard(id)

Mark a dashboard as favorite



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
api_instance = wavefront_api_client.DashboardApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Mark a dashboard as favorite
    api_response = api_instance.favorite_dashboard(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->favorite_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainer**](ResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_control_list**
> ResponseContainerListACL get_access_control_list(id=id)

Get list of Access Control Lists for the specified dashboards



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
api_instance = wavefront_api_client.DashboardApi(wavefront_api_client.ApiClient(configuration))
id = ['id_example'] # list[str] |  (optional)

try:
    # Get list of Access Control Lists for the specified dashboards
    api_response = api_instance.get_access_control_list(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->get_access_control_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**ResponseContainerListACL**](ResponseContainerListACL.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_dashboard**
> ResponseContainerPagedDashboard get_all_dashboard(offset=offset, limit=limit)

Get all dashboards for a customer



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
api_instance = wavefront_api_client.DashboardApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all dashboards for a customer
    api_response = api_instance.get_all_dashboard(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->get_all_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedDashboard**](ResponseContainerPagedDashboard.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard**
> ResponseContainerDashboard get_dashboard(id)

Get a specific dashboard



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
api_instance = wavefront_api_client.DashboardApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific dashboard
    api_response = api_instance.get_dashboard(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->get_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerDashboard**](ResponseContainerDashboard.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_history**
> ResponseContainerHistoryResponse get_dashboard_history(id, offset=offset, limit=limit)

Get the version history of a specific dashboard



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
api_instance = wavefront_api_client.DashboardApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get the version history of a specific dashboard
    api_response = api_instance.get_dashboard_history(id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->get_dashboard_history: %s\n" % e)
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

# **get_dashboard_tags**
> ResponseContainerTagsResponse get_dashboard_tags(id)

Get all tags associated with a specific dashboard



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
api_instance = wavefront_api_client.DashboardApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get all tags associated with a specific dashboard
    api_response = api_instance.get_dashboard_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->get_dashboard_tags: %s\n" % e)
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

# **get_dashboard_version**
> ResponseContainerDashboard get_dashboard_version(id, version)

Get a specific version of a specific dashboard



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
api_instance = wavefront_api_client.DashboardApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
version = 789 # int | 

try:
    # Get a specific version of a specific dashboard
    api_response = api_instance.get_dashboard_version(id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->get_dashboard_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **version** | **int**|  | 

### Return type

[**ResponseContainerDashboard**](ResponseContainerDashboard.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_access**
> remove_access(body=body)

Removes the specified ids from the given dashboards' ACL



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
api_instance = wavefront_api_client.DashboardApi(wavefront_api_client.ApiClient(configuration))
body = [wavefront_api_client.ACL()] # list[ACL] |  (optional)

try:
    # Removes the specified ids from the given dashboards' ACL
    api_instance.remove_access(body=body)
except ApiException as e:
    print("Exception when calling DashboardApi->remove_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ACL]**](ACL.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_dashboard_tag**
> ResponseContainer remove_dashboard_tag(id, tag_value)

Remove a tag from a specific dashboard



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
api_instance = wavefront_api_client.DashboardApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
tag_value = 'tag_value_example' # str | 

try:
    # Remove a tag from a specific dashboard
    api_response = api_instance.remove_dashboard_tag(id, tag_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->remove_dashboard_tag: %s\n" % e)
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

# **set_acl**
> set_acl(body=body)

Set ACL for the specified dashboards



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
api_instance = wavefront_api_client.DashboardApi(wavefront_api_client.ApiClient(configuration))
body = [wavefront_api_client.ACL()] # list[ACL] |  (optional)

try:
    # Set ACL for the specified dashboards
    api_instance.set_acl(body=body)
except ApiException as e:
    print("Exception when calling DashboardApi->set_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ACL]**](ACL.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_dashboard_tags**
> ResponseContainer set_dashboard_tags(id, body=body)

Set all tags associated with a specific dashboard



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
api_instance = wavefront_api_client.DashboardApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = [wavefront_api_client.list[str]()] # list[str] |  (optional)

try:
    # Set all tags associated with a specific dashboard
    api_response = api_instance.set_dashboard_tags(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->set_dashboard_tags: %s\n" % e)
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

# **undelete_dashboard**
> ResponseContainerDashboard undelete_dashboard(id)

Undelete a specific dashboard



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
api_instance = wavefront_api_client.DashboardApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Undelete a specific dashboard
    api_response = api_instance.undelete_dashboard(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->undelete_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerDashboard**](ResponseContainerDashboard.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unfavorite_dashboard**
> ResponseContainer unfavorite_dashboard(id)

Unmark a dashboard as favorite



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
api_instance = wavefront_api_client.DashboardApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Unmark a dashboard as favorite
    api_response = api_instance.unfavorite_dashboard(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->unfavorite_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainer**](ResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard**
> ResponseContainerDashboard update_dashboard(id, body=body)

Update a specific dashboard



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
api_instance = wavefront_api_client.DashboardApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.Dashboard() # Dashboard | Example Body:  <pre>{   \"name\": \"Dashboard API example\",   \"id\": \"api-example\",   \"url\": \"api-example\",   \"description\": \"Dashboard Description\",   \"sections\": [     {       \"name\": \"Section 1\",       \"rows\": [         {           \"charts\": [             {               \"name\": \"Chart 1\",               \"description\": \"description1\",               \"sources\": [                 {                   \"name\": \"Source1\",                   \"query\": \"ts()\"                 }               ]             }           ]         }       ]     }   ] }</pre> (optional)

try:
    # Update a specific dashboard
    api_response = api_instance.update_dashboard(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->update_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Dashboard**](Dashboard.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;Dashboard API example\&quot;,   \&quot;id\&quot;: \&quot;api-example\&quot;,   \&quot;url\&quot;: \&quot;api-example\&quot;,   \&quot;description\&quot;: \&quot;Dashboard Description\&quot;,   \&quot;sections\&quot;: [     {       \&quot;name\&quot;: \&quot;Section 1\&quot;,       \&quot;rows\&quot;: [         {           \&quot;charts\&quot;: [             {               \&quot;name\&quot;: \&quot;Chart 1\&quot;,               \&quot;description\&quot;: \&quot;description1\&quot;,               \&quot;sources\&quot;: [                 {                   \&quot;name\&quot;: \&quot;Source1\&quot;,                   \&quot;query\&quot;: \&quot;ts()\&quot;                 }               ]             }           ]         }       ]     }   ] }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerDashboard**](ResponseContainerDashboard.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

