# Chart

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **int** | If the chart has a log-scale Y-axis, the base for the logarithms | [optional] 
**description** | **str** | Description of the chart | [optional] 
**units** | **str** | String to label the units of the chart on the Y-axis | [optional] 
**interpolate_points** | **bool** | Whether to interpolate points in the charts produced. Default: true | [optional] 
**sources** | [**list[ChartSourceQuery]**](ChartSourceQuery.md) | Query expression to plot on the chart | 
**include_obsolete_metrics** | **bool** | Whether to show obsolete metrics.  Default: false | [optional] 
**no_default_events** | **bool** | Whether to hide events related to the sources in the charts produced. Default false (i.e. shows events) | [optional] 
**chart_attributes** | [**JsonNode**](JsonNode.md) | Experimental field for chart attributes | [optional] 
**summarization** | **str** | Summarization strategy for the chart.  MEAN is default | [optional] 
**chart_settings** | [**ChartSettings**](ChartSettings.md) |  | [optional] 
**name** | **str** | Name of the source | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


