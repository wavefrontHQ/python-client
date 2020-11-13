# EC2Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_credentials** | [**AWSBaseCredentials**](AWSBaseCredentials.md) |  | [optional] 
**host_name_tags** | **list[str]** | A list of AWS instance tags that, when found, will be used as the \&quot;source\&quot; name in a series.  Default: [\&quot;hostname\&quot;, \&quot;host\&quot;, \&quot;name\&quot;].  If no tag in this list is found, the series source is set to the instance id. | [optional] 
**instance_selection_tags_expr** | **str** | A string expressing the allow list of AWS instance tag-value pairs.  If the instance&#39;s AWS tags match this allow list, data about this instance is ingested from EC2 APIs  Multiple entries are OR&#39;ed.  Key-value pairs in the string are separated by commas and in the form k&#x3D;v.  Example: \&quot;k1&#x3D;v1, k1&#x3D;v2, k3&#x3D;v3\&quot;. | [optional] 
**metric_filter_regex** | **str** | A regular expression that a metric name must match (case-insensitively) in order to be ingested | [optional] 
**point_tag_filter_regex** | **str** | A regular expression that AWS tag key name must match (case-insensitively) in order to be ingested | [optional] 
**volume_selection_tags_expr** | **str** | A string expressing the allow list of AWS volume tag-value pairs.  If the volume&#39;s AWS tags match this allow list, Data about this volume is ingested from EBS APIs.  Multiple entries are OR&#39;ed.  Key-value pairs in the string are separated by commas and in the form k&#x3D;v.  Example: \&quot;k1&#x3D;v1, k1&#x3D;v2, k3&#x3D;v3\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


