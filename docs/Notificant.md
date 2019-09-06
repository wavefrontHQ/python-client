# Notificant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | The value of the Content-Type header of the webhook POST request. | [optional] 
**created_epoch_millis** | **int** |  | [optional] 
**creator_id** | **str** |  | [optional] 
**custom_http_headers** | **dict(str, str)** | A string-&gt;string map specifying the custom HTTP header key / value pairs that will be sent in the requests of this web hook | [optional] 
**customer_id** | **str** |  | [optional] 
**description** | **str** | Description | 
**email_subject** | **str** | The subject title of an email notification target | [optional] 
**id** | **str** |  | [optional] 
**is_html_content** | **bool** | Determine whether the email alert target content is sent as html or text. | [optional] 
**method** | **str** | The notification method used for notification target. | 
**recipient** | **str** | The end point for the notification target.EMAIL: email address.  PAGERDUTY: PagerDuty routing Key.  WEBHOOK: URL end point | 
**routes** | [**list[AlertRoute]**](AlertRoute.md) | List of routing targets that this notificant will notify. | [optional] 
**template** | **str** | A mustache template that will form the body of the POST request, email and summary of the PagerDuty. | 
**title** | **str** | Title | 
**triggers** | **list[str]** | A list of occurrences on which this webhook will be fired.  Valid values are ALERT_OPENED, ALERT_UPDATED, ALERT_RESOLVED, ALERT_MAINTENANCE, ALERT_SNOOZED | 
**updated_epoch_millis** | **int** |  | [optional] 
**updater_id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


