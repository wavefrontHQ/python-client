# wavefront_api_client.SourceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_source_tag**](SourceApi.md#add_source_tag) | **PUT** /api/v2/source/{id}/tag/{tagValue} | Add a tag to a specific source
[**create_source**](SourceApi.md#create_source) | **POST** /api/v2/source | Create metadata (description or tags) for a specific source
[**delete_source**](SourceApi.md#delete_source) | **DELETE** /api/v2/source/{id} | Delete metadata (description and tags) for a specific source
[**get_all_source**](SourceApi.md#get_all_source) | **GET** /api/v2/source | Get all sources for a customer
[**get_source**](SourceApi.md#get_source) | **GET** /api/v2/source/{id} | Get a specific source for a customer
[**get_source_tags**](SourceApi.md#get_source_tags) | **GET** /api/v2/source/{id}/tag | Get all tags associated with a specific source
[**remove_description**](SourceApi.md#remove_description) | **DELETE** /api/v2/source/{id}/description | Remove description from a specific source
[**remove_source_tag**](SourceApi.md#remove_source_tag) | **DELETE** /api/v2/source/{id}/tag/{tagValue} | Remove a tag from a specific source
[**set_description**](SourceApi.md#set_description) | **POST** /api/v2/source/{id}/description | Set description associated with a specific source
[**set_source_tags**](SourceApi.md#set_source_tags) | **POST** /api/v2/source/{id}/tag | Set all tags associated with a specific source
[**update_source**](SourceApi.md#update_source) | **PUT** /api/v2/source/{id} | Update metadata (description or tags) for a specific source.


# **add_source_tag**
> ResponseContainer add_source_tag(id, tag_value)

Add a tag to a specific source



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
api_instance = wavefront_api_client.SourceApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
tag_value = 'tag_value_example' # str | 

try:
    # Add a tag to a specific source
    api_response = api_instance.add_source_tag(id, tag_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->add_source_tag: %s\n" % e)
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

# **create_source**
> ResponseContainerSource create_source(body=body)

Create metadata (description or tags) for a specific source



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
api_instance = wavefront_api_client.SourceApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.Source() # Source | Example Body:  <pre>{     \"sourceName\": \"source.name\",     \"tags\": {\"sourceTag1\": true},     \"description\": \"Source Description\" }</pre> (optional)

try:
    # Create metadata (description or tags) for a specific source
    api_response = api_instance.create_source(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->create_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Source**](Source.md)| Example Body:  &lt;pre&gt;{     \&quot;sourceName\&quot;: \&quot;source.name\&quot;,     \&quot;tags\&quot;: {\&quot;sourceTag1\&quot;: true},     \&quot;description\&quot;: \&quot;Source Description\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerSource**](ResponseContainerSource.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_source**
> ResponseContainerSource delete_source(id)

Delete metadata (description and tags) for a specific source



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
api_instance = wavefront_api_client.SourceApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete metadata (description and tags) for a specific source
    api_response = api_instance.delete_source(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->delete_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerSource**](ResponseContainerSource.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_source**
> ResponseContainerPagedSource get_all_source(cursor=cursor, limit=limit)

Get all sources for a customer



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
api_instance = wavefront_api_client.SourceApi(wavefront_api_client.ApiClient(configuration))
cursor = 'cursor_example' # str |  (optional)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all sources for a customer
    api_response = api_instance.get_all_source(cursor=cursor, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->get_all_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedSource**](ResponseContainerPagedSource.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source**
> ResponseContainerSource get_source(id)

Get a specific source for a customer



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
api_instance = wavefront_api_client.SourceApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific source for a customer
    api_response = api_instance.get_source(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->get_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerSource**](ResponseContainerSource.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_tags**
> ResponseContainerTagsResponse get_source_tags(id)

Get all tags associated with a specific source



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
api_instance = wavefront_api_client.SourceApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get all tags associated with a specific source
    api_response = api_instance.get_source_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->get_source_tags: %s\n" % e)
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

# **remove_description**
> ResponseContainer remove_description(id)

Remove description from a specific source



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
api_instance = wavefront_api_client.SourceApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Remove description from a specific source
    api_response = api_instance.remove_description(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->remove_description: %s\n" % e)
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

# **remove_source_tag**
> ResponseContainer remove_source_tag(id, tag_value)

Remove a tag from a specific source



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
api_instance = wavefront_api_client.SourceApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
tag_value = 'tag_value_example' # str | 

try:
    # Remove a tag from a specific source
    api_response = api_instance.remove_source_tag(id, tag_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->remove_source_tag: %s\n" % e)
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

# **set_description**
> ResponseContainer set_description(id, body=body)

Set description associated with a specific source



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
api_instance = wavefront_api_client.SourceApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = 'body_example' # str |  (optional)

try:
    # Set description associated with a specific source
    api_response = api_instance.set_description(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->set_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

[**ResponseContainer**](ResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_source_tags**
> ResponseContainer set_source_tags(id, body=body)

Set all tags associated with a specific source



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
api_instance = wavefront_api_client.SourceApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = [wavefront_api_client.list[str]()] # list[str] |  (optional)

try:
    # Set all tags associated with a specific source
    api_response = api_instance.set_source_tags(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->set_source_tags: %s\n" % e)
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

# **update_source**
> ResponseContainerSource update_source(id, body=body)

Update metadata (description or tags) for a specific source.

The \"hidden\" property is stored as a tag. To set the value, add \"hidden\": &lt;value&gt; to the list of tags.

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
api_instance = wavefront_api_client.SourceApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.Source() # Source | Example Body:  <pre>{     \"sourceName\": \"source.name\",     \"tags\": {\"sourceTag1\": true},     \"description\": \"Source Description\" }</pre> (optional)

try:
    # Update metadata (description or tags) for a specific source.
    api_response = api_instance.update_source(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->update_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Source**](Source.md)| Example Body:  &lt;pre&gt;{     \&quot;sourceName\&quot;: \&quot;source.name\&quot;,     \&quot;tags\&quot;: {\&quot;sourceTag1\&quot;: true},     \&quot;description\&quot;: \&quot;Source Description\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerSource**](ResponseContainerSource.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

