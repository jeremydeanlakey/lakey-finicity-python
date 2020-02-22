import unittest


SAMPLE_CUSTOMERS_RESPONSE = '''
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
    pass
