# MaintenanceWindow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The purpose of this maintenance window | 
**id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**title** | **str** | Title of this maintenance window | 
**start_time_in_seconds** | **int** | The time in epoch seconds when this maintenance window will start | 
**end_time_in_seconds** | **int** | The time in epoch seconds when this maintenance window will end | 
**relevant_customer_tags** | **list[str]** | List of alert tags whose matching alerts will be put into maintenance because of this maintenance window | 
**relevant_host_tags** | **list[str]** | List of source/host tags whose matching sources/hosts will be put into maintenance because of this maintenance window | [optional] 
**relevant_host_names** | **list[str]** | List of source/host names that will be put into maintenance because of this maintenance window | [optional] 
**creator_id** | **str** |  | [optional] 
**updater_id** | **str** |  | [optional] 
**created_epoch_millis** | **int** |  | [optional] 
**updated_epoch_millis** | **int** |  | [optional] 
**relevant_host_tags_anded** | **bool** | Whether to AND source/host tags listed in relevantHostTags. If true, a source/host must contain all tags in order for the maintenance window to apply.  If false, the tags are OR&#39;ed, and a source/host must contain one of the tags. Default: false | [optional] 
**host_tag_group_host_names_group_anded** | **bool** | If true, a source/host must be in &#39;relevantHostNames&#39; and have tags matching the specification formed by &#39;relevantHostTags&#39; and &#39;relevantHostTagsAnded&#39; in order for this maintenance window to apply. If false, a source/host must either be in &#39;relevantHostNames&#39; or match &#39;relevantHostTags&#39; and &#39;relevantHostTagsAnded&#39;. Default: false | [optional] 
**event_name** | **str** | The name of an event associated with the creation/update of this maintenance window | [optional] 
**running_state** | **str** |  | [optional] 
**sort_attr** | **int** | Numeric value used in default sorting | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


