# wavefront_api_client.AccountServiceAccountApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_account**](AccountServiceAccountApi.md#activate_account) | **POST** /api/v2/account/serviceaccount/{id}/activate | Activates the given service account
[**create_service_account**](AccountServiceAccountApi.md#create_service_account) | **POST** /api/v2/account/serviceaccount | Creates a service account
[**deactivate_account**](AccountServiceAccountApi.md#deactivate_account) | **POST** /api/v2/account/serviceaccount/{id}/deactivate | Deactivates the given service account
[**get_all_service_accounts**](AccountServiceAccountApi.md#get_all_service_accounts) | **GET** /api/v2/account/serviceaccount | Get all service accounts
[**get_service_account**](AccountServiceAccountApi.md#get_service_account) | **GET** /api/v2/account/serviceaccount/{id} | Retrieves a service account by identifier
[**update_service_account**](AccountServiceAccountApi.md#update_service_account) | **PUT** /api/v2/account/serviceaccount/{id} | Updates the service account


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
api_instance = wavefront_api_client.AccountServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Activates the given service account
    api_response = api_instance.activate_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountServiceAccountApi->activate_account: %s\n" % e)
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
api_instance = wavefront_api_client.AccountServiceAccountApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.ServiceAccountWrite() # ServiceAccountWrite |  (optional)

try:
    # Creates a service account
    api_response = api_instance.create_service_account(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountServiceAccountApi->create_service_account: %s\n" % e)
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
api_instance = wavefront_api_client.AccountServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Deactivates the given service account
    api_response = api_instance.deactivate_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountServiceAccountApi->deactivate_account: %s\n" % e)
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
api_instance = wavefront_api_client.AccountServiceAccountApi(wavefront_api_client.ApiClient(configuration))

try:
    # Get all service accounts
    api_response = api_instance.get_all_service_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountServiceAccountApi->get_all_service_accounts: %s\n" % e)
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
api_instance = wavefront_api_client.AccountServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Retrieves a service account by identifier
    api_response = api_instance.get_service_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountServiceAccountApi->get_service_account: %s\n" % e)
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
api_instance = wavefront_api_client.AccountServiceAccountApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.ServiceAccountWrite() # ServiceAccountWrite |  (optional)

try:
    # Updates the service account
    api_response = api_instance.update_service_account(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountServiceAccountApi->update_service_account: %s\n" % e)
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

