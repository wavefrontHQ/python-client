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
WAVEFRONT_URL = https://<INSTANCE>.wavefront.com
WAVEFRONT_API_TOKEN = Wavefront API token with Direct Data Ingestion permission.
IS_REPORT_STANDARD_METRICS = Set to False to not report standard lambda metrics directly to wavefront.  

## Usage

Decorate your AWS Lambda handler function with @wavefront_lambda.wrapper.

```Python
import wavefront_lambda

@wavefront_lambda.wrapper
def handler(event, context):
    # your code

```
