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
from wavefront_api_client.api.user_api import UserApi  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = wavefront_api_client.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_user_to_user_groups(self):
        """Test case for add_user_to_user_groups

        Adds specific groups to the user or service account  # noqa: E501
        """
        pass

    def test_create_user(self):
        """Test case for create_user

        Creates an user if the user doesn't already exist.  # noqa: E501
        """
        pass

    def test_delete_multiple_users(self):
        """Test case for delete_multiple_users

        Deletes multiple users or service accounts  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Deletes a user or service account identified by id  # noqa: E501
        """
        pass

    def test_get_all_users(self):
        """Test case for get_all_users

        Get all users  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Retrieves a user by identifier (email address)  # noqa: E501
        """
        pass

    def test_get_user_business_functions(self):
        """Test case for get_user_business_functions

        Returns business functions of a specific user or service account.  # noqa: E501
        """
        pass

    def test_grant_permission_to_users(self):
        """Test case for grant_permission_to_users

        Grants a specific permission to multiple users or service accounts  # noqa: E501
        """
        pass

    def test_grant_user_permission(self):
        """Test case for grant_user_permission

        Grants a specific permission to user or service account  # noqa: E501
        """
        pass

    def test_invite_users(self):
        """Test case for invite_users

        Invite users with given user groups and permissions.  # noqa: E501
        """
        pass

    def test_remove_user_from_user_groups(self):
        """Test case for remove_user_from_user_groups

        Removes specific groups from the user or service account  # noqa: E501
        """
        pass

    def test_revoke_permission_from_users(self):
        """Test case for revoke_permission_from_users

        Revokes a specific permission from multiple users or service accounts  # noqa: E501
        """
        pass

    def test_revoke_user_permission(self):
        """Test case for revoke_user_permission

        Revokes a specific permission from user or service account  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Update user with given user groups, permissions and ingestion policy.  # noqa: E501
        """
        pass

    def test_validate_users(self):
        """Test case for validate_users

        Returns valid users and service accounts, also invalid identifiers from the given list  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
