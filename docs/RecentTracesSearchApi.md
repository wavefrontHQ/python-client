# wavefront_api_client.RecentTracesSearchApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_recent_traces_search**](RecentTracesSearchApi.md#create_recent_traces_search) | **POST** /api/v2/recenttracessearch | Create a search
[**get_all_recent_traces_searches**](RecentTracesSearchApi.md#get_all_recent_traces_searches) | **GET** /api/v2/recenttracessearch | Get all searches for a user
[**get_recent_traces_search**](RecentTracesSearchApi.md#get_recent_traces_search) | **GET** /api/v2/recenttracessearch/{id} | Get a specific search


# **create_recent_traces_search**
> ResponseContainerRecentTracesSearch create_recent_traces_search(body=body)

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
api_instance = wavefront_api_client.RecentTracesSearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.RecentTracesSearch() # RecentTracesSearch | Example Body:  <pre>{   \"searchFilters\": {     \"filters\": [       {         \"filterType\": \"OPERATION\",         \"values\": {           \"logicalValue\": [             [               \"beachshirts.\", \"shopping.\", \"'*\"             ]           ]         }       }     ]   } }</pre> (optional)

try:
    # Create a search
    api_response = api_instance.create_recent_traces_search(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecentTracesSearchApi->create_recent_traces_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecentTracesSearch**](RecentTracesSearch.md)| Example Body:  &lt;pre&gt;{   \&quot;searchFilters\&quot;: {     \&quot;filters\&quot;: [       {         \&quot;filterType\&quot;: \&quot;OPERATION\&quot;,         \&quot;values\&quot;: {           \&quot;logicalValue\&quot;: [             [               \&quot;beachshirts.\&quot;, \&quot;shopping.\&quot;, \&quot;&#39;*\&quot;             ]           ]         }       }     ]   } }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerRecentTracesSearch**](ResponseContainerRecentTracesSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_recent_traces_searches**
> ResponseContainerPagedRecentTracesSearch get_all_recent_traces_searches(offset=offset, limit=limit)

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
api_instance = wavefront_api_client.RecentTracesSearchApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all searches for a user
    api_response = api_instance.get_all_recent_traces_searches(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecentTracesSearchApi->get_all_recent_traces_searches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedRecentTracesSearch**](ResponseContainerPagedRecentTracesSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recent_traces_search**
> ResponseContainerRecentTracesSearch get_recent_traces_search(id)

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
api_instance = wavefront_api_client.RecentTracesSearchApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific search
    api_response = api_instance.get_recent_traces_search(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecentTracesSearchApi->get_recent_traces_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerRecentTracesSearch**](ResponseContainerRecentTracesSearch.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

