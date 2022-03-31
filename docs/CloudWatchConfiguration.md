# CloudWatchConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_credentials** | [**AWSBaseCredentials**](AWSBaseCredentials.md) |  | [optional] 
**instance_selection_tags** | **dict(str, str)** | A string-&gt;string map of allow list of AWS instance tag-value pairs (in AWS).  If the instance&#39;s AWS tags match this allow list, CloudWatch data about this instance is ingested.  Multiple entries are OR&#39;ed | [optional] 
**instance_selection_tags_expr** | **str** | A string expressing the allow list of AWS instance tag-value pairs.  If the instance&#39;s AWS tags match this allow list, CloudWatch data about this instance is ingested.  Multiple entries are OR&#39;ed and also OR&#39;ed with entries from instanceSelectionTags.  Key-value pairs in the string are separated by commas and in the form k&#x3D;v.  Example: \&quot;k1&#x3D;v1, k1&#x3D;v2, k3&#x3D;v3\&quot;. | [optional] 
**metric_filter_regex** | **str** | A regular expression that a CloudWatch metric name must match (case-insensitively) in order to be ingested | [optional] 
**namespaces** | **list[str]** | A list of namespace that limit what we query from CloudWatch. | [optional] 
**point_tag_filter_regex** | **str** | A regular expression that AWS tag key name must match (case-insensitively) in order to be ingested | [optional] 
**thread_distribution_in_mins** | **int** | ThreadDistributionInMins | [optional] 
**volume_selection_tags** | **dict(str, str)** | A string-&gt;string map of allow list of AWS volume tag-value pairs (in AWS).  If the volume&#39;s AWS tags match this allow list, CloudWatch data about this volume is ingested.  Multiple entries are OR&#39;ed | [optional] 
**volume_selection_tags_expr** | **str** | A string expressing the allow list of AWS volume tag-value pairs.  If the volume&#39;s AWS tags match this allow list, CloudWatch data about this volume is ingested.  Multiple entries are OR&#39;ed and also OR&#39;ed with entries from volumeSelectionTags.  Key-value pairs in the string are separated by commas and in the form k&#x3D;v.  Example: \&quot;k1&#x3D;v1, k1&#x3D;v2, k3&#x3D;v3\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


