# EventTimeRange

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earliest_start_time_epoch_millis** | **int** | Start of search time window, in milliseconds since the Unix Epoch.  Events whose start time occurs after this value will be returned.  If no value is supplied, defaults to 2 hours prior the present time. | [optional] 
**latest_start_time_epoch_millis** | **int** | End of the search time window, in milliseconds since the Unix Epoch.  Events whose start time occurs before this value will be returned.   If no value is supplied, defaults to now. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


