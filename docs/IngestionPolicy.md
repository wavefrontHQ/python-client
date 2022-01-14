# IngestionPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_count** | **int** | Total number of accounts that are linked to the ingestion policy | [optional] 
**customer** | **str** | ID of the customer to which the ingestion policy belongs | [optional] 
**description** | **str** | The description of the ingestion policy | [optional] 
**group_count** | **int** | Total number of groups that are linked to the ingestion policy | [optional] 
**id** | **str** | The unique ID for the ingestion policy | [optional] 
**is_limited** | **bool** | Whether the ingestion policy is limited | [optional] 
**last_updated_account_id** | **str** | The account that updated this ingestion policy last time | [optional] 
**last_updated_ms** | **int** | The last time when the ingestion policy is updated, in epoch milliseconds | [optional] 
**limit_pps** | **int** | The PPS limit of the ingestion policy | [optional] 
**name** | **str** | The name of the ingestion policy | [optional] 
**sampled_accounts** | **list[str]** | A sample of the accounts assigned to this ingestion policy. Please use the Ingestion Policy facet of the Account Search API to get the full list of accounts for this policy | [optional] 
**sampled_groups** | [**list[UserGroup]**](UserGroup.md) | A sample of the groups assigned to this ingestion policy. Please use the Ingestion Policy facet of the Group Search API to get the full list of groups for this policy | [optional] 
**sampled_service_accounts** | **list[str]** | A sample of the service accounts accounts assigned to this ingestion policy. Please use the Ingestion Policy facet of the Account Search API to get the full list of service accounts for this policy | [optional] 
**sampled_user_accounts** | **list[str]** | A sample of the user accounts assigned to this ingestion policy. Please use the Ingestion Policy facet of the Account Search API to get the full list of users for this policy | [optional] 
**scope** | **str** | The scope of the ingestion policy | [optional] 
**service_account_count** | **int** | Total number of service accounts that are linked to the ingestion policy | [optional] 
**user_account_count** | **int** | Total number of user accounts that are linked to the ingestion policy | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


