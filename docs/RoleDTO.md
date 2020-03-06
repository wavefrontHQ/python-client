# RoleDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_epoch_millis** | **int** |  | [optional] 
**customer** | **str** | The id of the customer to which the role belongs | [optional] 
**description** | **str** | The description of the role | [optional] 
**id** | **str** | The unique identifier of the role | [optional] 
**last_updated_account_id** | **str** | The account that updated this role last time | [optional] 
**last_updated_ms** | **int** | The last time when the role is updated, in epoch milliseconds | [optional] 
**linked_accounts_count** | **int** | Total number of accounts that are linked to the role | [optional] 
**linked_groups_count** | **int** | Total number of groups that are linked to the role | [optional] 
**name** | **str** | The name of the role | [optional] 
**permissions** | **list[str]** | List of permissions the role has been granted access to | [optional] 
**sample_linked_accounts** | **list[str]** | A sample of the accounts assigned to this role. Please use the Role facet of the Account Search API to get the full list of accounts for this role | [optional] 
**sample_linked_groups** | [**list[UserGroup]**](UserGroup.md) | A sample of the groups assigned to this role. Please use the Role facet of the Group Search API to get the full list of groups for this role | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


