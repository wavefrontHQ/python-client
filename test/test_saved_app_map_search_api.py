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
from wavefront_api_client.api.saved_app_map_search_api import SavedAppMapSearchApi  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestSavedAppMapSearchApi(unittest.TestCase):
    """SavedAppMapSearchApi unit test stubs"""

    def setUp(self):
        self.api = wavefront_api_client.api.saved_app_map_search_api.SavedAppMapSearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_saved_app_map_search(self):
        """Test case for create_saved_app_map_search

        Create a search  # noqa: E501
        """
        pass

    def test_default_app_map_search(self):
        """Test case for default_app_map_search

        Get default app map search for a user  # noqa: E501
        """
        pass

    def test_default_app_map_search_0(self):
        """Test case for default_app_map_search_0

        Set default app map search at user level  # noqa: E501
        """
        pass

    def test_default_customer_app_map_search(self):
        """Test case for default_customer_app_map_search

        Set default app map search at customer level  # noqa: E501
        """
        pass

    def test_delete_saved_app_map_search(self):
        """Test case for delete_saved_app_map_search

        Delete a search  # noqa: E501
        """
        pass

    def test_delete_saved_app_map_search_for_user(self):
        """Test case for delete_saved_app_map_search_for_user

        Delete a search belonging to the user  # noqa: E501
        """
        pass

    def test_get_all_saved_app_map_searches(self):
        """Test case for get_all_saved_app_map_searches

        Get all searches for a customer  # noqa: E501
        """
        pass

    def test_get_all_saved_app_map_searches_for_user(self):
        """Test case for get_all_saved_app_map_searches_for_user

        Get all searches for a user  # noqa: E501
        """
        pass

    def test_get_saved_app_map_search(self):
        """Test case for get_saved_app_map_search

        Get a specific search  # noqa: E501
        """
        pass

    def test_update_saved_app_map_search(self):
        """Test case for update_saved_app_map_search

        Update a search  # noqa: E501
        """
        pass

    def test_update_saved_app_map_search_for_user(self):
        """Test case for update_saved_app_map_search_for_user

        Update a search belonging to the user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
