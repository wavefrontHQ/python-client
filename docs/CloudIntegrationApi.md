# wavefront_api_client.CloudIntegrationApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_aws_external_id**](CloudIntegrationApi.md#create_aws_external_id) | **POST** /api/v2/cloudintegration/awsExternalId | Create an external id
[**create_cloud_integration**](CloudIntegrationApi.md#create_cloud_integration) | **POST** /api/v2/cloudintegration | Create a cloud integration
[**delete_aws_external_id**](CloudIntegrationApi.md#delete_aws_external_id) | **DELETE** /api/v2/cloudintegration/awsExternalId/{id} | DELETEs an external id that was created by Wavefront
[**delete_cloud_integration**](CloudIntegrationApi.md#delete_cloud_integration) | **DELETE** /api/v2/cloudintegration/{id} | Delete a specific cloud integration
[**disable_cloud_integration**](CloudIntegrationApi.md#disable_cloud_integration) | **POST** /api/v2/cloudintegration/{id}/disable | Disable a specific cloud integration
[**enable_cloud_integration**](CloudIntegrationApi.md#enable_cloud_integration) | **POST** /api/v2/cloudintegration/{id}/enable | Enable a specific cloud integration
[**get_all_cloud_integration**](CloudIntegrationApi.md#get_all_cloud_integration) | **GET** /api/v2/cloudintegration | Get all cloud integrations for a customer
[**get_aws_external_id**](CloudIntegrationApi.md#get_aws_external_id) | **GET** /api/v2/cloudintegration/awsExternalId/{id} | GETs (confirms) a valid external id that was created by Wavefront
[**get_cloud_integration**](CloudIntegrationApi.md#get_cloud_integration) | **GET** /api/v2/cloudintegration/{id} | Get a specific cloud integration
[**undelete_cloud_integration**](CloudIntegrationApi.md#undelete_cloud_integration) | **POST** /api/v2/cloudintegration/{id}/undelete | Undelete a specific cloud integration
[**update_cloud_integration**](CloudIntegrationApi.md#update_cloud_integration) | **PUT** /api/v2/cloudintegration/{id} | Update a specific cloud integration


# **create_aws_external_id**
> ResponseContainerString create_aws_external_id()

Create an external id



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
api_instance = wavefront_api_client.CloudIntegrationApi(wavefront_api_client.ApiClient(configuration))

try:
    # Create an external id
    api_response = api_instance.create_aws_external_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudIntegrationApi->create_aws_external_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseContainerString**](ResponseContainerString.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloud_integration**
> ResponseContainerCloudIntegration create_cloud_integration(body=body)

Create a cloud integration



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
api_instance = wavefront_api_client.CloudIntegrationApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.CloudIntegration() # CloudIntegration | Example Body:  <pre>{   \"name\":\"CloudWatch integration\",   \"service\":\"CLOUDWATCH\",   \"cloudWatch\":{     \"baseCredentials\":{       \"roleArn\":\"arn:aws:iam::&lt;accountid&gt;:role/&lt;rolename&gt;\"     },     \"metricFilterRegex\":\"^aws.(sqs|ec2|ebs|elb).*$\",     \"pointTagFilterRegex\":\"(region|name)\"   },   \"serviceRefreshRateInMins\":5 }</pre> (optional)

try:
    # Create a cloud integration
    api_response = api_instance.create_cloud_integration(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudIntegrationApi->create_cloud_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudIntegration**](CloudIntegration.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;:\&quot;CloudWatch integration\&quot;,   \&quot;service\&quot;:\&quot;CLOUDWATCH\&quot;,   \&quot;cloudWatch\&quot;:{     \&quot;baseCredentials\&quot;:{       \&quot;roleArn\&quot;:\&quot;arn:aws:iam::&amp;lt;accountid&amp;gt;:role/&amp;lt;rolename&amp;gt;\&quot;     },     \&quot;metricFilterRegex\&quot;:\&quot;^aws.(sqs|ec2|ebs|elb).*$\&quot;,     \&quot;pointTagFilterRegex\&quot;:\&quot;(region|name)\&quot;   },   \&quot;serviceRefreshRateInMins\&quot;:5 }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerCloudIntegration**](ResponseContainerCloudIntegration.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_aws_external_id**
> ResponseContainerString delete_aws_external_id(id)

DELETEs an external id that was created by Wavefront



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
api_instance = wavefront_api_client.CloudIntegrationApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # DELETEs an external id that was created by Wavefront
    api_response = api_instance.delete_aws_external_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudIntegrationApi->delete_aws_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerString**](ResponseContainerString.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_integration**
> ResponseContainerCloudIntegration delete_cloud_integration(id, skip_trash=skip_trash)

Delete a specific cloud integration



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
api_instance = wavefront_api_client.CloudIntegrationApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
skip_trash = false # bool |  (optional) (default to false)

try:
    # Delete a specific cloud integration
    api_response = api_instance.delete_cloud_integration(id, skip_trash=skip_trash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudIntegrationApi->delete_cloud_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **skip_trash** | **bool**|  | [optional] [default to false]

### Return type

[**ResponseContainerCloudIntegration**](ResponseContainerCloudIntegration.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_cloud_integration**
> ResponseContainerCloudIntegration disable_cloud_integration(id)

Disable a specific cloud integration



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
api_instance = wavefront_api_client.CloudIntegrationApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Disable a specific cloud integration
    api_response = api_instance.disable_cloud_integration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudIntegrationApi->disable_cloud_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerCloudIntegration**](ResponseContainerCloudIntegration.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_cloud_integration**
> ResponseContainerCloudIntegration enable_cloud_integration(id)

Enable a specific cloud integration



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
api_instance = wavefront_api_client.CloudIntegrationApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Enable a specific cloud integration
    api_response = api_instance.enable_cloud_integration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudIntegrationApi->enable_cloud_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerCloudIntegration**](ResponseContainerCloudIntegration.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_cloud_integration**
> ResponseContainerPagedCloudIntegration get_all_cloud_integration(offset=offset, limit=limit)

Get all cloud integrations for a customer



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
api_instance = wavefront_api_client.CloudIntegrationApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all cloud integrations for a customer
    api_response = api_instance.get_all_cloud_integration(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudIntegrationApi->get_all_cloud_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedCloudIntegration**](ResponseContainerPagedCloudIntegration.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_external_id**
> ResponseContainerString get_aws_external_id(id)

GETs (confirms) a valid external id that was created by Wavefront



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
api_instance = wavefront_api_client.CloudIntegrationApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # GETs (confirms) a valid external id that was created by Wavefront
    api_response = api_instance.get_aws_external_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudIntegrationApi->get_aws_external_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerString**](ResponseContainerString.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_integration**
> ResponseContainerCloudIntegration get_cloud_integration(id)

Get a specific cloud integration



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
api_instance = wavefront_api_client.CloudIntegrationApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific cloud integration
    api_response = api_instance.get_cloud_integration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudIntegrationApi->get_cloud_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerCloudIntegration**](ResponseContainerCloudIntegration.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undelete_cloud_integration**
> ResponseContainerCloudIntegration undelete_cloud_integration(id)

Undelete a specific cloud integration



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
api_instance = wavefront_api_client.CloudIntegrationApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Undelete a specific cloud integration
    api_response = api_instance.undelete_cloud_integration(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudIntegrationApi->undelete_cloud_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerCloudIntegration**](ResponseContainerCloudIntegration.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_integration**
> ResponseContainerCloudIntegration update_cloud_integration(id, body=body)

Update a specific cloud integration



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
api_instance = wavefront_api_client.CloudIntegrationApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.CloudIntegration() # CloudIntegration | Example Body:  <pre>{   \"name\":\"CloudWatch integration\",   \"service\":\"CLOUDWATCH\",   \"cloudWatch\":{     \"baseCredentials\":{       \"roleArn\":\"arn:aws:iam::&lt;accountid&gt;:role/&lt;rolename&gt;\"     },     \"metricFilterRegex\":\"^aws.(sqs|ec2|ebs|elb).*$\",     \"pointTagFilterRegex\":\"(region|name)\"   },   \"serviceRefreshRateInMins\":5 }</pre> (optional)

try:
    # Update a specific cloud integration
    api_response = api_instance.update_cloud_integration(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudIntegrationApi->update_cloud_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**CloudIntegration**](CloudIntegration.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;:\&quot;CloudWatch integration\&quot;,   \&quot;service\&quot;:\&quot;CLOUDWATCH\&quot;,   \&quot;cloudWatch\&quot;:{     \&quot;baseCredentials\&quot;:{       \&quot;roleArn\&quot;:\&quot;arn:aws:iam::&amp;lt;accountid&amp;gt;:role/&amp;lt;rolename&amp;gt;\&quot;     },     \&quot;metricFilterRegex\&quot;:\&quot;^aws.(sqs|ec2|ebs|elb).*$\&quot;,     \&quot;pointTagFilterRegex\&quot;:\&quot;(region|name)\&quot;   },   \&quot;serviceRefreshRateInMins\&quot;:5 }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerCloudIntegration**](ResponseContainerCloudIntegration.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

