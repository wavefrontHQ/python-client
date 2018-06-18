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
    1.WAVEFRONT_URL : your corp wavefront url
    2.WAVEFRONT_API_TOKEN : The users API authentication token
    3.IS_REPORT_STANDARD_METRICS : set to false to not report standard lambda
                                   metrics directly to wavefront.

    """
    def call_lambda_with_standard_metrics(*args, wf_reporter=None, **kwargs):
        # Set cold start counter
        global is_cold_start
        if is_cold_start:
            aws_cold_starts_counter = delta.delta_counter(reg, "coldstart")
            aws_cold_starts_counter.inc()
            aws_cold_starts_normal_counter = reg.counter("coldstart-normalcounter")
            aws_cold_starts_normal_counter.inc()
            is_cold_start = False
        # Set invocations counter
        aws_lambda_invocations_counter = delta.delta_counter(reg, "invocations")
        aws_lambda_invocations_counter.inc()
        time_start = datetime.now()
        try:
            result = func(*args, **kwargs)
            return result
        except:
            # Set error counter
            aws_lambda_errors_counter = delta.delta_counter(reg, "errors")
            aws_lambda_errors_counter.inc()
            raise
        finally:
            time_taken = datetime.now() - time_start
            # Set duration Gauge
            aws_lambda_duration_gauge = reg.gauge("duration")
            aws_lambda_duration_gauge.set_value(time_taken.total_seconds() * 1000)
            wf_reporter.report_now(registry=reg)

    def call_lambda_without_standard_metrics(*args, wf_reporter=None, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except:
            raise
        finally:
            wf_reporter.report_now(registry=reg)

    def wavefront_wrapper(*args, **kwargs):
        auth_token = os.environ.get('WAVEFRONT_API_TOKEN')
        server = os.environ.get('WAVEFRONT_URL')
        is_report_standard_metrics = True
        if os.environ.get('IS_REPORT_STANDARD_METRICS') in ['False', 'false']:
            is_report_standard_metrics = False
        # AWS lambda execution enviroment requires handler to consume two arguments
        # 1. Event - input of json format
        # 2. Context - The execution context object
        context = args[1]
        invoked_function_arn = context.invoked_function_arn
        invoked_function_version = context.function_version
        # Expected formats are:
        # 1. Invoking a specific lambda version:
        #    - arn:aws:lambda:region:accountId:function:functionName:function_version
        #    Ex: arn:aws:lambda:region:accountId:function:functionName:$LATEST
        #        arn:aws:lambda:region:accountId:function:functionName:2
        # 2. Invokeing a specific lambda via alias (which can point to any version):
        #    - arn:aws:lambda:region:accountId:function:functionName:function_alias
        split_arn = invoked_function_arn.split(':')
        point_tags = {
            'aws_lambda_arn': invoked_function_arn,
            'aws_region': split_arn[3],
            'aws_account_id': split_arn[4],
            'aws_function_version': invoked_function_version
        }
        if split_arn[5] == 'function':
            point_tags['aws_function_name'] = split_arn[6]
            if len(split_arn) == 8 and split_arn[7] != invoked_function_version:
                point_tags['aws_function_alias'] = split_arn[7]
        elif split_arn[5] == 'event-source-mappings':
            point_tags['event_source_mappings'] = split_arn[6]

        # Initialize registry for each lambda invocation
        global reg
        reg = MetricsRegistry()

        # Initialize the wavefront direct reporter
        src = "awslambda." + point_tags['aws_function_name']
        wf_direct_reporter = WavefrontDirectReporter(server=server,
                                                     token=auth_token,
                                                     registry=reg,
                                                     source=src,
                                                     tags=point_tags,
                                                     prefix="wf.aws.lambda.")

        if is_report_standard_metrics:
            call_lambda_with_standard_metrics(*args,
                                              wf_reporter=wf_direct_reporter,
                                              **kwargs)
        else:
            call_lambda_without_standard_metrics(*args,
                                                 wf_reporter=wf_direct_reporter,
                                                 **kwargs)

    return wavefront_wrapper


def get_registry():
    return reg