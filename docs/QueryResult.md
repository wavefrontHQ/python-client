# QueryResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this query | [optional] 
**query** | **str** | The query used to obtain this result | [optional] 
**stats** | [**StatsModel**](StatsModel.md) |  | [optional] 
**warnings** | **str** | The warnings incurred by this query | [optional] 
**granularity** | **int** | The granularity of the returned results, in seconds | [optional] 
**events** | [**list[QueryEvent]**](QueryEvent.md) |  | [optional] 
**timeseries** | [**list[Timeseries]**](Timeseries.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


