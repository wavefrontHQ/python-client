# SearchQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The entity facet (key) by which to search.  Valid keys are any property keys returned by the JSON representation of the entity.  Examples are &#39;creatorId&#39;, &#39;name&#39;, etc.  The following special key keywords are also valid:  &#39;tags&#39; performs a search on entity tags, &#39;tagpath&#39; performs a hierarchical search on tags, with  periods (.) as path level separators.  &#39;freetext&#39; performs a free text search across many fields of the entity | 
**value** | **str** | The entity facet value for which to search | 
**matching_method** | **str** | The method by which search matching is performed.  Default: CONTAINS | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


