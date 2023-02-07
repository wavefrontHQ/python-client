# IngestionPolicyWriteModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **list[str]** | The accounts associated with the ingestion policy | [optional] 
**alert** | [**IngestionPolicyAlert**](IngestionPolicyAlert.md) | The alert DTO object associated with the ingestion policy. | [optional] 
**alert_id** | **str** | The ingestion policy alert Id | [optional] 
**customer** | **str** | ID of the customer to which the ingestion policy belongs | [optional] 
**description** | **str** | The description of the ingestion policy | [optional] 
**groups** | **list[str]** | The groups associated with the ingestion policy | [optional] 
**id** | **str** | The unique ID for the ingestion policy | [optional] 
**is_limited** | **bool** | Whether the ingestion policy is limited | [optional] 
**last_updated_account_id** | **str** | The account that updated this ingestion policy last time | [optional] 
**last_updated_ms** | **int** | The last time when the ingestion policy is updated, in epoch milliseconds | [optional] 
**limit_pps** | **int** | The PPS limit of the ingestion policy | [optional] 
**name** | **str** | The name of the ingestion policy | [optional] 
**namespaces** | **list[str]** | The namespaces associated with the ingestion policy | [optional] 
**point_tags** | [**list[Annotation]**](Annotation.md) | The point tags associated with the ingestion policy | [optional] 
**scope** | **str** | The scope of the ingestion policy | [optional] 
**sources** | **list[str]** | The sources associated with the ingestion policy | [optional] 
**tags_anded** | **bool** | Whether tags should be AND-ed or OR-ed.If true, a metric must contain all tags in order for the ingestion policy to apply. If false, the tags are OR-ed, and a metric must contain one of the tags. Default: false | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


