import json
import unittest

from finicity.responses import TransactionsListResponse

EXAMPLE_TRANSACTIONS_RESPONSE = '''
{
  "found": 250,
  "displaying": 2,
  "moreAvailable": true,
  "fromDate": 1417045583,
  "toDate": 1422316026,
  "sort": "desc",
  "transactions": [
  {
    "id": 805353,
    "amount": -59.56,
    "accountId": 98684,
    "customerId": 41442,
    "status": "active",
    "description": "VERIZON WIRELESS PAYMENTS",
    "memo": "VERIZON WIRELESS PAYMENTS",
    "type": "directDebit",
    "postedDate": 1450852000,
    "createdDate": 1460621294,
    "categorization": {
      "normalizedPayeeName": "Verizon Wireless",
      "category": "Mobile Phone",
      "bestRepresentation": "Verizon Wireless PMT",
      "country": "USA"
    }
  },
  {
    "id": 805350,
    "amount": 647.96,
    "accountId": 98689,
    "customerId": 41442,
    "status": "active",
    "description": "Square Inc 168P2",
    "memo": "Square Inc 168P2",
    "type": "directDeposit",
    "postedDate": 1450152000,
    "createdDate": 1460621294,
    "categorization": {
      "normalizedPayeeName": "Deposit Square Type",
      "category": "Income",
      "bestRepresentation": "Square Inc",
      "country": "USA"
    }
  }
  ]
}
'''


EMPTY_RESULT = """
{"transactions":[]}
"""


TEST_TRANSACTION_ONLY = """
{"found":1,"displaying":1,"moreAvailable":"false","fromDate":"1583085842","toDate":"1583949842","sort":"asc","transactions":[{"id":100803586565,"amount":42.01,"accountId":1007861929,"customerId":1002249444,"status":"active","description":"test transaction","postedDate":1583906400,"transactionDate":1583906400,"createdDate":1583949620,"lastUpdatedDate":1583949620}]}
"""


class TestTransactionsResponse(unittest.TestCase):

    def test_transactions_response(self):
        response_dict = json.loads(EXAMPLE_TRANSACTIONS_RESPONSE)
        response = TransactionsListResponse.from_dict(response_dict)
        self.assertEqual({}, response._unused_fields)
        for transaction in response.transactions:
            self.assertEqual({}, transaction._unused_fields)
            self.assertEqual({}, transaction.categorization._unused_fields)

    def test_empty_response(self):
        response_dict = json.loads(EMPTY_RESULT)
        response = TransactionsListResponse.from_dict(response_dict)
        self.assertEqual({}, response._unused_fields)
        for transaction in response.transactions:
            self.assertEqual({}, transaction._unused_fields)
            self.assertEqual({}, transaction.categorization._unused_fields)

    def test_empty_test(self):
        response_dict = json.loads(TEST_TRANSACTION_ONLY)
        response = TransactionsListResponse.from_dict(response_dict)
        self.assertEqual({}, response._unused_fields)
        for transaction in response.transactions:
            self.assertEqual({}, transaction._unused_fields)
            if transaction.categorization:
                self.assertEqual({}, transaction.categorization._unused_fields)
