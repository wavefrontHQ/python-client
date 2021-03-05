# wavefront_api_client.AccessPolicyApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_policy**](AccessPolicyApi.md#get_access_policy) | **GET** /api/v2/accesspolicy | Get the access policy
[**update_access_policy**](AccessPolicyApi.md#update_access_policy) | **PUT** /api/v2/accesspolicy | Update the access policy
[**validate_url**](AccessPolicyApi.md#validate_url) | **GET** /api/v2/accesspolicy/validate | Validate a given url and ip address


# **get_access_policy**
> ResponseContainerAccessPolicy get_access_policy()

Get the access policy



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
api_instance = wavefront_api_client.AccessPolicyApi(wavefront_api_client.ApiClient(configuration))

try:
    # Get the access policy
    api_response = api_instance.get_access_policy()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessPolicyApi->get_access_policy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseContainerAccessPolicy**](ResponseContainerAccessPolicy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_policy**
> ResponseContainerAccessPolicy update_access_policy(body=body)

Update the access policy



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
api_instance = wavefront_api_client.AccessPolicyApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.AccessPolicy() # AccessPolicy | Example Body:  <pre>{  \"policyRules\": [{    \"name\": \"rule name\",    \"description\": \"desc\",    \"action\": \"ALLOW\",    \"subnet\": \"12.148.72.0/23\"  }] }</pre> (optional)

try:
    # Update the access policy
    api_response = api_instance.update_access_policy(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessPolicyApi->update_access_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessPolicy**](AccessPolicy.md)| Example Body:  &lt;pre&gt;{  \&quot;policyRules\&quot;: [{    \&quot;name\&quot;: \&quot;rule name\&quot;,    \&quot;description\&quot;: \&quot;desc\&quot;,    \&quot;action\&quot;: \&quot;ALLOW\&quot;,    \&quot;subnet\&quot;: \&quot;12.148.72.0/23\&quot;  }] }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerAccessPolicy**](ResponseContainerAccessPolicy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_url**
> ResponseContainerAccessPolicyAction validate_url(ip=ip)

Validate a given url and ip address



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
api_instance = wavefront_api_client.AccessPolicyApi(wavefront_api_client.ApiClient(configuration))
ip = 'ip_example' # str |  (optional)

try:
    # Validate a given url and ip address
    api_response = api_instance.validate_url(ip=ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessPolicyApi->validate_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**|  | [optional] 

### Return type

[**ResponseContainerAccessPolicyAction**](ResponseContainerAccessPolicyAction.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

