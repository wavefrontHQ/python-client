# AlertSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_source_type** | **list[str]** | The types of the alert source (an array of CONDITION, AUDIT, VARIABLE) and the default one is [VARIABLE]. CONDITION alert source is the condition query in the alert. AUDIT alert source is the query to get more details when the alert changes state. VARIABLE alert source is a variable used in the other queries. | [optional] 
**color** | **str** | The color of the alert source. | [optional] 
**description** | **str** | The additional long description of the alert source. | [optional] 
**hidden** | **bool** | A flag to indicate whether the alert source is hidden or not. | [optional] 
**name** | **str** | The alert source query name. Used as the variable name in the other query. | [optional] 
**query** | **str** | The alert query. Support both Wavefront Query and Prometheus Query. | [optional] 
**query_builder_enabled** | **bool** | A flag indicate whether the alert source query builder enabled or not. | [optional] 
**query_builder_serialization** | **str** | The string serialization of the alert source query builder, mostly used by Tanzu Observability UI. | [optional] 
**query_type** | **str** | The type of the alert query. Supported types are [PROMQL, WQL]. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


