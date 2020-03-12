import json
import unittest

from lakey_finicity.models import Consumer

# https://community.finicity.com/s/article/Report-Consumers
EXAMPLE_CONSUMER_PROPOSED = '''
{
  "firstName": "FIRST_NAME",
  "lastName": "LAST_NAME",
  "address": "ADDRESS",
  "city": "CITY",
  "state": "STATE",
  "zip": "ZIP",
  "phone": "PHONE",
  "ssn": "123-45-6789",
  "birthday": {
    "year": "1972",
    "month": "07",
    "dayOfMonth": "03"
  },
  "email": "EMAIL_ADDRESS"
}
'''

EXAMPLE_CONSUMER = '''
{
  "id": "0h7h3r301md83",
  "firstName": "FIRST_NAME",
  "lastName": "LAST_NAME",
  "address": "ADDRESS",
  "city": "CITY",
  "state": "STATE",
  "zip": "ZIP",
  "phone": "PHONE",
  "ssn": "6789",
  "birthday": {
    "year": "1972",
    "month": "07",
    "dayOfMonth": "03"
  },
  "email": "EMAIL_ADDRESS",
  "createdDate": 1507658822
}
'''


class TestConsumer(unittest.TestCase):
    def test_account_detail_response(self):
        response_dict = json.loads(EXAMPLE_CONSUMER)
        response = Consumer.from_dict(response_dict)
        self.assertEqual({}, response._unused_fields)
