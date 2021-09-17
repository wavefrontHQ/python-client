# SpanSamplingPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether span sampling policy is active | [optional] 
**created_epoch_millis** | **int** | Created time of the span sampling policy | [optional] 
**creator_id** | **str** | Creator user of the span sampling policy | [optional] 
**deleted** | **bool** | Whether span sampling policy is soft-deleted, can be modified with delete/undelete api | [optional] 
**description** | **str** | Span sampling policy description | [optional] 
**expression** | **str** | Span sampling policy expression | 
**id** | **str** | Unique identifier of the span sampling policy | 
**name** | **str** | Span sampling policy name | 
**sampling_percent** | **int** | Sampling percent of policy, 100 means keeping all the spans that matches the policy | [optional] 
**updated_epoch_millis** | **int** | Last updated time of the span sampling policy | [optional] 
**updater_id** | **str** | Updater user of the span sampling policy | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


