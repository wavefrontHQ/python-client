# Integration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**list[IntegrationAlert]**](IntegrationAlert.md) | A list of alerts belonging to this integration | [optional] 
**alias_integrations** | [**list[IntegrationAlias]**](IntegrationAlias.md) | If set, a list of objects describing integrations that alias this one. | [optional] 
**alias_of** | **str** | If set, designates this integration as an alias integration, of the integration whose id is specified. | [optional] 
**base_url** | **str** | Base URL for this integration&#39;s assets | [optional] 
**created_epoch_millis** | **int** |  | [optional] 
**creator_id** | **str** |  | [optional] 
**dashboards** | [**list[IntegrationDashboard]**](IntegrationDashboard.md) | A list of dashboards belonging to this integration | [optional] 
**deleted** | **bool** |  | [optional] 
**description** | **str** | Integration description | 
**icon** | **str** | URI path to the integration icon | 
**id** | **str** |  | [optional] 
**metrics** | [**IntegrationMetrics**](IntegrationMetrics.md) |  | [optional] 
**name** | **str** | Integration name | 
**overview** | **str** | Descriptive text giving an overview of integration functionality | [optional] 
**setup** | **str** | How the integration will be set-up | [optional] 
**status** | [**IntegrationStatus**](IntegrationStatus.md) |  | [optional] 
**updated_epoch_millis** | **int** |  | [optional] 
**updater_id** | **str** |  | [optional] 
**version** | **str** | Integration version string | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


