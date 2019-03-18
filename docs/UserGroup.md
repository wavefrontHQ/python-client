# UserGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_epoch_millis** | **int** |  | [optional] 
**customer** | **str** | The id of the customer to which the user group belongs | [optional] 
**id** | **str** | The unique identifier of the user group | [optional] 
**name** | **str** | The name of the user group | 
**permissions** | **list[str]** | List of permissions the user group has been granted access to | 
**properties** | [**UserGroupPropertiesDTO**](UserGroupPropertiesDTO.md) | The properties of the user group(name editable, users editable, etc.) | [optional] 
**user_count** | **int** | Total number of users that are members of the user group | [optional] 
**users** | **list[str]** | List(may be incomplete) of users that are members of the user group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


