# Proxy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**name** | **str** | Proxy name (modifiable) | 
**id** | **str** |  | [optional] 
**status** | **str** | the proxy&#39;s status | [optional] 
**customer_id** | **str** |  | [optional] 
**in_trash** | **bool** |  | [optional] 
**hostname** | **str** | Host name of the machine running the proxy | [optional] 
**last_check_in_time** | **int** | Last time when this proxy checked in (in milliseconds since the unix epoch) | [optional] 
**last_known_error** | **str** | deprecated | [optional] 
**last_error_time** | **int** | deprecated | [optional] 
**last_error_event** | [**Event**](Event.md) |  | [optional] 
**time_drift** | **int** | Time drift of the proxy&#39;s clock compared to Wavefront servers | [optional] 
**bytes_left_for_buffer** | **int** | Number of bytes of space remaining in the persistent disk queue of this proxy | [optional] 
**bytes_per_minute_for_buffer** | **int** | Bytes used per minute by the persistent disk queue of this proxy | [optional] 
**local_queue_size** | **int** | Number of items in the persistent disk queue of this proxy | [optional] 
**ssh_agent** | **bool** | deprecated | [optional] 
**ephemeral** | **bool** | When true, this proxy is expected to be ephemeral (possibly hosted on a short-lived container) and will be deleted after a period of inactivity (not checking in) | [optional] 
**deleted** | **bool** |  | [optional] 
**status_cause** | **str** | The reason why the proxy is in current status | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


