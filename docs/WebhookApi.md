# wavefront_api_client.WebhookApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhookApi.md#create_webhook) | **POST** /api/v2/webhook | Create a specific webhook
[**delete_webhook**](WebhookApi.md#delete_webhook) | **DELETE** /api/v2/webhook/{id} | Delete a specific webhook
[**get_all_webhooks**](WebhookApi.md#get_all_webhooks) | **GET** /api/v2/webhook | Get all webhooks for a customer
[**get_webhook**](WebhookApi.md#get_webhook) | **GET** /api/v2/webhook/{id} | Get a specific webhook
[**update_webhook**](WebhookApi.md#update_webhook) | **PUT** /api/v2/webhook/{id} | Update a specific webhook


# **create_webhook**
> ResponseContainerNotificant create_webhook(body=body)

Create a specific webhook



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
api_instance = wavefront_api_client.WebhookApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.Notificant() # Notificant | Example Body:  <pre>{   \"description\": \"WebHook Description\",   \"template\": \"POST Body -- Mustache syntax\",   \"title\": \"WebHook Title\",   \"triggers\": [     \"ALERT_OPENED\"   ],   \"recipient\": \"http://example.com\",   \"customHttpHeaders\": {},   \"contentType\": \"text/plain\" }</pre> (optional)

try:
    # Create a specific webhook
    api_response = api_instance.create_webhook(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Notificant**](Notificant.md)| Example Body:  &lt;pre&gt;{   \&quot;description\&quot;: \&quot;WebHook Description\&quot;,   \&quot;template\&quot;: \&quot;POST Body -- Mustache syntax\&quot;,   \&quot;title\&quot;: \&quot;WebHook Title\&quot;,   \&quot;triggers\&quot;: [     \&quot;ALERT_OPENED\&quot;   ],   \&quot;recipient\&quot;: \&quot;http://example.com\&quot;,   \&quot;customHttpHeaders\&quot;: {},   \&quot;contentType\&quot;: \&quot;text/plain\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerNotificant**](ResponseContainerNotificant.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> ResponseContainerNotificant delete_webhook(id)

Delete a specific webhook



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
api_instance = wavefront_api_client.WebhookApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a specific webhook
    api_response = api_instance.delete_webhook(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->delete_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerNotificant**](ResponseContainerNotificant.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_webhooks**
> ResponseContainerPagedNotificant get_all_webhooks(offset=offset, limit=limit)

Get all webhooks for a customer



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
api_instance = wavefront_api_client.WebhookApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all webhooks for a customer
    api_response = api_instance.get_all_webhooks(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->get_all_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedNotificant**](ResponseContainerPagedNotificant.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> ResponseContainerNotificant get_webhook(id)

Get a specific webhook



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
api_instance = wavefront_api_client.WebhookApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific webhook
    api_response = api_instance.get_webhook(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->get_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerNotificant**](ResponseContainerNotificant.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> ResponseContainerNotificant update_webhook(id, body=body)

Update a specific webhook



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
api_instance = wavefront_api_client.WebhookApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.Notificant() # Notificant | Example Body:  <pre>{   \"description\": \"WebHook Description\",   \"template\": \"POST Body -- Mustache syntax\",   \"title\": \"WebHook Title\",   \"triggers\": [     \"ALERT_OPENED\"   ],   \"recipient\": \"http://example.com\",   \"customHttpHeaders\": {},   \"contentType\": \"text/plain\" }</pre> (optional)

try:
    # Update a specific webhook
    api_response = api_instance.update_webhook(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->update_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Notificant**](Notificant.md)| Example Body:  &lt;pre&gt;{   \&quot;description\&quot;: \&quot;WebHook Description\&quot;,   \&quot;template\&quot;: \&quot;POST Body -- Mustache syntax\&quot;,   \&quot;title\&quot;: \&quot;WebHook Title\&quot;,   \&quot;triggers\&quot;: [     \&quot;ALERT_OPENED\&quot;   ],   \&quot;recipient\&quot;: \&quot;http://example.com\&quot;,   \&quot;customHttpHeaders\&quot;: {},   \&quot;contentType\&quot;: \&quot;text/plain\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerNotificant**](ResponseContainerNotificant.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

