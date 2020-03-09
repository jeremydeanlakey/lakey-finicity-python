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

EXAMPLE_ACCOUNTS_RESPONSE = """
{
  "accounts": [
    {
      "id": "1007547418",
      "number": "111111",
      "name": "Checking",
      "balance": 9357.24,
      "type": "checking",
      "status": "active",
      "customerId": "1002191232",
      "institutionId": "102105",
      "balanceDate": 1583716651,
      "aggregationAttemptDate": 1583723079,
      "createdDate": 1583716651,
      "lastUpdatedDate": 1583716663,
      "currency": "USD",
      "institutionLoginId": 1002841562,
      "detail": {
        "availableBalanceAmount": 0
      },
      "displayPosition": 1
    },
    {
      "id": "1007547419",
      "number": "222222",
      "name": "Savings",
      "balance": 22327.3,
      "type": "savings",
      "status": "active",
      "customerId": "1002191232",
      "institutionId": "102105",
      "balanceDate": 1583716651,
      "aggregationAttemptDate": 1583723079,
      "createdDate": 1583716651,
      "lastUpdatedDate": 1583716663,
      "currency": "USD",
      "institutionLoginId": 1002841562,
      "displayPosition": 2
    },
    {
      "id": "1007547420",
      "number": "101010",
      "name": "Personal Investments",
      "balance": 100000,
      "type": "investment",
      "status": "active",
      "customerId": "1002191232",
      "institutionId": "102105",
      "balanceDate": 1583716651,
      "aggregationAttemptDate": 1583723079,
      "createdDate": 1583716651,
      "lastUpdatedDate": 1583716663,
      "currency": "USD",
      "institutionLoginId": 1002841562,
      "detail": {},
      "displayPosition": 3
    },
    {
      "id": "1007547421",
      "number": "121212",
      "name": "My 401k",
      "balance": 265000,
      "type": "investmentTaxDeferred",
      "status": "active",
      "customerId": "1002191232",
      "institutionId": "102105",
      "balanceDate": 1583716651,
      "aggregationAttemptDate": 1583723079,
      "createdDate": 1583716651,
      "lastUpdatedDate": 1583716663,
      "currency": "USD",
      "institutionLoginId": 1002841562,
      "detail": {},
      "displayPosition": 4
    },
    {
      "id": "1007547422",
      "number": "232323",
      "name": "ROTH",
      "balance": 11001,
      "type": "roth",
      "status": "active",
      "customerId": "1002191232",
      "institutionId": "102105",
      "balanceDate": 1583716651,
      "aggregationAttemptDate": 1583723079,
      "createdDate": 1583716651,
      "lastUpdatedDate": 1583716663,
      "currency": "USD",
      "institutionLoginId": 1002841562,
      "detail": {},
      "displayPosition": 5
    }
  ]
}
"""


class TestAccountsListResponse(unittest.TestCase):

    def test_accounts_response(self):
        response_dict = json.loads(EXAMPLE_ACCOUNTS_RESPONSE)
        response = AccountsResponse.from_dict(response_dict)
        self.assertEqual({}, response._unused_fields)
        for account in response.accounts:
            self.assertEqual({}, account._unused_fields)
            if account.detail:
                self.assertEqual({}, account.detail._unused_fields)
