# wavefront_api_client.SearchApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_account_entities**](SearchApi.md#search_account_entities) | **POST** /api/v2/search/account | Search over a customer&#39;s accounts
[**search_account_for_facet**](SearchApi.md#search_account_for_facet) | **POST** /api/v2/search/account/{facet} | Lists the values of a specific facet over the customer&#39;s accounts
[**search_account_for_facets**](SearchApi.md#search_account_for_facets) | **POST** /api/v2/search/account/facets | Lists the values of one or more facets over the customer&#39;s accounts
[**search_alert_deleted_entities**](SearchApi.md#search_alert_deleted_entities) | **POST** /api/v2/search/alert/deleted | Search over a customer&#39;s deleted alerts
[**search_alert_deleted_for_facet**](SearchApi.md#search_alert_deleted_for_facet) | **POST** /api/v2/search/alert/deleted/{facet} | Lists the values of a specific facet over the customer&#39;s deleted alerts
[**search_alert_deleted_for_facets**](SearchApi.md#search_alert_deleted_for_facets) | **POST** /api/v2/search/alert/deleted/facets | Lists the values of one or more facets over the customer&#39;s deleted alerts
[**search_alert_entities**](SearchApi.md#search_alert_entities) | **POST** /api/v2/search/alert | Search over a customer&#39;s non-deleted alerts
[**search_alert_for_facet**](SearchApi.md#search_alert_for_facet) | **POST** /api/v2/search/alert/{facet} | Lists the values of a specific facet over the customer&#39;s non-deleted alerts
[**search_alert_for_facets**](SearchApi.md#search_alert_for_facets) | **POST** /api/v2/search/alert/facets | Lists the values of one or more facets over the customer&#39;s non-deleted alerts
[**search_cloud_integration_deleted_entities**](SearchApi.md#search_cloud_integration_deleted_entities) | **POST** /api/v2/search/cloudintegration/deleted | Search over a customer&#39;s deleted cloud integrations
[**search_cloud_integration_deleted_for_facet**](SearchApi.md#search_cloud_integration_deleted_for_facet) | **POST** /api/v2/search/cloudintegration/deleted/{facet} | Lists the values of a specific facet over the customer&#39;s deleted cloud integrations
[**search_cloud_integration_deleted_for_facets**](SearchApi.md#search_cloud_integration_deleted_for_facets) | **POST** /api/v2/search/cloudintegration/deleted/facets | Lists the values of one or more facets over the customer&#39;s deleted cloud integrations
[**search_cloud_integration_entities**](SearchApi.md#search_cloud_integration_entities) | **POST** /api/v2/search/cloudintegration | Search over a customer&#39;s non-deleted cloud integrations
[**search_cloud_integration_for_facet**](SearchApi.md#search_cloud_integration_for_facet) | **POST** /api/v2/search/cloudintegration/{facet} | Lists the values of a specific facet over the customer&#39;s non-deleted cloud integrations
[**search_cloud_integration_for_facets**](SearchApi.md#search_cloud_integration_for_facets) | **POST** /api/v2/search/cloudintegration/facets | Lists the values of one or more facets over the customer&#39;s non-deleted cloud integrations
[**search_dashboard_deleted_entities**](SearchApi.md#search_dashboard_deleted_entities) | **POST** /api/v2/search/dashboard/deleted | Search over a customer&#39;s deleted dashboards
[**search_dashboard_deleted_for_facet**](SearchApi.md#search_dashboard_deleted_for_facet) | **POST** /api/v2/search/dashboard/deleted/{facet} | Lists the values of a specific facet over the customer&#39;s deleted dashboards
[**search_dashboard_deleted_for_facets**](SearchApi.md#search_dashboard_deleted_for_facets) | **POST** /api/v2/search/dashboard/deleted/facets | Lists the values of one or more facets over the customer&#39;s deleted dashboards
[**search_dashboard_entities**](SearchApi.md#search_dashboard_entities) | **POST** /api/v2/search/dashboard | Search over a customer&#39;s non-deleted dashboards
[**search_dashboard_for_facet**](SearchApi.md#search_dashboard_for_facet) | **POST** /api/v2/search/dashboard/{facet} | Lists the values of a specific facet over the customer&#39;s non-deleted dashboards
[**search_dashboard_for_facets**](SearchApi.md#search_dashboard_for_facets) | **POST** /api/v2/search/dashboard/facets | Lists the values of one or more facets over the customer&#39;s non-deleted dashboards
[**search_external_link_entities**](SearchApi.md#search_external_link_entities) | **POST** /api/v2/search/extlink | Search over a customer&#39;s external links
[**search_external_links_for_facet**](SearchApi.md#search_external_links_for_facet) | **POST** /api/v2/search/extlink/{facet} | Lists the values of a specific facet over the customer&#39;s external links
[**search_external_links_for_facets**](SearchApi.md#search_external_links_for_facets) | **POST** /api/v2/search/extlink/facets | Lists the values of one or more facets over the customer&#39;s external links
[**search_ingestion_policy_entities**](SearchApi.md#search_ingestion_policy_entities) | **POST** /api/v2/search/ingestionpolicy | Search over a customer&#39;s ingestion policies
[**search_ingestion_policy_for_facet**](SearchApi.md#search_ingestion_policy_for_facet) | **POST** /api/v2/search/ingestionpolicy/{facet} | Lists the values of a specific facet over the customer&#39;s ingestion policies
[**search_ingestion_policy_for_facets**](SearchApi.md#search_ingestion_policy_for_facets) | **POST** /api/v2/search/ingestionpolicy/facets | Lists the values of one or more facets over the customer&#39;s ingestion policies
[**search_maintenance_window_entities**](SearchApi.md#search_maintenance_window_entities) | **POST** /api/v2/search/maintenancewindow | Search over a customer&#39;s maintenance windows
[**search_maintenance_window_for_facet**](SearchApi.md#search_maintenance_window_for_facet) | **POST** /api/v2/search/maintenancewindow/{facet} | Lists the values of a specific facet over the customer&#39;s maintenance windows
[**search_maintenance_window_for_facets**](SearchApi.md#search_maintenance_window_for_facets) | **POST** /api/v2/search/maintenancewindow/facets | Lists the values of one or more facets over the customer&#39;s maintenance windows
[**search_monitored_cluster_entities**](SearchApi.md#search_monitored_cluster_entities) | **POST** /api/v2/search/monitoredcluster | Search over all the customer&#39;s non-deleted monitored clusters
[**search_monitored_cluster_for_facet**](SearchApi.md#search_monitored_cluster_for_facet) | **POST** /api/v2/search/monitoredcluster/{facet} | Lists the values of a specific facet over the customer&#39;s non-deleted monitored cluster
[**search_monitored_cluster_for_facets**](SearchApi.md#search_monitored_cluster_for_facets) | **POST** /api/v2/search/monitoredcluster/facets | Lists the values of one or more facets over the customer&#39;s non-deleted monitored clusters
[**search_notficant_for_facets**](SearchApi.md#search_notficant_for_facets) | **POST** /api/v2/search/notificant/facets | Lists the values of one or more facets over the customer&#39;s notificants
[**search_notificant_entities**](SearchApi.md#search_notificant_entities) | **POST** /api/v2/search/notificant | Search over a customer&#39;s notificants
[**search_notificant_for_facet**](SearchApi.md#search_notificant_for_facet) | **POST** /api/v2/search/notificant/{facet} | Lists the values of a specific facet over the customer&#39;s notificants
[**search_proxy_deleted_entities**](SearchApi.md#search_proxy_deleted_entities) | **POST** /api/v2/search/proxy/deleted | Search over a customer&#39;s deleted proxies
[**search_proxy_deleted_for_facet**](SearchApi.md#search_proxy_deleted_for_facet) | **POST** /api/v2/search/proxy/deleted/{facet} | Lists the values of a specific facet over the customer&#39;s deleted proxies
[**search_proxy_deleted_for_facets**](SearchApi.md#search_proxy_deleted_for_facets) | **POST** /api/v2/search/proxy/deleted/facets | Lists the values of one or more facets over the customer&#39;s deleted proxies
[**search_proxy_entities**](SearchApi.md#search_proxy_entities) | **POST** /api/v2/search/proxy | Search over a customer&#39;s non-deleted proxies
[**search_proxy_for_facet**](SearchApi.md#search_proxy_for_facet) | **POST** /api/v2/search/proxy/{facet} | Lists the values of a specific facet over the customer&#39;s non-deleted proxies
[**search_proxy_for_facets**](SearchApi.md#search_proxy_for_facets) | **POST** /api/v2/search/proxy/facets | Lists the values of one or more facets over the customer&#39;s non-deleted proxies
[**search_registered_query_deleted_entities**](SearchApi.md#search_registered_query_deleted_entities) | **POST** /api/v2/search/derivedmetric/deleted | Search over a customer&#39;s deleted derived metric definitions
[**search_registered_query_deleted_for_facet**](SearchApi.md#search_registered_query_deleted_for_facet) | **POST** /api/v2/search/derivedmetric/deleted/{facet} | Lists the values of a specific facet over the customer&#39;s deleted derived metric definitions
[**search_registered_query_deleted_for_facets**](SearchApi.md#search_registered_query_deleted_for_facets) | **POST** /api/v2/search/derivedmetric/deleted/facets | Lists the values of one or more facets over the customer&#39;s deleted derived metric definitions
[**search_registered_query_entities**](SearchApi.md#search_registered_query_entities) | **POST** /api/v2/search/derivedmetric | Search over a customer&#39;s non-deleted derived metric definitions
[**search_registered_query_for_facet**](SearchApi.md#search_registered_query_for_facet) | **POST** /api/v2/search/derivedmetric/{facet} | Lists the values of a specific facet over the customer&#39;s non-deleted derived metric definitions
[**search_registered_query_for_facets**](SearchApi.md#search_registered_query_for_facets) | **POST** /api/v2/search/derivedmetric/facets | Lists the values of one or more facets over the customer&#39;s non-deleted derived metric definition
[**search_related_report_event_entities**](SearchApi.md#search_related_report_event_entities) | **POST** /api/v2/search/event/related/{eventId} | List the related events over a firing event
[**search_report_event_entities**](SearchApi.md#search_report_event_entities) | **POST** /api/v2/search/event | Search over a customer&#39;s events
[**search_report_event_for_facet**](SearchApi.md#search_report_event_for_facet) | **POST** /api/v2/search/event/{facet} | Lists the values of a specific facet over the customer&#39;s events
[**search_report_event_for_facets**](SearchApi.md#search_report_event_for_facets) | **POST** /api/v2/search/event/facets | Lists the values of one or more facets over the customer&#39;s events
[**search_role_entities**](SearchApi.md#search_role_entities) | **POST** /api/v2/search/role | Search over a customer&#39;s roles
[**search_role_for_facet**](SearchApi.md#search_role_for_facet) | **POST** /api/v2/search/role/{facet} | Lists the values of a specific facet over the customer&#39;s roles
[**search_role_for_facets**](SearchApi.md#search_role_for_facets) | **POST** /api/v2/search/role/facets | Lists the values of one or more facets over the customer&#39;s roles
[**search_service_account_entities**](SearchApi.md#search_service_account_entities) | **POST** /api/v2/search/serviceaccount | Search over a customer&#39;s service accounts
[**search_service_account_for_facet**](SearchApi.md#search_service_account_for_facet) | **POST** /api/v2/search/serviceaccount/{facet} | Lists the values of a specific facet over the customer&#39;s service accounts
[**search_service_account_for_facets**](SearchApi.md#search_service_account_for_facets) | **POST** /api/v2/search/serviceaccount/facets | Lists the values of one or more facets over the customer&#39;s service accounts
[**search_tagged_source_entities**](SearchApi.md#search_tagged_source_entities) | **POST** /api/v2/search/source | Search over a customer&#39;s sources
[**search_tagged_source_for_facet**](SearchApi.md#search_tagged_source_for_facet) | **POST** /api/v2/search/source/{facet} | Lists the values of a specific facet over the customer&#39;s sources
[**search_tagged_source_for_facets**](SearchApi.md#search_tagged_source_for_facets) | **POST** /api/v2/search/source/facets | Lists the values of one or more facets over the customer&#39;s sources
[**search_user_entities**](SearchApi.md#search_user_entities) | **POST** /api/v2/search/user | Search over a customer&#39;s users
[**search_user_for_facet**](SearchApi.md#search_user_for_facet) | **POST** /api/v2/search/user/{facet} | Lists the values of a specific facet over the customer&#39;s users
[**search_user_for_facets**](SearchApi.md#search_user_for_facets) | **POST** /api/v2/search/user/facets | Lists the values of one or more facets over the customer&#39;s users
[**search_user_group_entities**](SearchApi.md#search_user_group_entities) | **POST** /api/v2/search/usergroup | Search over a customer&#39;s user groups
[**search_user_group_for_facet**](SearchApi.md#search_user_group_for_facet) | **POST** /api/v2/search/usergroup/{facet} | Lists the values of a specific facet over the customer&#39;s user groups
[**search_user_group_for_facets**](SearchApi.md#search_user_group_for_facets) | **POST** /api/v2/search/usergroup/facets | Lists the values of one or more facets over the customer&#39;s user groups
[**search_web_hook_entities**](SearchApi.md#search_web_hook_entities) | **POST** /api/v2/search/webhook | Search over a customer&#39;s webhooks
[**search_web_hook_for_facet**](SearchApi.md#search_web_hook_for_facet) | **POST** /api/v2/search/webhook/{facet} | Lists the values of a specific facet over the customer&#39;s webhooks
[**search_webhook_for_facets**](SearchApi.md#search_webhook_for_facets) | **POST** /api/v2/search/webhook/facets | Lists the values of one or more facets over the customer&#39;s webhooks


# **search_account_entities**
> ResponseContainerPagedAccount search_account_entities(body=body)

Search over a customer's accounts



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's accounts
    api_response = api_instance.search_account_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_account_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedAccount**](ResponseContainerPagedAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_account_for_facet**
> ResponseContainerFacetResponse search_account_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's accounts



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's accounts
    api_response = api_instance.search_account_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_account_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_account_for_facets**
> ResponseContainerFacetsResponseContainer search_account_for_facets(body=body)

Lists the values of one or more facets over the customer's accounts



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's accounts
    api_response = api_instance.search_account_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_account_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_alert_deleted_entities**
> ResponseContainerPagedAlert search_alert_deleted_entities(body=body)

Search over a customer's deleted alerts



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's deleted alerts
    api_response = api_instance.search_alert_deleted_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_alert_deleted_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedAlert**](ResponseContainerPagedAlert.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_alert_deleted_for_facet**
> ResponseContainerFacetResponse search_alert_deleted_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's deleted alerts



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's deleted alerts
    api_response = api_instance.search_alert_deleted_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_alert_deleted_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_alert_deleted_for_facets**
> ResponseContainerFacetsResponseContainer search_alert_deleted_for_facets(body=body)

Lists the values of one or more facets over the customer's deleted alerts



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's deleted alerts
    api_response = api_instance.search_alert_deleted_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_alert_deleted_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_alert_entities**
> ResponseContainerPagedAlertWithStats search_alert_entities(body=body)

Search over a customer's non-deleted alerts



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's non-deleted alerts
    api_response = api_instance.search_alert_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_alert_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedAlertWithStats**](ResponseContainerPagedAlertWithStats.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_alert_for_facet**
> ResponseContainerFacetResponse search_alert_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's non-deleted alerts



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's non-deleted alerts
    api_response = api_instance.search_alert_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_alert_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_alert_for_facets**
> ResponseContainerFacetsResponseContainer search_alert_for_facets(body=body)

Lists the values of one or more facets over the customer's non-deleted alerts



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's non-deleted alerts
    api_response = api_instance.search_alert_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_alert_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_cloud_integration_deleted_entities**
> ResponseContainerPagedCloudIntegration search_cloud_integration_deleted_entities(body=body)

Search over a customer's deleted cloud integrations



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's deleted cloud integrations
    api_response = api_instance.search_cloud_integration_deleted_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_cloud_integration_deleted_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedCloudIntegration**](ResponseContainerPagedCloudIntegration.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_cloud_integration_deleted_for_facet**
> ResponseContainerFacetResponse search_cloud_integration_deleted_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's deleted cloud integrations



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's deleted cloud integrations
    api_response = api_instance.search_cloud_integration_deleted_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_cloud_integration_deleted_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_cloud_integration_deleted_for_facets**
> ResponseContainerFacetsResponseContainer search_cloud_integration_deleted_for_facets(body=body)

Lists the values of one or more facets over the customer's deleted cloud integrations



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's deleted cloud integrations
    api_response = api_instance.search_cloud_integration_deleted_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_cloud_integration_deleted_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_cloud_integration_entities**
> ResponseContainerPagedCloudIntegration search_cloud_integration_entities(body=body)

Search over a customer's non-deleted cloud integrations



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's non-deleted cloud integrations
    api_response = api_instance.search_cloud_integration_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_cloud_integration_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedCloudIntegration**](ResponseContainerPagedCloudIntegration.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_cloud_integration_for_facet**
> ResponseContainerFacetResponse search_cloud_integration_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's non-deleted cloud integrations



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's non-deleted cloud integrations
    api_response = api_instance.search_cloud_integration_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_cloud_integration_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_cloud_integration_for_facets**
> ResponseContainerFacetsResponseContainer search_cloud_integration_for_facets(body=body)

Lists the values of one or more facets over the customer's non-deleted cloud integrations



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's non-deleted cloud integrations
    api_response = api_instance.search_cloud_integration_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_cloud_integration_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_dashboard_deleted_entities**
> ResponseContainerPagedDashboard search_dashboard_deleted_entities(body=body)

Search over a customer's deleted dashboards



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's deleted dashboards
    api_response = api_instance.search_dashboard_deleted_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_dashboard_deleted_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedDashboard**](ResponseContainerPagedDashboard.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_dashboard_deleted_for_facet**
> ResponseContainerFacetResponse search_dashboard_deleted_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's deleted dashboards



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's deleted dashboards
    api_response = api_instance.search_dashboard_deleted_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_dashboard_deleted_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_dashboard_deleted_for_facets**
> ResponseContainerFacetsResponseContainer search_dashboard_deleted_for_facets(body=body)

Lists the values of one or more facets over the customer's deleted dashboards



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's deleted dashboards
    api_response = api_instance.search_dashboard_deleted_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_dashboard_deleted_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_dashboard_entities**
> ResponseContainerPagedDashboard search_dashboard_entities(body=body)

Search over a customer's non-deleted dashboards



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's non-deleted dashboards
    api_response = api_instance.search_dashboard_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_dashboard_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedDashboard**](ResponseContainerPagedDashboard.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_dashboard_for_facet**
> ResponseContainerFacetResponse search_dashboard_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's non-deleted dashboards



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's non-deleted dashboards
    api_response = api_instance.search_dashboard_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_dashboard_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_dashboard_for_facets**
> ResponseContainerFacetsResponseContainer search_dashboard_for_facets(body=body)

Lists the values of one or more facets over the customer's non-deleted dashboards



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's non-deleted dashboards
    api_response = api_instance.search_dashboard_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_dashboard_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_external_link_entities**
> ResponseContainerPagedExternalLink search_external_link_entities(body=body)

Search over a customer's external links



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's external links
    api_response = api_instance.search_external_link_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_external_link_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedExternalLink**](ResponseContainerPagedExternalLink.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_external_links_for_facet**
> ResponseContainerFacetResponse search_external_links_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's external links



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's external links
    api_response = api_instance.search_external_links_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_external_links_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_external_links_for_facets**
> ResponseContainerFacetsResponseContainer search_external_links_for_facets(body=body)

Lists the values of one or more facets over the customer's external links



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's external links
    api_response = api_instance.search_external_links_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_external_links_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_ingestion_policy_entities**
> ResponseContainerPagedIngestionPolicy search_ingestion_policy_entities(body=body)

Search over a customer's ingestion policies



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's ingestion policies
    api_response = api_instance.search_ingestion_policy_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_ingestion_policy_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedIngestionPolicy**](ResponseContainerPagedIngestionPolicy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_ingestion_policy_for_facet**
> ResponseContainerFacetResponse search_ingestion_policy_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's ingestion policies



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's ingestion policies
    api_response = api_instance.search_ingestion_policy_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_ingestion_policy_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_ingestion_policy_for_facets**
> ResponseContainerFacetsResponseContainer search_ingestion_policy_for_facets(body=body)

Lists the values of one or more facets over the customer's ingestion policies



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's ingestion policies
    api_response = api_instance.search_ingestion_policy_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_ingestion_policy_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_maintenance_window_entities**
> ResponseContainerPagedMaintenanceWindow search_maintenance_window_entities(body=body)

Search over a customer's maintenance windows



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's maintenance windows
    api_response = api_instance.search_maintenance_window_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_maintenance_window_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedMaintenanceWindow**](ResponseContainerPagedMaintenanceWindow.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_maintenance_window_for_facet**
> ResponseContainerFacetResponse search_maintenance_window_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's maintenance windows



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's maintenance windows
    api_response = api_instance.search_maintenance_window_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_maintenance_window_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_maintenance_window_for_facets**
> ResponseContainerFacetsResponseContainer search_maintenance_window_for_facets(body=body)

Lists the values of one or more facets over the customer's maintenance windows



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's maintenance windows
    api_response = api_instance.search_maintenance_window_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_maintenance_window_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_monitored_cluster_entities**
> ResponseContainerPagedMonitoredCluster search_monitored_cluster_entities(body=body)

Search over all the customer's non-deleted monitored clusters



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over all the customer's non-deleted monitored clusters
    api_response = api_instance.search_monitored_cluster_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_monitored_cluster_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedMonitoredCluster**](ResponseContainerPagedMonitoredCluster.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_monitored_cluster_for_facet**
> ResponseContainerFacetResponse search_monitored_cluster_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's non-deleted monitored cluster



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's non-deleted monitored cluster
    api_response = api_instance.search_monitored_cluster_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_monitored_cluster_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_monitored_cluster_for_facets**
> ResponseContainerFacetsResponseContainer search_monitored_cluster_for_facets(body=body)

Lists the values of one or more facets over the customer's non-deleted monitored clusters



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's non-deleted monitored clusters
    api_response = api_instance.search_monitored_cluster_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_monitored_cluster_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_notficant_for_facets**
> ResponseContainerFacetsResponseContainer search_notficant_for_facets(body=body)

Lists the values of one or more facets over the customer's notificants



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's notificants
    api_response = api_instance.search_notficant_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_notficant_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_notificant_entities**
> ResponseContainerPagedNotificant search_notificant_entities(body=body)

Search over a customer's notificants



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's notificants
    api_response = api_instance.search_notificant_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_notificant_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedNotificant**](ResponseContainerPagedNotificant.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_notificant_for_facet**
> ResponseContainerFacetResponse search_notificant_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's notificants



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's notificants
    api_response = api_instance.search_notificant_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_notificant_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_proxy_deleted_entities**
> ResponseContainerPagedProxy search_proxy_deleted_entities(body=body)

Search over a customer's deleted proxies



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's deleted proxies
    api_response = api_instance.search_proxy_deleted_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_proxy_deleted_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedProxy**](ResponseContainerPagedProxy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_proxy_deleted_for_facet**
> ResponseContainerFacetResponse search_proxy_deleted_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's deleted proxies



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's deleted proxies
    api_response = api_instance.search_proxy_deleted_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_proxy_deleted_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_proxy_deleted_for_facets**
> ResponseContainerFacetsResponseContainer search_proxy_deleted_for_facets(body=body)

Lists the values of one or more facets over the customer's deleted proxies



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's deleted proxies
    api_response = api_instance.search_proxy_deleted_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_proxy_deleted_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_proxy_entities**
> ResponseContainerPagedProxy search_proxy_entities(body=body)

Search over a customer's non-deleted proxies



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's non-deleted proxies
    api_response = api_instance.search_proxy_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_proxy_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedProxy**](ResponseContainerPagedProxy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_proxy_for_facet**
> ResponseContainerFacetResponse search_proxy_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's non-deleted proxies



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's non-deleted proxies
    api_response = api_instance.search_proxy_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_proxy_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_proxy_for_facets**
> ResponseContainerFacetsResponseContainer search_proxy_for_facets(body=body)

Lists the values of one or more facets over the customer's non-deleted proxies



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's non-deleted proxies
    api_response = api_instance.search_proxy_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_proxy_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_registered_query_deleted_entities**
> ResponseContainerPagedDerivedMetricDefinition search_registered_query_deleted_entities(body=body)

Search over a customer's deleted derived metric definitions



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's deleted derived metric definitions
    api_response = api_instance.search_registered_query_deleted_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_registered_query_deleted_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedDerivedMetricDefinition**](ResponseContainerPagedDerivedMetricDefinition.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_registered_query_deleted_for_facet**
> ResponseContainerFacetResponse search_registered_query_deleted_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's deleted derived metric definitions



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's deleted derived metric definitions
    api_response = api_instance.search_registered_query_deleted_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_registered_query_deleted_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_registered_query_deleted_for_facets**
> ResponseContainerFacetsResponseContainer search_registered_query_deleted_for_facets(body=body)

Lists the values of one or more facets over the customer's deleted derived metric definitions



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's deleted derived metric definitions
    api_response = api_instance.search_registered_query_deleted_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_registered_query_deleted_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_registered_query_entities**
> ResponseContainerPagedDerivedMetricDefinitionWithStats search_registered_query_entities(body=body)

Search over a customer's non-deleted derived metric definitions



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's non-deleted derived metric definitions
    api_response = api_instance.search_registered_query_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_registered_query_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedDerivedMetricDefinitionWithStats**](ResponseContainerPagedDerivedMetricDefinitionWithStats.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_registered_query_for_facet**
> ResponseContainerFacetResponse search_registered_query_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's non-deleted derived metric definitions



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's non-deleted derived metric definitions
    api_response = api_instance.search_registered_query_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_registered_query_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_registered_query_for_facets**
> ResponseContainerFacetsResponseContainer search_registered_query_for_facets(body=body)

Lists the values of one or more facets over the customer's non-deleted derived metric definition



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's non-deleted derived metric definition
    api_response = api_instance.search_registered_query_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_registered_query_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_related_report_event_entities**
> ResponseContainerPagedRelatedEvent search_related_report_event_entities(event_id, body=body)

List the related events over a firing event



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
event_id = 'event_id_example' # str | 
body = wavefront_api_client.EventSearchRequest() # EventSearchRequest |  (optional)

try:
    # List the related events over a firing event
    api_response = api_instance.search_related_report_event_entities(event_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_related_report_event_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 
 **body** | [**EventSearchRequest**](EventSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedRelatedEvent**](ResponseContainerPagedRelatedEvent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_report_event_entities**
> ResponseContainerPagedEvent search_report_event_entities(body=body)

Search over a customer's events



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.EventSearchRequest() # EventSearchRequest |  (optional)

try:
    # Search over a customer's events
    api_response = api_instance.search_report_event_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_report_event_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EventSearchRequest**](EventSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedEvent**](ResponseContainerPagedEvent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_report_event_for_facet**
> ResponseContainerFacetResponse search_report_event_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's events



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's events
    api_response = api_instance.search_report_event_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_report_event_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_report_event_for_facets**
> ResponseContainerFacetsResponseContainer search_report_event_for_facets(body=body)

Lists the values of one or more facets over the customer's events



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's events
    api_response = api_instance.search_report_event_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_report_event_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_role_entities**
> ResponseContainerPagedRoleDTO search_role_entities(body=body)

Search over a customer's roles



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's roles
    api_response = api_instance.search_role_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_role_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedRoleDTO**](ResponseContainerPagedRoleDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_role_for_facet**
> ResponseContainerFacetResponse search_role_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's roles



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's roles
    api_response = api_instance.search_role_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_role_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_role_for_facets**
> ResponseContainerFacetsResponseContainer search_role_for_facets(body=body)

Lists the values of one or more facets over the customer's roles



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's roles
    api_response = api_instance.search_role_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_role_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_service_account_entities**
> ResponseContainerPagedServiceAccount search_service_account_entities(body=body)

Search over a customer's service accounts



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's service accounts
    api_response = api_instance.search_service_account_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_service_account_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedServiceAccount**](ResponseContainerPagedServiceAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_service_account_for_facet**
> ResponseContainerFacetResponse search_service_account_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's service accounts



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's service accounts
    api_response = api_instance.search_service_account_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_service_account_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_service_account_for_facets**
> ResponseContainerFacetsResponseContainer search_service_account_for_facets(body=body)

Lists the values of one or more facets over the customer's service accounts



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's service accounts
    api_response = api_instance.search_service_account_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_service_account_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tagged_source_entities**
> ResponseContainerPagedSource search_tagged_source_entities(body=body)

Search over a customer's sources



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SourceSearchRequestContainer() # SourceSearchRequestContainer |  (optional)

try:
    # Search over a customer's sources
    api_response = api_instance.search_tagged_source_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_tagged_source_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SourceSearchRequestContainer**](SourceSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerPagedSource**](ResponseContainerPagedSource.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tagged_source_for_facet**
> ResponseContainerFacetResponse search_tagged_source_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's sources



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's sources
    api_response = api_instance.search_tagged_source_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_tagged_source_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tagged_source_for_facets**
> ResponseContainerFacetsResponseContainer search_tagged_source_for_facets(body=body)

Lists the values of one or more facets over the customer's sources



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's sources
    api_response = api_instance.search_tagged_source_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_tagged_source_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_user_entities**
> ResponseContainerPagedCustomerFacingUserObject search_user_entities(body=body)

Search over a customer's users



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's users
    api_response = api_instance.search_user_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_user_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedCustomerFacingUserObject**](ResponseContainerPagedCustomerFacingUserObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_user_for_facet**
> ResponseContainerFacetResponse search_user_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's users



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's users
    api_response = api_instance.search_user_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_user_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_user_for_facets**
> ResponseContainerFacetsResponseContainer search_user_for_facets(body=body)

Lists the values of one or more facets over the customer's users



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's users
    api_response = api_instance.search_user_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_user_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_user_group_entities**
> ResponseContainerPagedUserGroupModel search_user_group_entities(body=body)

Search over a customer's user groups



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's user groups
    api_response = api_instance.search_user_group_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_user_group_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedUserGroupModel**](ResponseContainerPagedUserGroupModel.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_user_group_for_facet**
> ResponseContainerFacetResponse search_user_group_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's user groups



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's user groups
    api_response = api_instance.search_user_group_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_user_group_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_user_group_for_facets**
> ResponseContainerFacetsResponseContainer search_user_group_for_facets(body=body)

Lists the values of one or more facets over the customer's user groups



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's user groups
    api_response = api_instance.search_user_group_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_user_group_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_web_hook_entities**
> ResponseContainerPagedNotificant search_web_hook_entities(body=body)

Search over a customer's webhooks



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.SortableSearchRequest() # SortableSearchRequest |  (optional)

try:
    # Search over a customer's webhooks
    api_response = api_instance.search_web_hook_entities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_web_hook_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SortableSearchRequest**](SortableSearchRequest.md)|  | [optional] 

### Return type

[**ResponseContainerPagedNotificant**](ResponseContainerPagedNotificant.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_web_hook_for_facet**
> ResponseContainerFacetResponse search_web_hook_for_facet(facet, body=body)

Lists the values of a specific facet over the customer's webhooks



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
facet = 'facet_example' # str | 
body = wavefront_api_client.FacetSearchRequestContainer() # FacetSearchRequestContainer |  (optional)

try:
    # Lists the values of a specific facet over the customer's webhooks
    api_response = api_instance.search_web_hook_for_facet(facet, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_web_hook_for_facet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facet** | **str**|  | 
 **body** | [**FacetSearchRequestContainer**](FacetSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetResponse**](ResponseContainerFacetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_webhook_for_facets**
> ResponseContainerFacetsResponseContainer search_webhook_for_facets(body=body)

Lists the values of one or more facets over the customer's webhooks



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
api_instance = wavefront_api_client.SearchApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.FacetsSearchRequestContainer() # FacetsSearchRequestContainer |  (optional)

try:
    # Lists the values of one or more facets over the customer's webhooks
    api_response = api_instance.search_webhook_for_facets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_webhook_for_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FacetsSearchRequestContainer**](FacetsSearchRequestContainer.md)|  | [optional] 

### Return type

[**ResponseContainerFacetsResponseContainer**](ResponseContainerFacetsResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

