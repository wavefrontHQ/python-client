# wavefront_api_client.UserGroupApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_users_to_user_group**](UserGroupApi.md#add_users_to_user_group) | **POST** /api/v2/usergroup/{id}/addUsers | Add multiple users to a specific user group
[**create_user_group**](UserGroupApi.md#create_user_group) | **POST** /api/v2/usergroup | Create a specific user group
[**delete_user_group**](UserGroupApi.md#delete_user_group) | **DELETE** /api/v2/usergroup/{id} | Delete a specific user group
[**get_all_user_groups**](UserGroupApi.md#get_all_user_groups) | **GET** /api/v2/usergroup | Get all user groups for a customer
[**get_user_group**](UserGroupApi.md#get_user_group) | **GET** /api/v2/usergroup/{id} | Get a specific user group
[**grant_permission_to_user_groups**](UserGroupApi.md#grant_permission_to_user_groups) | **POST** /api/v2/usergroup/grant/{permission} | Grants a single permission to user group(s)
[**remove_users_from_user_group**](UserGroupApi.md#remove_users_from_user_group) | **POST** /api/v2/usergroup/{id}/removeUsers | Remove multiple users from a specific user group
[**revoke_permission_from_user_groups**](UserGroupApi.md#revoke_permission_from_user_groups) | **POST** /api/v2/usergroup/revoke/{permission} | Revokes a single permission from user group(s)
[**update_user_group**](UserGroupApi.md#update_user_group) | **PUT** /api/v2/usergroup/{id} | Update a specific user group


# **add_users_to_user_group**
> ResponseContainerUserGroup add_users_to_user_group(id, body=body)

Add multiple users to a specific user group



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
api_instance = wavefront_api_client.UserGroupApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = [wavefront_api_client.list[str]()] # list[str] | List of users that should be added to user group (optional)

try:
    # Add multiple users to a specific user group
    api_response = api_instance.add_users_to_user_group(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->add_users_to_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **list[str]**| List of users that should be added to user group | [optional] 

### Return type

[**ResponseContainerUserGroup**](ResponseContainerUserGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_group**
> ResponseContainerUserGroup create_user_group(body=body)

Create a specific user group



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
api_instance = wavefront_api_client.UserGroupApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.UserGroupWrite() # UserGroupWrite | Example Body:  <pre>{   \"name\": \"UserGroup name\",   \"permissions\": [   \"permission1\",   \"permission2\",   \"permission3\"   ] }</pre> (optional)

try:
    # Create a specific user group
    api_response = api_instance.create_user_group(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->create_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserGroupWrite**](UserGroupWrite.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;UserGroup name\&quot;,   \&quot;permissions\&quot;: [   \&quot;permission1\&quot;,   \&quot;permission2\&quot;,   \&quot;permission3\&quot;   ] }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerUserGroup**](ResponseContainerUserGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_group**
> ResponseContainerUserGroup delete_user_group(id)

Delete a specific user group



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
api_instance = wavefront_api_client.UserGroupApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a specific user group
    api_response = api_instance.delete_user_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->delete_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerUserGroup**](ResponseContainerUserGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_user_groups**
> ResponseContainerPagedUserGroup get_all_user_groups(offset=offset, limit=limit)

Get all user groups for a customer



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
api_instance = wavefront_api_client.UserGroupApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all user groups for a customer
    api_response = api_instance.get_all_user_groups(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->get_all_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedUserGroup**](ResponseContainerPagedUserGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group**
> ResponseContainerUserGroup get_user_group(id)

Get a specific user group



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
api_instance = wavefront_api_client.UserGroupApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific user group
    api_response = api_instance.get_user_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->get_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerUserGroup**](ResponseContainerUserGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_permission_to_user_groups**
> ResponseContainerUserGroup grant_permission_to_user_groups(permission, body=body)

Grants a single permission to user group(s)



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
api_instance = wavefront_api_client.UserGroupApi(wavefront_api_client.ApiClient(configuration))
permission = 'permission_example' # str | Permission to grant to user group(s).
body = [wavefront_api_client.list[str]()] # list[str] | List of user groups. (optional)

try:
    # Grants a single permission to user group(s)
    api_response = api_instance.grant_permission_to_user_groups(permission, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->grant_permission_to_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | **str**| Permission to grant to user group(s). | 
 **body** | **list[str]**| List of user groups. | [optional] 

### Return type

[**ResponseContainerUserGroup**](ResponseContainerUserGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_users_from_user_group**
> ResponseContainerUserGroup remove_users_from_user_group(id, body=body)

Remove multiple users from a specific user group



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
api_instance = wavefront_api_client.UserGroupApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = [wavefront_api_client.list[str]()] # list[str] | List of users that should be removed from user group (optional)

try:
    # Remove multiple users from a specific user group
    api_response = api_instance.remove_users_from_user_group(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->remove_users_from_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **list[str]**| List of users that should be removed from user group | [optional] 

### Return type

[**ResponseContainerUserGroup**](ResponseContainerUserGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_permission_from_user_groups**
> ResponseContainerUserGroup revoke_permission_from_user_groups(permission, body=body)

Revokes a single permission from user group(s)



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
api_instance = wavefront_api_client.UserGroupApi(wavefront_api_client.ApiClient(configuration))
permission = 'permission_example' # str | Permission to revoke from user group(s).
body = [wavefront_api_client.list[str]()] # list[str] | List of user groups. (optional)

try:
    # Revokes a single permission from user group(s)
    api_response = api_instance.revoke_permission_from_user_groups(permission, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->revoke_permission_from_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | **str**| Permission to revoke from user group(s). | 
 **body** | **list[str]**| List of user groups. | [optional] 

### Return type

[**ResponseContainerUserGroup**](ResponseContainerUserGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_group**
> ResponseContainerUserGroup update_user_group(id, body=body)

Update a specific user group



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
api_instance = wavefront_api_client.UserGroupApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.UserGroupWrite() # UserGroupWrite | Example Body:  <pre>{   \"id\": \"UserGroup identifier\",   \"name\": \"UserGroup name\",   \"permissions\": [   \"permission1\",   \"permission2\",   \"permission3\"   ] }</pre> (optional)

try:
    # Update a specific user group
    api_response = api_instance.update_user_group(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->update_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**UserGroupWrite**](UserGroupWrite.md)| Example Body:  &lt;pre&gt;{   \&quot;id\&quot;: \&quot;UserGroup identifier\&quot;,   \&quot;name\&quot;: \&quot;UserGroup name\&quot;,   \&quot;permissions\&quot;: [   \&quot;permission1\&quot;,   \&quot;permission2\&quot;,   \&quot;permission3\&quot;   ] }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerUserGroup**](ResponseContainerUserGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

