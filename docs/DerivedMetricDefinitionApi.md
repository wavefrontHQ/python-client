# wavefront_api_client.DerivedMetricDefinitionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tag_to_derived_metric_definition**](DerivedMetricDefinitionApi.md#add_tag_to_derived_metric_definition) | **PUT** /api/v2/derivedmetricdefinition/{id}/tag/{tagValue} | Add a tag to a specific Derived Metric Definition
[**create_derived_metric_definition**](DerivedMetricDefinitionApi.md#create_derived_metric_definition) | **POST** /api/v2/derivedmetricdefinition | Create a specific derived metric definition
[**delete_derived_metric_definition**](DerivedMetricDefinitionApi.md#delete_derived_metric_definition) | **DELETE** /api/v2/derivedmetricdefinition/{id} | Delete a specific derived metric definition
[**get_all_derived_metric_definitions**](DerivedMetricDefinitionApi.md#get_all_derived_metric_definitions) | **GET** /api/v2/derivedmetricdefinition | Get all derived metric definitions for a customer
[**get_derived_metric_definition_by_version**](DerivedMetricDefinitionApi.md#get_derived_metric_definition_by_version) | **GET** /api/v2/derivedmetricdefinition/{id}/history/{version} | Get a specific historical version of a specific derived metric definition
[**get_derived_metric_definition_history**](DerivedMetricDefinitionApi.md#get_derived_metric_definition_history) | **GET** /api/v2/derivedmetricdefinition/{id}/history | Get the version history of a specific derived metric definition
[**get_derived_metric_definition_tags**](DerivedMetricDefinitionApi.md#get_derived_metric_definition_tags) | **GET** /api/v2/derivedmetricdefinition/{id}/tag | Get all tags associated with a specific derived metric definition
[**get_registered_query**](DerivedMetricDefinitionApi.md#get_registered_query) | **GET** /api/v2/derivedmetricdefinition/{id} | Get a specific registered query
[**remove_tag_from_derived_metric_definition**](DerivedMetricDefinitionApi.md#remove_tag_from_derived_metric_definition) | **DELETE** /api/v2/derivedmetricdefinition/{id}/tag/{tagValue} | Remove a tag from a specific Derived Metric Definition
[**set_derived_metric_definition_tags**](DerivedMetricDefinitionApi.md#set_derived_metric_definition_tags) | **POST** /api/v2/derivedmetricdefinition/{id}/tag | Set all tags associated with a specific derived metric definition
[**undelete_derived_metric_definition**](DerivedMetricDefinitionApi.md#undelete_derived_metric_definition) | **POST** /api/v2/derivedmetricdefinition/{id}/undelete | Undelete a specific derived metric definition
[**update_derived_metric_definition**](DerivedMetricDefinitionApi.md#update_derived_metric_definition) | **PUT** /api/v2/derivedmetricdefinition/{id} | Update a specific derived metric definition


# **add_tag_to_derived_metric_definition**
> ResponseContainer add_tag_to_derived_metric_definition(id, tag_value)

Add a tag to a specific Derived Metric Definition



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
api_instance = wavefront_api_client.DerivedMetricDefinitionApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
tag_value = 'tag_value_example' # str | 

try:
    # Add a tag to a specific Derived Metric Definition
    api_response = api_instance.add_tag_to_derived_metric_definition(id, tag_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DerivedMetricDefinitionApi->add_tag_to_derived_metric_definition: %s\n" % e)
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

# **create_derived_metric_definition**
> ResponseContainerDerivedMetricDefinition create_derived_metric_definition(body=body)

Create a specific derived metric definition



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
api_instance = wavefront_api_client.DerivedMetricDefinitionApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.DerivedMetricDefinition() # DerivedMetricDefinition | Example Body:  <pre>{   \"name\": \"Query Name\",   \"query\": \"aliasMetric(ts(~sample.cpu.loadavg.1m), \\\"my.new.metric\\\")\",   \"minutes\": 5,   \"additionalInformation\": \"Additional Info\" }</pre> (optional)

try:
    # Create a specific derived metric definition
    api_response = api_instance.create_derived_metric_definition(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DerivedMetricDefinitionApi->create_derived_metric_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DerivedMetricDefinition**](DerivedMetricDefinition.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;Query Name\&quot;,   \&quot;query\&quot;: \&quot;aliasMetric(ts(~sample.cpu.loadavg.1m), \\\&quot;my.new.metric\\\&quot;)\&quot;,   \&quot;minutes\&quot;: 5,   \&quot;additionalInformation\&quot;: \&quot;Additional Info\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerDerivedMetricDefinition**](ResponseContainerDerivedMetricDefinition.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_derived_metric_definition**
> ResponseContainerDerivedMetricDefinition delete_derived_metric_definition(id)

Delete a specific derived metric definition



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
api_instance = wavefront_api_client.DerivedMetricDefinitionApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a specific derived metric definition
    api_response = api_instance.delete_derived_metric_definition(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DerivedMetricDefinitionApi->delete_derived_metric_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerDerivedMetricDefinition**](ResponseContainerDerivedMetricDefinition.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_derived_metric_definitions**
> ResponseContainerPagedDerivedMetricDefinition get_all_derived_metric_definitions(offset=offset, limit=limit)

Get all derived metric definitions for a customer



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
api_instance = wavefront_api_client.DerivedMetricDefinitionApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all derived metric definitions for a customer
    api_response = api_instance.get_all_derived_metric_definitions(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DerivedMetricDefinitionApi->get_all_derived_metric_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedDerivedMetricDefinition**](ResponseContainerPagedDerivedMetricDefinition.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_derived_metric_definition_by_version**
> ResponseContainerDerivedMetricDefinition get_derived_metric_definition_by_version(id, version)

Get a specific historical version of a specific derived metric definition



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
api_instance = wavefront_api_client.DerivedMetricDefinitionApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
version = 789 # int | 

try:
    # Get a specific historical version of a specific derived metric definition
    api_response = api_instance.get_derived_metric_definition_by_version(id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DerivedMetricDefinitionApi->get_derived_metric_definition_by_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **version** | **int**|  | 

### Return type

[**ResponseContainerDerivedMetricDefinition**](ResponseContainerDerivedMetricDefinition.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_derived_metric_definition_history**
> ResponseContainerHistoryResponse get_derived_metric_definition_history(id, offset=offset, limit=limit)

Get the version history of a specific derived metric definition



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
api_instance = wavefront_api_client.DerivedMetricDefinitionApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get the version history of a specific derived metric definition
    api_response = api_instance.get_derived_metric_definition_history(id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DerivedMetricDefinitionApi->get_derived_metric_definition_history: %s\n" % e)
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

# **get_derived_metric_definition_tags**
> ResponseContainerTagsResponse get_derived_metric_definition_tags(id)

Get all tags associated with a specific derived metric definition



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
api_instance = wavefront_api_client.DerivedMetricDefinitionApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get all tags associated with a specific derived metric definition
    api_response = api_instance.get_derived_metric_definition_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DerivedMetricDefinitionApi->get_derived_metric_definition_tags: %s\n" % e)
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

# **get_registered_query**
> ResponseContainerDerivedMetricDefinition get_registered_query(id)

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
api_instance = wavefront_api_client.DerivedMetricDefinitionApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific registered query
    api_response = api_instance.get_registered_query(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DerivedMetricDefinitionApi->get_registered_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerDerivedMetricDefinition**](ResponseContainerDerivedMetricDefinition.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_tag_from_derived_metric_definition**
> ResponseContainer remove_tag_from_derived_metric_definition(id, tag_value)

Remove a tag from a specific Derived Metric Definition



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
api_instance = wavefront_api_client.DerivedMetricDefinitionApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
tag_value = 'tag_value_example' # str | 

try:
    # Remove a tag from a specific Derived Metric Definition
    api_response = api_instance.remove_tag_from_derived_metric_definition(id, tag_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DerivedMetricDefinitionApi->remove_tag_from_derived_metric_definition: %s\n" % e)
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

# **set_derived_metric_definition_tags**
> ResponseContainer set_derived_metric_definition_tags(id, body=body)

Set all tags associated with a specific derived metric definition



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
api_instance = wavefront_api_client.DerivedMetricDefinitionApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = [wavefront_api_client.list[str]()] # list[str] |  (optional)

try:
    # Set all tags associated with a specific derived metric definition
    api_response = api_instance.set_derived_metric_definition_tags(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DerivedMetricDefinitionApi->set_derived_metric_definition_tags: %s\n" % e)
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

# **undelete_derived_metric_definition**
> ResponseContainerDerivedMetricDefinition undelete_derived_metric_definition(id)

Undelete a specific derived metric definition



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
api_instance = wavefront_api_client.DerivedMetricDefinitionApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Undelete a specific derived metric definition
    api_response = api_instance.undelete_derived_metric_definition(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DerivedMetricDefinitionApi->undelete_derived_metric_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerDerivedMetricDefinition**](ResponseContainerDerivedMetricDefinition.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_derived_metric_definition**
> ResponseContainerDerivedMetricDefinition update_derived_metric_definition(id, body=body)

Update a specific derived metric definition



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
api_instance = wavefront_api_client.DerivedMetricDefinitionApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.DerivedMetricDefinition() # DerivedMetricDefinition | Example Body:  <pre>{   \"id\": \"1459375928549\",   \"name\": \"Query Name\",   \"createUserId\": \"user\",   \"query\": \"aliasMetric(ts(~sample.cpu.loadavg.1m), \\\"my.new.metric\\\")\",   \"minutes\": 5,   \"additionalInformation\": \"Additional Info\" }</pre> (optional)

try:
    # Update a specific derived metric definition
    api_response = api_instance.update_derived_metric_definition(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DerivedMetricDefinitionApi->update_derived_metric_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**DerivedMetricDefinition**](DerivedMetricDefinition.md)| Example Body:  &lt;pre&gt;{   \&quot;id\&quot;: \&quot;1459375928549\&quot;,   \&quot;name\&quot;: \&quot;Query Name\&quot;,   \&quot;createUserId\&quot;: \&quot;user\&quot;,   \&quot;query\&quot;: \&quot;aliasMetric(ts(~sample.cpu.loadavg.1m), \\\&quot;my.new.metric\\\&quot;)\&quot;,   \&quot;minutes\&quot;: 5,   \&quot;additionalInformation\&quot;: \&quot;Additional Info\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerDerivedMetricDefinition**](ResponseContainerDerivedMetricDefinition.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

