# wavefront_api_client.SavedSearchApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_saved_search**](SavedSearchApi.md#create_saved_search) | **POST** /api/v2/savedsearch | Create a saved search
[**delete_saved_search**](SavedSearchApi.md#delete_saved_search) | **DELETE** /api/v2/savedsearch/{id} | Delete a specific saved search
[**get_all_entity_type_saved_searches**](SavedSearchApi.md#get_all_entity_type_saved_searches) | **GET** /api/v2/savedsearch/type/{entitytype} | Get all saved searches for a specific entity type for a user
[**get_all_saved_searches**](SavedSearchApi.md#get_all_saved_searches) | **GET** /api/v2/savedsearch | Get all saved searches for a user
[**get_saved_search**](SavedSearchApi.md#get_saved_search) | **GET** /api/v2/savedsearch/{id} | Get a specific saved search
[**update_saved_search**](SavedSearchApi.md#update_saved_search) | **PUT** /api/v2/savedsearch/{id} | Update a specific saved search


# **create_saved_search**
> ResponseContainerSavedSearch create_saved_search(body=body)

Create a saved search



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
api_instance = wavefront_api_client.SavedSearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SavedSearch() # SavedSearch | Example Body:  <pre>{   \"query\": {     \"foo\": \"{\\\"searchTerms\\\":[{\\\"type\\\":\\\"freetext\\\",\\\"value\\\":\\\"foo\\\"}]}\"   },   \"entityType\": \"DASHBOARD\" }</pre> (optional)

try:
    # Create a saved search
    api_response = api_instance.create_saved_search(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedSearchApi->create_saved_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SavedSearch**](SavedSearch.md)| Example Body:  &lt;pre&gt;{   \&quot;query\&quot;: {     \&quot;foo\&quot;: \&quot;{\\\&quot;searchTerms\\\&quot;:[{\\\&quot;type\\\&quot;:\\\&quot;freetext\\\&quot;,\\\&quot;value\\\&quot;:\\\&quot;foo\\\&quot;}]}\&quot;   },   \&quot;entityType\&quot;: \&quot;DASHBOARD\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerSavedSearch**](ResponseContainerSavedSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saved_search**
> ResponseContainerSavedSearch delete_saved_search(id)

Delete a specific saved search



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
api_instance = wavefront_api_client.SavedSearchApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a specific saved search
    api_response = api_instance.delete_saved_search(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedSearchApi->delete_saved_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerSavedSearch**](ResponseContainerSavedSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_entity_type_saved_searches**
> ResponseContainerPagedSavedSearch get_all_entity_type_saved_searches(entitytype, offset=offset, limit=limit)

Get all saved searches for a specific entity type for a user



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
api_instance = wavefront_api_client.SavedSearchApi(wavefront_api_client.ApiClient(configuration))
entitytype = 'entitytype_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all saved searches for a specific entity type for a user
    api_response = api_instance.get_all_entity_type_saved_searches(entitytype, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedSearchApi->get_all_entity_type_saved_searches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitytype** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedSavedSearch**](ResponseContainerPagedSavedSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_saved_searches**
> ResponseContainerPagedSavedSearch get_all_saved_searches(offset=offset, limit=limit)

Get all saved searches for a user



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
api_instance = wavefront_api_client.SavedSearchApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all saved searches for a user
    api_response = api_instance.get_all_saved_searches(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedSearchApi->get_all_saved_searches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedSavedSearch**](ResponseContainerPagedSavedSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saved_search**
> ResponseContainerSavedSearch get_saved_search(id)

Get a specific saved search



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
api_instance = wavefront_api_client.SavedSearchApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific saved search
    api_response = api_instance.get_saved_search(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedSearchApi->get_saved_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerSavedSearch**](ResponseContainerSavedSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saved_search**
> ResponseContainerSavedSearch update_saved_search(id, body=body)

Update a specific saved search



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
api_instance = wavefront_api_client.SavedSearchApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.SavedSearch() # SavedSearch | Example Body:  <pre>{   \"query\": {     \"foo\": \"{\\\"searchTerms\\\":[{\\\"type\\\":\\\"freetext\\\",\\\"value\\\":\\\"foo\\\"}]}\"   },   \"entityType\": \"DASHBOARD\" }</pre> (optional)

try:
    # Update a specific saved search
    api_response = api_instance.update_saved_search(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedSearchApi->update_saved_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SavedSearch**](SavedSearch.md)| Example Body:  &lt;pre&gt;{   \&quot;query\&quot;: {     \&quot;foo\&quot;: \&quot;{\\\&quot;searchTerms\\\&quot;:[{\\\&quot;type\\\&quot;:\\\&quot;freetext\\\&quot;,\\\&quot;value\\\&quot;:\\\&quot;foo\\\&quot;}]}\&quot;   },   \&quot;entityType\&quot;: \&quot;DASHBOARD\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerSavedSearch**](ResponseContainerSavedSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

