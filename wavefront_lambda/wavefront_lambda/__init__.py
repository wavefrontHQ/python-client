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
    standard metrics and reports it directly to the set wavefront url. It
    requires the following Environmental variables to be set:
    1.WAVEFRONT_URL : https://<INSTANCE>.wavefront.com
    2.WAVEFRONT_API_TOKEN : Wavefront API token with Direct Data Ingestion permission
    3.IS_REPORT_STANDARD_METRICS : Set to False to not report standard lambda
                                   metrics directly to wavefront.

    """
    def call_lambda_with_standard_metrics(wf_reporter, *args, **kwargs):
        METRIC_PREFIX = "aws.lambda.wf."
        # Set cold start counter
        global is_cold_start
        if is_cold_start:
            aws_cold_starts_counter = delta.delta_counter(reg, METRIC_PREFIX + "coldstarts")
            aws_cold_starts_counter.inc()
            aws_cold_starts_normal_counter = reg.counter(METRIC_PREFIX + "coldstarts_raw")
            aws_cold_starts_normal_counter.inc()
            is_cold_start = False
        # Set invocations counter
        aws_lambda_invocations_counter = delta.delta_counter(reg, METRIC_PREFIX + "invocations")
        aws_lambda_invocations_counter.inc()
        time_start = datetime.now()
        try:
            result = func(*args, **kwargs)
            return result
        except:
            # Set error counter
            aws_lambda_errors_counter = delta.delta_counter(reg, METRIC_PREFIX + "errors")
            aws_lambda_errors_counter.inc()
            raise
        finally:
            time_taken = datetime.now() - time_start
            # Set duration Gauge
            aws_lambda_duration_gauge = reg.gauge(METRIC_PREFIX + "duration")
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
            raise ValueError("Environmental variable WAVEFRONT_URL is not set.")
        auth_token = os.environ.get('WAVEFRONT_API_TOKEN')
        if not auth_token:
            raise ValueError("Environmental variable WAVEFRONT_API_TOKEN is not set.")
        is_report_standard_metrics = True
        if os.environ.get('IS_REPORT_STANDARD_METRICS') in ['False', 'false']:
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
            'Region': split_arn[3],
            'accountId': split_arn[4],
            'ExecutedVersion': context.function_version
        }
        if split_arn[5] == 'function':
            point_tags['FunctionName'] = split_arn[6]
            point_tags['Resource'] = split_arn[6]
            if len(split_arn) == 8 and split_arn[7] != context.function_version:
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
