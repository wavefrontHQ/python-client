# EventSearchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** | The id (exclusive) from which search results resume returning.  Users should supply an entity &#39;id&#39; to this property.  Its main purpose is to resume where a previous search left off because of the &#39;limit&#39; parameter.  If a user supplies the last id in a set of results to cursor, while keeping the query the same, the system will return the next page of results | [optional] 
**limit** | **int** | The number of results to return.  Default: 100 | [optional] 
**query** | [**list[SearchQuery]**](SearchQuery.md) | A list of queries by which to limit the search results | [optional] 
**related_event_time_range** | [**RelatedEventTimeRange**](RelatedEventTimeRange.md) |  | [optional] 
**sort_score_method** | **str** | Whether to sort events on similarity score : {NONE, SCORE_ASC, SCORE_DES}. Default: NONE. If sortScoreMethod is set to SCORE_ASC or SCORE_DES, it will override time sort | [optional] 
**sort_time_ascending** | **bool** | Whether to sort event results ascending in start time.  Default: false | [optional] 
**time_range** | [**EventTimeRange**](EventTimeRange.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


