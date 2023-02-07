# UserToCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** | The (unique) identifier of the user to create. Must be a valid email address | 
**groups** | **list[str]** | List of permission groups to grant to this user. Please note that &#39;host_tag_management&#39; is the equivalent of the &#39;Source Tag Management&#39; permission.  Possible values are log_management, dashboard_management, events_management, alerts_management, derived_metrics_management, host_tag_management, agent_management, token_management, ingestion, user_management, embedded_charts, metrics_management, external_links_management, application_management, batch_query_priority, saml_sso_management, monitored_application_service_management | 
**roles** | **list[str]** | The list of role ids, the user will be added to. | [optional] 
**user_groups** | **list[str]** | List of user groups to this user.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


