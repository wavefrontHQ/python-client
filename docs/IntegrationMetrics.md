# IntegrationMetrics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefixes** | **list[str]** | Set of metric prefix namespaces belonging to this integration | 
**display** | **list[str]** | Set of metrics that are displayed in the metric panel during integration setup | 
**charts** | **list[str]** | URLs for JSON definitions of charts that display info about this integration&#39;s metrics | 
**chart_objs** | [**list[Chart]**](Chart.md) | Chart JSONs materialized from the links in &#x60;charts&#x60; | [optional] 
**required** | **list[str]** | Set of \&quot;canary\&quot; metrics that define the \&quot;liveness\&quot; of this integration&#39;s metric ingestion | 
**pps_dimensions** | **list[str]** | For reported points belonging to this integration, these point tags are escalated to the internal point-rate counters so that reporting can be broken out by these dimensions | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


