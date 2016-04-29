# wavefront_client.DashboardApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_dashboard**](DashboardApi.md#clone_dashboard) | **POST** /api/dashboard/{id}/clone | Clones a dashboard
[**create_dashboard**](DashboardApi.md#create_dashboard) | **POST** /api/dashboard/{id}/create | Creates an empty dashboard
[**dashboard_history**](DashboardApi.md#dashboard_history) | **GET** /api/dashboard/{id}/history | Returns version history about a dashboard
[**dashboards**](DashboardApi.md#dashboards) | **GET** /api/dashboard | Lists dashboards
[**delete_dashboard**](DashboardApi.md#delete_dashboard) | **POST** /api/dashboard/{id}/delete | Deletes the dashboard at {id}
[**get_dashboard**](DashboardApi.md#get_dashboard) | **GET** /api/dashboard/{id} | Returns data about a dashboard, the latest version
[**get_dashboard_version**](DashboardApi.md#get_dashboard_version) | **GET** /api/dashboard/{id}/{version} | Returns data about a dashboard, a specific version
[**save_dashboard**](DashboardApi.md#save_dashboard) | **POST** /api/dashboard | Saves or creates a JSON-specified dashboard.
[**undelete_dashboard**](DashboardApi.md#undelete_dashboard) | **POST** /api/dashboard/{id}/undelete | Undeletes the dashboard at {id}


# **clone_dashboard**
> clone_dashboard(id, name, url, v=v)

Clones a dashboard



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
api_instance = wavefront_client.DashboardApi()
id = 'id_example' # str | id (URL) of dashboard to clone
name = 'name_example' # str | Name of cloned dashboard
url = 'url_example' # str | id (URL) of cloned dashboard
v = 789 # int | Version of the dashboard to clone, null for latest (optional)

try: 
    # Clones a dashboard
    api_instance.clone_dashboard(id, name, url, v=v)
except ApiException as e:
    print "Exception when calling DashboardApi->clone_dashboard: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id (URL) of dashboard to clone | 
 **name** | **str**| Name of cloned dashboard | 
 **url** | **str**| id (URL) of cloned dashboard | 
 **v** | **int**| Version of the dashboard to clone, null for latest | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dashboard**
> create_dashboard(id, name)

Creates an empty dashboard



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
api_instance = wavefront_client.DashboardApi()
id = 'id_example' # str | id (URL) of the dashboard
name = 'name_example' # str | name of the dashboard

try: 
    # Creates an empty dashboard
    api_instance.create_dashboard(id, name)
except ApiException as e:
    print "Exception when calling DashboardApi->create_dashboard: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id (URL) of the dashboard | 
 **name** | **str**| name of the dashboard | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_history**
> DashboardHistory dashboard_history(id, start, limit=limit)

Returns version history about a dashboard



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
api_instance = wavefront_client.DashboardApi()
id = 'id_example' # str | id (URL) of the dashboard
start = 100 # int | highest version number from which to descend (default to 100)
limit = 100 # int |  (optional) (default to 100)

try: 
    # Returns version history about a dashboard
    api_response = api_instance.dashboard_history(id, start, limit=limit)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DashboardApi->dashboard_history: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id (URL) of the dashboard | 
 **start** | **int**| highest version number from which to descend | [default to 100]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**DashboardHistory**](DashboardHistory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards**
> list[DashboardMetadata] dashboards(customer_tag=customer_tag, user_tag=user_tag)

Lists dashboards

Return summary data for each dashboard.  Use the individual endpoint for full data.

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
api_instance = wavefront_client.DashboardApi()
customer_tag = ['customer_tag_example'] # list[str] | Restrict result to alerts with this shared tag (optional)
user_tag = ['user_tag_example'] # list[str] | Restrict result to alerts with this private tag (optional)

try: 
    # Lists dashboards
    api_response = api_instance.dashboards(customer_tag=customer_tag, user_tag=user_tag)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DashboardApi->dashboards: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_tag** | [**list[str]**](str.md)| Restrict result to alerts with this shared tag | [optional] 
 **user_tag** | [**list[str]**](str.md)| Restrict result to alerts with this private tag | [optional] 

### Return type

[**list[DashboardMetadata]**](DashboardMetadata.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard**
> delete_dashboard(id)

Deletes the dashboard at {id}



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
api_instance = wavefront_client.DashboardApi()
id = 'id_example' # str | id (URL) of the dashboard

try: 
    # Deletes the dashboard at {id}
    api_instance.delete_dashboard(id)
except ApiException as e:
    print "Exception when calling DashboardApi->delete_dashboard: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id (URL) of the dashboard | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard**
> Dashboard get_dashboard(id)

Returns data about a dashboard, the latest version



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
api_instance = wavefront_client.DashboardApi()
id = 'id_example' # str | id (URL) of the dashboard

try: 
    # Returns data about a dashboard, the latest version
    api_response = api_instance.get_dashboard(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DashboardApi->get_dashboard: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id (URL) of the dashboard | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_version**
> Dashboard get_dashboard_version(id, version)

Returns data about a dashboard, a specific version



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
api_instance = wavefront_client.DashboardApi()
id = 'id_example' # str | id (URL) of the dashboard
version = 789 # int | 

try: 
    # Returns data about a dashboard, a specific version
    api_response = api_instance.get_dashboard_version(id, version)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DashboardApi->get_dashboard_version: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id (URL) of the dashboard | 
 **version** | **int**|  | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_dashboard**
> save_dashboard(body, reject_if_exists=reject_if_exists)

Saves or creates a JSON-specified dashboard.



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
api_instance = wavefront_client.DashboardApi()
body = wavefront_client.Dashboard() # Dashboard | JSON representation of the dashboard
reject_if_exists = true # bool | Disallow overwrite of an existing dashboard at the same url. Default false (allows overwrites) (optional)

try: 
    # Saves or creates a JSON-specified dashboard.
    api_instance.save_dashboard(body, reject_if_exists=reject_if_exists)
except ApiException as e:
    print "Exception when calling DashboardApi->save_dashboard: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dashboard**](Dashboard.md)| JSON representation of the dashboard | 
 **reject_if_exists** | **bool**| Disallow overwrite of an existing dashboard at the same url. Default false (allows overwrites) | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undelete_dashboard**
> undelete_dashboard(id)

Undeletes the dashboard at {id}



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
api_instance = wavefront_client.DashboardApi()
id = 'id_example' # str | id (URL) of the dashboard

try: 
    # Undeletes the dashboard at {id}
    api_instance.undelete_dashboard(id)
except ApiException as e:
    print "Exception when calling DashboardApi->undelete_dashboard: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id (URL) of the dashboard | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

