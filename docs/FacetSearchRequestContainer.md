# FacetSearchRequestContainer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facet_query** | **str** | A string against which facet results are compared.  If the facet result CONTAINs, STARTSWITH, or is an EXACT match for this value, as specified by facetQueryMatchingMethod, then it is returned. | [optional] 
**facet_query_matching_method** | **str** | The matching method used to filter when &#39;facetQuery&#39; is used. Defaults to CONTAINS. | [optional] 
**limit** | **int** | The number of results to return.  Default: 100, Maximum allowed: 1000 | [optional] 
**offset** | **int** | The number of results to skip before returning values.  Default: 0 | [optional] 
**query** | [**list[SearchQuery]**](SearchQuery.md) | A list of queries by which to limit the search results.  Entities that match ALL queries in the list are returned | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


