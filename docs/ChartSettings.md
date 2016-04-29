# ChartSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_data_spacing** | **int** | Threshold (in seconds) for time delta between consecutive points in a series above which a dotted line will replace a solid line in line plots.  60s is default. | [optional] 
**line_type** | **str** | Plot interpolation type.  linear is default | [optional] 
**max** | **float** | Max value of Y-axis.  Set to null for auto | [optional] 
**min** | **float** | Min value of Y-axis.  Set to null for auto | [optional] 
**show_hosts** | **bool** | For table \&quot;plots\&quot;, whether to display sources.  Default true | [optional] [default to False]
**show_labels** | **bool** | For table \&quot;plots\&quot;, whether to display labels.  Default true | [optional] [default to False]
**show_raw_values** | **bool** | For table \&quot;plots\&quot;, whether to display raw values.  Default false | [optional] [default to False]
**stack_type** | **str** | Type of stacked chart (applicable only if chart type is stacked).  zero (default) means stacked from y&#x3D;0.  expand means Normalized from 0 to 1.  wiggle means Minimize weighted changes. silhouette means to Center the Stream | [optional] 
**time_based_coloring** | **bool** | Fox x-y scatterplots, whether to color more recent points as darker than older points. Default false | [optional] [default to False]
**type** | **str** | Chart type.  &#39;line&#39; is default | [optional] 
**window_size** | **int** | Width, in minutes, of the time window to use for \&quot;last\&quot; windowing | [optional] 
**windowing** | **str** | For table \&quot;plots\&quot;, whether to use the full time window for the query or the last x minutes | [optional] 
**xmax** | **float** | For x-y scatterplots, max value for x-axis.  Set null for auto | [optional] 
**xmin** | **float** | For x-y scatterplots, min value for x-axis.  Set null for auto | [optional] 
**ymax** | **float** | For x-y scatterplots, max value for y-axis.  Set null for auto | [optional] 
**ymin** | **float** | For x-y scatterplots, min value for y-axis.  Set null for auto | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


