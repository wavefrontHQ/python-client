# wavefront_api_client.WavefrontApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster_info**](WavefrontApi.md#get_cluster_info) | **GET** /api/v2/cluster/info | API endpoint to get cluster info


# **get_cluster_info**
> ResponseContainerClusterInfoDTO get_cluster_info()

API endpoint to get cluster info



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
api_instance = wavefront_api_client.WavefrontApi(wavefront_api_client.ApiClient(configuration))

try:
    # API endpoint to get cluster info
    api_response = api_instance.get_cluster_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WavefrontApi->get_cluster_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseContainerClusterInfoDTO**](ResponseContainerClusterInfoDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

