# Chart

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **int** | If the chart has a log-scale y-axis, the base for the logarithms | [optional] 
**chart_settings** | [**ChartSettings**](ChartSettings.md) | Chart settings | [optional] 
**description** | **str** | Description of the chart | [optional] 
**include_obsolete_metrics** | **bool** | Whether to show obsolete metrics.  Default false. | [optional] [default to False]
**interpolate_points** | **bool** | Whether to interpolate points on the chart. Default true. | [optional] [default to False]
**name** | **str** | Name of the chart | 
**no_default_events** | **bool** | Don&#39;t show events related to the sources in queries on the chart. Default false (i.e. shows events) | [optional] [default to False]
**sources** | [**list[ChartSource]**](ChartSource.md) | Sources for the chart | 
**summarization** | **str** | Summarization strategy for the chart.  MEAN is default | [optional] 
**units** | **str** | String to label the units of the chart on the y-axis | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


