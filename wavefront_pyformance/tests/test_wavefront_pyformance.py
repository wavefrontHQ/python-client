from unittest import TestCase
import unittest
from pyformance import MetricsRegistry
import delta
from wavefront_reporter import WavefrontReporter, WavefrontProxyReporter, WavefrontDirectReporter
import time


def get_base_reporter(registry=None):
    return WavefrontReporter(registry=registry, source="python-test", tags={"key1":"val1"}, prefix="python.test.")

def get_direct_reporter(registry=None):
    return WavefrontDirectReporter(server="https://foo.wavefront.com", token="token",
                                   registry=registry, source="python-test", prefix="python.direct.", tags={"key1":"val1"})


class TestReporter(TestCase):
    def test_collect_metrics(self):
        # should return a list of point lines
        reg = MetricsRegistry()
        reg.counter("foo_counter_1")
        reg.counter("foo_counter_2")

        wf_reporter = get_base_reporter(reg)
        lines = wf_reporter._collect_metrics(reg)
        assert(len(lines) == 2) # equals no. of registered counters

        delta.delta_counter(reg, "foo_delta_1")
        delta.delta_counter(reg, "foo_delta_2")
        lines = wf_reporter._collect_metrics(reg)
        assert(len(lines) == 4) # added two more counters

    def test_delta_reset(self):
        reg = MetricsRegistry()
        counter = delta.delta_counter(reg, "foo_delta_1")
        counter.inc(10)
        wf_reporter = get_base_reporter(reg)
        wf_reporter._collect_metrics(reg)
        assert(counter.get_count() == 0) # delta decremented by count

    def test_get_metric_line(self):
        wf_reporter = get_base_reporter()
        out = wf_reporter._get_metric_line("foo", 10, timestamp=None)
        assert(out == 'foo 10 source=\"python-test\" \"key1\"=\"val1\"') # w/o timestamp

        out = wf_reporter._get_metric_line("foo", 10, timestamp=123456)
        assert(out == 'foo 10 123456 source=\"python-test\" \"key1\"=\"val1\"') # with timestamp

    def test_chunking(self):
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        wf_reporter = get_direct_reporter()
        chunks = wf_reporter._get_chunks(l, 2)
        for chunk in chunks:
            assert(len(chunk) == 2)
        chunks = wf_reporter._get_chunks(l, 100)
        for chunk in chunks:
            assert(len(chunk) == 10)


class TestDelta(TestCase):
    def test_delta_counter(self):
        reg = MetricsRegistry()
        counter = delta.delta_counter(reg, "foo")
        assert(isinstance(counter, delta.DeltaCounter))

        # test duplicate (should return previously registered counter)
        duplicate_counter = delta.delta_counter(reg, "foo")
        assert(counter == duplicate_counter)
        assert(delta.is_delta_counter(delta.DeltaCounter.DELTA_PREFIX + "foo", reg))

        different_counter = delta.delta_counter(reg, "foobar")
        assert(counter != different_counter)

    def test_has_delta_prefix(self):
        assert(delta._has_delta_prefix(delta.DeltaCounter.DELTA_PREFIX + "foo")) # valid prefix
        assert(delta._has_delta_prefix(delta.DeltaCounter.ALT_DELTA_PREFIX + "foo")) # valid prefix
        assert(delta._has_delta_prefix("foo") is False) # invalid prefix

    def test_get_delta_name(self):
        d = delta.get_delta_name('delta.prefix', delta.DeltaCounter.DELTA_PREFIX + 'foo', 'count')
        assert(d.startswith(delta.DeltaCounter.DELTA_PREFIX))


if __name__ == '__main__':
    # run 'python -m unittest discover' from toplevel to run tests
    unittest.main()