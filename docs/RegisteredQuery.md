# RegisteredQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | **str** |  | [optional] 
**query** | **str** | A Wavefront query that is evaluated at regular intervals (default 1m). | 
**tags** | [**WFTags**](WFTags.md) |  | [optional] 
**status** | **list[str]** | Lists the current state of the registered query. Can be one or more of: INVALID, ACTIVE, TRASH, NO_DATA | [optional] 
**process_rate_minutes** | **int** | The interval between executing the query, in minutes.  Defaults to 1 minute | [optional] 
**last_processed_millis** | **int** | The time when the registered query was rawn, in epoch millis | [optional] 
**update_user_id** | **str** | The user that last updated this registered query | [optional] 
**last_query_time** | **int** | Time for the query execute, averaged on hourly basis | [optional] 
**in_trash** | **bool** |  | [optional] 
**query_failing** | **bool** | Whether there was an exception when the query last ran | [optional] 
**updated** | **int** | When the registered query was last updated, in epoch millis | [optional] 
**create_user_id** | **str** |  | [optional] 
**metrics_used** | **list[str]** | Number of metrics checked by the query | [optional] 
**created** | **int** | When this registered query was created, in epoch millis | [optional] 
**creator_id** | **str** |  | [optional] 
**updater_id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**additional_information** | **str** | User-supplied additional explanatory information for the registered query. | [optional] 
**last_failed_time** | **int** | The time of the last error encountered when running the query, in epoch millis | [optional] 
**last_error_message** | **str** | The last error encountered when running the query | [optional] 
**hosts_used** | **list[str]** | Number of hosts checked by the query | [optional] 
**points_scanned_at_last_query** | **int** | A derived field recording the number of data points scanned when the system last computed the query | [optional] 
**include_obsolete_metrics** | **bool** | Whether to include obsolete metrics in query | [optional] 
**query_qb_enabled** | **bool** | Whether the  query was created using the Query Builder. Default false | [optional] 
**query_qb_serialization** | **str** | The special serialization of the Query Builder that corresponds to the query.  Applicable only when queryQBEnabled is true | [optional] 
**created_epoch_millis** | **int** |  | [optional] 
**updated_epoch_millis** | **int** |  | [optional] 
**minutes** | **int** | How frequency the registered query is ran | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


