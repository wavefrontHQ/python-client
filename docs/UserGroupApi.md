# wavefront_api_client.UserGroupApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ingestion_policy**](UserGroupApi.md#add_ingestion_policy) | **POST** /api/v2/usergroup/addIngestionPolicy | Add single ingestion policy to multiple groups
[**add_roles_to_user_group**](UserGroupApi.md#add_roles_to_user_group) | **POST** /api/v2/usergroup/{id}/addRoles | Add multiple roles to a specific user group
[**add_users_to_user_group**](UserGroupApi.md#add_users_to_user_group) | **POST** /api/v2/usergroup/{id}/addUsers | Add multiple users to a specific user group
[**create_user_group**](UserGroupApi.md#create_user_group) | **POST** /api/v2/usergroup | Create a specific user group
[**delete_user_group**](UserGroupApi.md#delete_user_group) | **DELETE** /api/v2/usergroup/{id} | Delete a specific user group
[**get_all_user_groups**](UserGroupApi.md#get_all_user_groups) | **GET** /api/v2/usergroup | Get all user groups for a customer
[**get_user_group**](UserGroupApi.md#get_user_group) | **GET** /api/v2/usergroup/{id} | Get a specific user group
[**remove_ingestion_policy**](UserGroupApi.md#remove_ingestion_policy) | **POST** /api/v2/usergroup/removeIngestionPolicy | Removes single ingestion policy from multiple groups
[**remove_roles_from_user_group**](UserGroupApi.md#remove_roles_from_user_group) | **POST** /api/v2/usergroup/{id}/removeRoles | Remove multiple roles from a specific user group
[**remove_users_from_user_group**](UserGroupApi.md#remove_users_from_user_group) | **POST** /api/v2/usergroup/{id}/removeUsers | Remove multiple users from a specific user group
[**update_user_group**](UserGroupApi.md#update_user_group) | **PUT** /api/v2/usergroup/{id} | Update a specific user group


# **add_ingestion_policy**
> ResponseContainerUserGroupModel add_ingestion_policy(body=body)

Add single ingestion policy to multiple groups



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
body = wavefront_api_client.IngestionPolicyMapping() # IngestionPolicyMapping | Example Body:  <pre>{   \"ingestionPolicyId\": \"Ingestion policy identifier\",   \"accounts\": [   \"account1\",   \"account2\",   \"account3\"   ],   \"groups\": [   \"group1\",   \"group2\"   ] }</pre> (optional)

try:
    # Add single ingestion policy to multiple groups
    api_response = api_instance.add_ingestion_policy(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->add_ingestion_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IngestionPolicyMapping**](IngestionPolicyMapping.md)| Example Body:  &lt;pre&gt;{   \&quot;ingestionPolicyId\&quot;: \&quot;Ingestion policy identifier\&quot;,   \&quot;accounts\&quot;: [   \&quot;account1\&quot;,   \&quot;account2\&quot;,   \&quot;account3\&quot;   ],   \&quot;groups\&quot;: [   \&quot;group1\&quot;,   \&quot;group2\&quot;   ] }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerUserGroupModel**](ResponseContainerUserGroupModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_roles_to_user_group**
> ResponseContainerUserGroupModel add_roles_to_user_group(id, body=body)

Add multiple roles to a specific user group



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
body = [wavefront_api_client.list[str]()] # list[str] | List of roles that should be added to user group (optional)

try:
    # Add multiple roles to a specific user group
    api_response = api_instance.add_roles_to_user_group(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->add_roles_to_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **list[str]**| List of roles that should be added to user group | [optional] 

### Return type

[**ResponseContainerUserGroupModel**](ResponseContainerUserGroupModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_users_to_user_group**
> ResponseContainerUserGroupModel add_users_to_user_group(id, body=body)

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

[**ResponseContainerUserGroupModel**](ResponseContainerUserGroupModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_group**
> ResponseContainerUserGroupModel create_user_group(body=body)

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
body = wavefront_api_client.UserGroupWrite() # UserGroupWrite | Example Body:  <pre>{   \"name\": \"UserGroup name\",   \"roleIDs\": [   \"role1\",   \"role2\",   \"role3\"   ],   \"description\": \"UserGroup description\" }</pre> (optional)

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
 **body** | [**UserGroupWrite**](UserGroupWrite.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;UserGroup name\&quot;,   \&quot;roleIDs\&quot;: [   \&quot;role1\&quot;,   \&quot;role2\&quot;,   \&quot;role3\&quot;   ],   \&quot;description\&quot;: \&quot;UserGroup description\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerUserGroupModel**](ResponseContainerUserGroupModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_group**
> ResponseContainerUserGroupModel delete_user_group(id)

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

[**ResponseContainerUserGroupModel**](ResponseContainerUserGroupModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_user_groups**
> ResponseContainerPagedUserGroupModel get_all_user_groups(offset=offset, limit=limit)

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

[**ResponseContainerPagedUserGroupModel**](ResponseContainerPagedUserGroupModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group**
> ResponseContainerUserGroupModel get_user_group(id)

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

[**ResponseContainerUserGroupModel**](ResponseContainerUserGroupModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_ingestion_policy**
> ResponseContainerUserGroupModel remove_ingestion_policy(body=body)

Removes single ingestion policy from multiple groups



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
body = wavefront_api_client.IngestionPolicyMapping() # IngestionPolicyMapping | Example Body:  <pre>{   \"ingestionPolicyId\": \"Ingestion policy identifier\",   \"accounts\": [   \"account1\",   \"account2\",   \"account3\"   ],   \"groups\": [   \"group1\",   \"group2\"   ] }</pre> (optional)

try:
    # Removes single ingestion policy from multiple groups
    api_response = api_instance.remove_ingestion_policy(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->remove_ingestion_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IngestionPolicyMapping**](IngestionPolicyMapping.md)| Example Body:  &lt;pre&gt;{   \&quot;ingestionPolicyId\&quot;: \&quot;Ingestion policy identifier\&quot;,   \&quot;accounts\&quot;: [   \&quot;account1\&quot;,   \&quot;account2\&quot;,   \&quot;account3\&quot;   ],   \&quot;groups\&quot;: [   \&quot;group1\&quot;,   \&quot;group2\&quot;   ] }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerUserGroupModel**](ResponseContainerUserGroupModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_roles_from_user_group**
> ResponseContainerUserGroupModel remove_roles_from_user_group(id, body=body)

Remove multiple roles from a specific user group



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
body = [wavefront_api_client.list[str]()] # list[str] | List of roles that should be removed from user group (optional)

try:
    # Remove multiple roles from a specific user group
    api_response = api_instance.remove_roles_from_user_group(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->remove_roles_from_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **list[str]**| List of roles that should be removed from user group | [optional] 

### Return type

[**ResponseContainerUserGroupModel**](ResponseContainerUserGroupModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_users_from_user_group**
> ResponseContainerUserGroupModel remove_users_from_user_group(id, body=body)

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

[**ResponseContainerUserGroupModel**](ResponseContainerUserGroupModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_group**
> ResponseContainerUserGroupModel update_user_group(id, body=body)

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
body = wavefront_api_client.UserGroupWrite() # UserGroupWrite | Example Body:  <pre>{   \"id\": \"UserGroup identifier\",   \"name\": \"UserGroup name\",   \"roleIDs\": [   \"role1\",   \"role2\",   \"role3\"   ],   \"description\": \"UserGroup description\" }</pre> (optional)

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
 **body** | [**UserGroupWrite**](UserGroupWrite.md)| Example Body:  &lt;pre&gt;{   \&quot;id\&quot;: \&quot;UserGroup identifier\&quot;,   \&quot;name\&quot;: \&quot;UserGroup name\&quot;,   \&quot;roleIDs\&quot;: [   \&quot;role1\&quot;,   \&quot;role2\&quot;,   \&quot;role3\&quot;   ],   \&quot;description\&quot;: \&quot;UserGroup description\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerUserGroupModel**](ResponseContainerUserGroupModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

