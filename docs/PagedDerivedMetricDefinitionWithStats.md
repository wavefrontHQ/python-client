# PagedDerivedMetricDefinitionWithStats

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**list[DerivedMetricDefinition]**](DerivedMetricDefinition.md) | List of requested items | [optional] 
**offset** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**cursor** | **str** | The id at which the current (limited) search can be continued to obtain more matching items | [optional] 
**total_items** | **int** | An estimate (lower-bound) of the total number of items available for return.  May not be a tight estimate for facet queries | [optional] 
**more_items** | **bool** | Whether more items are available for return by increment offset or cursor | [optional] 
**sort** | [**Sorting**](Sorting.md) |  | [optional] 
**counts** | **dict(str, int)** | A map from the state of the derived metric definition to the number of entities in that state within the search results | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


