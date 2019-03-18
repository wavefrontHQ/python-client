# Notificant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description | 
**method** | **str** | The notification method used for notification target. | 
**content_type** | **str** | The value of the Content-Type header of the webhook POST request. | [optional] 
**customer_id** | **str** |  | [optional] 
**title** | **str** | Title | 
**creator_id** | **str** |  | [optional] 
**updater_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**created_epoch_millis** | **int** |  | [optional] 
**updated_epoch_millis** | **int** |  | [optional] 
**template** | **str** | A mustache template that will form the body of the POST request, email and summary of the PagerDuty. | 
**triggers** | **list[str]** | A list of occurrences on which this webhook will be fired.  Valid values are ALERT_OPENED, ALERT_UPDATED, ALERT_RESOLVED, ALERT_MAINTENANCE, ALERT_SNOOZED | 
**recipient** | **str** | The end point for the notification target.EMAIL: email address.  PAGERDUTY: PagerDuty routing Key.  WEBHOOK: URL end point | 
**custom_http_headers** | **dict(str, str)** | A string-&gt;string map specifying the custom HTTP header key / value pairs that will be sent in the requests of this web hook | [optional] 
**email_subject** | **str** | The subject title of an email notification target | [optional] 
**is_html_content** | **bool** | Determine whether the email alert target content is sent as html or text. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


