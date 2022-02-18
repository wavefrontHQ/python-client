# wavefront_api_client.SavedTracesSearchApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_saved_traces_search**](SavedTracesSearchApi.md#create_saved_traces_search) | **POST** /api/v2/savedtracessearch | Create a search
[**delete_saved_traces_search**](SavedTracesSearchApi.md#delete_saved_traces_search) | **DELETE** /api/v2/savedtracessearch/{id} | Delete a search
[**delete_saved_traces_search_for_user**](SavedTracesSearchApi.md#delete_saved_traces_search_for_user) | **DELETE** /api/v2/savedtracessearch/owned/{id} | Delete a search belonging to the user
[**get_all_saved_traces_searches**](SavedTracesSearchApi.md#get_all_saved_traces_searches) | **GET** /api/v2/savedtracessearch | Get all searches for a customer
[**get_all_saved_traces_searches_for_user**](SavedTracesSearchApi.md#get_all_saved_traces_searches_for_user) | **GET** /api/v2/savedtracessearch/owned | Get all searches for a user
[**get_saved_traces_search**](SavedTracesSearchApi.md#get_saved_traces_search) | **GET** /api/v2/savedtracessearch/{id} | Get a specific search
[**update_saved_traces_search**](SavedTracesSearchApi.md#update_saved_traces_search) | **PUT** /api/v2/savedtracessearch/{id} | Update a search
[**update_saved_traces_search_for_user**](SavedTracesSearchApi.md#update_saved_traces_search_for_user) | **PUT** /api/v2/savedtracessearch/owned/{id} | Update a search belonging to the user


# **create_saved_traces_search**
> ResponseContainerSavedTracesSearch create_saved_traces_search(body=body)

Create a search



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
api_instance = wavefront_api_client.SavedTracesSearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SavedTracesSearch() # SavedTracesSearch | Example Body:  <pre>{   \"name\": \"beachshirts shopping\",   \"searchFilters\": {     \"filters\": [       {         \"filterType\": \"OPERATION\",         \"values\": {           \"logicalValue\": [             [               \"beachshirts.\", \"shopping.\", \"'*\"             ]           ]         }       }     ]   } }</pre> (optional)

try:
    # Create a search
    api_response = api_instance.create_saved_traces_search(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedTracesSearchApi->create_saved_traces_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SavedTracesSearch**](SavedTracesSearch.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;beachshirts shopping\&quot;,   \&quot;searchFilters\&quot;: {     \&quot;filters\&quot;: [       {         \&quot;filterType\&quot;: \&quot;OPERATION\&quot;,         \&quot;values\&quot;: {           \&quot;logicalValue\&quot;: [             [               \&quot;beachshirts.\&quot;, \&quot;shopping.\&quot;, \&quot;&#39;*\&quot;             ]           ]         }       }     ]   } }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerSavedTracesSearch**](ResponseContainerSavedTracesSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saved_traces_search**
> ResponseContainerSavedTracesSearch delete_saved_traces_search(id)

Delete a search



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
api_instance = wavefront_api_client.SavedTracesSearchApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a search
    api_response = api_instance.delete_saved_traces_search(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedTracesSearchApi->delete_saved_traces_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerSavedTracesSearch**](ResponseContainerSavedTracesSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saved_traces_search_for_user**
> ResponseContainerSavedTracesSearch delete_saved_traces_search_for_user(id)

Delete a search belonging to the user



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
api_instance = wavefront_api_client.SavedTracesSearchApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a search belonging to the user
    api_response = api_instance.delete_saved_traces_search_for_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedTracesSearchApi->delete_saved_traces_search_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerSavedTracesSearch**](ResponseContainerSavedTracesSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_saved_traces_searches**
> ResponseContainerPagedSavedTracesSearch get_all_saved_traces_searches(offset=offset, limit=limit)

Get all searches for a customer



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
api_instance = wavefront_api_client.SavedTracesSearchApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all searches for a customer
    api_response = api_instance.get_all_saved_traces_searches(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedTracesSearchApi->get_all_saved_traces_searches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedSavedTracesSearch**](ResponseContainerPagedSavedTracesSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_saved_traces_searches_for_user**
> ResponseContainerPagedSavedTracesSearch get_all_saved_traces_searches_for_user(offset=offset, limit=limit)

Get all searches for a user



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
api_instance = wavefront_api_client.SavedTracesSearchApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all searches for a user
    api_response = api_instance.get_all_saved_traces_searches_for_user(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedTracesSearchApi->get_all_saved_traces_searches_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedSavedTracesSearch**](ResponseContainerPagedSavedTracesSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saved_traces_search**
> ResponseContainerSavedTracesSearch get_saved_traces_search(id)

Get a specific search



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
api_instance = wavefront_api_client.SavedTracesSearchApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific search
    api_response = api_instance.get_saved_traces_search(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedTracesSearchApi->get_saved_traces_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerSavedTracesSearch**](ResponseContainerSavedTracesSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saved_traces_search**
> ResponseContainerSavedTracesSearch update_saved_traces_search(id, body=body)

Update a search



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
api_instance = wavefront_api_client.SavedTracesSearchApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.SavedTracesSearch() # SavedTracesSearch | Example Body:  <pre>{   \"name\": \"beachshirts shopping\",   \"searchFilters\": {     \"filters\": [       {         \"filterType\": \"OPERATION\",         \"values\": {           \"logicalValue\": [             [               \"beachshirts.\", \"shopping.\", \"'*\"             ]           ]         }       }     ]   } }</pre> (optional)

try:
    # Update a search
    api_response = api_instance.update_saved_traces_search(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedTracesSearchApi->update_saved_traces_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SavedTracesSearch**](SavedTracesSearch.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;beachshirts shopping\&quot;,   \&quot;searchFilters\&quot;: {     \&quot;filters\&quot;: [       {         \&quot;filterType\&quot;: \&quot;OPERATION\&quot;,         \&quot;values\&quot;: {           \&quot;logicalValue\&quot;: [             [               \&quot;beachshirts.\&quot;, \&quot;shopping.\&quot;, \&quot;&#39;*\&quot;             ]           ]         }       }     ]   } }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerSavedTracesSearch**](ResponseContainerSavedTracesSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saved_traces_search_for_user**
> ResponseContainerSavedTracesSearch update_saved_traces_search_for_user(id, body=body)

Update a search belonging to the user



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
api_instance = wavefront_api_client.SavedTracesSearchApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.SavedTracesSearch() # SavedTracesSearch | Example Body:  <pre>{   \"name\": \"beachshirts shopping\",   \"searchFilters\": {     \"filters\": [       {         \"filterType\": \"OPERATION\",         \"values\": {           \"logicalValue\": [             [               \"beachshirts.\", \"shopping.\", \"'*\"             ]           ]         }       }     ]   } }</pre> (optional)

try:
    # Update a search belonging to the user
    api_response = api_instance.update_saved_traces_search_for_user(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedTracesSearchApi->update_saved_traces_search_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SavedTracesSearch**](SavedTracesSearch.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;beachshirts shopping\&quot;,   \&quot;searchFilters\&quot;: {     \&quot;filters\&quot;: [       {         \&quot;filterType\&quot;: \&quot;OPERATION\&quot;,         \&quot;values\&quot;: {           \&quot;logicalValue\&quot;: [             [               \&quot;beachshirts.\&quot;, \&quot;shopping.\&quot;, \&quot;&#39;*\&quot;             ]           ]         }       }     ]   } }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerSavedTracesSearch**](ResponseContainerSavedTracesSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

