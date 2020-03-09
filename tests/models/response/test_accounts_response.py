import json
import unittest

from finicity.responses.accounts_response import AccountsResponse


EXAMPLE_REFRESH_ACCOUNTS_RESPONSE = '''
{
  "accounts": [
  {
    "id": "2083",
    "number": "8000008888",
    "name": "Auto Loan",
    "type": "loan",
    "status": "active",
    "balance": "-1234.56",
    "customerId": "41442",
    "institutionId": "101732",
    "balanceDate": "1421996400",
    "createdDate": "1415255907",
    "lastUpdatedDate": "1422467353",
    "institutionLoginId": "17478973",
    "detail": {
    }
  },
  {
    "id": "3203",
    "number": "4100007777",
    "name": "Visa",
    "type": "creditCard",
    "status": "active",
    "balance": "-1208.25",
    "customerId": "41442",
    "institutionId": "101732",
    "balanceDate": "1418022000",
    "createdDate": "1418080904",
    "lastUpdatedDate": "1422467353",
    "institutionLoginId": "17478973",
    "detail": {
    }
  } ]
}
'''


class TestAccountsListResponse(unittest.TestCase):

    def test_accounts_response(self):
        response_dict = json.loads(EXAMPLE_REFRESH_ACCOUNTS_RESPONSE)
        response = AccountsResponse.from_dict(response_dict)
        self.assertEqual({}, response._unused_fields)
        for account in response.accounts:
            self.assertEqual({}, account._unused_fields)
            if account.detail:
                self.assertEqual({}, account.detail._unused_fields)
