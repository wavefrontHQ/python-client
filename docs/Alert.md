# Alert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_maintenance_windows** | **list[str]** |  | [optional] 
**additional_information** | **str** | Additional information of the alert for runbooks, etc. | [optional] 
**condition** | **str** | The condition in which to evaluate whether the alert is firing | [optional] 
**condition_qb_enabled** | **bool** |  | [optional] [default to False]
**condition_qb_serialization** | **str** |  | [optional] 
**created** | **int** | The creation time in milliseconds for the alert | [optional] 
**display_expression** | **str** |  | [optional] 
**display_expression_qb_enabled** | **bool** |  | [optional] [default to False]
**display_expression_qb_serialization** | **str** |  | [optional] 
**event** | [**ReportEvent**](ReportEvent.md) | The event associated with the firing of the alert. Can be null if the alert has never fired. If the alert is not currently firing, the event holds the last known firing of the alert | [optional] 
**failing_host_label_pairs_override** | [**list[HostLabelPair]**](HostLabelPair.md) | Failing host/metric pairs X | [optional] 
**hosts_used** | **list[str]** |  | [optional] 
**in_maintenance_host_label_pairs** | [**list[HostLabelPair]**](HostLabelPair.md) |  | [optional] 
**in_trash** | **bool** |  | [optional] [default to False]
**last_error_message** | **str** |  | [optional] 
**last_failed_time** | **int** |  | [optional] 
**last_updated** | **int** |  | [optional] 
**metrics_used** | **list[str]** |  | [optional] 
**minutes** | **int** | The time to elapse before firing or resolving the alert when the condition evaluates to true or false (respectively) | [optional] 
**name** | **str** | The name of the alert | [optional] 
**notificants** | **list[str]** |  | [optional] 
**prefiring_host_label_pairs** | [**list[HostLabelPair]**](HostLabelPair.md) |  | [optional] 
**query_failing** | **bool** |  | [optional] [default to False]
**resolve_after_minutes** | **int** |  | [optional] 
**severity** | **str** | The severity of the alert | [optional] 
**snoozed** | **int** | Milliseconds since the epoch the alert is snoozed until. A value in the past indicates that the alert is not snoozed | [optional] 
**tags** | [**Tags**](Tags.md) | Associated tags | [optional] 
**target** | **str** | The email address or integration endpoint (such as PagerDuty) to notify when the alert state changes | [optional] 
**update_user_id** | **str** |  | [optional] 
**updated** | **int** | The last known update time of the alert by a user | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


