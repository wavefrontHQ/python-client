# wavefront_api_client.ApiTokenApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](ApiTokenApi.md#create_token) | **POST** /api/v2/apitoken | Create new api token
[**delete_token**](ApiTokenApi.md#delete_token) | **DELETE** /api/v2/apitoken/{id} | Delete the specified api token
[**get_all_tokens**](ApiTokenApi.md#get_all_tokens) | **GET** /api/v2/apitoken | Get all api tokens for a user
[**update_token_name**](ApiTokenApi.md#update_token_name) | **PUT** /api/v2/apitoken/{id} | Update the name of the specified api token


# **create_token**
> ResponseContainerListUserApiToken create_token()

Create new api token

Returns the list of all api tokens for a user. The newly created api token is the last element of returned list.

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
api_instance = wavefront_api_client.ApiTokenApi(wavefront_api_client.ApiClient(configuration))

try:
    # Create new api token
    api_response = api_instance.create_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokenApi->create_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseContainerListUserApiToken**](ResponseContainerListUserApiToken.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token**
> ResponseContainerListUserApiToken delete_token(id)

Delete the specified api token



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
api_instance = wavefront_api_client.ApiTokenApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete the specified api token
    api_response = api_instance.delete_token(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokenApi->delete_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerListUserApiToken**](ResponseContainerListUserApiToken.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_tokens**
> ResponseContainerListUserApiToken get_all_tokens()

Get all api tokens for a user



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
api_instance = wavefront_api_client.ApiTokenApi(wavefront_api_client.ApiClient(configuration))

try:
    # Get all api tokens for a user
    api_response = api_instance.get_all_tokens()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokenApi->get_all_tokens: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseContainerListUserApiToken**](ResponseContainerListUserApiToken.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_token_name**
> ResponseContainerUserApiToken update_token_name(id, body=body)

Update the name of the specified api token



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
api_instance = wavefront_api_client.ApiTokenApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.UserApiToken() # UserApiToken | Example Body:  <pre>{   \"tokenID\": \"Token identifier\",   \"tokenName\": \"Token name\" }</pre> (optional)

try:
    # Update the name of the specified api token
    api_response = api_instance.update_token_name(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokenApi->update_token_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**UserApiToken**](UserApiToken.md)| Example Body:  &lt;pre&gt;{   \&quot;tokenID\&quot;: \&quot;Token identifier\&quot;,   \&quot;tokenName\&quot;: \&quot;Token name\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerUserApiToken**](ResponseContainerUserApiToken.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

