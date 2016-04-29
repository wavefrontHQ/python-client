# QueryResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**list[ReportEvent]**](ReportEvent.md) | The events occurring during this time span | [optional] 
**granularity** | **int** |  | [optional] 
**host_tags_used** | **list[str]** |  | [optional] 
**hosts_used** | **list[str]** |  | [optional] 
**metrics_used** | **list[str]** |  | [optional] 
**name** | **str** | The name of this query | [optional] 
**num_compilation_tasks** | **int** |  | [optional] 
**query** | **str** | The query string used to obtain this result | [optional] 
**query_keys** | [**list[QueryKeyContainer]**](QueryKeyContainer.md) |  | [optional] 
**skip** | **int** | Unused/deprecated | [optional] 
**stats** | [**StatsModel**](StatsModel.md) | Statistics about the result data | [optional] 
**timeseries** | [**list[Timeseries]**](Timeseries.md) | The time series data for this query | [optional] 
**warnings** | **str** | The warnings incurred by this query | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


