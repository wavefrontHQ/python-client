# QueryResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Error message, if query execution did not finish successfully | [optional] 
**error_type** | **str** | Error type, if query execution did not finish successfully | [optional] 
**events** | [**list[QueryEvent]**](QueryEvent.md) |  | [optional] 
**granularity** | **int** | The granularity of the returned results, in seconds | [optional] 
**name** | **str** | The name of this query | [optional] 
**query** | **str** | The query used to obtain this result | [optional] 
**spans** | [**list[Span]**](Span.md) |  | [optional] 
**stats** | [**StatsModelInternalUse**](StatsModelInternalUse.md) |  | [optional] 
**timeseries** | [**list[Timeseries]**](Timeseries.md) |  | [optional] 
**traces** | [**list[Trace]**](Trace.md) |  | [optional] 
**warnings** | **str** | The warnings incurred by this query | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


