# PolicyRuleWriteModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | The access type of the policy rule | [optional] 
**accounts** | **list[str]** | The list of account identifiers of the policy rule | [optional] 
**description** | **str** | The description of the policy rule | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** | The name of the policy rule | 
**prefixes** | **list[str]** | The prefixes of the policy rule | [optional] 
**roles** | **list[str]** | The list of role identifiers of the policy rule | [optional] 
**tags** | [**list[Annotation]**](Annotation.md) | The tag/value pairs of the policy rule | [optional] 
**tags_anded** | **bool** | Whether tags should be AND-ed or OR-ed.If true, a metric must contain all tags in order for the policy rule to apply. If false, the tags are OR-ed, and a metric must contain one of the tags. Default: false | [optional] 
**user_groups** | **list[str]** | The list of user group identifiers of the policy rule | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


