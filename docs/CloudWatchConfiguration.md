# CloudWatchConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_credentials** | [**AWSBaseCredentials**](AWSBaseCredentials.md) |  | [optional] 
**instance_selection_tags** | **dict(str, str)** | A string-&gt;string map of white list of AWS instance tag-value pairs (in AWS).  If the instance&#39;s AWS tags match this whitelist, CloudWatch data about this instance is ingested.  Multiple entries are OR&#39;ed | [optional] 
**metric_filter_regex** | **str** | A regular expression that a CloudWatch metric name must match (case-insensitively) in order to be ingested | [optional] 
**namespaces** | **list[str]** | A list of namespace that limit what we query from CloudWatch. | [optional] 
**point_tag_filter_regex** | **str** | A regular expression that AWS tag key name must match (case-insensitively) in order to be ingested | [optional] 
**volume_selection_tags** | **dict(str, str)** | A string-&gt;string map of white list of AWS volume tag-value pairs (in AWS).  If the volume&#39;s AWS tags match this whitelist, CloudWatch data about this volume is ingested.  Multiple entries are OR&#39;ed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


