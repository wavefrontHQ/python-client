# Message

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Message source.  System messages will com from &#39;system@wavefront.com&#39; | 
**attributes** | **dict(str, str)** | A string-&gt;string map of additional properties associated with this message | [optional] 
**id** | **str** |  | [optional] 
**target** | **str** | For scope&#x3D;CUSTOMER or scope&#x3D;USER, the individual customer or user id | [optional] 
**content** | **str** | Message content | 
**scope** | **str** | The audience scope that this message should reach | 
**title** | **str** | Title of this message | 
**severity** | **str** | Message severity | 
**start_epoch_millis** | **int** | When this message will begin to be displayed, in epoch millis | 
**end_epoch_millis** | **int** | When this message will stop being displayed, in epoch millis | 
**display** | **str** | The form of display for this message | 
**read** | **bool** | A derived field for whether the current user has read this message | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


