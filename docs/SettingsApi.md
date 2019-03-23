# wavefront_api_client.SettingsApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_permissions**](SettingsApi.md#get_all_permissions) | **GET** /api/v2/customer/permissions | Get all permissions
[**get_customer_preferences**](SettingsApi.md#get_customer_preferences) | **GET** /api/v2/customer/preferences | Get customer preferences
[**get_default_user_groups**](SettingsApi.md#get_default_user_groups) | **GET** /api/v2/customer/preferences/defaultUserGroups | Get default user groups customer preferences
[**post_customer_preferences**](SettingsApi.md#post_customer_preferences) | **POST** /api/v2/customer/preferences | Update selected fields of customer preferences


# **get_all_permissions**
> list[BusinessActionGroupBasicDTO] get_all_permissions()

Get all permissions

Returns all permissions' info data

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
api_instance = wavefront_api_client.SettingsApi(wavefront_api_client.ApiClient(configuration))

try:
    # Get all permissions
    api_response = api_instance.get_all_permissions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_all_permissions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BusinessActionGroupBasicDTO]**](BusinessActionGroupBasicDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_preferences**
> CustomerPreferences get_customer_preferences()

Get customer preferences



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
api_instance = wavefront_api_client.SettingsApi(wavefront_api_client.ApiClient(configuration))

try:
    # Get customer preferences
    api_response = api_instance.get_customer_preferences()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_customer_preferences: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomerPreferences**](CustomerPreferences.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_user_groups**
> ResponseContainerListUserGroup get_default_user_groups(body=body)

Get default user groups customer preferences



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
api_instance = wavefront_api_client.SettingsApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.User() # User |  (optional)

try:
    # Get default user groups customer preferences
    api_response = api_instance.get_default_user_groups(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_default_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)|  | [optional] 

### Return type

[**ResponseContainerListUserGroup**](ResponseContainerListUserGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_customer_preferences**
> CustomerPreferences post_customer_preferences(body=body)

Update selected fields of customer preferences



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
api_instance = wavefront_api_client.SettingsApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.CustomerPreferencesUpdating() # CustomerPreferencesUpdating |  (optional)

try:
    # Update selected fields of customer preferences
    api_response = api_instance.post_customer_preferences(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->post_customer_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomerPreferencesUpdating**](CustomerPreferencesUpdating.md)|  | [optional] 

### Return type

[**CustomerPreferences**](CustomerPreferences.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

