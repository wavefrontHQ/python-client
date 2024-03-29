# coding: utf-8

"""
    Wavefront REST API Documentation

    <p>The REST API enables you to interact with the Wavefront service by using standard REST API tools. You can use the REST API to automate commonly executed operations, for example to tag sources automatically.</p><p>When you make REST API calls outside the REST API documentation UI, to authenticate to the service, you must use an API token associated with a user account or a service account. For information on how to get the API token and examples, see <a href=\"http://docs.wavefront.com/using_wavefront_api.html\">Use the Wavefront REST API.</a></p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import wavefront_api_client
from wavefront_api_client.api.usage_api import UsageApi  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestUsageApi(unittest.TestCase):
    """UsageApi unit test stubs"""

    def setUp(self):
        self.api = wavefront_api_client.api.usage_api.UsageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_ingestion_policy(self):
        """Test case for create_ingestion_policy

        Create a specific ingestion policy  # noqa: E501
        """
        pass

    def test_delete_ingestion_policy(self):
        """Test case for delete_ingestion_policy

        Delete a specific ingestion policy  # noqa: E501
        """
        pass

    def test_export_csv(self):
        """Test case for export_csv

        Export a CSV report  # noqa: E501
        """
        pass

    def test_get_all_ingestion_policies(self):
        """Test case for get_all_ingestion_policies

        Get all ingestion policies for a customer  # noqa: E501
        """
        pass

    def test_get_ingestion_policy(self):
        """Test case for get_ingestion_policy

        Get a specific ingestion policy  # noqa: E501
        """
        pass

    def test_get_ingestion_policy_by_version(self):
        """Test case for get_ingestion_policy_by_version

        Get a specific historical version of a ingestion policy  # noqa: E501
        """
        pass

    def test_get_ingestion_policy_history(self):
        """Test case for get_ingestion_policy_history

        Get the version history of ingestion policy  # noqa: E501
        """
        pass

    def test_revert_ingestion_policy_by_version(self):
        """Test case for revert_ingestion_policy_by_version

        Revert to a specific historical version of a ingestion policy  # noqa: E501
        """
        pass

    def test_update_ingestion_policy(self):
        """Test case for update_ingestion_policy

        Update a specific ingestion policy  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
