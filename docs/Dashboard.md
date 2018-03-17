# Dashboard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the dashboard | 
**id** | **str** | Unique identifier, also URL slug, of the dashboard | 
**parameters** | **dict(str, str)** | Deprecated.  An obsolete representation of dashboard parameters | [optional] 
**description** | **str** | Human-readable description of the dashboard | [optional] 
**tags** | [**WFTags**](WFTags.md) |  | [optional] 
**customer** | **str** | id of the customer to which this dashboard belongs | [optional] 
**hidden** | **bool** |  | [optional] 
**creator_id** | **str** |  | [optional] 
**updater_id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**system_owned** | **bool** | Whether this dashboard is system-owned and not writeable | [optional] 
**created_epoch_millis** | **int** |  | [optional] 
**updated_epoch_millis** | **int** |  | [optional] 
**url** | **str** | Unique identifier, also URL slug, of the dashboard | 
**event_filter_type** | **str** | How charts belonging to this dashboard should display events.  BYCHART is default if unspecified | [optional] 
**sections** | [**list[DashboardSection]**](DashboardSection.md) | Dashboard chart sections | 
**parameter_details** | [**dict(str, DashboardParameterValue)**](DashboardParameterValue.md) | The current (as of Wavefront 4.0) JSON representation of dashboard parameters.  This is a map from a parameter name to its representation | [optional] 
**display_description** | **bool** | Whether the dashboard description section is opened by default when the dashboard is shown | [optional] 
**display_section_table_of_contents** | **bool** | Whether the \&quot;pills\&quot; quick-linked the sections of the dashboard are displayed by default when the dashboard is shown | [optional] 
**display_query_parameters** | **bool** | Whether the dashboard parameters section is opened by default when the dashboard is shown | [optional] 
**chart_title_scalar** | **int** | Scale (normally 100) of chart title text size | [optional] 
**event_query** | **str** | Event query to run on dashboard charts | [optional] 
**default_time_window** | **str** | Default time window to query charts | [optional] 
**default_start_time** | **int** | Default start time in milliseconds to query charts | [optional] 
**default_end_time** | **int** | Default end time in milliseconds to query charts | [optional] 
**chart_title_color** | **str** | Text color of the chart title text are, in rgba(rvalue,gvalue,bvalue,avalue) | [optional] 
**chart_title_bg_color** | **str** | Background color of the chart title text area, in rgba(rvalue,gvalue,bvalue,avalue) | [optional] 
**views_last_day** | **int** |  | [optional] 
**views_last_week** | **int** |  | [optional] 
**views_last_month** | **int** |  | [optional] 
**num_charts** | **int** |  | [optional] 
**num_favorites** | **int** |  | [optional] 
**favorite** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


