# wavefront_client.UserApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_rest**](UserApi.md#create_user_rest) | **POST** /api/user/create | Creates a new user
[**delete_user_rest**](UserApi.md#delete_user_rest) | **DELETE** /api/user/{id} | Deletes a user identified by {id}
[**get_all_users_rest**](UserApi.md#get_all_users_rest) | **GET** /api/user/all | Get all users
[**get_user_rest**](UserApi.md#get_user_rest) | **GET** /api/user/{id} | Retrieves a user by identifier (email addr)
[**grant_user_rest**](UserApi.md#grant_user_rest) | **POST** /api/user/{id}/grant | Grants a specific user permission
[**revoke_user_rest**](UserApi.md#revoke_user_rest) | **POST** /api/user/{id}/revoke | Revokes a specific user permission


# **create_user_rest**
> User create_user_rest(send_email=send_email, id=id, groups=groups)

Creates a new user



### Example 
```python
import time
import wavefront_client
from wavefront_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
wavefront_client.configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# wavefront_client.configuration.api_key_prefix['X-AUTH-TOKEN'] = 'BEARER'

# create an instance of the API class
api_instance = wavefront_client.UserApi()
send_email = true # bool | Whether to send email notification to the created user.  Defaults to false (optional)
id = 'id_example' # str | The (unique) identifier of the user to create.  Must be a valid email address (optional)
groups = ['groups_example'] # list[str] | List of permission groups to grant to this user.  Please note that 'host_tag_management' is the equivalent of the 'Source Tag Management' permission.  Also, please send a list of values as 'groups=val1&groups=val2'.  NOTE: due to a bug in a library, the API console does not currently format requests with multiple selected groups properly. (The actual API endpoint will work fine.) (optional)

try: 
    # Creates a new user
    api_response = api_instance.create_user_rest(send_email=send_email, id=id, groups=groups)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->create_user_rest: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_email** | **bool**| Whether to send email notification to the created user.  Defaults to false | [optional] 
 **id** | **str**| The (unique) identifier of the user to create.  Must be a valid email address | [optional] 
 **groups** | [**list[str]**](str.md)| List of permission groups to grant to this user.  Please note that &#39;host_tag_management&#39; is the equivalent of the &#39;Source Tag Management&#39; permission.  Also, please send a list of values as &#39;groups&#x3D;val1&amp;groups&#x3D;val2&#39;.  NOTE: due to a bug in a library, the API console does not currently format requests with multiple selected groups properly. (The actual API endpoint will work fine.) | [optional] 

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_rest**
> delete_user_rest(id)

Deletes a user identified by {id}



### Example 
```python
import time
import wavefront_client
from wavefront_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
wavefront_client.configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# wavefront_client.configuration.api_key_prefix['X-AUTH-TOKEN'] = 'BEARER'

# create an instance of the API class
api_instance = wavefront_client.UserApi()
id = 'id_example' # str | 

try: 
    # Deletes a user identified by {id}
    api_instance.delete_user_rest(id)
except ApiException as e:
    print "Exception when calling UserApi->delete_user_rest: %s\n" % e
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users_rest**
> list[User] get_all_users_rest()

Get all users

Returns all users

### Example 
```python
import time
import wavefront_client
from wavefront_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
wavefront_client.configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# wavefront_client.configuration.api_key_prefix['X-AUTH-TOKEN'] = 'BEARER'

# create an instance of the API class
api_instance = wavefront_client.UserApi()

try: 
    # Get all users
    api_response = api_instance.get_all_users_rest()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->get_all_users_rest: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[User]**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_rest**
> User get_user_rest(id)

Retrieves a user by identifier (email addr)



### Example 
```python
import time
import wavefront_client
from wavefront_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
wavefront_client.configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# wavefront_client.configuration.api_key_prefix['X-AUTH-TOKEN'] = 'BEARER'

# create an instance of the API class
api_instance = wavefront_client.UserApi()
id = 'id_example' # str | 

try: 
    # Retrieves a user by identifier (email addr)
    api_response = api_instance.get_user_rest(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->get_user_rest: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_user_rest**
> User grant_user_rest(id, group=group)

Grants a specific user permission



### Example 
```python
import time
import wavefront_client
from wavefront_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
wavefront_client.configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# wavefront_client.configuration.api_key_prefix['X-AUTH-TOKEN'] = 'BEARER'

# create an instance of the API class
api_instance = wavefront_client.UserApi()
id = 'id_example' # str | 
group = 'group_example' # str | Permission group to grant to this user.  Please note that 'host_tag_management' is the equivalent of the 'Source Tag Management' permission (optional)

try: 
    # Grants a specific user permission
    api_response = api_instance.grant_user_rest(id, group=group)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->grant_user_rest: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **group** | **str**| Permission group to grant to this user.  Please note that &#39;host_tag_management&#39; is the equivalent of the &#39;Source Tag Management&#39; permission | [optional] 

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_user_rest**
> User revoke_user_rest(id, group=group)

Revokes a specific user permission



### Example 
```python
import time
import wavefront_client
from wavefront_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
wavefront_client.configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# wavefront_client.configuration.api_key_prefix['X-AUTH-TOKEN'] = 'BEARER'

# create an instance of the API class
api_instance = wavefront_client.UserApi()
id = 'id_example' # str | 
group = 'group_example' # str | Permission group to revoke from this user.  Please note that 'host_tag_management' is the equivalent of the 'Source Tag Management' permission (optional)

try: 
    # Revokes a specific user permission
    api_response = api_instance.revoke_user_rest(id, group=group)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UserApi->revoke_user_rest: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **group** | **str**| Permission group to revoke from this user.  Please note that &#39;host_tag_management&#39; is the equivalent of the &#39;Source Tag Management&#39; permission | [optional] 

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

