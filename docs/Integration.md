# Integration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Integration description | 
**version** | **str** | Integration version string | 
**icon** | **str** | URI path to the integration icon | 
**metrics** | [**IntegrationMetrics**](IntegrationMetrics.md) |  | [optional] 
**base_url** | **str** | Base URL for this integration&#39;s assets | [optional] 
**status** | [**IntegrationStatus**](IntegrationStatus.md) |  | [optional] 
**alerts** | [**list[IntegrationAlert]**](IntegrationAlert.md) | A list of alerts belonging to this integration | [optional] 
**creator_id** | **str** |  | [optional] 
**updater_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**created_epoch_millis** | **int** |  | [optional] 
**updated_epoch_millis** | **int** |  | [optional] 
**alias_of** | **str** | If set, designates this integration as an alias integration, of the integration whose id is specified. | [optional] 
**alias_integrations** | [**list[IntegrationAlias]**](IntegrationAlias.md) | If set, a list of objects describing integrations that alias this one. | [optional] 
**dashboards** | [**list[IntegrationDashboard]**](IntegrationDashboard.md) | A list of dashboards belonging to this integration | [optional] 
**deleted** | **bool** |  | [optional] 
**overview** | **str** | Descriptive text giving an overview of integration functionality | [optional] 
**setup** | **str** | How the integration will be set-up | [optional] 
**name** | **str** | Integration name | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


