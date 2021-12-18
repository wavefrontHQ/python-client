# wavefront_api_client.AlertApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_alert_access**](AlertApi.md#add_alert_access) | **POST** /api/v2/alert/acl/add | Adds the specified ids to the given alerts&#39; ACL
[**add_alert_tag**](AlertApi.md#add_alert_tag) | **PUT** /api/v2/alert/{id}/tag/{tagValue} | Add a tag to a specific alert
[**check_query_type**](AlertApi.md#check_query_type) | **POST** /api/v2/alert/checkQuery | Return the type of provided query.
[**clone_alert**](AlertApi.md#clone_alert) | **POST** /api/v2/alert/{id}/clone | Clones the specified alert
[**create_alert**](AlertApi.md#create_alert) | **POST** /api/v2/alert | Create a specific alert
[**delete_alert**](AlertApi.md#delete_alert) | **DELETE** /api/v2/alert/{id} | Delete a specific alert
[**get_alert**](AlertApi.md#get_alert) | **GET** /api/v2/alert/{id} | Get a specific alert
[**get_alert_access_control_list**](AlertApi.md#get_alert_access_control_list) | **GET** /api/v2/alert/acl | Get Access Control Lists&#39; union for the specified alerts
[**get_alert_history**](AlertApi.md#get_alert_history) | **GET** /api/v2/alert/{id}/history | Get the version history of a specific alert
[**get_alert_tags**](AlertApi.md#get_alert_tags) | **GET** /api/v2/alert/{id}/tag | Get all tags associated with a specific alert
[**get_alert_version**](AlertApi.md#get_alert_version) | **GET** /api/v2/alert/{id}/history/{version} | Get a specific historical version of a specific alert
[**get_alerts_summary**](AlertApi.md#get_alerts_summary) | **GET** /api/v2/alert/summary | Count alerts of various statuses for a customer
[**get_all_alert**](AlertApi.md#get_all_alert) | **GET** /api/v2/alert | Get all alerts for a customer
[**hide_alert**](AlertApi.md#hide_alert) | **POST** /api/v2/alert/{id}/uninstall | Hide a specific integration alert 
[**preview_alert_notification**](AlertApi.md#preview_alert_notification) | **POST** /api/v2/alert/preview | Get all the notification preview for a specific alert
[**remove_alert_access**](AlertApi.md#remove_alert_access) | **POST** /api/v2/alert/acl/remove | Removes the specified ids from the given alerts&#39; ACL
[**remove_alert_tag**](AlertApi.md#remove_alert_tag) | **DELETE** /api/v2/alert/{id}/tag/{tagValue} | Remove a tag from a specific alert
[**set_alert_acl**](AlertApi.md#set_alert_acl) | **PUT** /api/v2/alert/acl/set | Set ACL for the specified alerts
[**set_alert_tags**](AlertApi.md#set_alert_tags) | **POST** /api/v2/alert/{id}/tag | Set all tags associated with a specific alert
[**snooze_alert**](AlertApi.md#snooze_alert) | **POST** /api/v2/alert/{id}/snooze | Snooze a specific alert for some number of seconds
[**undelete_alert**](AlertApi.md#undelete_alert) | **POST** /api/v2/alert/{id}/undelete | Undelete a specific alert
[**unhide_alert**](AlertApi.md#unhide_alert) | **POST** /api/v2/alert/{id}/install | Unhide a specific integration alert
[**unsnooze_alert**](AlertApi.md#unsnooze_alert) | **POST** /api/v2/alert/{id}/unsnooze | Unsnooze a specific alert
[**update_alert**](AlertApi.md#update_alert) | **PUT** /api/v2/alert/{id} | Update a specific alert


# **add_alert_access**
> add_alert_access(body=body)

Adds the specified ids to the given alerts' ACL



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
body = [wavefront_api_client.AccessControlListWriteDTO()] # list[AccessControlListWriteDTO] |  (optional)

try:
    # Adds the specified ids to the given alerts' ACL
    api_instance.add_alert_access(body=body)
except ApiException as e:
    print("Exception when calling AlertApi->add_alert_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AccessControlListWriteDTO]**](AccessControlListWriteDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_alert_tag**
> ResponseContainerVoid add_alert_tag(id, tag_value)

Add a tag to a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
tag_value = 'tag_value_example' # str | Supported Characters of Tags:  <pre>Tag names can contain alphanumeric (a-z, A-Z, 0-9),  dash (-), underscore (_), and colon (:) characters. The space character is not supported.</pre> 

try:
    # Add a tag to a specific alert
    api_response = api_instance.add_alert_tag(id, tag_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->add_alert_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tag_value** | **str**| Supported Characters of Tags:  &lt;pre&gt;Tag names can contain alphanumeric (a-z, A-Z, 0-9),  dash (-), underscore (_), and colon (:) characters. The space character is not supported.&lt;/pre&gt;  | 

### Return type

[**ResponseContainerVoid**](ResponseContainerVoid.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_query_type**
> ResponseContainerQueryTypeDTO check_query_type(body=body)

Return the type of provided query.



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.QueryTypeDTO() # QueryTypeDTO |  (optional)

try:
    # Return the type of provided query.
    api_response = api_instance.check_query_type(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->check_query_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QueryTypeDTO**](QueryTypeDTO.md)|  | [optional] 

### Return type

[**ResponseContainerQueryTypeDTO**](ResponseContainerQueryTypeDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_alert**
> ResponseContainerAlert clone_alert(id, name=name, v=v)

Clones the specified alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
name = 'name_example' # str |  (optional)
v = 789 # int |  (optional)

try:
    # Clones the specified alert
    api_response = api_instance.clone_alert(id, name=name, v=v)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->clone_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**|  | [optional] 
 **v** | **int**|  | [optional] 

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_alert**
> ResponseContainerAlert create_alert(use_multi_query=use_multi_query, body=body)

Create a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
use_multi_query = false # bool | A flag indicates whether to use the new multi-query alert structures when thefeature is enabled.<br/> When the flag is true, the $.alertSources is the source of truth and will update $.condition and $.displayExpression with the corresponding expanded queries.<br/> When the flag is false, it goes through the old way and the $.condition and$.displayExpression is the source of truth and will auto-create $.alertSources  (optional) (default to false)
body = wavefront_api_client.Alert() # Alert | Example Classic Body:  <pre>{   \"name\": \"Alert Name\",   \"target\": \"target:alert-target-id\",   \"condition\": \"ts(~sample.cpu.loadavg.1m) > 1\",   \"conditionQueryType\": \"WQL\",   \"displayExpression\": \"ts(~sample.cpu.loadavg.1m)\",   \"displayExpressionQueryType\": \"WQL\",   \"minutes\": 5,   \"resolveAfterMinutes\": 2,   \"severity\": \"INFO\",   \"alertTriageDashboards\": [{     \"dashboardId\": \"dashboard-name\",     \"parameters\": {       \"constants\": {         \"key\": \"value\"         }       },    \"description\": \"dashboard description\"     }   ],   \"additionalInformation\": \"Additional Info\",   \"tags\": {     \"customerTags\": [       \"alertTag1\"     ]   } }</pre> Example Classic Body with multi queries:  <pre>{     \"name\": \"Alert Name\",     \"alertType\": \"CLASSIC\",     \"alertSources\": [        {             \"name\": \"A\",             \"query\": \"${B} > 2\",             \"queryType\": \"PROMQL\",             \"alertSourceType\": [\"CONDITION\"]         },         {             \"name\": \"B\",             \"query\": \"sum_over_time(~sample.network.bytes.recv[1m])\",             \"queryType\": \"PROMQL\",             \"alertSourceType\": [\"AUDIT\"]         }     ],     \"severity\": \"WARN\",     \"minutes\": 5 }</pre> Example Threshold Body:  <pre>{     \"name\": \"Alert Name\",     \"alertType\": \"THRESHOLD\",     \"conditions\": {         \"info\": \"ts(~sample.cpu.loadavg.1m) > 0\",         \"warn\": \"ts(~sample.cpu.loadavg.1m) > 2\"     },     \"displayExpression\": \"ts(~sample.cpu.loadavg.1m)\",     \"minutes\": 5,     \"additionalInformation\": \"conditions value entry needs to be of the form: displayExpression operator threshold\" }</pre> Example Threshold Body with multi queries:  <pre>{   \"name\": \"Alert Name\",   \"alertType\": \"THRESHOLD\",   \"alertSources\": [     {       \"name\": \"A\",       \"query\": \"${B}\",       \"queryType\": \"PROMQL\",       \"alertSourceType\": [\"CONDITION\"]     },     {       \"name\": \"B\",       \"query\": \"sum_over_time(~sample.network.bytes.recv[1m])\",       \"queryType\": \"PROMQL\",       \"alertSourceType\": [\"AUDIT\"]     }   ],   \"conditions\": {     \"info\": \"${B} > bool 0\",     \"warn\": \"${B} > bool 2\"   },   \"minutes\": 5 }</pre> Supported Characters of Tags:  <pre>Tag names can contain alphanumeric (a-z, A-Z, 0-9),  dash (-), underscore (_), and colon (:) characters. The space character is not supported.</pre>  (optional)

try:
    # Create a specific alert
    api_response = api_instance.create_alert(use_multi_query=use_multi_query, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->create_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_multi_query** | **bool**| A flag indicates whether to use the new multi-query alert structures when thefeature is enabled.&lt;br/&gt; When the flag is true, the $.alertSources is the source of truth and will update $.condition and $.displayExpression with the corresponding expanded queries.&lt;br/&gt; When the flag is false, it goes through the old way and the $.condition and$.displayExpression is the source of truth and will auto-create $.alertSources  | [optional] [default to false]
 **body** | [**Alert**](Alert.md)| Example Classic Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;Alert Name\&quot;,   \&quot;target\&quot;: \&quot;target:alert-target-id\&quot;,   \&quot;condition\&quot;: \&quot;ts(~sample.cpu.loadavg.1m) &gt; 1\&quot;,   \&quot;conditionQueryType\&quot;: \&quot;WQL\&quot;,   \&quot;displayExpression\&quot;: \&quot;ts(~sample.cpu.loadavg.1m)\&quot;,   \&quot;displayExpressionQueryType\&quot;: \&quot;WQL\&quot;,   \&quot;minutes\&quot;: 5,   \&quot;resolveAfterMinutes\&quot;: 2,   \&quot;severity\&quot;: \&quot;INFO\&quot;,   \&quot;alertTriageDashboards\&quot;: [{     \&quot;dashboardId\&quot;: \&quot;dashboard-name\&quot;,     \&quot;parameters\&quot;: {       \&quot;constants\&quot;: {         \&quot;key\&quot;: \&quot;value\&quot;         }       },    \&quot;description\&quot;: \&quot;dashboard description\&quot;     }   ],   \&quot;additionalInformation\&quot;: \&quot;Additional Info\&quot;,   \&quot;tags\&quot;: {     \&quot;customerTags\&quot;: [       \&quot;alertTag1\&quot;     ]   } }&lt;/pre&gt; Example Classic Body with multi queries:  &lt;pre&gt;{     \&quot;name\&quot;: \&quot;Alert Name\&quot;,     \&quot;alertType\&quot;: \&quot;CLASSIC\&quot;,     \&quot;alertSources\&quot;: [        {             \&quot;name\&quot;: \&quot;A\&quot;,             \&quot;query\&quot;: \&quot;${B} &gt; 2\&quot;,             \&quot;queryType\&quot;: \&quot;PROMQL\&quot;,             \&quot;alertSourceType\&quot;: [\&quot;CONDITION\&quot;]         },         {             \&quot;name\&quot;: \&quot;B\&quot;,             \&quot;query\&quot;: \&quot;sum_over_time(~sample.network.bytes.recv[1m])\&quot;,             \&quot;queryType\&quot;: \&quot;PROMQL\&quot;,             \&quot;alertSourceType\&quot;: [\&quot;AUDIT\&quot;]         }     ],     \&quot;severity\&quot;: \&quot;WARN\&quot;,     \&quot;minutes\&quot;: 5 }&lt;/pre&gt; Example Threshold Body:  &lt;pre&gt;{     \&quot;name\&quot;: \&quot;Alert Name\&quot;,     \&quot;alertType\&quot;: \&quot;THRESHOLD\&quot;,     \&quot;conditions\&quot;: {         \&quot;info\&quot;: \&quot;ts(~sample.cpu.loadavg.1m) &gt; 0\&quot;,         \&quot;warn\&quot;: \&quot;ts(~sample.cpu.loadavg.1m) &gt; 2\&quot;     },     \&quot;displayExpression\&quot;: \&quot;ts(~sample.cpu.loadavg.1m)\&quot;,     \&quot;minutes\&quot;: 5,     \&quot;additionalInformation\&quot;: \&quot;conditions value entry needs to be of the form: displayExpression operator threshold\&quot; }&lt;/pre&gt; Example Threshold Body with multi queries:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;Alert Name\&quot;,   \&quot;alertType\&quot;: \&quot;THRESHOLD\&quot;,   \&quot;alertSources\&quot;: [     {       \&quot;name\&quot;: \&quot;A\&quot;,       \&quot;query\&quot;: \&quot;${B}\&quot;,       \&quot;queryType\&quot;: \&quot;PROMQL\&quot;,       \&quot;alertSourceType\&quot;: [\&quot;CONDITION\&quot;]     },     {       \&quot;name\&quot;: \&quot;B\&quot;,       \&quot;query\&quot;: \&quot;sum_over_time(~sample.network.bytes.recv[1m])\&quot;,       \&quot;queryType\&quot;: \&quot;PROMQL\&quot;,       \&quot;alertSourceType\&quot;: [\&quot;AUDIT\&quot;]     }   ],   \&quot;conditions\&quot;: {     \&quot;info\&quot;: \&quot;${B} &gt; bool 0\&quot;,     \&quot;warn\&quot;: \&quot;${B} &gt; bool 2\&quot;   },   \&quot;minutes\&quot;: 5 }&lt;/pre&gt; Supported Characters of Tags:  &lt;pre&gt;Tag names can contain alphanumeric (a-z, A-Z, 0-9),  dash (-), underscore (_), and colon (:) characters. The space character is not supported.&lt;/pre&gt;  | [optional] 

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert**
> ResponseContainerAlert delete_alert(id, skip_trash=skip_trash)

Delete a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
skip_trash = false # bool |  (optional) (default to false)

try:
    # Delete a specific alert
    api_response = api_instance.delete_alert(id, skip_trash=skip_trash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->delete_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **skip_trash** | **bool**|  | [optional] [default to false]

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert**
> ResponseContainerAlert get_alert(id)

Get a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific alert
    api_response = api_instance.get_alert(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_access_control_list**
> ResponseContainerListAccessControlListReadDTO get_alert_access_control_list(id=id)

Get Access Control Lists' union for the specified alerts



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = ['id_example'] # list[str] |  (optional)

try:
    # Get Access Control Lists' union for the specified alerts
    api_response = api_instance.get_alert_access_control_list(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_alert_access_control_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**ResponseContainerListAccessControlListReadDTO**](ResponseContainerListAccessControlListReadDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_history**
> ResponseContainerHistoryResponse get_alert_history(id, offset=offset, limit=limit)

Get the version history of a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get the version history of a specific alert
    api_response = api_instance.get_alert_history(id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_alert_history: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_tags**
> ResponseContainerTagsResponse get_alert_tags(id)

Get all tags associated with a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get all tags associated with a specific alert
    api_response = api_instance.get_alert_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_alert_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerTagsResponse**](ResponseContainerTagsResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_version**
> ResponseContainerAlert get_alert_version(id, version)

Get a specific historical version of a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
version = 789 # int | 

try:
    # Get a specific historical version of a specific alert
    api_response = api_instance.get_alert_version(id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_alert_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **version** | **int**|  | 

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts_summary**
> ResponseContainerMapStringInteger get_alerts_summary()

Count alerts of various statuses for a customer



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))

try:
    # Count alerts of various statuses for a customer
    api_response = api_instance.get_alerts_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_alerts_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseContainerMapStringInteger**](ResponseContainerMapStringInteger.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_alert**
> ResponseContainerPagedAlert get_all_alert(offset=offset, limit=limit)

Get all alerts for a customer



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all alerts for a customer
    api_response = api_instance.get_all_alert(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_all_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedAlert**](ResponseContainerPagedAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hide_alert**
> ResponseContainerAlert hide_alert(id)

Hide a specific integration alert 



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 789 # int | 

try:
    # Hide a specific integration alert 
    api_response = api_instance.hide_alert(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->hide_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_alert_notification**
> ResponseContainerListNotificationMessages preview_alert_notification(body=body)

Get all the notification preview for a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.Alert() # Alert |  (optional)

try:
    # Get all the notification preview for a specific alert
    api_response = api_instance.preview_alert_notification(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->preview_alert_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Alert**](Alert.md)|  | [optional] 

### Return type

[**ResponseContainerListNotificationMessages**](ResponseContainerListNotificationMessages.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_alert_access**
> remove_alert_access(body=body)

Removes the specified ids from the given alerts' ACL



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
body = [wavefront_api_client.AccessControlListWriteDTO()] # list[AccessControlListWriteDTO] |  (optional)

try:
    # Removes the specified ids from the given alerts' ACL
    api_instance.remove_alert_access(body=body)
except ApiException as e:
    print("Exception when calling AlertApi->remove_alert_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AccessControlListWriteDTO]**](AccessControlListWriteDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_alert_tag**
> ResponseContainerVoid remove_alert_tag(id, tag_value)

Remove a tag from a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
tag_value = 'tag_value_example' # str | Supported Characters of Tags:  <pre>Tag names can contain alphanumeric (a-z, A-Z, 0-9),  dash (-), underscore (_), and colon (:) characters. The space character is not supported.</pre> 

try:
    # Remove a tag from a specific alert
    api_response = api_instance.remove_alert_tag(id, tag_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->remove_alert_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tag_value** | **str**| Supported Characters of Tags:  &lt;pre&gt;Tag names can contain alphanumeric (a-z, A-Z, 0-9),  dash (-), underscore (_), and colon (:) characters. The space character is not supported.&lt;/pre&gt;  | 

### Return type

[**ResponseContainerVoid**](ResponseContainerVoid.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_alert_acl**
> set_alert_acl(body=body)

Set ACL for the specified alerts



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
body = [wavefront_api_client.AccessControlListWriteDTO()] # list[AccessControlListWriteDTO] |  (optional)

try:
    # Set ACL for the specified alerts
    api_instance.set_alert_acl(body=body)
except ApiException as e:
    print("Exception when calling AlertApi->set_alert_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AccessControlListWriteDTO]**](AccessControlListWriteDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_alert_tags**
> ResponseContainerVoid set_alert_tags(id, body=body)

Set all tags associated with a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = [wavefront_api_client.list[str]()] # list[str] | Supported Characters of Tags:  <pre>Tag names can contain alphanumeric (a-z, A-Z, 0-9),  dash (-), underscore (_), and colon (:) characters. The space character is not supported.</pre>  (optional)

try:
    # Set all tags associated with a specific alert
    api_response = api_instance.set_alert_tags(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->set_alert_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **list[str]**| Supported Characters of Tags:  &lt;pre&gt;Tag names can contain alphanumeric (a-z, A-Z, 0-9),  dash (-), underscore (_), and colon (:) characters. The space character is not supported.&lt;/pre&gt;  | [optional] 

### Return type

[**ResponseContainerVoid**](ResponseContainerVoid.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snooze_alert**
> ResponseContainerAlert snooze_alert(id, seconds=seconds)

Snooze a specific alert for some number of seconds



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
seconds = 789 # int |  (optional)

try:
    # Snooze a specific alert for some number of seconds
    api_response = api_instance.snooze_alert(id, seconds=seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->snooze_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **seconds** | **int**|  | [optional] 

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undelete_alert**
> ResponseContainerAlert undelete_alert(id)

Undelete a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 789 # int | 

try:
    # Undelete a specific alert
    api_response = api_instance.undelete_alert(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->undelete_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unhide_alert**
> ResponseContainerAlert unhide_alert(id)

Unhide a specific integration alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 789 # int | 

try:
    # Unhide a specific integration alert
    api_response = api_instance.unhide_alert(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->unhide_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsnooze_alert**
> ResponseContainerAlert unsnooze_alert(id)

Unsnooze a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 789 # int | 

try:
    # Unsnooze a specific alert
    api_response = api_instance.unsnooze_alert(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->unsnooze_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert**
> ResponseContainerAlert update_alert(id, use_multi_query=use_multi_query, body=body)

Update a specific alert



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
api_instance = wavefront_api_client.AlertApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
use_multi_query = false # bool | A flag indicates whether to use the new multi-query alert structures when the feature is enabled.<br/> When the flag is true, the $.alertSources is the source of truth and will update $.condition and $.displayExpression with the corresponding expanded queries.<br/> When the flag is false, it goes through the old way and the $.condition and$.displayExpression is the source of truth and will auto-update $.alertSources  (optional) (default to false)
body = wavefront_api_client.Alert() # Alert | Example Classic Body:  <pre>{   \"id\": \"1459375928549\",   \"name\": \"Alert Name\",   \"target\": \"target:alert-target-id\",   \"condition\": \"ts(~sample.cpu.loadavg.1m) > 1\",   \"conditionQueryType\": \"WQL\",   \"displayExpression\": \"ts(~sample.cpu.loadavg.1m)\",   \"displayExpressionQueryType\": \"WQL\",   \"minutes\": 5,   \"resolveAfterMinutes\": 2,   \"severity\": \"INFO\",   \"additionalInformation\": \"Additional Info\",   \"tags\": {     \"customerTags\": [       \"alertTag1\"     ]   } }</pre> Example Classic Body with multi queries:  <pre>{   \"id\": \"1459375928549\",     \"name\": \"Alert Name\",     \"alertType\": \"CLASSIC\",     \"alertSources\": [        {             \"name\": \"A\",             \"query\": \"${B} > 2\",             \"queryType\": \"PROMQL\",             \"alertSourceType\": [\"CONDITION\"]         },         {             \"name\": \"B\",             \"query\": \"sum_over_time(~sample.network.bytes.recv[1m])\",             \"queryType\": \"PROMQL\",             \"alertSourceType\": [\"AUDIT\"]         }     ],     \"severity\": \"WARN\",     \"minutes\": 5 }</pre> Example Threshold Body:  <pre>{     \"id\": \"1459375928550\",     \"name\": \"Alert Name\",     \"alertType\": \"THRESHOLD\",     \"conditions\": {         \"info\": \"ts(~sample.cpu.loadavg.1m) > 0\",         \"warn\": \"ts(~sample.cpu.loadavg.1m) > 5\"     },     \"displayExpression\": \"ts(~sample.cpu.loadavg.1m)\",     \"minutes\": 5,     \"resolveAfterMinutes\": 2,     \"additionalInformation\": \"conditions value entry needs to be of the form: displayExpression operator threshold\" }</pre> Example Threshold Body with multi queries:  <pre>{   \"id\": \"1459375928549\",   \"name\": \"Alert Name\",   \"alertType\": \"THRESHOLD\",   \"alertSources\": [     {       \"name\": \"A\",       \"query\": \"${B}\",       \"queryType\": \"PROMQL\",       \"alertSourceType\": [\"CONDITION\"]     },     {       \"name\": \"B\",       \"query\": \"sum_over_time(~sample.network.bytes.recv[1m])\",       \"queryType\": \"PROMQL\",       \"alertSourceType\": [\"AUDIT\"]     }   ],   \"conditions\": {     \"info\": \"${B} > bool 0\",     \"warn\": \"${B} > bool 2\"   },   \"minutes\": 5 }</pre> Supported Characters of Tags:  <pre>Tag names can contain alphanumeric (a-z, A-Z, 0-9),  dash (-), underscore (_), and colon (:) characters. The space character is not supported.</pre>  (optional)

try:
    # Update a specific alert
    api_response = api_instance.update_alert(id, use_multi_query=use_multi_query, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->update_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **use_multi_query** | **bool**| A flag indicates whether to use the new multi-query alert structures when the feature is enabled.&lt;br/&gt; When the flag is true, the $.alertSources is the source of truth and will update $.condition and $.displayExpression with the corresponding expanded queries.&lt;br/&gt; When the flag is false, it goes through the old way and the $.condition and$.displayExpression is the source of truth and will auto-update $.alertSources  | [optional] [default to false]
 **body** | [**Alert**](Alert.md)| Example Classic Body:  &lt;pre&gt;{   \&quot;id\&quot;: \&quot;1459375928549\&quot;,   \&quot;name\&quot;: \&quot;Alert Name\&quot;,   \&quot;target\&quot;: \&quot;target:alert-target-id\&quot;,   \&quot;condition\&quot;: \&quot;ts(~sample.cpu.loadavg.1m) &gt; 1\&quot;,   \&quot;conditionQueryType\&quot;: \&quot;WQL\&quot;,   \&quot;displayExpression\&quot;: \&quot;ts(~sample.cpu.loadavg.1m)\&quot;,   \&quot;displayExpressionQueryType\&quot;: \&quot;WQL\&quot;,   \&quot;minutes\&quot;: 5,   \&quot;resolveAfterMinutes\&quot;: 2,   \&quot;severity\&quot;: \&quot;INFO\&quot;,   \&quot;additionalInformation\&quot;: \&quot;Additional Info\&quot;,   \&quot;tags\&quot;: {     \&quot;customerTags\&quot;: [       \&quot;alertTag1\&quot;     ]   } }&lt;/pre&gt; Example Classic Body with multi queries:  &lt;pre&gt;{   \&quot;id\&quot;: \&quot;1459375928549\&quot;,     \&quot;name\&quot;: \&quot;Alert Name\&quot;,     \&quot;alertType\&quot;: \&quot;CLASSIC\&quot;,     \&quot;alertSources\&quot;: [        {             \&quot;name\&quot;: \&quot;A\&quot;,             \&quot;query\&quot;: \&quot;${B} &gt; 2\&quot;,             \&quot;queryType\&quot;: \&quot;PROMQL\&quot;,             \&quot;alertSourceType\&quot;: [\&quot;CONDITION\&quot;]         },         {             \&quot;name\&quot;: \&quot;B\&quot;,             \&quot;query\&quot;: \&quot;sum_over_time(~sample.network.bytes.recv[1m])\&quot;,             \&quot;queryType\&quot;: \&quot;PROMQL\&quot;,             \&quot;alertSourceType\&quot;: [\&quot;AUDIT\&quot;]         }     ],     \&quot;severity\&quot;: \&quot;WARN\&quot;,     \&quot;minutes\&quot;: 5 }&lt;/pre&gt; Example Threshold Body:  &lt;pre&gt;{     \&quot;id\&quot;: \&quot;1459375928550\&quot;,     \&quot;name\&quot;: \&quot;Alert Name\&quot;,     \&quot;alertType\&quot;: \&quot;THRESHOLD\&quot;,     \&quot;conditions\&quot;: {         \&quot;info\&quot;: \&quot;ts(~sample.cpu.loadavg.1m) &gt; 0\&quot;,         \&quot;warn\&quot;: \&quot;ts(~sample.cpu.loadavg.1m) &gt; 5\&quot;     },     \&quot;displayExpression\&quot;: \&quot;ts(~sample.cpu.loadavg.1m)\&quot;,     \&quot;minutes\&quot;: 5,     \&quot;resolveAfterMinutes\&quot;: 2,     \&quot;additionalInformation\&quot;: \&quot;conditions value entry needs to be of the form: displayExpression operator threshold\&quot; }&lt;/pre&gt; Example Threshold Body with multi queries:  &lt;pre&gt;{   \&quot;id\&quot;: \&quot;1459375928549\&quot;,   \&quot;name\&quot;: \&quot;Alert Name\&quot;,   \&quot;alertType\&quot;: \&quot;THRESHOLD\&quot;,   \&quot;alertSources\&quot;: [     {       \&quot;name\&quot;: \&quot;A\&quot;,       \&quot;query\&quot;: \&quot;${B}\&quot;,       \&quot;queryType\&quot;: \&quot;PROMQL\&quot;,       \&quot;alertSourceType\&quot;: [\&quot;CONDITION\&quot;]     },     {       \&quot;name\&quot;: \&quot;B\&quot;,       \&quot;query\&quot;: \&quot;sum_over_time(~sample.network.bytes.recv[1m])\&quot;,       \&quot;queryType\&quot;: \&quot;PROMQL\&quot;,       \&quot;alertSourceType\&quot;: [\&quot;AUDIT\&quot;]     }   ],   \&quot;conditions\&quot;: {     \&quot;info\&quot;: \&quot;${B} &gt; bool 0\&quot;,     \&quot;warn\&quot;: \&quot;${B} &gt; bool 2\&quot;   },   \&quot;minutes\&quot;: 5 }&lt;/pre&gt; Supported Characters of Tags:  &lt;pre&gt;Tag names can contain alphanumeric (a-z, A-Z, 0-9),  dash (-), underscore (_), and colon (:) characters. The space character is not supported.&lt;/pre&gt;  | [optional] 

### Return type

[**ResponseContainerAlert**](ResponseContainerAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

