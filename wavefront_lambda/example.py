import wavefront_lambda
from wavefront_pyformance import delta


@wavefront_lambda.wrapper
def lambda_handler(event, context):
    # Get registry to report metrics.
    registry = wavefront_lambda.get_registry()

    # Report Delta Counters
    delta_counter = delta.delta_counter(registry, "deltaCounter")
    delta_counter.inc()

    # Report Counters
    counter = registry.counter("counter")
    counter.inc()

    # Report Gauge
    gauge_value = registry.gauge("gaugeValue")
    gauge_value.set_value(5.5)
