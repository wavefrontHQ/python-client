# Source

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hidden** | **bool** | A derived field denoting whether this source has been hidden (e.g. excluding it from query autocomplete among other things) | [optional] 
**id** | **str** | id of this source, must be exactly equivalent to &#39;sourceName&#39; | 
**description** | **str** | Description of this source | [optional] 
**tags** | **dict(str, bool)** | A Map (String -&gt; boolean) Representing the source tags associated with this source.  To create a tag, set it as a KEY in this map, with associated value equal to true | [optional] 
**creator_id** | **str** |  | [optional] 
**updater_id** | **str** |  | [optional] 
**created_epoch_millis** | **int** |  | [optional] 
**updated_epoch_millis** | **int** |  | [optional] 
**marked_new_epoch_millis** | **int** | Epoch Millis when this source was marked as ~status.new | [optional] 
**source_name** | **str** | The name of the source, usually set by ingested telemetry | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


