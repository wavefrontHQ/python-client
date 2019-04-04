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
from wavefront_api_client.models.response_container_list_user_group import ResponseContainerListUserGroup  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestResponseContainerListUserGroup(unittest.TestCase):
    """ResponseContainerListUserGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseContainerListUserGroup(self):
        """Test ResponseContainerListUserGroup"""
        # FIXME: construct object with mandatory attributes with example values
        # model = wavefront_api_client.models.response_container_list_user_group.ResponseContainerListUserGroup()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
