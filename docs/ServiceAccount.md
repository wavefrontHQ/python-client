# ServiceAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | The state of the service account. | 
**description** | **str** | The description of the service account. | [optional] 
**groups** | **list[str]** | The list of service account&#39;s permissions. | [optional] 
**identifier** | **str** | The unique identifier of a service account. | 
**last_used** | **int** | The last time when a token of the service account was used. | [optional] 
**tokens** | [**list[UserApiToken]**](UserApiToken.md) | The service account&#39;s API tokens. | [optional] 
**user_groups** | [**list[UserGroup]**](UserGroup.md) | The list of service account&#39;s user groups. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


