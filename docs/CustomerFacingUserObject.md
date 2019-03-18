# CustomerFacingUserObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_groups** | **list[str]** | List of user group identifiers this user belongs to | [optional] 
**identifier** | **str** | The unique identifier of this user, which should be their valid email address | 
**_self** | **bool** | Whether this user is the one calling the API | 
**groups** | **list[str]** | List of permission groups this user has been granted access to | [optional] 
**customer** | **str** | The id of the customer to which the user belongs | 
**id** | **str** | The unique identifier of this user, which should be their valid email address | 
**last_successful_login** | **int** | The last time the user logged in, in epoch milliseconds | [optional] 
**gravatar_url** | **str** | URL id For User&#39;s gravatar (see gravatar.com), if one exists. | [optional] 
**escaped_identifier** | **str** | URL Escaped Identifier | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


