# MaintenanceWindow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** | The creation time for this maintenance window in milliseconds. Used as the id | [optional] 
**creator_user_id** | **str** | Id of the user who created this maintenance window | [optional] 
**customer_id** | **str** |  | [optional] 
**end_time_in_seconds** | **int** | The time in seconds for when this maintenance window will end | [optional] 
**event_name** | **str** |  | [optional] 
**reason** | **str** | Description on the purpose of this maintenance window | [optional] 
**relevant_customer_tags** | **list[str]** | List of shared alert tags that will be put into maintenance because of this maintenance window | [optional] 
**relevant_host_names** | **list[str]** | List of the specific hosts that will be put into maintenance because of this maintenance window | [optional] 
**relevant_host_tags** | **list[str]** | List of host tags whose matching hosts will be put into maintenance because of this maintenance window | [optional] 
**start_time_in_seconds** | **int** | The time in seconds for when this maintenance window will start | [optional] 
**title** | **str** | Title text | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


