# IntegrationStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_status** | **str** | Status of integration content, e.g. dashboards | 
**install_status** | **str** | Whether the customer or an automated process has chosen to install this integration | 
**metric_statuses** | [**dict(str, MetricStatus)**](MetricStatus.md) | A Map from names of the required metrics to an object representing their reporting status.  The reporting status object has 3 boolean fields denoting whether the metric has been received during the corresponding time period: &#x60;ever&#x60;, &#x60;recentExceptNow&#x60;, and &#x60;now&#x60;.  &#x60;now&#x60; is on the order of a few hours, and &#x60;recentExceptNow&#x60; is on the order of the past few days, excluding the period considered to be &#x60;now&#x60;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


