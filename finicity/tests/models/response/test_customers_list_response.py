import json
import unittest

from finicity.models import CustomersListResponse

EXAMPLE_CUSTOMERS_RESPONSE = '''
{
  "found": 7,
  "displaying": 2,
  "moreAvailable": true,
  "customers": [
  {
    "id": 41442,
    "username": "rsmith",
    "firstName": "Ron",
    "lastName": "Smith",
    "type": "active",
    "createdDate": 1412792539
  },
  {
    "id": 41463,
    "username": "sbrown",
    "firstName": "Smithie",
    "lastName": "Brown",
    "type": "active",
    "createdDate": 1412884724
  }
  ]
}
'''


class TestCustomersResponse(unittest.TestCase):
    def test_account_detail_response(self):
        response_dict = json.loads(EXAMPLE_CUSTOMERS_RESPONSE)
        response = CustomersListResponse.from_dict(response_dict)
        self.assertEqual({}, response.unused_fields)
        for customer in response.customers:
            self.assertEqual({}, customer.unused_fields)
