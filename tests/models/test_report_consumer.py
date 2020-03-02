import json
import unittest

from finicity.models import ReportConsumer

# https://community.finicity.com/s/article/Report-Consumers
EXAMPLE_REPORT_CONSUMER_PROPOSED = '''
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

EXAMPLE_REPORT_CONSUMER = '''
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


class TestReportConsumer(unittest.TestCase):
    def test_account_detail_response(self):
        response_dict = json.loads(EXAMPLE_REPORT_CONSUMER)
        response = ReportConsumer.from_dict(response_dict)
        self.assertEqual({}, response.unused_fields)
