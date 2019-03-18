# AzureConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_credentials** | [**AzureBaseCredentials**](AzureBaseCredentials.md) |  | [optional] 
**category_filter** | **list[str]** | A list of Azure services (such as Microsoft.Compute/virtualMachines, Microsoft.Cache/redis etc) from which to pull metrics. | [optional] 
**metric_filter_regex** | **str** | A regular expression that a metric name must match (case-insensitively) in order to be ingested | [optional] 
**resource_group_filter** | **list[str]** | A list of Azure resource groups from which to pull metrics. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


