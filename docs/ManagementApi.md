# wavefront_client.ManagementApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_host_details**](ManagementApi.md#get_host_details) | **GET** /api/manage/source/{source} | Return applied tags and description for a source/host
[**get_hosts**](ManagementApi.md#get_hosts) | **GET** /api/manage/source | Request a subset of sources
[**remove_all_source_tags**](ManagementApi.md#remove_all_source_tags) | **DELETE** /api/manage/source/{source}/tags | Remove all tags from a source/host
[**set_source_description**](ManagementApi.md#set_source_description) | **POST** /api/manage/source/{source}/description | Set description for a source/host
[**tag_source**](ManagementApi.md#tag_source) | **POST** /api/manage/source/{source}/tags/{tag} | Tag a source/host
[**un_tag_source**](ManagementApi.md#un_tag_source) | **DELETE** /api/manage/source/{source}/tags/{tag} | Remove tag from a source/host


# **get_host_details**
> TaggedSource get_host_details(source)

Return applied tags and description for a source/host



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
api_instance = wavefront_client.ManagementApi()
source = 'source_example' # str | 

try: 
    # Return applied tags and description for a source/host
    api_response = api_instance.get_host_details(source)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ManagementApi->get_host_details: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**|  | 

### Return type

[**TaggedSource**](TaggedSource.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hosts**
> TaggedSourceBundle get_hosts(last_entity_id=last_entity_id, desc=desc, limit=limit)

Request a subset of sources



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
api_instance = wavefront_client.ManagementApi()
last_entity_id = 'last_entity_id_example' # str | the last source received in a previous API call, to set the starting point for this query (starts from beginning if not specified). (optional)
desc = true # bool | return sources in alphabetical (true) or reverse alphabetical (false) order. (optional) (default to true)
limit = 100 # int | max number of sources to be returned by this call (defaults to 100 if not specified, must be <= 10000). (optional) (default to 100)

try: 
    # Request a subset of sources
    api_response = api_instance.get_hosts(last_entity_id=last_entity_id, desc=desc, limit=limit)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ManagementApi->get_hosts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_entity_id** | **str**| the last source received in a previous API call, to set the starting point for this query (starts from beginning if not specified). | [optional] 
 **desc** | **bool**| return sources in alphabetical (true) or reverse alphabetical (false) order. | [optional] [default to true]
 **limit** | **int**| max number of sources to be returned by this call (defaults to 100 if not specified, must be &lt;&#x3D; 10000). | [optional] [default to 100]

### Return type

[**TaggedSourceBundle**](TaggedSourceBundle.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_source_tags**
> remove_all_source_tags(source)

Remove all tags from a source/host

Method is idempotent. There is no response.

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
api_instance = wavefront_client.ManagementApi()
source = 'source_example' # str | 

try: 
    # Remove all tags from a source/host
    api_instance.remove_all_source_tags(source)
except ApiException as e:
    print "Exception when calling ManagementApi->remove_all_source_tags: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_source_description**
> set_source_description(source, body=body)

Set description for a source/host

Method is idempotent. There is no response.

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
api_instance = wavefront_client.ManagementApi()
source = 'source_example' # str | 
body = 'body_example' # str | description (optional)

try: 
    # Set description for a source/host
    api_instance.set_source_description(source, body=body)
except ApiException as e:
    print "Exception when calling ManagementApi->set_source_description: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**|  | 
 **body** | **str**| description | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_source**
> tag_source(source, tag)

Tag a source/host

Method is idempotent. There is no response.

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
api_instance = wavefront_client.ManagementApi()
source = 'source_example' # str | 
tag = 'tag_example' # str | 

try: 
    # Tag a source/host
    api_instance.tag_source(source, tag)
except ApiException as e:
    print "Exception when calling ManagementApi->tag_source: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**|  | 
 **tag** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **un_tag_source**
> un_tag_source(source, source2)

Remove tag from a source/host

Method is idempotent. There is no response.

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
api_instance = wavefront_client.ManagementApi()
source = 'source_example' # str | 
source2 = 'source_example' # str | 

try: 
    # Remove tag from a source/host
    api_instance.un_tag_source(source, source2)
except ApiException as e:
    print "Exception when calling ManagementApi->un_tag_source: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**|  | 
 **source2** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

