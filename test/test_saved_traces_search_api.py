# coding: utf-8

"""
    Wavefront REST API Documentation

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import wavefront_api_client
from wavefront_api_client.api.saved_traces_search_api import SavedTracesSearchApi  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestSavedTracesSearchApi(unittest.TestCase):
    """SavedTracesSearchApi unit test stubs"""

    def setUp(self):
        self.api = wavefront_api_client.api.saved_traces_search_api.SavedTracesSearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_saved_traces_search(self):
        """Test case for create_saved_traces_search

        Create a search  # noqa: E501
        """
        pass

    def test_delete_saved_traces_search(self):
        """Test case for delete_saved_traces_search

        Delete a search  # noqa: E501
        """
        pass

    def test_delete_saved_traces_search_for_user(self):
        """Test case for delete_saved_traces_search_for_user

        Delete a search belonging to the user  # noqa: E501
        """
        pass

    def test_get_all_saved_traces_searches(self):
        """Test case for get_all_saved_traces_searches

        Get all searches for a customer  # noqa: E501
        """
        pass

    def test_get_all_saved_traces_searches_for_user(self):
        """Test case for get_all_saved_traces_searches_for_user

        Get all searches for a user  # noqa: E501
        """
        pass

    def test_get_saved_traces_search(self):
        """Test case for get_saved_traces_search

        Get a specific search  # noqa: E501
        """
        pass

    def test_update_saved_traces_search(self):
        """Test case for update_saved_traces_search

        Update a search  # noqa: E501
        """
        pass

    def test_update_saved_traces_search_for_user(self):
        """Test case for update_saved_traces_search_for_user

        Update a search belonging to the user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
