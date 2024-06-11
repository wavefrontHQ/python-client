# wavefront_api_client.RoleApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_assignees**](RoleApi.md#add_assignees) | **POST** /api/v2/role/{id}/addAssignees | Add accounts and groups to a role
[**create_role**](RoleApi.md#create_role) | **POST** /api/v2/role | Create a role
[**delete_role**](RoleApi.md#delete_role) | **DELETE** /api/v2/role/{id} | Delete a role by ID
[**get_all_roles**](RoleApi.md#get_all_roles) | **GET** /api/v2/role | Get all roles
[**get_role**](RoleApi.md#get_role) | **GET** /api/v2/role/{id} | Get a role by ID
[**grant_permission_to_roles**](RoleApi.md#grant_permission_to_roles) | **POST** /api/v2/role/grant/{permission} | Grant a permission to roles
[**remove_assignees**](RoleApi.md#remove_assignees) | **POST** /api/v2/role/{id}/removeAssignees | Remove accounts and groups from a role
[**revoke_permission_from_roles**](RoleApi.md#revoke_permission_from_roles) | **POST** /api/v2/role/revoke/{permission} | Revoke a permission from roles
[**update_role**](RoleApi.md#update_role) | **PUT** /api/v2/role/{id} | Update a role by ID


# **add_assignees**
> ResponseContainerRoleDTO add_assignees(id, body)

Add accounts and groups to a role

Assigns a role with a given ID to a list of user and service accounts and groups. <b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
id = 'id_example' # str | The ID of the role to assign. If you don't know the role's ID, run the <code>Get all roles</code> API call to return all roles and their IDs.
body = [wavefront_api_client.list[str]()] # list[str] | A list of accounts and groups to add to the role.

try:
    # Add accounts and groups to a role
    api_response = api_instance.add_assignees(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->add_assignees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the role to assign. If you don&#39;t know the role&#39;s ID, run the &lt;code&gt;Get all roles&lt;/code&gt; API call to return all roles and their IDs. | 
 **body** | **list[str]**| A list of accounts and groups to add to the role. | 

### Return type

[**ResponseContainerRoleDTO**](ResponseContainerRoleDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> ResponseContainerRoleDTO create_role(body)

Create a role

Creates a role with a specific unique name. Optionally, you can grant permissions to the role, assign the role to accounts and groups, specify a description, and configure the management properties of the role. <b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
body = wavefront_api_client.RoleCreateDTO() # RoleCreateDTO | An example body for a role with all permissions:  <pre>{    \"name\": \"<i>Role_name</i>\",    \"permissions\": [        \"agent_management\", \"alerts_management\",        \"application_management\", \"batch_query_priority\",        \"dashboard_management\", \"derived_metrics_management\",        \"embedded_charts\", \"events_management\",        \"external_links_management\", \"host_tag_management\",        \"ingestion\", \"metrics_management\",        \"monitored_application_service_management\", \"saml_sso_management\",        \"token_management\", \"user_management\"    ],    \"description\": \"<i>Role_description</i>\" }</pre>

try:
    # Create a role
    api_response = api_instance.create_role(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->create_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleCreateDTO**](RoleCreateDTO.md)| An example body for a role with all permissions:  &lt;pre&gt;{    \&quot;name\&quot;: \&quot;&lt;i&gt;Role_name&lt;/i&gt;\&quot;,    \&quot;permissions\&quot;: [        \&quot;agent_management\&quot;, \&quot;alerts_management\&quot;,        \&quot;application_management\&quot;, \&quot;batch_query_priority\&quot;,        \&quot;dashboard_management\&quot;, \&quot;derived_metrics_management\&quot;,        \&quot;embedded_charts\&quot;, \&quot;events_management\&quot;,        \&quot;external_links_management\&quot;, \&quot;host_tag_management\&quot;,        \&quot;ingestion\&quot;, \&quot;metrics_management\&quot;,        \&quot;monitored_application_service_management\&quot;, \&quot;saml_sso_management\&quot;,        \&quot;token_management\&quot;, \&quot;user_management\&quot;    ],    \&quot;description\&quot;: \&quot;&lt;i&gt;Role_description&lt;/i&gt;\&quot; }&lt;/pre&gt; | 

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

Delete a role by ID

Deletes a role with a given ID. <b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
id = 'id_example' # str | The ID of the role to delete. If you don't know the role's ID, run the <code>Get all roles</code> API call to return all roles and their IDs.

try:
    # Delete a role by ID
    api_response = api_instance.delete_role(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the role to delete. If you don&#39;t know the role&#39;s ID, run the &lt;code&gt;Get all roles&lt;/code&gt; API call to return all roles and their IDs. | 

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

Get all roles

Returns all existing roles in the service instance with detailed information for each role, including assigned groups and accounts, management properties, permissions, name, ID, description, and the time of the last update and who has done it. <b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
    # Get all roles
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

Get a role by ID

Returns the details of a role with a given ID. The response includes assigned groups and accounts, management properties, permissions, name, description, and the time of the last update and who has done it. <b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
id = 'id_example' # str | The ID of the role to get. If you don't know the role's ID, run the <code>Get all roles</code> API call to return all roles and their IDs.

try:
    # Get a role by ID
    api_response = api_instance.get_role(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the role to get. If you don&#39;t know the role&#39;s ID, run the &lt;code&gt;Get all roles&lt;/code&gt; API call to return all roles and their IDs. | 

### Return type

[**ResponseContainerRoleDTO**](ResponseContainerRoleDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_permission_to_roles**
> ResponseContainerRoleDTO grant_permission_to_roles(permission, body)

Grant a permission to roles

Grants a given permission to a list of roles. <b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
permission = 'permission_example' # str | The permission to grant. Note that <code>host_tag_management</code> is the equivalent of the **Source Tag Management** permission, <code>monitored_application_service_management</code> is the equivalent of the **Integrations** permission, <code>agent_management</code> is the equivalent of the **Proxies** permission.
body = [wavefront_api_client.list[str]()] # list[str] | A list of role IDs to which to grant the permission.

try:
    # Grant a permission to roles
    api_response = api_instance.grant_permission_to_roles(permission, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->grant_permission_to_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | **str**| The permission to grant. Note that &lt;code&gt;host_tag_management&lt;/code&gt; is the equivalent of the **Source Tag Management** permission, &lt;code&gt;monitored_application_service_management&lt;/code&gt; is the equivalent of the **Integrations** permission, &lt;code&gt;agent_management&lt;/code&gt; is the equivalent of the **Proxies** permission. | 
 **body** | **list[str]**| A list of role IDs to which to grant the permission. | 

### Return type

[**ResponseContainerRoleDTO**](ResponseContainerRoleDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_assignees**
> ResponseContainerRoleDTO remove_assignees(id, body)

Remove accounts and groups from a role

Revokes a role with a given ID from a list of user and service accounts and groups. <b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
id = 'id_example' # str | The ID of the role to revoke. If you don't know the role's ID, run the <code>Get all roles</code> API call to return all roles and their IDs.
body = [wavefront_api_client.list[str]()] # list[str] | A list of accounts and groups to remove from the role.

try:
    # Remove accounts and groups from a role
    api_response = api_instance.remove_assignees(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->remove_assignees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the role to revoke. If you don&#39;t know the role&#39;s ID, run the &lt;code&gt;Get all roles&lt;/code&gt; API call to return all roles and their IDs. | 
 **body** | **list[str]**| A list of accounts and groups to remove from the role. | 

### Return type

[**ResponseContainerRoleDTO**](ResponseContainerRoleDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_permission_from_roles**
> ResponseContainerRoleDTO revoke_permission_from_roles(permission, body)

Revoke a permission from roles

Revokes a given permission from a list of roles. <b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
permission = 'permission_example' # str | The permission to revoke. Note that <code>host_tag_management</code> is the equivalent of the **Source Tag Management** permission, <code>monitored_application_service_management</code> is the equivalent of the **Integrations** permission, <code>agent_management</code> is the equivalent of the **Proxies** permission.
body = [wavefront_api_client.list[str]()] # list[str] | A list of role IDs from which to revoke the permission.

try:
    # Revoke a permission from roles
    api_response = api_instance.revoke_permission_from_roles(permission, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->revoke_permission_from_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | **str**| The permission to revoke. Note that &lt;code&gt;host_tag_management&lt;/code&gt; is the equivalent of the **Source Tag Management** permission, &lt;code&gt;monitored_application_service_management&lt;/code&gt; is the equivalent of the **Integrations** permission, &lt;code&gt;agent_management&lt;/code&gt; is the equivalent of the **Proxies** permission. | 
 **body** | **list[str]**| A list of role IDs from which to revoke the permission. | 

### Return type

[**ResponseContainerRoleDTO**](ResponseContainerRoleDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> ResponseContainerRoleDTO update_role(id, body)

Update a role by ID

Updates a role with a given ID. You can update the assigned groups and accounts, management properties, permissions, ID, name, and description. <b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
id = 'id_example' # str | The ID of the role to update. If you don't know the role's ID, run the <code>Get all roles</code> API call to return all roles and their IDs.
body = wavefront_api_client.RoleUpdateDTO() # RoleUpdateDTO | You can first run the <code>Get a role by ID</code> API call, and then you can copy and edit the response body. An example body for a role with all permissions:  <pre>{   \"id\": \"<i>Role_ID</i>\",   \"name\": \"<i>Role_name</i>\",   \"permissions\": [      \"agent_management\", \"alerts_management\",      \"application_management\", \"batch_query_priority\",      \"derived_metrics_management\", \"dashboard_management\",      \"embedded_charts\", \"events_management\",      \"external_links_management\", \"host_tag_management\",      \"ingestion\", \"metrics_management\",      \"monitored_application_service_management\", \"saml_sso_management\",      \"token_management\", \"user_management\"   ],   \"description\": \"<i>Role_description</i>\" }</pre>

try:
    # Update a role by ID
    api_response = api_instance.update_role(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the role to update. If you don&#39;t know the role&#39;s ID, run the &lt;code&gt;Get all roles&lt;/code&gt; API call to return all roles and their IDs. | 
 **body** | [**RoleUpdateDTO**](RoleUpdateDTO.md)| You can first run the &lt;code&gt;Get a role by ID&lt;/code&gt; API call, and then you can copy and edit the response body. An example body for a role with all permissions:  &lt;pre&gt;{   \&quot;id\&quot;: \&quot;&lt;i&gt;Role_ID&lt;/i&gt;\&quot;,   \&quot;name\&quot;: \&quot;&lt;i&gt;Role_name&lt;/i&gt;\&quot;,   \&quot;permissions\&quot;: [      \&quot;agent_management\&quot;, \&quot;alerts_management\&quot;,      \&quot;application_management\&quot;, \&quot;batch_query_priority\&quot;,      \&quot;derived_metrics_management\&quot;, \&quot;dashboard_management\&quot;,      \&quot;embedded_charts\&quot;, \&quot;events_management\&quot;,      \&quot;external_links_management\&quot;, \&quot;host_tag_management\&quot;,      \&quot;ingestion\&quot;, \&quot;metrics_management\&quot;,      \&quot;monitored_application_service_management\&quot;, \&quot;saml_sso_management\&quot;,      \&quot;token_management\&quot;, \&quot;user_management\&quot;   ],   \&quot;description\&quot;: \&quot;&lt;i&gt;Role_description&lt;/i&gt;\&quot; }&lt;/pre&gt; | 

### Return type

[**ResponseContainerRoleDTO**](ResponseContainerRoleDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

