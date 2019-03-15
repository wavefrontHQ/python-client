# ExternalLink

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Human-readable description for this external link | 
**name** | **str** | Name of the external link.  Will be displayed in context (right-click) menus on charts | 
**id** | **str** |  | [optional] 
**creator_id** | **str** |  | [optional] 
**updater_id** | **str** |  | [optional] 
**template** | **str** | The mustache template for this link.  This template must expand to a full URL, including scheme, origin, etc | 
**metric_filter_regex** | **str** | Controls whether a link displayed in the context menu of a highlighted series.  If present, the metric name of the highlighted series must match this regular expression in order for the link to be displayed | [optional] 
**source_filter_regex** | **str** | Controls whether a link displayed in the context menu of a highlighted series.  If present, the source name of the highlighted series must match this regular expression in order for the link to be displayed | [optional] 
**point_tag_filter_regexes** | **dict(str, str)** | Controls whether a link displayed in the context menu of a highlighted series.  This is a map from string to regular expression. The highlighted series must contain point tags whose keys are present in the keys of this map and whose values match the regular expressions associated with those keys in order for the link to be displayed | [optional] 
**created_epoch_millis** | **int** |  | [optional] 
**updated_epoch_millis** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


