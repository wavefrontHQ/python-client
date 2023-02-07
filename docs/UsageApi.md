# wavefront_api_client.UsageApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ingestion_policy**](UsageApi.md#create_ingestion_policy) | **POST** /api/v2/usage/ingestionpolicy | Create a specific ingestion policy
[**delete_ingestion_policy**](UsageApi.md#delete_ingestion_policy) | **DELETE** /api/v2/usage/ingestionpolicy/{id} | Delete a specific ingestion policy
[**export_csv**](UsageApi.md#export_csv) | **GET** /api/v2/usage/exportcsv | Export a CSV report
[**get_all_ingestion_policies**](UsageApi.md#get_all_ingestion_policies) | **GET** /api/v2/usage/ingestionpolicy | Get all ingestion policies for a customer
[**get_ingestion_policy**](UsageApi.md#get_ingestion_policy) | **GET** /api/v2/usage/ingestionpolicy/{id} | Get a specific ingestion policy
[**get_ingestion_policy_by_version**](UsageApi.md#get_ingestion_policy_by_version) | **GET** /api/v2/usage/ingestionpolicy/{id}/history/{version} | Get a specific historical version of a ingestion policy
[**get_ingestion_policy_history**](UsageApi.md#get_ingestion_policy_history) | **GET** /api/v2/usage/ingestionpolicy/{id}/history | Get the version history of ingestion policy
[**revert_ingestion_policy_by_version**](UsageApi.md#revert_ingestion_policy_by_version) | **POST** /api/v2/usage/ingestionpolicy/{id}/revert/{version} | Revert to a specific historical version of a ingestion policy
[**update_ingestion_policy**](UsageApi.md#update_ingestion_policy) | **PUT** /api/v2/usage/ingestionpolicy/{id} | Update a specific ingestion policy


# **create_ingestion_policy**
> ResponseContainerIngestionPolicyReadModel create_ingestion_policy(body=body)

Create a specific ingestion policy



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
api_instance = wavefront_api_client.UsageApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.IngestionPolicyWriteModel() # IngestionPolicyWriteModel | Example Body:  <pre>{   \"name\": \"Ingestion policy name\",   \"description\": \"Ingestion policy description\",   \"scope\": \"GROUP\",   \"groups\": [\"g1\",\"g2\"],   \"isLimited\": \"true\",   \"limitPPS\": \"1000\",   \"alert\": {        \"name\": \"Alert Name\",        \"targets\": {            \"severe\": \"user1@mail.com\"         },        \"conditionPercentages\": {            \"info\": 70,            \"warn\": 90         },        \"minutes\": 5,        \"resolveAfterMinutes\": 2,        \"evaluateRealtimeData\": false,        \"additionalInformation\": \"Additional Info\",        \"tags\": {           \"customerTags\": [             \"alertTag1\"           ]         },        \"conditionsThresholdOperator\": \">\"     } }</pre> (optional)

try:
    # Create a specific ingestion policy
    api_response = api_instance.create_ingestion_policy(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->create_ingestion_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IngestionPolicyWriteModel**](IngestionPolicyWriteModel.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;Ingestion policy name\&quot;,   \&quot;description\&quot;: \&quot;Ingestion policy description\&quot;,   \&quot;scope\&quot;: \&quot;GROUP\&quot;,   \&quot;groups\&quot;: [\&quot;g1\&quot;,\&quot;g2\&quot;],   \&quot;isLimited\&quot;: \&quot;true\&quot;,   \&quot;limitPPS\&quot;: \&quot;1000\&quot;,   \&quot;alert\&quot;: {        \&quot;name\&quot;: \&quot;Alert Name\&quot;,        \&quot;targets\&quot;: {            \&quot;severe\&quot;: \&quot;user1@mail.com\&quot;         },        \&quot;conditionPercentages\&quot;: {            \&quot;info\&quot;: 70,            \&quot;warn\&quot;: 90         },        \&quot;minutes\&quot;: 5,        \&quot;resolveAfterMinutes\&quot;: 2,        \&quot;evaluateRealtimeData\&quot;: false,        \&quot;additionalInformation\&quot;: \&quot;Additional Info\&quot;,        \&quot;tags\&quot;: {           \&quot;customerTags\&quot;: [             \&quot;alertTag1\&quot;           ]         },        \&quot;conditionsThresholdOperator\&quot;: \&quot;&gt;\&quot;     } }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerIngestionPolicyReadModel**](ResponseContainerIngestionPolicyReadModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ingestion_policy**
> ResponseContainerIngestionPolicyReadModel delete_ingestion_policy(id)

Delete a specific ingestion policy



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
api_instance = wavefront_api_client.UsageApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a specific ingestion policy
    api_response = api_instance.delete_ingestion_policy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->delete_ingestion_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerIngestionPolicyReadModel**](ResponseContainerIngestionPolicyReadModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_csv**
> export_csv(start_time, end_time=end_time)

Export a CSV report



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
api_instance = wavefront_api_client.UsageApi(wavefront_api_client.ApiClient(configuration))
start_time = 789 # int | start time in epoch seconds
end_time = 789 # int | end time in epoch seconds, null to use now (optional)

try:
    # Export a CSV report
    api_instance.export_csv(start_time, end_time=end_time)
except ApiException as e:
    print("Exception when calling UsageApi->export_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| start time in epoch seconds | 
 **end_time** | **int**| end time in epoch seconds, null to use now | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ingestion_policies**
> ResponseContainerPagedIngestionPolicyReadModel get_all_ingestion_policies(offset=offset, limit=limit)

Get all ingestion policies for a customer



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
api_instance = wavefront_api_client.UsageApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all ingestion policies for a customer
    api_response = api_instance.get_all_ingestion_policies(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_all_ingestion_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedIngestionPolicyReadModel**](ResponseContainerPagedIngestionPolicyReadModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ingestion_policy**
> ResponseContainerIngestionPolicyReadModel get_ingestion_policy(id)

Get a specific ingestion policy



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
api_instance = wavefront_api_client.UsageApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific ingestion policy
    api_response = api_instance.get_ingestion_policy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_ingestion_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerIngestionPolicyReadModel**](ResponseContainerIngestionPolicyReadModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ingestion_policy_by_version**
> ResponseContainerIngestionPolicyReadModel get_ingestion_policy_by_version(id, version)

Get a specific historical version of a ingestion policy



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
api_instance = wavefront_api_client.UsageApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
version = 789 # int | 

try:
    # Get a specific historical version of a ingestion policy
    api_response = api_instance.get_ingestion_policy_by_version(id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_ingestion_policy_by_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **version** | **int**|  | 

### Return type

[**ResponseContainerIngestionPolicyReadModel**](ResponseContainerIngestionPolicyReadModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ingestion_policy_history**
> ResponseContainerHistoryResponse get_ingestion_policy_history(id, offset=offset, limit=limit)

Get the version history of ingestion policy



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
api_instance = wavefront_api_client.UsageApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get the version history of ingestion policy
    api_response = api_instance.get_ingestion_policy_history(id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_ingestion_policy_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **revert_ingestion_policy_by_version**
> ResponseContainerIngestionPolicyReadModel revert_ingestion_policy_by_version(id, version)

Revert to a specific historical version of a ingestion policy



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
api_instance = wavefront_api_client.UsageApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
version = 789 # int | 

try:
    # Revert to a specific historical version of a ingestion policy
    api_response = api_instance.revert_ingestion_policy_by_version(id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->revert_ingestion_policy_by_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **version** | **int**|  | 

### Return type

[**ResponseContainerIngestionPolicyReadModel**](ResponseContainerIngestionPolicyReadModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ingestion_policy**
> ResponseContainerIngestionPolicyReadModel update_ingestion_policy(id, body=body)

Update a specific ingestion policy



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
api_instance = wavefront_api_client.UsageApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.IngestionPolicyWriteModel() # IngestionPolicyWriteModel | Example Body:  <pre>{   \"name\": \"Ingestion policy name\",   \"description\": \"Ingestion policy description\",   \"scope\": \"GROUP\",   \"groups\": [\"g1\",\"g2\"],   \"isLimited\": \"true\",   \"limitPPS\": \"1000\",   \"alert\": {        \"name\": \"Alert Name\",        \"targets\": {            \"severe\": \"user1@mail.com\"         },        \"conditionPercentages\": {            \"info\": 70,            \"warn\": 90         },        \"minutes\": 5,        \"resolveAfterMinutes\": 2,        \"evaluateRealtimeData\": false,        \"additionalInformation\": \"Additional Info\",        \"tags\": {           \"customerTags\": [             \"alertTag1\"           ]         },        \"conditionsThresholdOperator\": \">\"     } }</pre> (optional)

try:
    # Update a specific ingestion policy
    api_response = api_instance.update_ingestion_policy(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->update_ingestion_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**IngestionPolicyWriteModel**](IngestionPolicyWriteModel.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;Ingestion policy name\&quot;,   \&quot;description\&quot;: \&quot;Ingestion policy description\&quot;,   \&quot;scope\&quot;: \&quot;GROUP\&quot;,   \&quot;groups\&quot;: [\&quot;g1\&quot;,\&quot;g2\&quot;],   \&quot;isLimited\&quot;: \&quot;true\&quot;,   \&quot;limitPPS\&quot;: \&quot;1000\&quot;,   \&quot;alert\&quot;: {        \&quot;name\&quot;: \&quot;Alert Name\&quot;,        \&quot;targets\&quot;: {            \&quot;severe\&quot;: \&quot;user1@mail.com\&quot;         },        \&quot;conditionPercentages\&quot;: {            \&quot;info\&quot;: 70,            \&quot;warn\&quot;: 90         },        \&quot;minutes\&quot;: 5,        \&quot;resolveAfterMinutes\&quot;: 2,        \&quot;evaluateRealtimeData\&quot;: false,        \&quot;additionalInformation\&quot;: \&quot;Additional Info\&quot;,        \&quot;tags\&quot;: {           \&quot;customerTags\&quot;: [             \&quot;alertTag1\&quot;           ]         },        \&quot;conditionsThresholdOperator\&quot;: \&quot;&gt;\&quot;     } }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerIngestionPolicyReadModel**](ResponseContainerIngestionPolicyReadModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

