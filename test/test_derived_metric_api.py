# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import wavefront_api_client
from wavefront_api_client.api.derived_metric_api import DerivedMetricApi  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestDerivedMetricApi(unittest.TestCase):
    """DerivedMetricApi unit test stubs"""

    def setUp(self):
        self.api = wavefront_api_client.api.derived_metric_api.DerivedMetricApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_tag_to_derived_metric(self):
        """Test case for add_tag_to_derived_metric

        Add a tag to a specific Derived Metric  # noqa: E501
        """
        pass

    def test_create_derived_metric(self):
        """Test case for create_derived_metric

        Create a specific derived metric definition  # noqa: E501
        """
        pass

    def test_delete_derived_metric(self):
        """Test case for delete_derived_metric

        Delete a specific derived metric definition  # noqa: E501
        """
        pass

    def test_get_all_derived_metrics(self):
        """Test case for get_all_derived_metrics

        Get all derived metric definitions for a customer  # noqa: E501
        """
        pass

    def test_get_derived_metric(self):
        """Test case for get_derived_metric

        Get a specific registered query  # noqa: E501
        """
        pass

    def test_get_derived_metric_by_version(self):
        """Test case for get_derived_metric_by_version

        Get a specific historical version of a specific derived metric definition  # noqa: E501
        """
        pass

    def test_get_derived_metric_history(self):
        """Test case for get_derived_metric_history

        Get the version history of a specific derived metric definition  # noqa: E501
        """
        pass

    def test_get_derived_metric_tags(self):
        """Test case for get_derived_metric_tags

        Get all tags associated with a specific derived metric definition  # noqa: E501
        """
        pass

    def test_remove_tag_from_derived_metric(self):
        """Test case for remove_tag_from_derived_metric

        Remove a tag from a specific Derived Metric  # noqa: E501
        """
        pass

    def test_set_derived_metric_tags(self):
        """Test case for set_derived_metric_tags

        Set all tags associated with a specific derived metric definition  # noqa: E501
        """
        pass

    def test_undelete_derived_metric(self):
        """Test case for undelete_derived_metric

        Undelete a specific derived metric definition  # noqa: E501
        """
        pass

    def test_update_derived_metric(self):
        """Test case for update_derived_metric

        Update a specific derived metric definition  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
