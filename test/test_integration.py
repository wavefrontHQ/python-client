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
from wavefront_api_client.models.integration import Integration  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestIntegration(unittest.TestCase):
    """Integration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIntegration(self):
        """Test Integration"""
        # FIXME: construct object with mandatory attributes with example values
        # model = wavefront_api_client.models.integration.Integration()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
