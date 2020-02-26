import json
import unittest

from finicity.models.response.account_detail_response import AccountDetailResponse


EXAMPLE_ACCOUNT_DETAIL_RESPONSE = '''
{
  "routingNumber": "123456789",
  "realAccountNumber": "002345678901"
}
'''


class TestAccountDetailResponse(unittest.TestCase):
    def test_account_detail_response(self):
        response_dict = json.loads(EXAMPLE_ACCOUNT_DETAIL_RESPONSE)
        response = AccountDetailResponse.from_dict(response_dict)
        self.assertEqual({}, response.unused_fields)
