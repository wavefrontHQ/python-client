# UserModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | **str** | The id of the customer to which this user belongs | 
**groups** | **list[str]** | The permissions granted to this user | 
**identifier** | **str** | The unique identifier of this user, which must be their valid email address | 
**ingestion_policy** | [**IngestionPolicy**](IngestionPolicy.md) |  | [optional] 
**last_successful_login** | **int** |  | [optional] 
**roles** | [**list[RoleDTO]**](RoleDTO.md) |  | [optional] 
**sso_id** | **str** |  | [optional] 
**user_groups** | [**list[UserGroup]**](UserGroup.md) | The list of user groups the user belongs to | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


