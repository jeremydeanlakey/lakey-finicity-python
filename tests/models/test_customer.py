import json
import unittest

from finicity.models import Customer


EXAMPLE_CUSTOMER = '''
{
"id":"1001788930",
"username":"johndoe",
"firstName":"John",
"lastName":"Doe",
"type":"testing",
"createdDate":"1583006931"
}
'''


class TestCustomer(unittest.TestCase):

    def test_from_dict(self):
        response_dict = json.loads(EXAMPLE_CUSTOMER)
        response = Customer.from_dict(response_dict)
        self.assertEqual({}, response._unused_fields)
