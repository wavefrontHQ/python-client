# -*- coding: utf-8 -*-
from pyformance.meters import Counter


def delta_counter(registry, name):
    """
    Registers a DeltaCounter with the given registry and returns the instance.

    The given name is prefixed with DeltaCounter.DELTA_PREFIX for registering.

    :param registry: the metrics registry to register with
    :param name: the delta counter name
    :return: the registered DeltaCounter instance
    """
    if not name:
        raise ValueError("invalid counter name")

    name = name if _has_delta_prefix(name) else DeltaCounter.DELTA_PREFIX + name
    try:
        ret_counter = DeltaCounter()
        registry.add(name, ret_counter)
        return ret_counter
    except LookupError:
        return registry.counter(name)


def is_delta_counter(name, registry):
    counter = registry.counter(name)
    return counter and isinstance(counter, DeltaCounter)


def get_delta_name(prefix, name, value_key):
    """
    returns the name of the delta metric name of the form: ∆prefix.name.value_key
    """
    return "%s%s.%s" % (DeltaCounter.DELTA_PREFIX + prefix, name[1:], value_key)


def _has_delta_prefix(name):
    return name and name.startswith(DeltaCounter.DELTA_PREFIX) or name.startswith(DeltaCounter.ALT_DELTA_PREFIX)


class DeltaCounter(Counter):
    """
    A counter for Wavefront delta metrics.

    Differs from a counter in that it is reset in the WavefrontReporter every time the value is reported.
    """

    DELTA_PREFIX = u"\u2206"
    ALT_DELTA_PREFIX = u"\u0394"

    def __init__(self):
        super(DeltaCounter, self).__init__()
