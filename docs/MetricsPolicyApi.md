# wavefront_api_client.MetricsPolicyApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metrics_policy**](MetricsPolicyApi.md#get_metrics_policy) | **GET** /api/v2/metricspolicy | Get the metrics policy
[**get_metrics_policy_by_version**](MetricsPolicyApi.md#get_metrics_policy_by_version) | **GET** /api/v2/metricspolicy/history/{version} | Get a specific historical version of a metrics policy
[**get_metrics_policy_history**](MetricsPolicyApi.md#get_metrics_policy_history) | **GET** /api/v2/metricspolicy/history | Get the version history of metrics policy
[**revert_metrics_policy_by_version**](MetricsPolicyApi.md#revert_metrics_policy_by_version) | **POST** /api/v2/metricspolicy/revert/{version} | Revert to a specific historical version of a metrics policy
[**update_metrics_policy**](MetricsPolicyApi.md#update_metrics_policy) | **PUT** /api/v2/metricspolicy | Update the metrics policy


# **get_metrics_policy**
> ResponseContainerMetricsPolicyReadModel get_metrics_policy()

Get the metrics policy



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
api_instance = wavefront_api_client.MetricsPolicyApi(wavefront_api_client.ApiClient(configuration))

try:
    # Get the metrics policy
    api_response = api_instance.get_metrics_policy()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsPolicyApi->get_metrics_policy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseContainerMetricsPolicyReadModel**](ResponseContainerMetricsPolicyReadModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics_policy_by_version**
> ResponseContainerMetricsPolicyReadModel get_metrics_policy_by_version(version)

Get a specific historical version of a metrics policy



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
api_instance = wavefront_api_client.MetricsPolicyApi(wavefront_api_client.ApiClient(configuration))
version = 789 # int | 

try:
    # Get a specific historical version of a metrics policy
    api_response = api_instance.get_metrics_policy_by_version(version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsPolicyApi->get_metrics_policy_by_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **int**|  | 

### Return type

[**ResponseContainerMetricsPolicyReadModel**](ResponseContainerMetricsPolicyReadModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics_policy_history**
> ResponseContainerHistoryResponse get_metrics_policy_history(offset=offset, limit=limit)

Get the version history of metrics policy



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
api_instance = wavefront_api_client.MetricsPolicyApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get the version history of metrics policy
    api_response = api_instance.get_metrics_policy_history(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsPolicyApi->get_metrics_policy_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerHistoryResponse**](ResponseContainerHistoryResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_metrics_policy_by_version**
> ResponseContainerMetricsPolicyReadModel revert_metrics_policy_by_version(version)

Revert to a specific historical version of a metrics policy



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
api_instance = wavefront_api_client.MetricsPolicyApi(wavefront_api_client.ApiClient(configuration))
version = 789 # int | 

try:
    # Revert to a specific historical version of a metrics policy
    api_response = api_instance.revert_metrics_policy_by_version(version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsPolicyApi->revert_metrics_policy_by_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **int**|  | 

### Return type

[**ResponseContainerMetricsPolicyReadModel**](ResponseContainerMetricsPolicyReadModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metrics_policy**
> ResponseContainerMetricsPolicyReadModel update_metrics_policy(body=body)

Update the metrics policy



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
api_instance = wavefront_api_client.MetricsPolicyApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.MetricsPolicyWriteModel() # MetricsPolicyWriteModel | Example Body:  <pre>{ \"policyRules\": [{   \"name\": \"Policy rule1 name\",   \"description\": \"Policy rule1 description\",   \"prefixes\": [\"revenue.*\"],   \"tags\": [{\"key\":\"sensitive\",  \"value\":\"false\"},              {\"key\":\"source\",  \"value\":\"app1\"}],   \"tagsAnded\": \"true\",   \"accessType\": \"ALLOW\",   \"accounts\": [\"accountId1\", \"accountId2\"],   \"userGroups\": [\"userGroupId1\"],   \"roles\": [\"roleId\"] }, {   \"name\": \"Policy rule2 name\",   \"description\": \"Policy rule2 description\",   \"prefixes\": [\"revenue.*\"],   \"accessType\": \"BLOCK\",   \"accounts\": [\"accountId3\"],   \"userGroups\": [\"userGroupId1\"] }] }</pre> (optional)

try:
    # Update the metrics policy
    api_response = api_instance.update_metrics_policy(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsPolicyApi->update_metrics_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetricsPolicyWriteModel**](MetricsPolicyWriteModel.md)| Example Body:  &lt;pre&gt;{ \&quot;policyRules\&quot;: [{   \&quot;name\&quot;: \&quot;Policy rule1 name\&quot;,   \&quot;description\&quot;: \&quot;Policy rule1 description\&quot;,   \&quot;prefixes\&quot;: [\&quot;revenue.*\&quot;],   \&quot;tags\&quot;: [{\&quot;key\&quot;:\&quot;sensitive\&quot;,  \&quot;value\&quot;:\&quot;false\&quot;},              {\&quot;key\&quot;:\&quot;source\&quot;,  \&quot;value\&quot;:\&quot;app1\&quot;}],   \&quot;tagsAnded\&quot;: \&quot;true\&quot;,   \&quot;accessType\&quot;: \&quot;ALLOW\&quot;,   \&quot;accounts\&quot;: [\&quot;accountId1\&quot;, \&quot;accountId2\&quot;],   \&quot;userGroups\&quot;: [\&quot;userGroupId1\&quot;],   \&quot;roles\&quot;: [\&quot;roleId\&quot;] }, {   \&quot;name\&quot;: \&quot;Policy rule2 name\&quot;,   \&quot;description\&quot;: \&quot;Policy rule2 description\&quot;,   \&quot;prefixes\&quot;: [\&quot;revenue.*\&quot;],   \&quot;accessType\&quot;: \&quot;BLOCK\&quot;,   \&quot;accounts\&quot;: [\&quot;accountId3\&quot;],   \&quot;userGroups\&quot;: [\&quot;userGroupId1\&quot;] }] }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerMetricsPolicyReadModel**](ResponseContainerMetricsPolicyReadModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

