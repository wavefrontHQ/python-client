# VropsConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adapter_names** | **dict(str, list[str])** | Adapter names: Metrics will be fetched of only these adapter if given | [optional] 
**base_url** | **str** | The base url for vrops api, Default : https://www.mgmt.cloud.vmware.com/vrops-cloud | [optional] 
**categories_to_fetch** | **list[str]** | A list of vRops Adpater and Resource kind to fetch metrics.  Allowable values are VMWARE_DATASTORE, VMWARE_DATASTORE) | [optional] 
**metric_filter_regex** | **str** | A regular expression that a metric name must match (case-insensitively) in order to be ingested | [optional] 
**organization_id** | **str** | OrganizationID will be derived from api token | [optional] 
**vrops_api_token** | **str** | The vRops API Token | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


