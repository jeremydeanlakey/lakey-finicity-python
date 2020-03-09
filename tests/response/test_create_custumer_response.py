import json
import unittest

from finicity.responses.create_customer_response import CreateCustomerResponse


# https://community.finicity.com/s/article/201703219-Customers#add_customer
DOCS_EXAMPLE_CREATE_CONSUMER_RESPONSE = """
{
   "id": "41442",
   "createdDate": "1412792539" 
}
"""


class TestCreateCustomerResponse(unittest.TestCase):

    def test_create_customer_response(self):
        response_dict = json.loads(DOCS_EXAMPLE_CREATE_CONSUMER_RESPONSE)
        response = CreateCustomerResponse.from_dict(response_dict)
        self.assertEqual({}, response._unused_fields)
