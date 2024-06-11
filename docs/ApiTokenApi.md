# wavefront_api_client.ApiTokenApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](ApiTokenApi.md#create_token) | **POST** /api/v2/apitoken | Create new api token
[**delete_customer_token**](ApiTokenApi.md#delete_customer_token) | **PUT** /api/v2/apitoken/customertokens/revoke | Delete the specified api token for a customer
[**delete_token**](ApiTokenApi.md#delete_token) | **DELETE** /api/v2/apitoken/{id} | Delete the specified api token
[**delete_token_service_account**](ApiTokenApi.md#delete_token_service_account) | **DELETE** /api/v2/apitoken/serviceaccount/{id}/{token} | Delete the specified api token of the given service account
[**generate_token_service_account**](ApiTokenApi.md#generate_token_service_account) | **POST** /api/v2/apitoken/serviceaccount/{id} | Create a new api token for the service account
[**get_all_tokens**](ApiTokenApi.md#get_all_tokens) | **GET** /api/v2/apitoken | Get all api tokens for a user
[**get_customer_token**](ApiTokenApi.md#get_customer_token) | **GET** /api/v2/apitoken/customertokens/{id} | Get the specified api token for a customer
[**get_customer_tokens**](ApiTokenApi.md#get_customer_tokens) | **GET** /api/v2/apitoken/customertokens | Get all api tokens for a customer
[**get_tokens_service_account**](ApiTokenApi.md#get_tokens_service_account) | **GET** /api/v2/apitoken/serviceaccount/{id} | Get all api tokens for the given service account
[**update_token_name**](ApiTokenApi.md#update_token_name) | **PUT** /api/v2/apitoken/{id} | Update the name of the specified api token
[**update_token_name_service_account**](ApiTokenApi.md#update_token_name_service_account) | **PUT** /api/v2/apitoken/serviceaccount/{id}/{token} | Update the name of the specified api token for the given service account


# **create_token**
> ResponseContainerListUserApiToken create_token()

Create new api token

Returns the list of all api tokens for a user. The newly created api token is the last element of returned list. <b>Note</b>: Applies only to original Tanzu Observability instances that are not onboarded to VMware Cloud services.

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

# **delete_customer_token**
> ResponseContainerUserApiToken delete_customer_token(body=body)

Delete the specified api token for a customer



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
body = wavefront_api_client.UserApiToken() # UserApiToken |  (optional)

try:
    # Delete the specified api token for a customer
    api_response = api_instance.delete_customer_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokenApi->delete_customer_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserApiToken**](UserApiToken.md)|  | [optional] 

### Return type

[**ResponseContainerUserApiToken**](ResponseContainerUserApiToken.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
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

# **delete_token_service_account**
> ResponseContainerListUserApiToken delete_token_service_account(id, token)

Delete the specified api token of the given service account



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
token = 'token_example' # str | 

try:
    # Delete the specified api token of the given service account
    api_response = api_instance.delete_token_service_account(id, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokenApi->delete_token_service_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **token** | **str**|  | 

### Return type

[**ResponseContainerListUserApiToken**](ResponseContainerListUserApiToken.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_token_service_account**
> ResponseContainerListUserApiToken generate_token_service_account(id, body=body)

Create a new api token for the service account

Returns the list of all api tokens for the service account. The newly created api token is the last element of returned list. 

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
body = wavefront_api_client.UserApiToken() # UserApiToken |  (optional)

try:
    # Create a new api token for the service account
    api_response = api_instance.generate_token_service_account(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokenApi->generate_token_service_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**UserApiToken**](UserApiToken.md)|  | [optional] 

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

# **get_customer_token**
> ResponseContainerApiTokenModel get_customer_token(id)

Get the specified api token for a customer



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
    # Get the specified api token for a customer
    api_response = api_instance.get_customer_token(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokenApi->get_customer_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerApiTokenModel**](ResponseContainerApiTokenModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_tokens**
> ResponseContainerListApiTokenModel get_customer_tokens()

Get all api tokens for a customer



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
    # Get all api tokens for a customer
    api_response = api_instance.get_customer_tokens()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokenApi->get_customer_tokens: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseContainerListApiTokenModel**](ResponseContainerListApiTokenModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens_service_account**
> ResponseContainerListUserApiToken get_tokens_service_account(id)

Get all api tokens for the given service account



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
    # Get all api tokens for the given service account
    api_response = api_instance.get_tokens_service_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokenApi->get_tokens_service_account: %s\n" % e)
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

# **update_token_name_service_account**
> ResponseContainerUserApiToken update_token_name_service_account(id, token, body=body)

Update the name of the specified api token for the given service account



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
token = 'token_example' # str | 
body = wavefront_api_client.UserApiToken() # UserApiToken | Example Body:  <pre>{   \"tokenID\": \"Token identifier\",   \"tokenName\": \"Token name\" }</pre> (optional)

try:
    # Update the name of the specified api token for the given service account
    api_response = api_instance.update_token_name_service_account(id, token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokenApi->update_token_name_service_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **token** | **str**|  | 
 **body** | [**UserApiToken**](UserApiToken.md)| Example Body:  &lt;pre&gt;{   \&quot;tokenID\&quot;: \&quot;Token identifier\&quot;,   \&quot;tokenName\&quot;: \&quot;Token name\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerUserApiToken**](ResponseContainerUserApiToken.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

