# wavefront_api_client.SavedTracesSearchGroupApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_saved_traces_search_to_group**](SavedTracesSearchGroupApi.md#add_saved_traces_search_to_group) | **POST** /api/v2/savedtracessearchgroup/{id}/addSearch/{searchId} | Add a search to a search group
[**create_saved_traces_search_group**](SavedTracesSearchGroupApi.md#create_saved_traces_search_group) | **POST** /api/v2/savedtracessearchgroup | Create a search group
[**delete_saved_traces_search_group**](SavedTracesSearchGroupApi.md#delete_saved_traces_search_group) | **DELETE** /api/v2/savedtracessearchgroup/{id} | Delete a search group
[**get_all_saved_traces_search_group**](SavedTracesSearchGroupApi.md#get_all_saved_traces_search_group) | **GET** /api/v2/savedtracessearchgroup | Get all search groups for a user
[**get_saved_traces_search_group**](SavedTracesSearchGroupApi.md#get_saved_traces_search_group) | **GET** /api/v2/savedtracessearchgroup/{id} | Get a specific search group
[**get_saved_traces_searches_for_group**](SavedTracesSearchGroupApi.md#get_saved_traces_searches_for_group) | **GET** /api/v2/savedtracessearchgroup/{id}/searches | Get all searches for a search group
[**remove_saved_traces_search_from_group**](SavedTracesSearchGroupApi.md#remove_saved_traces_search_from_group) | **POST** /api/v2/savedtracessearchgroup/{id}/removeSearch/{searchId} | Remove a search from a search group
[**update_saved_traces_search_group**](SavedTracesSearchGroupApi.md#update_saved_traces_search_group) | **PUT** /api/v2/savedtracessearchgroup/{id} | Update a search group


# **add_saved_traces_search_to_group**
> ResponseContainer add_saved_traces_search_to_group(id, search_id)

Add a search to a search group



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
api_instance = wavefront_api_client.SavedTracesSearchGroupApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
search_id = 'search_id_example' # str | 

try:
    # Add a search to a search group
    api_response = api_instance.add_saved_traces_search_to_group(id, search_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedTracesSearchGroupApi->add_saved_traces_search_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **search_id** | **str**|  | 

### Return type

[**ResponseContainer**](ResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_saved_traces_search_group**
> ResponseContainerSavedTracesSearchGroup create_saved_traces_search_group(body=body)

Create a search group



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
api_instance = wavefront_api_client.SavedTracesSearchGroupApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SavedTracesSearchGroup() # SavedTracesSearchGroup | Example Body:  <pre>{   \"name\": \"Search Group 1\" }</pre> (optional)

try:
    # Create a search group
    api_response = api_instance.create_saved_traces_search_group(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedTracesSearchGroupApi->create_saved_traces_search_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SavedTracesSearchGroup**](SavedTracesSearchGroup.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;Search Group 1\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerSavedTracesSearchGroup**](ResponseContainerSavedTracesSearchGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saved_traces_search_group**
> ResponseContainerSavedTracesSearchGroup delete_saved_traces_search_group(id)

Delete a search group



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
api_instance = wavefront_api_client.SavedTracesSearchGroupApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a search group
    api_response = api_instance.delete_saved_traces_search_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedTracesSearchGroupApi->delete_saved_traces_search_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerSavedTracesSearchGroup**](ResponseContainerSavedTracesSearchGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_saved_traces_search_group**
> ResponseContainerPagedSavedTracesSearchGroup get_all_saved_traces_search_group(offset=offset, limit=limit)

Get all search groups for a user



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
api_instance = wavefront_api_client.SavedTracesSearchGroupApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all search groups for a user
    api_response = api_instance.get_all_saved_traces_search_group(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedTracesSearchGroupApi->get_all_saved_traces_search_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedSavedTracesSearchGroup**](ResponseContainerPagedSavedTracesSearchGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saved_traces_search_group**
> ResponseContainerSavedTracesSearchGroup get_saved_traces_search_group(id)

Get a specific search group



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
api_instance = wavefront_api_client.SavedTracesSearchGroupApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific search group
    api_response = api_instance.get_saved_traces_search_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedTracesSearchGroupApi->get_saved_traces_search_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerSavedTracesSearchGroup**](ResponseContainerSavedTracesSearchGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saved_traces_searches_for_group**
> ResponseContainerPagedSavedTracesSearch get_saved_traces_searches_for_group(id, offset=offset, limit=limit)

Get all searches for a search group



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
api_instance = wavefront_api_client.SavedTracesSearchGroupApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all searches for a search group
    api_response = api_instance.get_saved_traces_searches_for_group(id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedTracesSearchGroupApi->get_saved_traces_searches_for_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **remove_saved_traces_search_from_group**
> ResponseContainer remove_saved_traces_search_from_group(id, search_id)

Remove a search from a search group



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
api_instance = wavefront_api_client.SavedTracesSearchGroupApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
search_id = 'search_id_example' # str | 

try:
    # Remove a search from a search group
    api_response = api_instance.remove_saved_traces_search_from_group(id, search_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedTracesSearchGroupApi->remove_saved_traces_search_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **search_id** | **str**|  | 

### Return type

[**ResponseContainer**](ResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saved_traces_search_group**
> ResponseContainerSavedTracesSearchGroup update_saved_traces_search_group(id, body=body)

Update a search group



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
api_instance = wavefront_api_client.SavedTracesSearchGroupApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.SavedTracesSearchGroup() # SavedTracesSearchGroup | Example Body:  <pre>{   \"name\": \"Search Group 1\" }</pre> (optional)

try:
    # Update a search group
    api_response = api_instance.update_saved_traces_search_group(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedTracesSearchGroupApi->update_saved_traces_search_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SavedTracesSearchGroup**](SavedTracesSearchGroup.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;Search Group 1\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerSavedTracesSearchGroup**](ResponseContainerSavedTracesSearchGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

