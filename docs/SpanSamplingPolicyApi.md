# wavefront_api_client.SpanSamplingPolicyApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_span_sampling_policy**](SpanSamplingPolicyApi.md#create_span_sampling_policy) | **POST** /api/v2/spansamplingpolicy | Create a span sampling policy
[**delete_span_sampling_policy**](SpanSamplingPolicyApi.md#delete_span_sampling_policy) | **DELETE** /api/v2/spansamplingpolicy/{id} | Delete a specific span sampling policy
[**get_all_deleted_span_sampling_policy**](SpanSamplingPolicyApi.md#get_all_deleted_span_sampling_policy) | **GET** /api/v2/spansamplingpolicy/deleted | Get all deleted sampling policies for a customer
[**get_all_span_sampling_policy**](SpanSamplingPolicyApi.md#get_all_span_sampling_policy) | **GET** /api/v2/spansamplingpolicy | Get all sampling policies for a customer
[**get_span_sampling_policy**](SpanSamplingPolicyApi.md#get_span_sampling_policy) | **GET** /api/v2/spansamplingpolicy/{id} | Get a specific span sampling policy
[**get_span_sampling_policy_history**](SpanSamplingPolicyApi.md#get_span_sampling_policy_history) | **GET** /api/v2/spansamplingpolicy/{id}/history | Get the version history of a specific sampling policy
[**get_span_sampling_policy_version**](SpanSamplingPolicyApi.md#get_span_sampling_policy_version) | **GET** /api/v2/spansamplingpolicy/{id}/history/{version} | Get a specific historical version of a specific sampling policy
[**undelete_span_sampling_policy**](SpanSamplingPolicyApi.md#undelete_span_sampling_policy) | **POST** /api/v2/spansamplingpolicy/{id}/undelete | Restore a deleted span sampling policy
[**update_span_sampling_policy**](SpanSamplingPolicyApi.md#update_span_sampling_policy) | **PUT** /api/v2/spansamplingpolicy/{id} | Update a specific span sampling policy


# **create_span_sampling_policy**
> ResponseContainerSpanSamplingPolicy create_span_sampling_policy(body=body)

Create a span sampling policy



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
api_instance = wavefront_api_client.SpanSamplingPolicyApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SpanSamplingPolicy() # SpanSamplingPolicy | Example Body:  <pre>{   \"name\": \"Test\",   \"id\": \"test\",   \"active\": false,   \"expression\": \"{{sourceName}}='localhost'\",   \"description\": \"test description\",   \"samplingPercent\": 100 }</pre> (optional)

try:
    # Create a span sampling policy
    api_response = api_instance.create_span_sampling_policy(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpanSamplingPolicyApi->create_span_sampling_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpanSamplingPolicy**](SpanSamplingPolicy.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;Test\&quot;,   \&quot;id\&quot;: \&quot;test\&quot;,   \&quot;active\&quot;: false,   \&quot;expression\&quot;: \&quot;{{sourceName}}&#x3D;&#39;localhost&#39;\&quot;,   \&quot;description\&quot;: \&quot;test description\&quot;,   \&quot;samplingPercent\&quot;: 100 }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerSpanSamplingPolicy**](ResponseContainerSpanSamplingPolicy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_span_sampling_policy**
> ResponseContainerSpanSamplingPolicy delete_span_sampling_policy(id)

Delete a specific span sampling policy



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
api_instance = wavefront_api_client.SpanSamplingPolicyApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a specific span sampling policy
    api_response = api_instance.delete_span_sampling_policy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpanSamplingPolicyApi->delete_span_sampling_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerSpanSamplingPolicy**](ResponseContainerSpanSamplingPolicy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_deleted_span_sampling_policy**
> ResponseContainerPagedSpanSamplingPolicy get_all_deleted_span_sampling_policy(offset=offset, limit=limit)

Get all deleted sampling policies for a customer



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
api_instance = wavefront_api_client.SpanSamplingPolicyApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all deleted sampling policies for a customer
    api_response = api_instance.get_all_deleted_span_sampling_policy(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpanSamplingPolicyApi->get_all_deleted_span_sampling_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedSpanSamplingPolicy**](ResponseContainerPagedSpanSamplingPolicy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_span_sampling_policy**
> ResponseContainerPagedSpanSamplingPolicy get_all_span_sampling_policy(offset=offset, limit=limit)

Get all sampling policies for a customer



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
api_instance = wavefront_api_client.SpanSamplingPolicyApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all sampling policies for a customer
    api_response = api_instance.get_all_span_sampling_policy(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpanSamplingPolicyApi->get_all_span_sampling_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedSpanSamplingPolicy**](ResponseContainerPagedSpanSamplingPolicy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_span_sampling_policy**
> ResponseContainerSpanSamplingPolicy get_span_sampling_policy(id)

Get a specific span sampling policy



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
api_instance = wavefront_api_client.SpanSamplingPolicyApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific span sampling policy
    api_response = api_instance.get_span_sampling_policy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpanSamplingPolicyApi->get_span_sampling_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerSpanSamplingPolicy**](ResponseContainerSpanSamplingPolicy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_span_sampling_policy_history**
> ResponseContainerHistoryResponse get_span_sampling_policy_history(id, offset=offset, limit=limit)

Get the version history of a specific sampling policy



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
api_instance = wavefront_api_client.SpanSamplingPolicyApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get the version history of a specific sampling policy
    api_response = api_instance.get_span_sampling_policy_history(id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpanSamplingPolicyApi->get_span_sampling_policy_history: %s\n" % e)
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

# **get_span_sampling_policy_version**
> ResponseContainerSpanSamplingPolicy get_span_sampling_policy_version(id, version)

Get a specific historical version of a specific sampling policy



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
api_instance = wavefront_api_client.SpanSamplingPolicyApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
version = 789 # int | 

try:
    # Get a specific historical version of a specific sampling policy
    api_response = api_instance.get_span_sampling_policy_version(id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpanSamplingPolicyApi->get_span_sampling_policy_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **version** | **int**|  | 

### Return type

[**ResponseContainerSpanSamplingPolicy**](ResponseContainerSpanSamplingPolicy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undelete_span_sampling_policy**
> ResponseContainerSpanSamplingPolicy undelete_span_sampling_policy(id)

Restore a deleted span sampling policy



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
api_instance = wavefront_api_client.SpanSamplingPolicyApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Restore a deleted span sampling policy
    api_response = api_instance.undelete_span_sampling_policy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpanSamplingPolicyApi->undelete_span_sampling_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerSpanSamplingPolicy**](ResponseContainerSpanSamplingPolicy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_span_sampling_policy**
> ResponseContainerSpanSamplingPolicy update_span_sampling_policy(id, body=body)

Update a specific span sampling policy



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
api_instance = wavefront_api_client.SpanSamplingPolicyApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.SpanSamplingPolicy() # SpanSamplingPolicy | Example Body:  <pre>{   \"name\": \"Test\",   \"id\": \"test\",   \"active\": false,   \"expression\": \"{{sourceName}}='localhost'\",   \"description\": \"test description\",   \"samplingPercent\": 100 }</pre> (optional)

try:
    # Update a specific span sampling policy
    api_response = api_instance.update_span_sampling_policy(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpanSamplingPolicyApi->update_span_sampling_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SpanSamplingPolicy**](SpanSamplingPolicy.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;Test\&quot;,   \&quot;id\&quot;: \&quot;test\&quot;,   \&quot;active\&quot;: false,   \&quot;expression\&quot;: \&quot;{{sourceName}}&#x3D;&#39;localhost&#39;\&quot;,   \&quot;description\&quot;: \&quot;test description\&quot;,   \&quot;samplingPercent\&quot;: 100 }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerSpanSamplingPolicy**](ResponseContainerSpanSamplingPolicy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

