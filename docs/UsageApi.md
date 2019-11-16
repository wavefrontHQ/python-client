# wavefront_api_client.UsageApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ingestion_policy**](UsageApi.md#create_ingestion_policy) | **POST** /api/v2/usage/ingestionpolicy | Create a specific ingestion policy
[**delete_ingestion_policy**](UsageApi.md#delete_ingestion_policy) | **DELETE** /api/v2/usage/ingestionpolicy/{id} | Delete a specific ingestion policy
[**export_csv**](UsageApi.md#export_csv) | **GET** /api/v2/usage/exportcsv | Export a CSV report
[**get_all_ingestion_policies**](UsageApi.md#get_all_ingestion_policies) | **GET** /api/v2/usage/ingestionpolicy | Get all ingestion policies for a customer
[**get_ingestion_policy**](UsageApi.md#get_ingestion_policy) | **GET** /api/v2/usage/ingestionpolicy/{id} | Get a specific ingestion policy
[**update_ingestion_policy**](UsageApi.md#update_ingestion_policy) | **PUT** /api/v2/usage/ingestionpolicy/{id} | Update a specific ingestion policy


# **create_ingestion_policy**
> ResponseContainerIngestionPolicy create_ingestion_policy(body=body)

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
body = wavefront_api_client.IngestionPolicy() # IngestionPolicy | Example Body:  <pre>{   \"name\": \"Ingestion policy name\",   \"description\": \"Ingestion policy description\" }</pre> (optional)

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
 **body** | [**IngestionPolicy**](IngestionPolicy.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;Ingestion policy name\&quot;,   \&quot;description\&quot;: \&quot;Ingestion policy description\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerIngestionPolicy**](ResponseContainerIngestionPolicy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ingestion_policy**
> ResponseContainerIngestionPolicy delete_ingestion_policy(id)

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

[**ResponseContainerIngestionPolicy**](ResponseContainerIngestionPolicy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
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

 - **Content-Type**: Not defined
 - **Accept**: application/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ingestion_policies**
> ResponseContainerPagedIngestionPolicy get_all_ingestion_policies(offset=offset, limit=limit)

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

[**ResponseContainerPagedIngestionPolicy**](ResponseContainerPagedIngestionPolicy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ingestion_policy**
> ResponseContainerIngestionPolicy get_ingestion_policy(id)

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

[**ResponseContainerIngestionPolicy**](ResponseContainerIngestionPolicy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ingestion_policy**
> ResponseContainerIngestionPolicy update_ingestion_policy(id, body=body)

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
body = wavefront_api_client.IngestionPolicy() # IngestionPolicy | Example Body:  <pre>{   \"name\": \"Ingestion policy name\",   \"description\": \"Ingestion policy description\" }</pre> (optional)

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
 **body** | [**IngestionPolicy**](IngestionPolicy.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;Ingestion policy name\&quot;,   \&quot;description\&quot;: \&quot;Ingestion policy description\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerIngestionPolicy**](ResponseContainerIngestionPolicy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

