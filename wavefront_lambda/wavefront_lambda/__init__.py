from wavefront_pyformance.wavefront_reporter import WavefrontDirectReporter
from pyformance import MetricsRegistry
import os
from datetime import datetime
from wavefront_pyformance import delta

is_cold_start = True
reg = None


def wrapper(func):
    """
    Returns the Wavefront Lambda wrapper. The wrapper collects aws lambda's
    standard metrics and reports it directly to the specified wavefront url. It
    requires the following Environment variables to be set:
    1.WAVEFRONT_URL : https://<INSTANCE>.wavefront.com
    2.WAVEFRONT_API_TOKEN : Wavefront API token with Direct Data Ingestion permission
    3.REPORT_STANDARD_METRICS : Set to False to not report standard lambda
                                   metrics directly to wavefront.

    """
    def call_lambda_with_standard_metrics(wf_reporter, *args, **kwargs):
        METRIC_PREFIX = "aws.lambda.wf."
        METRIC_EVENT_SUFFIX = "_event"
        # Register cold start counter
        aws_cold_starts_counter = delta.delta_counter(reg, METRIC_PREFIX + "coldstarts")
        aws_cold_start_event_counter = reg.counter(METRIC_PREFIX + "coldstart" + METRIC_EVENT_SUFFIX)
        global is_cold_start
        if is_cold_start:
            # Set cold start counter.
            aws_cold_starts_counter.inc()
            aws_cold_start_event_counter.inc()
            is_cold_start = False
        # Set invocations counter
        aws_lambda_invocations_counter = delta.delta_counter(reg, METRIC_PREFIX + "invocations")
        aws_lambda_invocations_counter.inc()
        aws_lambda_invocation_event_counter = reg.counter(METRIC_PREFIX + "invocation" + METRIC_EVENT_SUFFIX)
        aws_lambda_invocation_event_counter.inc()
        # Register duration gauge.
        aws_lambda_duration_gauge = reg.gauge(METRIC_PREFIX + "duration")
        # Register error counter.
        aws_lambda_errors_counter = delta.delta_counter(reg, METRIC_PREFIX + "errors")
        aws_lambda_error_event_counter = reg.counter(METRIC_PREFIX + "error" + METRIC_EVENT_SUFFIX)
        time_start = datetime.now()
        try:
            result = func(*args, **kwargs)
            return result
        except:
            # Set error counter
            aws_lambda_errors_counter.inc()
            aws_lambda_error_event_counter.inc()
            raise
        finally:
            time_taken = datetime.now() - time_start
            # Set duration gauge
            aws_lambda_duration_gauge.set_value(time_taken.total_seconds() * 1000)
            wf_reporter.report_now(registry=reg)

    def call_lambda_without_standard_metrics(wf_reporter, *args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except:
            raise
        finally:
            wf_reporter.report_now(registry=reg)

    def wavefront_wrapper(*args, **kwargs):
        server = os.environ.get('WAVEFRONT_URL')
        if not server:
            raise ValueError("Environment variable WAVEFRONT_URL is not set.")
        auth_token = os.environ.get('WAVEFRONT_API_TOKEN')
        if not auth_token:
            raise ValueError("Environment variable WAVEFRONT_API_TOKEN is not set.")
        is_report_standard_metrics = True
        if os.environ.get('REPORT_STANDARD_METRICS') in ['False', 'false']:
            is_report_standard_metrics = False
        # AWS lambda execution enviroment requires handler to consume two arguments
        # 1. Event - input of json format
        # 2. Context - The execution context object
        context = args[1]
        # Expected formats for Lambda ARN are:
        # https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda
        invoked_function_arn = context.invoked_function_arn
        split_arn = invoked_function_arn.split(':')
        point_tags = {
            'LambdaArn': invoked_function_arn,
            'FunctionName' : context.function_name,
            'ExecutedVersion': context.function_version,
            'Region': split_arn[3],
            'accountId': split_arn[4]
        }
        if split_arn[5] == 'function':
            point_tags['Resource'] = split_arn[6]
            if len(split_arn) == 8 :
                point_tags['Resource'] = point_tags['Resource'] + ":" + split_arn[7]
        elif split_arn[5] == 'event-source-mappings':
            point_tags['EventSourceMappings'] = split_arn[6]

        # Initialize registry for each lambda invocation
        global reg
        reg = MetricsRegistry()

        # Initialize the wavefront direct reporter
        wf_direct_reporter = WavefrontDirectReporter(server=server,
                                                     token=auth_token,
                                                     registry=reg,
                                                     source=point_tags['FunctionName'],
                                                     tags=point_tags,
                                                     prefix="")

        if is_report_standard_metrics:
            call_lambda_with_standard_metrics(wf_direct_reporter,
                                              *args,
                                              **kwargs)
        else:
            call_lambda_without_standard_metrics(wf_direct_reporter,
                                                 *args,
                                                 **kwargs)

    return wavefront_wrapper


def get_registry():
    return reg
