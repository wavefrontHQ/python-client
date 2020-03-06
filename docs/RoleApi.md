# wavefront_api_client.RoleApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_assignees**](RoleApi.md#add_assignees) | **POST** /api/v2/role/{id}/addAssignees | Add multiple users and user groups to a specific role
[**create_role**](RoleApi.md#create_role) | **POST** /api/v2/role | Create a specific role
[**delete_role**](RoleApi.md#delete_role) | **DELETE** /api/v2/role/{id} | Delete a specific role
[**get_all_roles**](RoleApi.md#get_all_roles) | **GET** /api/v2/role | Get all roles for a customer
[**get_role**](RoleApi.md#get_role) | **GET** /api/v2/role/{id} | Get a specific role
[**grant_permission_to_roles**](RoleApi.md#grant_permission_to_roles) | **POST** /api/v2/role/grant/{permission} | Grants a single permission to role(s)
[**remove_assignees**](RoleApi.md#remove_assignees) | **POST** /api/v2/role/{id}/removeAssignees | Remove multiple users and user groups from a specific role
[**revoke_permission_from_roles**](RoleApi.md#revoke_permission_from_roles) | **POST** /api/v2/role/revoke/{permission} | Revokes a single permission from role(s)
[**update_role**](RoleApi.md#update_role) | **PUT** /api/v2/role/{id} | Update a specific role


# **add_assignees**
> ResponseContainerRoleDTO add_assignees(id, body=body)

Add multiple users and user groups to a specific role



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
api_instance = wavefront_api_client.RoleApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = [wavefront_api_client.list[str]()] # list[str] | List of users and user groups thatshould be added to role (optional)

try:
    # Add multiple users and user groups to a specific role
    api_response = api_instance.add_assignees(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->add_assignees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **list[str]**| List of users and user groups thatshould be added to role | [optional] 

### Return type

[**ResponseContainerRoleDTO**](ResponseContainerRoleDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> ResponseContainerRoleDTO create_role(body=body)

Create a specific role



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
api_instance = wavefront_api_client.RoleApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.RoleDTO() # RoleDTO | Example Body:  <pre>{   \"name\": \"Role name\",   \"permissions\": [   \"permission1\",   \"permission2\",   \"permission3\"   ],   \"description\": \"Role description\" }</pre> (optional)

try:
    # Create a specific role
    api_response = api_instance.create_role(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->create_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleDTO**](RoleDTO.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;Role name\&quot;,   \&quot;permissions\&quot;: [   \&quot;permission1\&quot;,   \&quot;permission2\&quot;,   \&quot;permission3\&quot;   ],   \&quot;description\&quot;: \&quot;Role description\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerRoleDTO**](ResponseContainerRoleDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> ResponseContainerRoleDTO delete_role(id)

Delete a specific role



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
api_instance = wavefront_api_client.RoleApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a specific role
    api_response = api_instance.delete_role(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerRoleDTO**](ResponseContainerRoleDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_roles**
> ResponseContainerPagedRoleDTO get_all_roles(offset=offset, limit=limit)

Get all roles for a customer



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
api_instance = wavefront_api_client.RoleApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all roles for a customer
    api_response = api_instance.get_all_roles(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->get_all_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedRoleDTO**](ResponseContainerPagedRoleDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> ResponseContainerRoleDTO get_role(id)

Get a specific role



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
api_instance = wavefront_api_client.RoleApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific role
    api_response = api_instance.get_role(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerRoleDTO**](ResponseContainerRoleDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_permission_to_roles**
> ResponseContainerRoleDTO grant_permission_to_roles(permission, body=body)

Grants a single permission to role(s)



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
api_instance = wavefront_api_client.RoleApi(wavefront_api_client.ApiClient(configuration))
permission = 'permission_example' # str | Permission to grant to role(s).
body = [wavefront_api_client.list[str]()] # list[str] | List of roles. (optional)

try:
    # Grants a single permission to role(s)
    api_response = api_instance.grant_permission_to_roles(permission, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->grant_permission_to_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | **str**| Permission to grant to role(s). | 
 **body** | **list[str]**| List of roles. | [optional] 

### Return type

[**ResponseContainerRoleDTO**](ResponseContainerRoleDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_assignees**
> ResponseContainerRoleDTO remove_assignees(id, body=body)

Remove multiple users and user groups from a specific role



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
api_instance = wavefront_api_client.RoleApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = [wavefront_api_client.list[str]()] # list[str] | List of users and user groups thatshould be removed from role (optional)

try:
    # Remove multiple users and user groups from a specific role
    api_response = api_instance.remove_assignees(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->remove_assignees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **list[str]**| List of users and user groups thatshould be removed from role | [optional] 

### Return type

[**ResponseContainerRoleDTO**](ResponseContainerRoleDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_permission_from_roles**
> ResponseContainerRoleDTO revoke_permission_from_roles(permission, body=body)

Revokes a single permission from role(s)



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
api_instance = wavefront_api_client.RoleApi(wavefront_api_client.ApiClient(configuration))
permission = 'permission_example' # str | Permission to revoke from role(s).
body = [wavefront_api_client.list[str]()] # list[str] | List of roles. (optional)

try:
    # Revokes a single permission from role(s)
    api_response = api_instance.revoke_permission_from_roles(permission, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->revoke_permission_from_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | **str**| Permission to revoke from role(s). | 
 **body** | **list[str]**| List of roles. | [optional] 

### Return type

[**ResponseContainerRoleDTO**](ResponseContainerRoleDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> ResponseContainerRoleDTO update_role(id, body=body)

Update a specific role



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
api_instance = wavefront_api_client.RoleApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.RoleDTO() # RoleDTO | Example Body:  <pre>{   \"id\": \"Role identifier\",   \"name\": \"Role name\",   \"permissions\": [   \"permission1\",   \"permission2\",   \"permission3\"   ],   \"description\": \"Role description\" }</pre> (optional)

try:
    # Update a specific role
    api_response = api_instance.update_role(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**RoleDTO**](RoleDTO.md)| Example Body:  &lt;pre&gt;{   \&quot;id\&quot;: \&quot;Role identifier\&quot;,   \&quot;name\&quot;: \&quot;Role name\&quot;,   \&quot;permissions\&quot;: [   \&quot;permission1\&quot;,   \&quot;permission2\&quot;,   \&quot;permission3\&quot;   ],   \&quot;description\&quot;: \&quot;Role description\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerRoleDTO**](ResponseContainerRoleDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

