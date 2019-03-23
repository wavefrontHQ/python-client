# FacetsSearchRequestContainer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facet_query** | **str** | A string against which facet results are compared.  If the facet result either CONTAINs, STARTSWITH, or is an EXACT match for this value, as specified by facetQueryMatchingMethod, then it is returned | [optional] 
**facet_query_matching_method** | **str** | The matching method used to filter when &#39;facetQuery&#39; is used. Defaults to CONTAINS. | [optional] 
**facets** | **list[str]** | A list of facets (property keys) to return values from found in entities matching &#39;query&#39;.  Examples are &#39;tags&#39;, &#39;creatorId&#39;, etc | 
**limit** | **int** | The number of results to return.  Default 100 | [optional] 
**query** | [**list[SearchQuery]**](SearchQuery.md) | A list of queries by which to limit the search results.  Entities that match ALL queries in this list constitute a set of &#39;entity search results&#39;.  All facets listed in the &#39;facets&#39; search parameter of all entities within &#39;entity search results&#39; are scanned to produce the search results (of facet values). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


