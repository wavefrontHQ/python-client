# wavefront_api_client.DirectIngestionApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**report**](DirectIngestionApi.md#report) | **POST** /report | Directly ingest data/data stream with specified format


# **report**
> report(f=f, body=body)

Directly ingest data/data stream with specified format



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
api_instance = wavefront_api_client.DirectIngestionApi(wavefront_api_client.ApiClient(configuration))
f = 'wavefront' # str | Format of data to be ingested (optional) (default to wavefront)
body = 'body_example' # str | Data to be ingested, in the specified format.  See https://docs.wavefront.com/direct_ingestion.html for more detail on how to format the data. Example in \"wavefront\" format:  <pre>test.metric 100 source=test.source</pre> which ingests a time series point with metric name \"test.metric\", source name \"test.source\", and value of 100 with timestamp of now. (optional)

try:
    # Directly ingest data/data stream with specified format
    api_instance.report(f=f, body=body)
except ApiException as e:
    print("Exception when calling DirectIngestionApi->report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f** | **str**| Format of data to be ingested | [optional] [default to wavefront]
 **body** | **str**| Data to be ingested, in the specified format.  See https://docs.wavefront.com/direct_ingestion.html for more detail on how to format the data. Example in \&quot;wavefront\&quot; format:  &lt;pre&gt;test.metric 100 source&#x3D;test.source&lt;/pre&gt; which ingests a time series point with metric name \&quot;test.metric\&quot;, source name \&quot;test.source\&quot;, and value of 100 with timestamp of now. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/octet-stream, application/x-www-form-urlencoded, text/plain
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

