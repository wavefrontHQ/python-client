# AppDynamicsConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_filter_regex** | **list[str]** | List of regular expressions that a application name must match (case-insensitively) in order to be ingested. | [optional] 
**controller_name** | **str** | Name of the SaaS controller. | 
**enable_app_infra_metrics** | **bool** | Boolean flag to control Application Infrastructure metric injection. | [optional] 
**enable_backend_metrics** | **bool** | Boolean flag to control Backend metric injection. | [optional] 
**enable_business_trx_metrics** | **bool** | Boolean flag to control Business Transaction metric injection. | [optional] 
**enable_error_metrics** | **bool** | Boolean flag to control Error metric injection. | [optional] 
**enable_individual_node_metrics** | **bool** | Boolean flag to control Individual Node metric injection. | [optional] 
**enable_overall_perf_metrics** | **bool** | Boolean flag to control Overall Performance metric injection. | [optional] 
**enable_rollup** | **bool** | Set this to &#39;false&#39; to get separate results for all values within the time range, by default it is &#39;true&#39;. | [optional] 
**enable_service_endpoint_metrics** | **bool** | Boolean flag to control Service End point metric injection. | [optional] 
**encrypted_password** | **str** | Password for AppDynamics user. | 
**user_name** | **str** | Username is combination of userName and the account name. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


