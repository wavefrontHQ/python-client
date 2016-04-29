# Dashboard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | **str** | ID of the customer to which this dashboard belongs | 
**event_filter_type** | **str** | How should dashboard charts display events.  BYCHART is default if unspecified. | [optional] 
**name** | **str** | Name of the dashboard | 
**parameters** | **dict(str, str)** | Dashboard variables, specified in JSON an Object (k-v string:string map) | [optional] 
**sections** | [**list[DashboardSection]**](DashboardSection.md) | Dashboard chart sections | 
**url** | **str** | Unique identifier, also URL slug, of the dashboard | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


