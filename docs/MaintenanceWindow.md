# MaintenanceWindow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_epoch_millis** | **int** |  | [optional] 
**creator_id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**end_time_in_seconds** | **int** | The time in epoch seconds when this maintenance window will end | 
**event_name** | **str** | The name of an event associated with the creation/update of this maintenance window | [optional] 
**host_tag_group_host_names_group_anded** | **bool** | If true, a source/host must be in &#39;relevantHostNames&#39; and have tags matching the specification formed by &#39;relevantHostTags&#39; and &#39;relevantHostTagsAnded&#39; in order for this maintenance window to apply. If false, a source/host must either be in &#39;relevantHostNames&#39; or match &#39;relevantHostTags&#39; and &#39;relevantHostTagsAnded&#39;. Default: false | [optional] 
**id** | **str** |  | [optional] 
**point_tag_filter** | **str** | Query that filters on point tags of timeseries scanned by alert. | [optional] 
**reason** | **str** | The purpose of this maintenance window | 
**relevant_customer_tags** | **list[str]** | List of alert tags whose matching alerts will be put into maintenance because of this maintenance window | 
**relevant_customer_tags_anded** | **bool** | Whether to AND customer tags listed in relevantCustomerTags. If true, a customer must contain all tags in order for the maintenance window to apply.  If false, the tags are OR&#39;ed, and a customer must contain one of the tags. Default: false | [optional] 
**relevant_host_names** | **list[str]** | List of source/host names that will be put into maintenance because of this maintenance window | [optional] 
**relevant_host_tags** | **list[str]** | List of source/host tags whose matching sources/hosts will be put into maintenance because of this maintenance window | [optional] 
**relevant_host_tags_anded** | **bool** | Whether to AND source/host tags listed in relevantHostTags. If true, a source/host must contain all tags in order for the maintenance window to apply.  If false, the tags are OR&#39;ed, and a source/host must contain one of the tags. Default: false | [optional] 
**running_state** | **str** |  | [optional] 
**sort_attr** | **int** | Numeric value used in default sorting | [optional] 
**start_time_in_seconds** | **int** | The time in epoch seconds when this maintenance window will start | 
**targets** | **list[str]** | List of targets to notify, overriding the alert&#39;s targets. | [optional] 
**title** | **str** | Title of this maintenance window | 
**updated_epoch_millis** | **int** |  | [optional] 
**updater_id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


