# CustomerFacingUserObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of this user, which should be their valid email address | 
**customer** | **str** | The id of the customer to which the user belongs | 
**identifier** | **str** | The unique identifier of this user, which should be their valid email address | 
**groups** | **list[str]** | List of permission groups this user has been granted access to | [optional] 
**last_successful_login** | **int** | The last time the user logged in, in epoch milliseconds | [optional] 
**_self** | **bool** | Whether this user is the one calling the API | 
**escaped_identifier** | **str** | URL Escaped Identifier | [optional] 
**gravatar_url** | **str** | URL id For User&#39;s gravatar (see gravatar.com), if one exists. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


