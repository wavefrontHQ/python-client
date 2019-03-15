# UserModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | The unique identifier of this user, which must be their valid email address | 
**customer** | **str** | The id of the customer to which this user belongs | 
**sso_id** | **str** |  | [optional] 
**last_successful_login** | **int** |  | [optional] 
**groups** | **list[str]** | The permissions granted to this user | 
**user_groups** | [**list[UserGroup]**](UserGroup.md) | The list of user groups the user belongs to | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


