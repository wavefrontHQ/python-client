# wavefront_api_client.AccountUserAndServiceAccountApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_account**](AccountUserAndServiceAccountApi.md#activate_account) | **POST** /api/v2/account/serviceaccount/{id}/activate | Activates the given service account
[**add_account_to_roles**](AccountUserAndServiceAccountApi.md#add_account_to_roles) | **POST** /api/v2/account/{id}/addRoles | Adds specific roles to the account (user or service account)
[**add_account_to_user_groups**](AccountUserAndServiceAccountApi.md#add_account_to_user_groups) | **POST** /api/v2/account/{id}/addUserGroups | Adds specific groups to the account (user or service account)
[**create_or_update_user_account**](AccountUserAndServiceAccountApi.md#create_or_update_user_account) | **POST** /api/v2/account/user | Creates or updates a user account
[**create_service_account**](AccountUserAndServiceAccountApi.md#create_service_account) | **POST** /api/v2/account/serviceaccount | Creates a service account
[**deactivate_account**](AccountUserAndServiceAccountApi.md#deactivate_account) | **POST** /api/v2/account/serviceaccount/{id}/deactivate | Deactivates the given service account
[**delete_account**](AccountUserAndServiceAccountApi.md#delete_account) | **DELETE** /api/v2/account/{id} | Deletes an account (user or service account) identified by id
[**delete_multiple_accounts**](AccountUserAndServiceAccountApi.md#delete_multiple_accounts) | **POST** /api/v2/account/deleteAccounts | Deletes multiple accounts (users or service accounts)
[**get_account**](AccountUserAndServiceAccountApi.md#get_account) | **GET** /api/v2/account/{id} | Get a specific account (user or service account)
[**get_account_business_functions**](AccountUserAndServiceAccountApi.md#get_account_business_functions) | **GET** /api/v2/account/{id}/businessFunctions | Returns business functions of a specific account (user or service account).
[**get_all_accounts**](AccountUserAndServiceAccountApi.md#get_all_accounts) | **GET** /api/v2/account | Get all accounts (users and service accounts) of a customer
[**get_all_service_accounts**](AccountUserAndServiceAccountApi.md#get_all_service_accounts) | **GET** /api/v2/account/serviceaccount | Get all service accounts
[**get_all_user_accounts**](AccountUserAndServiceAccountApi.md#get_all_user_accounts) | **GET** /api/v2/account/user | Get all user accounts
[**get_service_account**](AccountUserAndServiceAccountApi.md#get_service_account) | **GET** /api/v2/account/serviceaccount/{id} | Retrieves a service account by identifier
[**get_user_account**](AccountUserAndServiceAccountApi.md#get_user_account) | **GET** /api/v2/account/user/{id} | Retrieves a user by identifier (email address)
[**get_users_with_accounts_permission**](AccountUserAndServiceAccountApi.md#get_users_with_accounts_permission) | **GET** /api/v2/account/user/admin | Get all users with Accounts permission
[**grant_account_permission**](AccountUserAndServiceAccountApi.md#grant_account_permission) | **POST** /api/v2/account/{id}/grant/{permission} | Grants a specific permission to account (user or service account)
[**grant_permission_to_accounts**](AccountUserAndServiceAccountApi.md#grant_permission_to_accounts) | **POST** /api/v2/account/grant/{permission} | Grant a permission to accounts (users or service accounts)
[**invite_user_accounts**](AccountUserAndServiceAccountApi.md#invite_user_accounts) | **POST** /api/v2/account/user/invite | Invite user accounts with given user groups and permissions.
[**remove_account_from_roles**](AccountUserAndServiceAccountApi.md#remove_account_from_roles) | **POST** /api/v2/account/{id}/removeRoles | Removes specific roles from the account (user or service account)
[**remove_account_from_user_groups**](AccountUserAndServiceAccountApi.md#remove_account_from_user_groups) | **POST** /api/v2/account/{id}/removeUserGroups | Removes specific groups from the account (user or service account)
[**revoke_account_permission**](AccountUserAndServiceAccountApi.md#revoke_account_permission) | **POST** /api/v2/account/{id}/revoke/{permission} | Revokes a specific permission from account (user or service account)
[**revoke_permission_from_accounts**](AccountUserAndServiceAccountApi.md#revoke_permission_from_accounts) | **POST** /api/v2/account/revoke/{permission} | Revoke a permission from accounts (users or service accounts)
[**update_service_account**](AccountUserAndServiceAccountApi.md#update_service_account) | **PUT** /api/v2/account/serviceaccount/{id} | Updates the service account
[**update_user_account**](AccountUserAndServiceAccountApi.md#update_user_account) | **PUT** /api/v2/account/user/{id} | Update user with given user groups and permissions.
[**validate_accounts**](AccountUserAndServiceAccountApi.md#validate_accounts) | **POST** /api/v2/account/validateAccounts | Returns valid accounts (users and service accounts), also invalid identifiers from the given list


# **activate_account**
> ResponseContainerServiceAccount activate_account(id)

Activates the given service account



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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Activates the given service account
    api_response = api_instance.activate_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->activate_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerServiceAccount**](ResponseContainerServiceAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_account_to_roles**
> UserModel add_account_to_roles(id, body=body)

Adds specific roles to the account (user or service account)

<b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = [wavefront_api_client.list[str]()] # list[str] | The list of roles that should be added to the account (optional)

try:
    # Adds specific roles to the account (user or service account)
    api_response = api_instance.add_account_to_roles(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->add_account_to_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **list[str]**| The list of roles that should be added to the account | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_account_to_user_groups**
> UserModel add_account_to_user_groups(id, body=body)

Adds specific groups to the account (user or service account)

<b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = [wavefront_api_client.list[str]()] # list[str] | The list of groups that should be added to the account (optional)

try:
    # Adds specific groups to the account (user or service account)
    api_response = api_instance.add_account_to_user_groups(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->add_account_to_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **list[str]**| The list of groups that should be added to the account | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_user_account**
> UserModel create_or_update_user_account(send_email=send_email, body=body)

Creates or updates a user account

<b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
send_email = true # bool | Whether to send email notification to the user, if created.  Default: false (optional)
body = wavefront_api_client.UserToCreate() # UserToCreate | Example Body:  <pre>{   \"emailAddress\": \"user@example.com\",   \"groups\": [     \"user_management\"   ],   \"userGroups\": [     \"8b23136b-ecd2-4cb5-8c92-62477dcc4090\"   ],   \"roles\": [     \"Role\"   ], }</pre> (optional)

try:
    # Creates or updates a user account
    api_response = api_instance.create_or_update_user_account(send_email=send_email, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->create_or_update_user_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_email** | **bool**| Whether to send email notification to the user, if created.  Default: false | [optional] 
 **body** | [**UserToCreate**](UserToCreate.md)| Example Body:  &lt;pre&gt;{   \&quot;emailAddress\&quot;: \&quot;user@example.com\&quot;,   \&quot;groups\&quot;: [     \&quot;user_management\&quot;   ],   \&quot;userGroups\&quot;: [     \&quot;8b23136b-ecd2-4cb5-8c92-62477dcc4090\&quot;   ],   \&quot;roles\&quot;: [     \&quot;Role\&quot;   ], }&lt;/pre&gt; | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service_account**
> ResponseContainerServiceAccount create_service_account(body=body)

Creates a service account



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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.ServiceAccountWrite() # ServiceAccountWrite |  (optional)

try:
    # Creates a service account
    api_response = api_instance.create_service_account(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->create_service_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceAccountWrite**](ServiceAccountWrite.md)|  | [optional] 

### Return type

[**ResponseContainerServiceAccount**](ResponseContainerServiceAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_account**
> ResponseContainerServiceAccount deactivate_account(id)

Deactivates the given service account



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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Deactivates the given service account
    api_response = api_instance.deactivate_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->deactivate_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerServiceAccount**](ResponseContainerServiceAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account**
> ResponseContainerAccount delete_account(id)

Deletes an account (user or service account) identified by id

<b>Note</b>: For original Tanzu Observability instances, applies to user accounts and service accounts. For Tanzu Observability instances that are onboarded to VMware Cloud services, applies only to service accounts.

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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Deletes an account (user or service account) identified by id
    api_response = api_instance.delete_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerAccount**](ResponseContainerAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_multiple_accounts**
> ResponseContainerListString delete_multiple_accounts(body=body)

Deletes multiple accounts (users or service accounts)

<b>Note</b>: For original Tanzu Observability instances, applies to user accounts and service accounts. For Tanzu Observability instances that are onboarded to VMware Cloud services, applies only to service accounts.

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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
body = [wavefront_api_client.list[str]()] # list[str] | list of accounts' identifiers to be deleted (optional)

try:
    # Deletes multiple accounts (users or service accounts)
    api_response = api_instance.delete_multiple_accounts(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->delete_multiple_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| list of accounts&#39; identifiers to be deleted | [optional] 

### Return type

[**ResponseContainerListString**](ResponseContainerListString.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> ResponseContainerAccount get_account(id)

Get a specific account (user or service account)

<b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific account (user or service account)
    api_response = api_instance.get_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerAccount**](ResponseContainerAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_business_functions**
> ResponseContainerSetBusinessFunction get_account_business_functions(id)

Returns business functions of a specific account (user or service account).



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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Returns business functions of a specific account (user or service account).
    api_response = api_instance.get_account_business_functions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->get_account_business_functions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerSetBusinessFunction**](ResponseContainerSetBusinessFunction.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_accounts**
> ResponseContainerPagedAccount get_all_accounts(offset=offset, limit=limit)

Get all accounts (users and service accounts) of a customer

<b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all accounts (users and service accounts) of a customer
    api_response = api_instance.get_all_accounts(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->get_all_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedAccount**](ResponseContainerPagedAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_service_accounts**
> ResponseContainerListServiceAccount get_all_service_accounts()

Get all service accounts



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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))

try:
    # Get all service accounts
    api_response = api_instance.get_all_service_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->get_all_service_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseContainerListServiceAccount**](ResponseContainerListServiceAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_user_accounts**
> ResponseContainerListUserDTO get_all_user_accounts()

Get all user accounts

<b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))

try:
    # Get all user accounts
    api_response = api_instance.get_all_user_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->get_all_user_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseContainerListUserDTO**](ResponseContainerListUserDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_account**
> ResponseContainerServiceAccount get_service_account(id)

Retrieves a service account by identifier



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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Retrieves a service account by identifier
    api_response = api_instance.get_service_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->get_service_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerServiceAccount**](ResponseContainerServiceAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_account**
> UserModel get_user_account(id)

Retrieves a user by identifier (email address)

<b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Retrieves a user by identifier (email address)
    api_response = api_instance.get_user_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->get_user_account: %s\n" % e)
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

# **get_users_with_accounts_permission**
> ResponseContainerListString get_users_with_accounts_permission()

Get all users with Accounts permission

<b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))

try:
    # Get all users with Accounts permission
    api_response = api_instance.get_users_with_accounts_permission()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->get_users_with_accounts_permission: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseContainerListString**](ResponseContainerListString.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_account_permission**
> UserModel grant_account_permission(id, permission)

Grants a specific permission to account (user or service account)

<b>Note</b>: For original Tanzu Observability instances, applies to user accounts and service accounts. For Tanzu Observability instances that are onboarded to VMware Cloud services, applies only to service accounts.

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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
permission = 'permission_example' # str | Permission to grant to the account. Please note that'host_tag_management' is the equivalent of the 'Source Tag Management' permission

try:
    # Grants a specific permission to account (user or service account)
    api_response = api_instance.grant_account_permission(id, permission)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->grant_account_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **permission** | **str**| Permission to grant to the account. Please note that&#39;host_tag_management&#39; is the equivalent of the &#39;Source Tag Management&#39; permission | 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_permission_to_accounts**
> UserModel grant_permission_to_accounts(permission, body=body)

Grant a permission to accounts (users or service accounts)

<b>Note</b>: For original Tanzu Observability instances, applies to user accounts and service accounts. For Tanzu Observability instances that are onboarded to VMware Cloud services, applies only to service accounts.

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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
permission = 'permission_example' # str | The permission to grant. Note that <code>host_tag_management</code> is the equivalent of the **Source Tag Management** permission, <code>monitored_application_service_management</code> is the equivalent of the **Integrations** permission, <code>agent_management</code> is the equivalent of the **Proxies** permission.
body = [wavefront_api_client.list[str]()] # list[str] | List of accounts the specified permission to be granted to (optional)

try:
    # Grant a permission to accounts (users or service accounts)
    api_response = api_instance.grant_permission_to_accounts(permission, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->grant_permission_to_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | **str**| The permission to grant. Note that &lt;code&gt;host_tag_management&lt;/code&gt; is the equivalent of the **Source Tag Management** permission, &lt;code&gt;monitored_application_service_management&lt;/code&gt; is the equivalent of the **Integrations** permission, &lt;code&gt;agent_management&lt;/code&gt; is the equivalent of the **Proxies** permission. | 
 **body** | **list[str]**| List of accounts the specified permission to be granted to | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_user_accounts**
> UserModel invite_user_accounts(body=body)

Invite user accounts with given user groups and permissions.

<b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
body = [wavefront_api_client.UserToCreate()] # list[UserToCreate] | Example Body:  <pre>[ {   \"emailAddress\": \"user@example.com\",   \"groups\": [     \"user_management\"   ],   \"userGroups\": [     \"8b23136b-ecd2-4cb5-8c92-62477dcc4090\"   ],   \"roles\": [     \"Role\"   ], } ]</pre> (optional)

try:
    # Invite user accounts with given user groups and permissions.
    api_response = api_instance.invite_user_accounts(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->invite_user_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[UserToCreate]**](UserToCreate.md)| Example Body:  &lt;pre&gt;[ {   \&quot;emailAddress\&quot;: \&quot;user@example.com\&quot;,   \&quot;groups\&quot;: [     \&quot;user_management\&quot;   ],   \&quot;userGroups\&quot;: [     \&quot;8b23136b-ecd2-4cb5-8c92-62477dcc4090\&quot;   ],   \&quot;roles\&quot;: [     \&quot;Role\&quot;   ], } ]&lt;/pre&gt; | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_account_from_roles**
> UserModel remove_account_from_roles(id, body=body)

Removes specific roles from the account (user or service account)

<b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = [wavefront_api_client.list[str]()] # list[str] | The list of roles that should be removed from the account (optional)

try:
    # Removes specific roles from the account (user or service account)
    api_response = api_instance.remove_account_from_roles(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->remove_account_from_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **list[str]**| The list of roles that should be removed from the account | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_account_from_user_groups**
> UserModel remove_account_from_user_groups(id, body=body)

Removes specific groups from the account (user or service account)

<b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = [wavefront_api_client.list[str]()] # list[str] | The list of groups that should be removed from the account (optional)

try:
    # Removes specific groups from the account (user or service account)
    api_response = api_instance.remove_account_from_user_groups(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->remove_account_from_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **list[str]**| The list of groups that should be removed from the account | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_account_permission**
> UserModel revoke_account_permission(id, permission)

Revokes a specific permission from account (user or service account)

<b>Note</b>: For original Tanzu Observability instances, applies to user accounts and service accounts. For Tanzu Observability instances that are onboarded to VMware Cloud services, applies only to service accounts.

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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
permission = 'permission_example' # str | 

try:
    # Revokes a specific permission from account (user or service account)
    api_response = api_instance.revoke_account_permission(id, permission)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->revoke_account_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **permission** | **str**|  | 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_permission_from_accounts**
> UserModel revoke_permission_from_accounts(permission, body=body)

Revoke a permission from accounts (users or service accounts)

<b>Note</b>: For original Tanzu Observability instances, applies to user accounts and service accounts. For Tanzu Observability instances that are onboarded to VMware Cloud services, applies only to service accounts.

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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
permission = 'permission_example' # str | The permission to revoke. Note that <code>host_tag_management</code> is the equivalent of the **Source Tag Management** permission, <code>monitored_application_service_management</code> is the equivalent of the **Integrations** permission, <code>agent_management</code> is the equivalent of the **Proxies** permission.
body = [wavefront_api_client.list[str]()] # list[str] | List of accounts the specified permission to be revoked from (optional)

try:
    # Revoke a permission from accounts (users or service accounts)
    api_response = api_instance.revoke_permission_from_accounts(permission, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->revoke_permission_from_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | **str**| The permission to revoke. Note that &lt;code&gt;host_tag_management&lt;/code&gt; is the equivalent of the **Source Tag Management** permission, &lt;code&gt;monitored_application_service_management&lt;/code&gt; is the equivalent of the **Integrations** permission, &lt;code&gt;agent_management&lt;/code&gt; is the equivalent of the **Proxies** permission. | 
 **body** | **list[str]**| List of accounts the specified permission to be revoked from | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_account**
> ResponseContainerServiceAccount update_service_account(id, body=body)

Updates the service account



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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.ServiceAccountWrite() # ServiceAccountWrite |  (optional)

try:
    # Updates the service account
    api_response = api_instance.update_service_account(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->update_service_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ServiceAccountWrite**](ServiceAccountWrite.md)|  | [optional] 

### Return type

[**ResponseContainerServiceAccount**](ResponseContainerServiceAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_account**
> UserModel update_user_account(id, body=body)

Update user with given user groups and permissions.

<b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.UserRequestDTO() # UserRequestDTO | Example Body:  <pre>{   \"identifier\": \"user@example.com\",   \"groups\": [     \"user_management\"   ],   \"userGroups\": [     \"8b23136b-ecd2-4cb5-8c92-62477dcc4090\"   ],   \"roles\": [     \"Role\"   ] }</pre> (optional)

try:
    # Update user with given user groups and permissions.
    api_response = api_instance.update_user_account(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->update_user_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**UserRequestDTO**](UserRequestDTO.md)| Example Body:  &lt;pre&gt;{   \&quot;identifier\&quot;: \&quot;user@example.com\&quot;,   \&quot;groups\&quot;: [     \&quot;user_management\&quot;   ],   \&quot;userGroups\&quot;: [     \&quot;8b23136b-ecd2-4cb5-8c92-62477dcc4090\&quot;   ],   \&quot;roles\&quot;: [     \&quot;Role\&quot;   ] }&lt;/pre&gt; | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_accounts**
> ResponseContainerValidatedUsersDTO validate_accounts(body=body)

Returns valid accounts (users and service accounts), also invalid identifiers from the given list



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
api_instance = wavefront_api_client.AccountUserAndServiceAccountApi(wavefront_api_client.ApiClient(configuration))
body = [wavefront_api_client.list[str]()] # list[str] |  (optional)

try:
    # Returns valid accounts (users and service accounts), also invalid identifiers from the given list
    api_response = api_instance.validate_accounts(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUserAndServiceAccountApi->validate_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**|  | [optional] 

### Return type

[**ResponseContainerValidatedUsersDTO**](ResponseContainerValidatedUsersDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

