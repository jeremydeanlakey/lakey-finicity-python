import unittest


SAMPLE_TRANSACTIONS_RESPONSE = '''
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


class TestTransactionsResponse(unittest.TestCase):
    pass
