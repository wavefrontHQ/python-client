# wavefront_api_client.MessageApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_get_messages**](MessageApi.md#user_get_messages) | **GET** /api/v2/message | Gets messages applicable to the current user, i.e. within time range and distribution scope
[**user_read_message**](MessageApi.md#user_read_message) | **POST** /api/v2/message/{id}/read | Mark a specific message as read


# **user_get_messages**
> ResponseContainerPagedMessage user_get_messages(offset=offset, limit=limit, unread_only=unread_only)

Gets messages applicable to the current user, i.e. within time range and distribution scope



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
api_instance = wavefront_api_client.MessageApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)
unread_only = true # bool |  (optional) (default to true)

try:
    # Gets messages applicable to the current user, i.e. within time range and distribution scope
    api_response = api_instance.user_get_messages(offset=offset, limit=limit, unread_only=unread_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->user_get_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **unread_only** | **bool**|  | [optional] [default to true]

### Return type

[**ResponseContainerPagedMessage**](ResponseContainerPagedMessage.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_read_message**
> ResponseContainerMessage user_read_message(id)

Mark a specific message as read



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
api_instance = wavefront_api_client.MessageApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Mark a specific message as read
    api_response = api_instance.user_read_message(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageApi->user_read_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerMessage**](ResponseContainerMessage.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

