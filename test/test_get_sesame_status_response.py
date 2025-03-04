# coding: utf-8

"""
    Version 3 of CANDY HOUSE’s Sesame API

    We use RESTful API to provide basic manipulation of the Sesame smart lock, including: * Get Sesame lock/unlock status * Get battery status * Lock and unlock Sesame * Sync Sesame status * Get results for lock, unlock, and sync commands   # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Contact: sesame@candyhouse.co
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import sesame_client
from sesame_client.models.get_sesame_status_response import GetSesameStatusResponse  # noqa: E501
from sesame_client.rest import ApiException


class TestGetSesameStatusResponse(unittest.TestCase):
    """GetSesameStatusResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetSesameStatusResponse(self):
        """Test GetSesameStatusResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = sesame_client.models.get_sesame_status_response.GetSesameStatusResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
