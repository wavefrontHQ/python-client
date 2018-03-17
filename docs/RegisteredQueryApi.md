# wavefront_api_client.RegisteredQueryApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_registered_query_tag**](RegisteredQueryApi.md#add_registered_query_tag) | **PUT** /api/v2/registeredquery/{id}/tag/{tagValue} | Add a tag to a specific registered query
[**create_registered_query**](RegisteredQueryApi.md#create_registered_query) | **POST** /api/v2/registeredquery | Create a specific registered query
[**delete_registered_query**](RegisteredQueryApi.md#delete_registered_query) | **DELETE** /api/v2/registeredquery/{id} | Delete a specific registered query
[**get_all_registered_queries**](RegisteredQueryApi.md#get_all_registered_queries) | **GET** /api/v2/registeredquery | Get all registered queries for a customer
[**get_registered_query**](RegisteredQueryApi.md#get_registered_query) | **GET** /api/v2/registeredquery/{id} | Get a specific registered query
[**get_registered_query_history**](RegisteredQueryApi.md#get_registered_query_history) | **GET** /api/v2/registeredquery/{id}/history | Get the version history of a specific registered query
[**get_registered_query_tags**](RegisteredQueryApi.md#get_registered_query_tags) | **GET** /api/v2/registeredquery/{id}/tag | Get all tags associated with a specific registered query
[**get_registered_query_version**](RegisteredQueryApi.md#get_registered_query_version) | **GET** /api/v2/registeredquery/{id}/history/{version} | Get a specific historical version of a specific registered query
[**remove_registered_query_tag**](RegisteredQueryApi.md#remove_registered_query_tag) | **DELETE** /api/v2/registeredquery/{id}/tag/{tagValue} | Remove a tag from a specific registered query
[**set_registered_query_tags**](RegisteredQueryApi.md#set_registered_query_tags) | **POST** /api/v2/registeredquery/{id}/tag | Set all tags associated with a specific registered query
[**undelete_registered_query**](RegisteredQueryApi.md#undelete_registered_query) | **POST** /api/v2/registeredquery/{id}/undelete | Undelete a specific registered query
[**update_registered_query**](RegisteredQueryApi.md#update_registered_query) | **PUT** /api/v2/registeredquery/{id} | Update a specific registered query


# **add_registered_query_tag**
> ResponseContainer add_registered_query_tag(id, tag_value)

Add a tag to a specific registered query



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
api_instance = wavefront_api_client.RegisteredQueryApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
tag_value = 'tag_value_example' # str | 

try:
    # Add a tag to a specific registered query
    api_response = api_instance.add_registered_query_tag(id, tag_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisteredQueryApi->add_registered_query_tag: %s\n" % e)
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

# **create_registered_query**
> ResponseContainerRegisteredQuery create_registered_query(body=body)

Create a specific registered query



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
api_instance = wavefront_api_client.RegisteredQueryApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.RegisteredQuery() # RegisteredQuery | Example Body:  <pre>{   \"name\": \"Query Name\",   \"query\": \"ts(~sample.cpu.loadavg.1m) > 1\",   \"minutes\": 5,   \"additionalInformation\": \"Additional Info\" }</pre> (optional)

try:
    # Create a specific registered query
    api_response = api_instance.create_registered_query(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisteredQueryApi->create_registered_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisteredQuery**](RegisteredQuery.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;Query Name\&quot;,   \&quot;query\&quot;: \&quot;ts(~sample.cpu.loadavg.1m) &gt; 1\&quot;,   \&quot;minutes\&quot;: 5,   \&quot;additionalInformation\&quot;: \&quot;Additional Info\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerRegisteredQuery**](ResponseContainerRegisteredQuery.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registered_query**
> ResponseContainerRegisteredQuery delete_registered_query(id)

Delete a specific registered query



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
api_instance = wavefront_api_client.RegisteredQueryApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a specific registered query
    api_response = api_instance.delete_registered_query(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisteredQueryApi->delete_registered_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerRegisteredQuery**](ResponseContainerRegisteredQuery.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_registered_queries**
> ResponseContainerPagedRegisteredQuery get_all_registered_queries(offset=offset, limit=limit)

Get all registered queries for a customer



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
api_instance = wavefront_api_client.RegisteredQueryApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all registered queries for a customer
    api_response = api_instance.get_all_registered_queries(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisteredQueryApi->get_all_registered_queries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedRegisteredQuery**](ResponseContainerPagedRegisteredQuery.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registered_query**
> ResponseContainerRegisteredQuery get_registered_query(id)

Get a specific registered query



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
api_instance = wavefront_api_client.RegisteredQueryApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific registered query
    api_response = api_instance.get_registered_query(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisteredQueryApi->get_registered_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerRegisteredQuery**](ResponseContainerRegisteredQuery.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registered_query_history**
> ResponseContainerHistoryResponse get_registered_query_history(id, offset=offset, limit=limit)

Get the version history of a specific registered query



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
api_instance = wavefront_api_client.RegisteredQueryApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get the version history of a specific registered query
    api_response = api_instance.get_registered_query_history(id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisteredQueryApi->get_registered_query_history: %s\n" % e)
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

# **get_registered_query_tags**
> ResponseContainerTagsResponse get_registered_query_tags(id)

Get all tags associated with a specific registered query



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
api_instance = wavefront_api_client.RegisteredQueryApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get all tags associated with a specific registered query
    api_response = api_instance.get_registered_query_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisteredQueryApi->get_registered_query_tags: %s\n" % e)
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

# **get_registered_query_version**
> ResponseContainerRegisteredQuery get_registered_query_version(id, version)

Get a specific historical version of a specific registered query



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
api_instance = wavefront_api_client.RegisteredQueryApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
version = 789 # int | 

try:
    # Get a specific historical version of a specific registered query
    api_response = api_instance.get_registered_query_version(id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisteredQueryApi->get_registered_query_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **version** | **int**|  | 

### Return type

[**ResponseContainerRegisteredQuery**](ResponseContainerRegisteredQuery.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_registered_query_tag**
> ResponseContainer remove_registered_query_tag(id, tag_value)

Remove a tag from a specific registered query



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
api_instance = wavefront_api_client.RegisteredQueryApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
tag_value = 'tag_value_example' # str | 

try:
    # Remove a tag from a specific registered query
    api_response = api_instance.remove_registered_query_tag(id, tag_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisteredQueryApi->remove_registered_query_tag: %s\n" % e)
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

# **set_registered_query_tags**
> ResponseContainer set_registered_query_tags(id, body=body)

Set all tags associated with a specific registered query



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
api_instance = wavefront_api_client.RegisteredQueryApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = [wavefront_api_client.list[str]()] # list[str] |  (optional)

try:
    # Set all tags associated with a specific registered query
    api_response = api_instance.set_registered_query_tags(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisteredQueryApi->set_registered_query_tags: %s\n" % e)
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

# **undelete_registered_query**
> ResponseContainerRegisteredQuery undelete_registered_query(id)

Undelete a specific registered query



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
api_instance = wavefront_api_client.RegisteredQueryApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Undelete a specific registered query
    api_response = api_instance.undelete_registered_query(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisteredQueryApi->undelete_registered_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerRegisteredQuery**](ResponseContainerRegisteredQuery.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_registered_query**
> ResponseContainerRegisteredQuery update_registered_query(id, body=body)

Update a specific registered query



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
api_instance = wavefront_api_client.RegisteredQueryApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.RegisteredQuery() # RegisteredQuery | Example Body:  <pre>{   \"id\": \"1459375928549\",   \"name\": \"Query Name\",   \"createUserId\": \"user\",   \"query\": \"ts(~sample.cpu.loadavg.1m) > 1\",   \"minutes\": 5,   \"additionalInformation\": \"Additional Info\" }</pre> (optional)

try:
    # Update a specific registered query
    api_response = api_instance.update_registered_query(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisteredQueryApi->update_registered_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**RegisteredQuery**](RegisteredQuery.md)| Example Body:  &lt;pre&gt;{   \&quot;id\&quot;: \&quot;1459375928549\&quot;,   \&quot;name\&quot;: \&quot;Query Name\&quot;,   \&quot;createUserId\&quot;: \&quot;user\&quot;,   \&quot;query\&quot;: \&quot;ts(~sample.cpu.loadavg.1m) &gt; 1\&quot;,   \&quot;minutes\&quot;: 5,   \&quot;additionalInformation\&quot;: \&quot;Additional Info\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerRegisteredQuery**](ResponseContainerRegisteredQuery.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

