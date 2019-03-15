# wavefront_api_client.ExternalLinkApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_external_link**](ExternalLinkApi.md#create_external_link) | **POST** /api/v2/extlink | Create a specific external link
[**delete_external_link**](ExternalLinkApi.md#delete_external_link) | **DELETE** /api/v2/extlink/{id} | Delete a specific external link
[**get_all_external_link**](ExternalLinkApi.md#get_all_external_link) | **GET** /api/v2/extlink | Get all external links for a customer
[**get_external_link**](ExternalLinkApi.md#get_external_link) | **GET** /api/v2/extlink/{id} | Get a specific external link
[**update_external_link**](ExternalLinkApi.md#update_external_link) | **PUT** /api/v2/extlink/{id} | Update a specific external link


# **create_external_link**
> ResponseContainerExternalLink create_external_link(body=body)

Create a specific external link



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
api_instance = wavefront_api_client.ExternalLinkApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.ExternalLink() # ExternalLink | Example Body:  <pre>{   \"name\": \"External Link API Example\",   \"template\": \"https://example.com/{{source}}\",   \"description\": \"External Link Description\" }</pre> (optional)

try:
    # Create a specific external link
    api_response = api_instance.create_external_link(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalLinkApi->create_external_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalLink**](ExternalLink.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;External Link API Example\&quot;,   \&quot;template\&quot;: \&quot;https://example.com/{{source}}\&quot;,   \&quot;description\&quot;: \&quot;External Link Description\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerExternalLink**](ResponseContainerExternalLink.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_external_link**
> ResponseContainerExternalLink delete_external_link(id)

Delete a specific external link



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
api_instance = wavefront_api_client.ExternalLinkApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a specific external link
    api_response = api_instance.delete_external_link(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalLinkApi->delete_external_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerExternalLink**](ResponseContainerExternalLink.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_external_link**
> ResponseContainerPagedExternalLink get_all_external_link(offset=offset, limit=limit)

Get all external links for a customer



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
api_instance = wavefront_api_client.ExternalLinkApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all external links for a customer
    api_response = api_instance.get_all_external_link(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalLinkApi->get_all_external_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedExternalLink**](ResponseContainerPagedExternalLink.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_link**
> ResponseContainerExternalLink get_external_link(id)

Get a specific external link



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
api_instance = wavefront_api_client.ExternalLinkApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific external link
    api_response = api_instance.get_external_link(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalLinkApi->get_external_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerExternalLink**](ResponseContainerExternalLink.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_link**
> ResponseContainerExternalLink update_external_link(id, body=body)

Update a specific external link



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
api_instance = wavefront_api_client.ExternalLinkApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.ExternalLink() # ExternalLink | Example Body:  <pre>{   \"name\": \"External Link API Example\",   \"template\": \"https://example.com/{{source}}\",   \"description\": \"External Link Description\" }</pre> (optional)

try:
    # Update a specific external link
    api_response = api_instance.update_external_link(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExternalLinkApi->update_external_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ExternalLink**](ExternalLink.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;External Link API Example\&quot;,   \&quot;template\&quot;: \&quot;https://example.com/{{source}}\&quot;,   \&quot;description\&quot;: \&quot;External Link Description\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerExternalLink**](ResponseContainerExternalLink.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

