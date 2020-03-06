# UserGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | **str** | ID of the customer to which the user group belongs | [optional] 
**description** | **str** | The description of the user group | [optional] 
**id** | **str** | Unique ID for the user group | [optional] 
**name** | **str** | Name of the user group | [optional] 
**permissions** | **list[str]** | Permission assigned to the user group | [optional] 
**properties** | [**UserGroupPropertiesDTO**](UserGroupPropertiesDTO.md) | The properties of the user group(name editable, users editable, etc.) | [optional] 
**roles** | [**list[RoleDTO]**](RoleDTO.md) | List of roles the user group has been linked to | [optional] 
**user_count** | **int** | Total number of users that are members of the user group | [optional] 
**users** | **list[str]** | List of Users that are members of the user group. Maybe incomplete. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


