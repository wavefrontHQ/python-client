# PagedAlertWithStats

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_counts** | **dict(str, int)** | A map from alert state to the number of alerts in that state within the search results | [optional] 
**cursor** | **str** | The id at which the current (limited) search can be continued to obtain more matching items | [optional] 
**items** | [**list[Alert]**](Alert.md) | List of requested items | [optional] 
**limit** | **int** |  | [optional] 
**more_items** | **bool** | Whether more items are available for return by increment offset or cursor | [optional] 
**offset** | **int** |  | [optional] 
**sort** | [**Sorting**](Sorting.md) |  | [optional] 
**total_items** | **int** | An estimate (lower-bound) of the total number of items available for return.  May not be a tight estimate for facet queries | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


