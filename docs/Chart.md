# Chart

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the source | 
**description** | **str** | Description of the chart | [optional] 
**base** | **int** | If the chart has a log-scale Y-axis, the base for the logarithms | [optional] 
**sources** | [**list[ChartSourceQuery]**](ChartSourceQuery.md) | Query expression to plot on the chart | 
**units** | **str** | String to label the units of the chart on the Y-axis | [optional] 
**include_obsolete_metrics** | **bool** | Whether to show obsolete metrics.  Default: false | [optional] 
**chart_settings** | [**ChartSettings**](ChartSettings.md) |  | [optional] 
**no_default_events** | **bool** | Whether to hide events related to the sources in the charts produced. Default false (i.e. shows events) | [optional] 
**interpolate_points** | **bool** | Whether to interpolate points in the charts produced. Default: true | [optional] 
**summarization** | **str** | Summarization strategy for the chart.  MEAN is default | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


