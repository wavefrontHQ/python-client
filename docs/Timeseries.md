# Timeseries

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label of this timeseries | [optional] 
**host** | **str** | Source/Host of this timeseries | [optional] 
**tags** | **dict(str, str)** | Tags (key-value annotations) of this timeseries | [optional] 
**data** | **list[list[float]]** | Data returned by this time series.  This is returned as a list of points, where each point is represented as a two-element list with 1st element being the timestamp in epoch SECONDS and the 2nd element being the numeric value of the series at the timestamp | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


