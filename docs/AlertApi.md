# wavefront_client.AlertApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alert_from_parts**](AlertApi.md#create_alert_from_parts) | **POST** /api/alert/create | Create an alert
[**get_active_alerts**](AlertApi.md#get_active_alerts) | **GET** /api/alert/active | Get Active Alerts
[**get_alert**](AlertApi.md#get_alert) | **GET** /api/alert | Retrieve a list of alerts for a particular view. (Deprecated: Retrieve a single alert by its id (creation time))
[**get_alerts**](AlertApi.md#get_alerts) | **GET** /api/alert/all | Get All Alerts
[**get_alerts_affected_by_maintenance**](AlertApi.md#get_alerts_affected_by_maintenance) | **GET** /api/alert/affected_by_maintenance | Get In Maintenance Alerts
[**get_invalid_alerts**](AlertApi.md#get_invalid_alerts) | **GET** /api/alert/invalid | Get Invalid Alerts
[**get_snoozed_alerts**](AlertApi.md#get_snoozed_alerts) | **GET** /api/alert/snoozed | Get Snoozed Alerts
[**get_specific_alert**](AlertApi.md#get_specific_alert) | **GET** /api/alert/{created} | Retrieve a single alert by its id (creation time)
[**update_alert_from_parts**](AlertApi.md#update_alert_from_parts) | **POST** /api/alert/{alertId} | Update an alert


# **create_alert_from_parts**
> Alert create_alert_from_parts(name, condition, minutes, notifications, severity, display_expression=display_expression, resolve_minutes=resolve_minutes, private_tags=private_tags, shared_tags=shared_tags, additional_information=additional_information)

Create an alert



### Example 
```python
import time
import wavefront_client
from wavefront_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
wavefront_client.configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# wavefront_client.configuration.api_key_prefix['X-AUTH-TOKEN'] = 'BEARER'

# create an instance of the API class
api_instance = wavefront_client.AlertApi()
name = 'name_example' # str | Descriptive name for the alert
condition = 'condition_example' # str | A query that will trigger the alert if non-zero results are observed for given number of minutes
minutes = 56 # int | Number of minutes for the query to return non-zero results before the alert fires. Must be 2 or higher
notifications = 'notifications_example' # str | Up to ten addresses can be listed, separated by commas. Notifications will be sent to all targets on the list. To trigger a PagerDuty incident, specify a \"pd:key\" target with the 32-digit hex API key you created. PagerDuty incidents will be automatically triggered, updated, and resolved.
severity = 'severity_example' # str | Severity
display_expression = 'display_expression_example' # str | An optional query that will be shown when the alert fires. Use this to show a more helpful chart, e.g. the underlying timeseries (optional)
resolve_minutes = 56 # int | Number of minutes for the query to return 0 as a result before the alert resolves. Defaults to the same as minutes to fire if not set. Must be 2 or higher (optional)
private_tags = 'private_tags_example' # str | Comma separated list of private tags to be associated with this alert (optional)
shared_tags = 'shared_tags_example' # str | Comma separated list of shared tags to be associated with this alert (optional)
additional_information = 'additional_information_example' # str | Any additional information to be included with this alert (optional)

try: 
    # Create an alert
    api_response = api_instance.create_alert_from_parts(name, condition, minutes, notifications, severity, display_expression=display_expression, resolve_minutes=resolve_minutes, private_tags=private_tags, shared_tags=shared_tags, additional_information=additional_information)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertApi->create_alert_from_parts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Descriptive name for the alert | 
 **condition** | **str**| A query that will trigger the alert if non-zero results are observed for given number of minutes | 
 **minutes** | **int**| Number of minutes for the query to return non-zero results before the alert fires. Must be 2 or higher | 
 **notifications** | **str**| Up to ten addresses can be listed, separated by commas. Notifications will be sent to all targets on the list. To trigger a PagerDuty incident, specify a \&quot;pd:key\&quot; target with the 32-digit hex API key you created. PagerDuty incidents will be automatically triggered, updated, and resolved. | 
 **severity** | **str**| Severity | 
 **display_expression** | **str**| An optional query that will be shown when the alert fires. Use this to show a more helpful chart, e.g. the underlying timeseries | [optional] 
 **resolve_minutes** | **int**| Number of minutes for the query to return 0 as a result before the alert resolves. Defaults to the same as minutes to fire if not set. Must be 2 or higher | [optional] 
 **private_tags** | **str**| Comma separated list of private tags to be associated with this alert | [optional] 
 **shared_tags** | **str**| Comma separated list of shared tags to be associated with this alert | [optional] 
 **additional_information** | **str**| Any additional information to be included with this alert | [optional] 

### Return type

[**Alert**](Alert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_alerts**
> list[Alert] get_active_alerts(customer_tag=customer_tag, user_tag=user_tag)

Get Active Alerts

Return all firing alerts

### Example 
```python
import time
import wavefront_client
from wavefront_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
wavefront_client.configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# wavefront_client.configuration.api_key_prefix['X-AUTH-TOKEN'] = 'BEARER'

# create an instance of the API class
api_instance = wavefront_client.AlertApi()
customer_tag = ['customer_tag_example'] # list[str] | Restrict result to alerts with this shared tag (optional)
user_tag = ['user_tag_example'] # list[str] | Restrict result to alerts with this private tag (optional)

try: 
    # Get Active Alerts
    api_response = api_instance.get_active_alerts(customer_tag=customer_tag, user_tag=user_tag)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertApi->get_active_alerts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_tag** | [**list[str]**](str.md)| Restrict result to alerts with this shared tag | [optional] 
 **user_tag** | [**list[str]**](str.md)| Restrict result to alerts with this private tag | [optional] 

### Return type

[**list[Alert]**](Alert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert**
> Alert get_alert(created=created, view=view, customer_tag=customer_tag, user_tag=user_tag)

Retrieve a list of alerts for a particular view. (Deprecated: Retrieve a single alert by its id (creation time))



### Example 
```python
import time
import wavefront_client
from wavefront_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
wavefront_client.configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# wavefront_client.configuration.api_key_prefix['X-AUTH-TOKEN'] = 'BEARER'

# create an instance of the API class
api_instance = wavefront_client.AlertApi()
created = 789 # int | (Deprecated) (optional)
view = 'view_example' # str |  (optional)
customer_tag = ['customer_tag_example'] # list[str] | Restrict result to alerts with this shared tag (optional)
user_tag = ['user_tag_example'] # list[str] | Restrict result to alerts with this private tag (optional)

try: 
    # Retrieve a list of alerts for a particular view. (Deprecated: Retrieve a single alert by its id (creation time))
    api_response = api_instance.get_alert(created=created, view=view, customer_tag=customer_tag, user_tag=user_tag)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertApi->get_alert: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created** | **int**| (Deprecated) | [optional] 
 **view** | **str**|  | [optional] 
 **customer_tag** | [**list[str]**](str.md)| Restrict result to alerts with this shared tag | [optional] 
 **user_tag** | [**list[str]**](str.md)| Restrict result to alerts with this private tag | [optional] 

### Return type

[**Alert**](Alert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts**
> list[Alert] get_alerts(customer_tag=customer_tag, user_tag=user_tag)

Get All Alerts

Return all alerts

### Example 
```python
import time
import wavefront_client
from wavefront_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
wavefront_client.configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# wavefront_client.configuration.api_key_prefix['X-AUTH-TOKEN'] = 'BEARER'

# create an instance of the API class
api_instance = wavefront_client.AlertApi()
customer_tag = ['customer_tag_example'] # list[str] | Restrict result to alerts with this shared tag (optional)
user_tag = ['user_tag_example'] # list[str] | Restrict result to alerts with this private tag (optional)

try: 
    # Get All Alerts
    api_response = api_instance.get_alerts(customer_tag=customer_tag, user_tag=user_tag)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertApi->get_alerts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_tag** | [**list[str]**](str.md)| Restrict result to alerts with this shared tag | [optional] 
 **user_tag** | [**list[str]**](str.md)| Restrict result to alerts with this private tag | [optional] 

### Return type

[**list[Alert]**](Alert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts_affected_by_maintenance**
> list[Alert] get_alerts_affected_by_maintenance(customer_tag=customer_tag, user_tag=user_tag)

Get In Maintenance Alerts

Return all alerts currently in a maintenance window

### Example 
```python
import time
import wavefront_client
from wavefront_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
wavefront_client.configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# wavefront_client.configuration.api_key_prefix['X-AUTH-TOKEN'] = 'BEARER'

# create an instance of the API class
api_instance = wavefront_client.AlertApi()
customer_tag = ['customer_tag_example'] # list[str] | Restrict result to alerts with this shared tag (optional)
user_tag = ['user_tag_example'] # list[str] | Restrict result to alerts with this private tag (optional)

try: 
    # Get In Maintenance Alerts
    api_response = api_instance.get_alerts_affected_by_maintenance(customer_tag=customer_tag, user_tag=user_tag)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertApi->get_alerts_affected_by_maintenance: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_tag** | [**list[str]**](str.md)| Restrict result to alerts with this shared tag | [optional] 
 **user_tag** | [**list[str]**](str.md)| Restrict result to alerts with this private tag | [optional] 

### Return type

[**list[Alert]**](Alert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invalid_alerts**
> list[Alert] get_invalid_alerts(customer_tag=customer_tag, user_tag=user_tag)

Get Invalid Alerts

Return all alerts that have an invalid query

### Example 
```python
import time
import wavefront_client
from wavefront_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
wavefront_client.configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# wavefront_client.configuration.api_key_prefix['X-AUTH-TOKEN'] = 'BEARER'

# create an instance of the API class
api_instance = wavefront_client.AlertApi()
customer_tag = ['customer_tag_example'] # list[str] | Restrict result to alerts with this shared tag (optional)
user_tag = ['user_tag_example'] # list[str] | Restrict result to alerts with this private tag (optional)

try: 
    # Get Invalid Alerts
    api_response = api_instance.get_invalid_alerts(customer_tag=customer_tag, user_tag=user_tag)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertApi->get_invalid_alerts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_tag** | [**list[str]**](str.md)| Restrict result to alerts with this shared tag | [optional] 
 **user_tag** | [**list[str]**](str.md)| Restrict result to alerts with this private tag | [optional] 

### Return type

[**list[Alert]**](Alert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snoozed_alerts**
> list[Alert] get_snoozed_alerts(customer_tag=customer_tag, user_tag=user_tag)

Get Snoozed Alerts

Return all snoozed alerts

### Example 
```python
import time
import wavefront_client
from wavefront_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
wavefront_client.configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# wavefront_client.configuration.api_key_prefix['X-AUTH-TOKEN'] = 'BEARER'

# create an instance of the API class
api_instance = wavefront_client.AlertApi()
customer_tag = ['customer_tag_example'] # list[str] | Restrict result to alerts with this shared tag (optional)
user_tag = ['user_tag_example'] # list[str] | Restrict result to alerts with this private tag (optional)

try: 
    # Get Snoozed Alerts
    api_response = api_instance.get_snoozed_alerts(customer_tag=customer_tag, user_tag=user_tag)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertApi->get_snoozed_alerts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_tag** | [**list[str]**](str.md)| Restrict result to alerts with this shared tag | [optional] 
 **user_tag** | [**list[str]**](str.md)| Restrict result to alerts with this private tag | [optional] 

### Return type

[**list[Alert]**](Alert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_specific_alert**
> Alert get_specific_alert(created)

Retrieve a single alert by its id (creation time)



### Example 
```python
import time
import wavefront_client
from wavefront_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
wavefront_client.configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# wavefront_client.configuration.api_key_prefix['X-AUTH-TOKEN'] = 'BEARER'

# create an instance of the API class
api_instance = wavefront_client.AlertApi()
created = 789 # int | 

try: 
    # Retrieve a single alert by its id (creation time)
    api_response = api_instance.get_specific_alert(created)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertApi->get_specific_alert: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created** | **int**|  | 

### Return type

[**Alert**](Alert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_from_parts**
> Alert update_alert_from_parts(alert_id, name=name, condition=condition, display_expression=display_expression, minutes=minutes, resolve_minutes=resolve_minutes, notifications=notifications, severity=severity, private_tags=private_tags, shared_tags=shared_tags, additional_information=additional_information)

Update an alert



### Example 
```python
import time
import wavefront_client
from wavefront_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
wavefront_client.configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. BEARER) for API key, if needed
# wavefront_client.configuration.api_key_prefix['X-AUTH-TOKEN'] = 'BEARER'

# create an instance of the API class
api_instance = wavefront_client.AlertApi()
alert_id = 789 # int | 
name = 'name_example' # str | Descriptive name for the alert (optional)
condition = 'condition_example' # str | A query that will trigger the alert if non-zero results are observed for given number of minutes (optional)
display_expression = 'display_expression_example' # str | An optional query that will be shown when the alert fires. Use this to show a more helpful chart, e.g. the underlying timeseries (optional)
minutes = 56 # int | Number of minutes for the query to return non-zero results before the alert fires. Must be 2 or higher (optional)
resolve_minutes = 56 # int | Number of minutes for the query to return 0 as a result before the alert resolves. Defaults to the same as minutes to fire if not set. Must be 2 or higher (optional)
notifications = 'notifications_example' # str | Up to ten addresses can be listed,  separated by commas. Notifications will be sent to all targets on the list. To trigger a PagerDuty incident, specify a \"pd:key\" target with the 32-digit hex API key you created. PagerDuty incidents will be automatically triggered, updated, and resolved. (optional)
severity = 'severity_example' # str | Severity (optional)
private_tags = 'private_tags_example' # str | Comma separated list of private tags to be associated with this alert (optional)
shared_tags = 'shared_tags_example' # str | Comma separated list of shared tags to be associated with this alert (optional)
additional_information = 'additional_information_example' # str | Any additional information to be included with this alert (optional)

try: 
    # Update an alert
    api_response = api_instance.update_alert_from_parts(alert_id, name=name, condition=condition, display_expression=display_expression, minutes=minutes, resolve_minutes=resolve_minutes, notifications=notifications, severity=severity, private_tags=private_tags, shared_tags=shared_tags, additional_information=additional_information)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AlertApi->update_alert_from_parts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **int**|  | 
 **name** | **str**| Descriptive name for the alert | [optional] 
 **condition** | **str**| A query that will trigger the alert if non-zero results are observed for given number of minutes | [optional] 
 **display_expression** | **str**| An optional query that will be shown when the alert fires. Use this to show a more helpful chart, e.g. the underlying timeseries | [optional] 
 **minutes** | **int**| Number of minutes for the query to return non-zero results before the alert fires. Must be 2 or higher | [optional] 
 **resolve_minutes** | **int**| Number of minutes for the query to return 0 as a result before the alert resolves. Defaults to the same as minutes to fire if not set. Must be 2 or higher | [optional] 
 **notifications** | **str**| Up to ten addresses can be listed,  separated by commas. Notifications will be sent to all targets on the list. To trigger a PagerDuty incident, specify a \&quot;pd:key\&quot; target with the 32-digit hex API key you created. PagerDuty incidents will be automatically triggered, updated, and resolved. | [optional] 
 **severity** | **str**| Severity | [optional] 
 **private_tags** | **str**| Comma separated list of private tags to be associated with this alert | [optional] 
 **shared_tags** | **str**| Comma separated list of shared tags to be associated with this alert | [optional] 
 **additional_information** | **str**| Any additional information to be included with this alert | [optional] 

### Return type

[**Alert**](Alert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

