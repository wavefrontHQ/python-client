# wavefront_api_client.UserApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_user**](UserApi.md#create_or_update_user) | **POST** /api/v2/user | Creates or updates a user
[**delete_user**](UserApi.md#delete_user) | **DELETE** /api/v2/user/{id} | Deletes a user identified by id
[**get_all_user**](UserApi.md#get_all_user) | **GET** /api/v2/user | Get all users
[**get_user**](UserApi.md#get_user) | **GET** /api/v2/user/{id} | Retrieves a user by identifier (email addr)
[**grant_user_permission**](UserApi.md#grant_user_permission) | **POST** /api/v2/user/{id}/grant | Grants a specific user permission
[**revoke_user_permission**](UserApi.md#revoke_user_permission) | **POST** /api/v2/user/{id}/revoke | Revokes a specific user permission


# **create_or_update_user**
> UserModel create_or_update_user(send_email=send_email, body=body)

Creates or updates a user



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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))
send_email = true # bool | Whether to send email notification to the user, if created.  Default: false (optional)
body = wavefront_api_client.UserToCreate() # UserToCreate | Example Body:  <pre>{   \"emailAddress\": \"user@example.com\",   \"groups\": [     \"browse\"   ] }</pre> (optional)

try:
    # Creates or updates a user
    api_response = api_instance.create_or_update_user(send_email=send_email, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_or_update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_email** | **bool**| Whether to send email notification to the user, if created.  Default: false | [optional] 
 **body** | [**UserToCreate**](UserToCreate.md)| Example Body:  &lt;pre&gt;{   \&quot;emailAddress\&quot;: \&quot;user@example.com\&quot;,   \&quot;groups\&quot;: [     \&quot;browse\&quot;   ] }&lt;/pre&gt; | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(id)

Deletes a user identified by id



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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Deletes a user identified by id
    api_instance.delete_user(id)
except ApiException as e:
    print("Exception when calling UserApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_user**
> list[UserModel] get_all_user()

Get all users

Returns all users

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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))

try:
    # Get all users
    api_response = api_instance.get_all_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_all_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserModel]**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserModel get_user(id)

Retrieves a user by identifier (email addr)



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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Retrieves a user by identifier (email addr)
    api_response = api_instance.get_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_user_permission**
> UserModel grant_user_permission(id, group=group)

Grants a specific user permission



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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
group = 'group_example' # str | Permission group to grant to this user.  Please note that 'host_tag_management' is the equivalent of the 'Source Tag Management' permission (optional)

try:
    # Grants a specific user permission
    api_response = api_instance.grant_user_permission(id, group=group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->grant_user_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **group** | **str**| Permission group to grant to this user.  Please note that &#39;host_tag_management&#39; is the equivalent of the &#39;Source Tag Management&#39; permission | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_user_permission**
> UserModel revoke_user_permission(id, group=group)

Revokes a specific user permission



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
api_instance = wavefront_api_client.UserApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
group = 'group_example' # str |  (optional)

try:
    # Revokes a specific user permission
    api_response = api_instance.revoke_user_permission(id, group=group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->revoke_user_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **group** | **str**|  | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

