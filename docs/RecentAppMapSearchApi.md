# wavefront_api_client.RecentAppMapSearchApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_recent_app_map_search**](RecentAppMapSearchApi.md#create_recent_app_map_search) | **POST** /api/v2/recentappmapsearch | Create a search
[**get_all_recent_app_map_searches**](RecentAppMapSearchApi.md#get_all_recent_app_map_searches) | **GET** /api/v2/recentappmapsearch | Get all searches for a user
[**get_recent_app_map_search**](RecentAppMapSearchApi.md#get_recent_app_map_search) | **GET** /api/v2/recentappmapsearch/{id} | Get a specific search


# **create_recent_app_map_search**
> ResponseContainerRecentAppMapSearch create_recent_app_map_search(body=body)

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
api_instance = wavefront_api_client.RecentAppMapSearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.RecentAppMapSearch() # RecentAppMapSearch | Example Body:  <pre>{   \"searchFilters\": {     \"filters\": [       {         \"filterType\": \"OPERATION\",         \"values\": {           \"logicalValue\": [             [               \"beachshirts.\", \"shopping\"             ]           ]         }       }     ]   } }</pre> (optional)

try:
    # Create a search
    api_response = api_instance.create_recent_app_map_search(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecentAppMapSearchApi->create_recent_app_map_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecentAppMapSearch**](RecentAppMapSearch.md)| Example Body:  &lt;pre&gt;{   \&quot;searchFilters\&quot;: {     \&quot;filters\&quot;: [       {         \&quot;filterType\&quot;: \&quot;OPERATION\&quot;,         \&quot;values\&quot;: {           \&quot;logicalValue\&quot;: [             [               \&quot;beachshirts.\&quot;, \&quot;shopping\&quot;             ]           ]         }       }     ]   } }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerRecentAppMapSearch**](ResponseContainerRecentAppMapSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_recent_app_map_searches**
> ResponseContainerPagedRecentAppMapSearch get_all_recent_app_map_searches(offset=offset, limit=limit)

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
api_instance = wavefront_api_client.RecentAppMapSearchApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 10 # int |  (optional) (default to 10)

try:
    # Get all searches for a user
    api_response = api_instance.get_all_recent_app_map_searches(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecentAppMapSearchApi->get_all_recent_app_map_searches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**ResponseContainerPagedRecentAppMapSearch**](ResponseContainerPagedRecentAppMapSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recent_app_map_search**
> ResponseContainerRecentAppMapSearch get_recent_app_map_search(id)

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
api_instance = wavefront_api_client.RecentAppMapSearchApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific search
    api_response = api_instance.get_recent_app_map_search(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecentAppMapSearchApi->get_recent_app_map_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerRecentAppMapSearch**](ResponseContainerRecentAppMapSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

