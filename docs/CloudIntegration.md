# CloudIntegration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_save** | **bool** |  | [optional] 
**name** | **str** | The human-readable name of this integration | 
**id** | **str** |  | [optional] 
**service** | **str** | A value denoting which cloud service this integration integrates with | 
**in_trash** | **bool** |  | [optional] 
**last_error_event** | [**Event**](Event.md) |  | [optional] 
**creator_id** | **str** |  | [optional] 
**updater_id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**ec2** | [**EC2Configuration**](EC2Configuration.md) |  | [optional] 
**additional_tags** | **dict(str, str)** | A list of point tag key-values to add to every point ingested using this integration | [optional] 
**last_received_data_point_ms** | **int** | Time that this integration last received a data point, in epoch millis | [optional] 
**last_metric_count** | **int** | Number of metrics / events ingested by this integration the last time it ran | [optional] 
**cloud_watch** | [**CloudWatchConfiguration**](CloudWatchConfiguration.md) |  | [optional] 
**cloud_trail** | [**CloudTrailConfiguration**](CloudTrailConfiguration.md) |  | [optional] 
**gcp** | [**GCPConfiguration**](GCPConfiguration.md) |  | [optional] 
**tesla** | [**TeslaConfiguration**](TeslaConfiguration.md) |  | [optional] 
**azure** | [**AzureConfiguration**](AzureConfiguration.md) |  | [optional] 
**azure_activity_log** | [**AzureActivityLogConfiguration**](AzureActivityLogConfiguration.md) |  | [optional] 
**last_error** | **str** | Digest of the last error encountered by Wavefront servers when fetching data using this integration | [optional] 
**last_error_ms** | **int** | Time, in epoch millis, of the last error encountered by Wavefront servers when fetching data using this integration | [optional] 
**disabled** | **bool** | True when an aws credential failed to authenticate. | [optional] 
**last_processor_id** | **str** | Opaque id of the last Wavefront integrations service to act on this integration | [optional] 
**last_processing_timestamp** | **int** | Time, in epoch millis, that this integration was last processed | [optional] 
**created_epoch_millis** | **int** |  | [optional] 
**updated_epoch_millis** | **int** |  | [optional] 
**service_refresh_rate_in_mins** | **int** | Service refresh rate in minutes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


