# DerivedMetricDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | **str** |  | [optional] 
**query** | **str** | A Wavefront query that is evaluated at regular intervals (default 1m). | 
**tags** | [**WFTags**](WFTags.md) |  | [optional] 
**status** | **list[str]** | Lists the current state of the derived metric. Can be one or more of: INVALID, ACTIVE, TRASH, NO_DATA | [optional] 
**include_obsolete_metrics** | **bool** | Whether to include obsolete metrics in query | [optional] 
**creator_id** | **str** |  | [optional] 
**additional_information** | **str** | User-supplied additional explanatory information for the derived metric | [optional] 
**minutes** | **int** | How frequently the query generating the derived metric is run | 
**query_failing** | **bool** | Whether there was an exception when the query last ran | [optional] 
**last_failed_time** | **int** | The time of the last error encountered when running the query, in epoch millis | [optional] 
**last_error_message** | **str** | The last error encountered when running the query | [optional] 
**metrics_used** | **list[str]** | Number of metrics checked by the query | [optional] 
**hosts_used** | **list[str]** | Number of hosts checked by the query | [optional] 
**last_processed_millis** | **int** | The last time when the derived metric query was run, in epoch millis | [optional] 
**process_rate_minutes** | **int** | The interval between executing the query, in minutes.  Defaults to 1 minute | [optional] 
**points_scanned_at_last_query** | **int** | A derived field recording the number of data points scanned when the system last computed the query | [optional] 
**query_qb_enabled** | **bool** | Whether the query was created using the Query Builder. Default false | [optional] 
**query_qb_serialization** | **str** | The special serialization of the Query Builder that corresponds to the query.  Applicable only when queryQBEnabled is true | [optional] 
**created_epoch_millis** | **int** |  | [optional] 
**updated_epoch_millis** | **int** |  | [optional] 
**updater_id** | **str** |  | [optional] 
**created** | **int** | When this derived metric was created, in epoch millis | [optional] 
**updated** | **int** | When the derived metric definition was last updated, in epoch millis | [optional] 
**update_user_id** | **str** | The user that last updated this derived metric definition | [optional] 
**last_query_time** | **int** | Time for the query execute, averaged on hourly basis | [optional] 
**in_trash** | **bool** |  | [optional] 
**create_user_id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


