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
from wavefront_api_client.api.account__service_account_api import AccountServiceAccountApi  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestAccountServiceAccountApi(unittest.TestCase):
    """AccountServiceAccountApi unit test stubs"""

    def setUp(self):
        self.api = wavefront_api_client.api.account__service_account_api.AccountServiceAccountApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activate_account(self):
        """Test case for activate_account

        Activates the given service account  # noqa: E501
        """
        pass

    def test_create_service_account(self):
        """Test case for create_service_account

        Creates a service account  # noqa: E501
        """
        pass

    def test_deactivate_account(self):
        """Test case for deactivate_account

        Deactivates the given service account  # noqa: E501
        """
        pass

    def test_get_all_service_accounts(self):
        """Test case for get_all_service_accounts

        Get all service accounts  # noqa: E501
        """
        pass

    def test_get_service_account(self):
        """Test case for get_service_account

        Retrieves a service account by identifier  # noqa: E501
        """
        pass

    def test_update_service_account(self):
        """Test case for update_service_account

        Updates the service account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
