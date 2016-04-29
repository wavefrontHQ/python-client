# ReportEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | Annotations for the event. Searchable during queries | [optional] 
**end_time** | **int** | End time in milliseconds for the event. If missing, the event is ongoing | [optional] 
**hosts** | **list[str]** | Hosts associated for the event | [optional] 
**is_ephemeral** | **bool** |  | [optional] [default to False]
**is_user_event** | **bool** |  | [optional] [default to False]
**name** | **str** | Name of the event | 
**start_time** | **int** | Start time in milliseconds for the event | 
**summarized_events** | **int** |  | [optional] 
**table** | **str** | The customer that owns the event | [optional] 
**tags** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


