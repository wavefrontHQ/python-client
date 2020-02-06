# wavefront_api_client.MonitoredClusterApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cluster_tag**](MonitoredClusterApi.md#add_cluster_tag) | **PUT** /api/v2/monitoredcluster/{id}/tag/{tagValue} | Add a tag to a specific cluster
[**create_cluster**](MonitoredClusterApi.md#create_cluster) | **POST** /api/v2/monitoredcluster | Create a specific cluster
[**delete_cluster**](MonitoredClusterApi.md#delete_cluster) | **DELETE** /api/v2/monitoredcluster/{id} | Delete a specific cluster
[**get_all_cluster**](MonitoredClusterApi.md#get_all_cluster) | **GET** /api/v2/monitoredcluster | Get all monitored clusters
[**get_cluster**](MonitoredClusterApi.md#get_cluster) | **GET** /api/v2/monitoredcluster/{id} | Get a specific cluster
[**get_cluster_tags**](MonitoredClusterApi.md#get_cluster_tags) | **GET** /api/v2/monitoredcluster/{id}/tag | Get all tags associated with a specific cluster
[**merge_clusters**](MonitoredClusterApi.md#merge_clusters) | **PUT** /api/v2/monitoredcluster/merge/{id1}/{id2} | Merge two monitored clusters.  The first cluster will remain and the second cluster will be deleted, with its id added as an alias to the first cluster.
[**remove_cluster_tag**](MonitoredClusterApi.md#remove_cluster_tag) | **DELETE** /api/v2/monitoredcluster/{id}/tag/{tagValue} | Remove a tag from a specific cluster
[**set_cluster_tags**](MonitoredClusterApi.md#set_cluster_tags) | **POST** /api/v2/monitoredcluster/{id}/tag | Set all tags associated with a specific cluster
[**update_cluster**](MonitoredClusterApi.md#update_cluster) | **PUT** /api/v2/monitoredcluster/{id} | Update a specific cluster


# **add_cluster_tag**
> ResponseContainer add_cluster_tag(id, tag_value)

Add a tag to a specific cluster



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
api_instance = wavefront_api_client.MonitoredClusterApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
tag_value = 'tag_value_example' # str | 

try:
    # Add a tag to a specific cluster
    api_response = api_instance.add_cluster_tag(id, tag_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredClusterApi->add_cluster_tag: %s\n" % e)
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

# **create_cluster**
> ResponseContainerMonitoredCluster create_cluster(body=body)

Create a specific cluster



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
api_instance = wavefront_api_client.MonitoredClusterApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.MonitoredCluster() # MonitoredCluster | Example Body:  <pre>{   \"id\": \"k8s-sample\",   \"name\": \"Sample cluster\",   \"platform\": \"EKS\",   \"version\": \"1.2\",   \"additionalTags\": {      \"region\" : \"us-west-2\",      \"az\" : \"testing\"    },   \"tags\": [      \"alertTag1\"    ] }</pre> (optional)

try:
    # Create a specific cluster
    api_response = api_instance.create_cluster(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredClusterApi->create_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MonitoredCluster**](MonitoredCluster.md)| Example Body:  &lt;pre&gt;{   \&quot;id\&quot;: \&quot;k8s-sample\&quot;,   \&quot;name\&quot;: \&quot;Sample cluster\&quot;,   \&quot;platform\&quot;: \&quot;EKS\&quot;,   \&quot;version\&quot;: \&quot;1.2\&quot;,   \&quot;additionalTags\&quot;: {      \&quot;region\&quot; : \&quot;us-west-2\&quot;,      \&quot;az\&quot; : \&quot;testing\&quot;    },   \&quot;tags\&quot;: [      \&quot;alertTag1\&quot;    ] }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerMonitoredCluster**](ResponseContainerMonitoredCluster.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster**
> ResponseContainerMonitoredCluster delete_cluster(id)

Delete a specific cluster



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
api_instance = wavefront_api_client.MonitoredClusterApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a specific cluster
    api_response = api_instance.delete_cluster(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredClusterApi->delete_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerMonitoredCluster**](ResponseContainerMonitoredCluster.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_cluster**
> ResponseContainerPagedMonitoredCluster get_all_cluster(offset=offset, limit=limit)

Get all monitored clusters



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
api_instance = wavefront_api_client.MonitoredClusterApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all monitored clusters
    api_response = api_instance.get_all_cluster(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredClusterApi->get_all_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedMonitoredCluster**](ResponseContainerPagedMonitoredCluster.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster**
> ResponseContainerMonitoredCluster get_cluster(id)

Get a specific cluster



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
api_instance = wavefront_api_client.MonitoredClusterApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific cluster
    api_response = api_instance.get_cluster(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredClusterApi->get_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerMonitoredCluster**](ResponseContainerMonitoredCluster.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_tags**
> ResponseContainerTagsResponse get_cluster_tags(id)

Get all tags associated with a specific cluster



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
api_instance = wavefront_api_client.MonitoredClusterApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get all tags associated with a specific cluster
    api_response = api_instance.get_cluster_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredClusterApi->get_cluster_tags: %s\n" % e)
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

# **merge_clusters**
> ResponseContainer merge_clusters(id1, id2)

Merge two monitored clusters.  The first cluster will remain and the second cluster will be deleted, with its id added as an alias to the first cluster.



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
api_instance = wavefront_api_client.MonitoredClusterApi(wavefront_api_client.ApiClient(configuration))
id1 = 'id1_example' # str | 
id2 = 'id2_example' # str | 

try:
    # Merge two monitored clusters.  The first cluster will remain and the second cluster will be deleted, with its id added as an alias to the first cluster.
    api_response = api_instance.merge_clusters(id1, id2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredClusterApi->merge_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id1** | **str**|  | 
 **id2** | **str**|  | 

### Return type

[**ResponseContainer**](ResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_cluster_tag**
> ResponseContainer remove_cluster_tag(id, tag_value)

Remove a tag from a specific cluster



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
api_instance = wavefront_api_client.MonitoredClusterApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
tag_value = 'tag_value_example' # str | 

try:
    # Remove a tag from a specific cluster
    api_response = api_instance.remove_cluster_tag(id, tag_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredClusterApi->remove_cluster_tag: %s\n" % e)
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

# **set_cluster_tags**
> ResponseContainer set_cluster_tags(id, body=body)

Set all tags associated with a specific cluster



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
api_instance = wavefront_api_client.MonitoredClusterApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = [wavefront_api_client.list[str]()] # list[str] |  (optional)

try:
    # Set all tags associated with a specific cluster
    api_response = api_instance.set_cluster_tags(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredClusterApi->set_cluster_tags: %s\n" % e)
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

# **update_cluster**
> ResponseContainerMonitoredCluster update_cluster(id, body=body)

Update a specific cluster



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
api_instance = wavefront_api_client.MonitoredClusterApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.MonitoredCluster() # MonitoredCluster | Example Body:  <pre>{   \"id\": \"k8s-sample\",   \"name\": \"Sample cluster\",   \"platform\": \"EKS\",   \"version\": \"1.2\",   \"additionalTags\": {      \"region\" : \"us-west-2\",      \"az\" : \"testing\"    },   \"tags\": [      \"alertTag1\"    ] }</pre> (optional)

try:
    # Update a specific cluster
    api_response = api_instance.update_cluster(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredClusterApi->update_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**MonitoredCluster**](MonitoredCluster.md)| Example Body:  &lt;pre&gt;{   \&quot;id\&quot;: \&quot;k8s-sample\&quot;,   \&quot;name\&quot;: \&quot;Sample cluster\&quot;,   \&quot;platform\&quot;: \&quot;EKS\&quot;,   \&quot;version\&quot;: \&quot;1.2\&quot;,   \&quot;additionalTags\&quot;: {      \&quot;region\&quot; : \&quot;us-west-2\&quot;,      \&quot;az\&quot; : \&quot;testing\&quot;    },   \&quot;tags\&quot;: [      \&quot;alertTag1\&quot;    ] }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerMonitoredCluster**](ResponseContainerMonitoredCluster.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

