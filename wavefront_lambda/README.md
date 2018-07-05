# wavefront_lambda

This is a Wavefront python wrapper for AWS Lambda python function handler to send metrics directly to wavefront.

## Requirements
Python 2.7 or 3.6.

## Installation
To install from PyPi
```
pip install wavefront_lambda
```

## Environmental variables
WAVEFRONT_URL = https://\<INSTANCE>.wavefront.com  
WAVEFRONT_API_TOKEN = Wavefront API token with Direct Data Ingestion permission.  
IS_REPORT_STANDARD_METRICS = Set to False or false to not report standard lambda metrics directly to wavefront.  

## Usage

Decorate your AWS Lambda handler function with @wavefront_lambda.wrapper.

```Python
import wavefront_lambda

@wavefront_lambda.wrapper
def handler(event, context):
    # your code

```

## Standard Lambda Metrics reported by Wavefront Lambda wrapper

The Lambda wrapper sends the following standard lambda metrics to wavefront:

| Metric Name                       |  Type              | Description                                                             |
| ----------------------------------|:------------------:| ----------------------------------------------------------------------- |
| aws.lambda.wf.invocations.count   | Delta Counter      | Count of number of lambda function invocations aggregated at the server.|
| aws.lambda.wf.errors.count        | Delta Counter      | Count of number of errors aggregated at the server.                     |
| aws.lambda.wf.coldstarts.count    | Delta Counter      | Count of number of cold starts aggregated at the server.                |
| aws.lambda.wf.coldstarts_raw.count| Counter            | Count of number of cold starts.                                         |
| aws.lambda.wf.duration.value      | Gauge              | Execution time of the Lambda handler function in milliseconds.          |

The Lambda wrapper adds the following point tags to all metrics sent to wavefront:

| Point Tag             | Description                                                                   |
| --------------------- | ----------------------------------------------------------------------------- |
| LambdaArn             | ARN(Amazon Resource Name) of the Lambda function.                             |
| Region                | AWS Region of the Lambda function.                                            |
| accountId             | AWS Account ID from which the Lambda function was invoked.                    |
| ExecutedVersion       | The version of Lambda function.                                               |
| FunctionName          | The name of Lambda function.                                                  |
| Resource              | Execution time of the Lambda.                                                 |
| EventSourceMappings   | AWS Function Name (In case of an event source mapping Lambda invocation only,)|

## Custom Lambda Metrics

The wavefront lambda wrapper reports custom business metrics via a metrics registry provided by the [pyformance plugin](https://github.com/wavefrontHQ/python-client/tree/master/wavefront_pyformance).  
Please refer to the [code sample](https://github.com/wavefrontHQ/python-client/blob/master/wavefront_lambda/example.py) which shows how you can send custom business metrics to wavefront from your lambda function.
