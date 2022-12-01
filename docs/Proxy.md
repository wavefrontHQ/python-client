# Proxy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_left_for_buffer** | **int** | Number of bytes of space remaining in the persistent disk queue of this proxy | [optional] 
**bytes_per_minute_for_buffer** | **int** | Bytes used per minute by the persistent disk queue of this proxy | [optional] 
**collector_rate_limit** | **int** | Proxy&#39;s rate limit | [optional] 
**collector_sets_rate_limit** | **bool** | When true, this proxy&#39;s rate limit is controlled remotely | [optional] 
**customer_id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**ephemeral** | **bool** | When true, this proxy is expected to be ephemeral (possibly hosted on a short-lived container) and will be deleted after a period of inactivity (not checking in) | [optional] 
**events_rate_limit** | **float** | Proxy&#39;s rate limit for events | [optional] 
**histo_disabled** | **bool** | Proxy&#39;s histogram feature disabled | [optional] 
**histogram_rate_limit** | **int** | Proxy&#39;s rate limit for histograms | [optional] 
**hostname** | **str** | Host name of the machine running the proxy | [optional] 
**id** | **str** |  | [optional] 
**in_trash** | **bool** |  | [optional] 
**ingestion_policies** | [**list[IngestionPolicy]**](IngestionPolicy.md) | Ingestion policies associated with the proxy through user and groups | [optional] 
**ingestion_policy** | [**IngestionPolicy**](IngestionPolicy.md) | Ingestion policy associated with the proxy | [optional] 
**last_check_in_time** | **int** | Last time when this proxy checked in (in milliseconds since the unix epoch) | [optional] 
**last_error_event** | [**Event**](Event.md) |  | [optional] 
**last_error_time** | **int** | deprecated | [optional] 
**last_known_error** | **str** | deprecated | [optional] 
**local_queue_size** | **int** | Number of items in the persistent disk queue of this proxy | [optional] 
**logs_disabled** | **bool** | Proxy&#39;s logs feature disabled for customer | [optional] 
**name** | **str** | Proxy name (modifiable) | 
**preprocessor_rules** | **str** | Proxy&#39;s preprocessor rules | [optional] 
**proxyname** | **str** | Proxy name set by customer | [optional] 
**shutdown** | **bool** | When true, attempt to shut down this proxy remotely | [optional] 
**source_tags_rate_limit** | **float** | Proxy&#39;s rate limit for source tag operations | [optional] 
**span_logs_disabled** | **bool** | Proxy&#39;s span logs feature disabled | [optional] 
**span_logs_rate_limit** | **int** | Proxy&#39;s rate limit for span logs | [optional] 
**span_rate_limit** | **int** | Proxy&#39;s rate limit for spans | [optional] 
**ssh_agent** | **bool** | deprecated | [optional] 
**status** | **str** | the proxy&#39;s status | [optional] 
**status_cause** | **str** | The reason why the proxy is in current status | [optional] 
**time_drift** | **int** | Time drift of the proxy&#39;s clock compared to Wavefront servers | [optional] 
**trace_disabled** | **bool** | Proxy&#39;s spans feature disabled | [optional] 
**truncate** | **bool** | When true, attempt to truncate down this proxy backlog remotely | [optional] 
**user_id** | **str** | The user associated with this proxy | [optional] 
**version** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


