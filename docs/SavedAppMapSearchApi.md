# wavefront_api_client.SavedAppMapSearchApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_saved_app_map_search**](SavedAppMapSearchApi.md#create_saved_app_map_search) | **POST** /api/v2/savedappmapsearch | Create a search
[**default_app_map_search**](SavedAppMapSearchApi.md#default_app_map_search) | **GET** /api/v2/savedappmapsearch/defaultAppMapSearch | Get default app map search for a user
[**default_app_map_search_0**](SavedAppMapSearchApi.md#default_app_map_search_0) | **POST** /api/v2/savedappmapsearch/defaultAppMapSearch | Set default app map search at user level
[**default_customer_app_map_search**](SavedAppMapSearchApi.md#default_customer_app_map_search) | **POST** /api/v2/savedappmapsearch/defaultCustomerAppMapSearch | Set default app map search at customer level
[**delete_saved_app_map_search**](SavedAppMapSearchApi.md#delete_saved_app_map_search) | **DELETE** /api/v2/savedappmapsearch/{id} | Delete a search
[**delete_saved_app_map_search_for_user**](SavedAppMapSearchApi.md#delete_saved_app_map_search_for_user) | **DELETE** /api/v2/savedappmapsearch/owned/{id} | Delete a search belonging to the user
[**get_all_saved_app_map_searches**](SavedAppMapSearchApi.md#get_all_saved_app_map_searches) | **GET** /api/v2/savedappmapsearch | Get all searches for a customer
[**get_all_saved_app_map_searches_for_user**](SavedAppMapSearchApi.md#get_all_saved_app_map_searches_for_user) | **GET** /api/v2/savedappmapsearch/owned | Get all searches for a user
[**get_saved_app_map_search**](SavedAppMapSearchApi.md#get_saved_app_map_search) | **GET** /api/v2/savedappmapsearch/{id} | Get a specific search
[**update_saved_app_map_search**](SavedAppMapSearchApi.md#update_saved_app_map_search) | **PUT** /api/v2/savedappmapsearch/{id} | Update a search
[**update_saved_app_map_search_for_user**](SavedAppMapSearchApi.md#update_saved_app_map_search_for_user) | **PUT** /api/v2/savedappmapsearch/owned/{id} | Update a search belonging to the user


# **create_saved_app_map_search**
> ResponseContainerSavedAppMapSearch create_saved_app_map_search(body=body)

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
api_instance = wavefront_api_client.SavedAppMapSearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SavedAppMapSearch() # SavedAppMapSearch | Example Body:  <pre>{   \"name\": \"beachshirts shopping\",   \"searchFilters\": {     \"filters\": [       {         \"filterType\": \"OPERATION\",         \"values\": {           \"logicalValue\": [             [               \"beachshirts.\", \"shopping\"             ]           ]         }       }     ]   } }</pre> (optional)

try:
    # Create a search
    api_response = api_instance.create_saved_app_map_search(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedAppMapSearchApi->create_saved_app_map_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SavedAppMapSearch**](SavedAppMapSearch.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;beachshirts shopping\&quot;,   \&quot;searchFilters\&quot;: {     \&quot;filters\&quot;: [       {         \&quot;filterType\&quot;: \&quot;OPERATION\&quot;,         \&quot;values\&quot;: {           \&quot;logicalValue\&quot;: [             [               \&quot;beachshirts.\&quot;, \&quot;shopping\&quot;             ]           ]         }       }     ]   } }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerSavedAppMapSearch**](ResponseContainerSavedAppMapSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **default_app_map_search**
> ResponseContainerDefaultSavedAppMapSearch default_app_map_search()

Get default app map search for a user



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
api_instance = wavefront_api_client.SavedAppMapSearchApi(wavefront_api_client.ApiClient(configuration))

try:
    # Get default app map search for a user
    api_response = api_instance.default_app_map_search()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedAppMapSearchApi->default_app_map_search: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseContainerDefaultSavedAppMapSearch**](ResponseContainerDefaultSavedAppMapSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **default_app_map_search_0**
> ResponseContainerString default_app_map_search_0(default_app_map_search=default_app_map_search)

Set default app map search at user level



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
api_instance = wavefront_api_client.SavedAppMapSearchApi(wavefront_api_client.ApiClient(configuration))
default_app_map_search = 'default_app_map_search_example' # str |  (optional)

try:
    # Set default app map search at user level
    api_response = api_instance.default_app_map_search_0(default_app_map_search=default_app_map_search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedAppMapSearchApi->default_app_map_search_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **default_app_map_search** | **str**|  | [optional] 

### Return type

[**ResponseContainerString**](ResponseContainerString.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **default_customer_app_map_search**
> ResponseContainerString default_customer_app_map_search(default_app_map_search=default_app_map_search)

Set default app map search at customer level



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
api_instance = wavefront_api_client.SavedAppMapSearchApi(wavefront_api_client.ApiClient(configuration))
default_app_map_search = 'default_app_map_search_example' # str |  (optional)

try:
    # Set default app map search at customer level
    api_response = api_instance.default_customer_app_map_search(default_app_map_search=default_app_map_search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedAppMapSearchApi->default_customer_app_map_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **default_app_map_search** | **str**|  | [optional] 

### Return type

[**ResponseContainerString**](ResponseContainerString.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saved_app_map_search**
> ResponseContainerSavedAppMapSearch delete_saved_app_map_search(id)

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
api_instance = wavefront_api_client.SavedAppMapSearchApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a search
    api_response = api_instance.delete_saved_app_map_search(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedAppMapSearchApi->delete_saved_app_map_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerSavedAppMapSearch**](ResponseContainerSavedAppMapSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saved_app_map_search_for_user**
> ResponseContainerSavedAppMapSearch delete_saved_app_map_search_for_user(id)

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
api_instance = wavefront_api_client.SavedAppMapSearchApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a search belonging to the user
    api_response = api_instance.delete_saved_app_map_search_for_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedAppMapSearchApi->delete_saved_app_map_search_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerSavedAppMapSearch**](ResponseContainerSavedAppMapSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_saved_app_map_searches**
> ResponseContainerPagedSavedAppMapSearch get_all_saved_app_map_searches(offset=offset, limit=limit)

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
api_instance = wavefront_api_client.SavedAppMapSearchApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all searches for a customer
    api_response = api_instance.get_all_saved_app_map_searches(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedAppMapSearchApi->get_all_saved_app_map_searches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedSavedAppMapSearch**](ResponseContainerPagedSavedAppMapSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_saved_app_map_searches_for_user**
> ResponseContainerPagedSavedAppMapSearch get_all_saved_app_map_searches_for_user(offset=offset, limit=limit)

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
api_instance = wavefront_api_client.SavedAppMapSearchApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all searches for a user
    api_response = api_instance.get_all_saved_app_map_searches_for_user(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedAppMapSearchApi->get_all_saved_app_map_searches_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedSavedAppMapSearch**](ResponseContainerPagedSavedAppMapSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saved_app_map_search**
> ResponseContainerSavedAppMapSearch get_saved_app_map_search(id)

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
api_instance = wavefront_api_client.SavedAppMapSearchApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific search
    api_response = api_instance.get_saved_app_map_search(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedAppMapSearchApi->get_saved_app_map_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerSavedAppMapSearch**](ResponseContainerSavedAppMapSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saved_app_map_search**
> ResponseContainerSavedAppMapSearch update_saved_app_map_search(id, body=body)

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
api_instance = wavefront_api_client.SavedAppMapSearchApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.SavedAppMapSearch() # SavedAppMapSearch | Example Body:  <pre>{   \"name\": \"beachshirts shopping\",   \"searchFilters\": {     \"filters\": [       {         \"filterType\": \"OPERATION\",         \"values\": {           \"logicalValue\": [             [               \"beachshirts.\", \"shopping\"             ]           ]         }       }     ]   } }</pre> (optional)

try:
    # Update a search
    api_response = api_instance.update_saved_app_map_search(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedAppMapSearchApi->update_saved_app_map_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SavedAppMapSearch**](SavedAppMapSearch.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;beachshirts shopping\&quot;,   \&quot;searchFilters\&quot;: {     \&quot;filters\&quot;: [       {         \&quot;filterType\&quot;: \&quot;OPERATION\&quot;,         \&quot;values\&quot;: {           \&quot;logicalValue\&quot;: [             [               \&quot;beachshirts.\&quot;, \&quot;shopping\&quot;             ]           ]         }       }     ]   } }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerSavedAppMapSearch**](ResponseContainerSavedAppMapSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saved_app_map_search_for_user**
> ResponseContainerSavedAppMapSearch update_saved_app_map_search_for_user(id, body=body)

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
api_instance = wavefront_api_client.SavedAppMapSearchApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.SavedAppMapSearch() # SavedAppMapSearch | Example Body:  <pre>{   \"name\": \"beachshirts shopping\",   \"searchFilters\": {     \"filters\": [       {         \"filterType\": \"OPERATION\",         \"values\": {           \"logicalValue\": [             [               \"beachshirts.\", \"shopping\"             ]           ]         }       }     ]   } }</pre> (optional)

try:
    # Update a search belonging to the user
    api_response = api_instance.update_saved_app_map_search_for_user(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedAppMapSearchApi->update_saved_app_map_search_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SavedAppMapSearch**](SavedAppMapSearch.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;beachshirts shopping\&quot;,   \&quot;searchFilters\&quot;: {     \&quot;filters\&quot;: [       {         \&quot;filterType\&quot;: \&quot;OPERATION\&quot;,         \&quot;values\&quot;: {           \&quot;logicalValue\&quot;: [             [               \&quot;beachshirts.\&quot;, \&quot;shopping\&quot;             ]           ]         }       }     ]   } }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerSavedAppMapSearch**](ResponseContainerSavedAppMapSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

