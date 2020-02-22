from finicity.models.institution.institution import Institution


@dataclass
class TransactionsListResponse(object):
    found: int  # Total number of records matching search criteria
    displaying: int  # Number of records in this response
    moreAvailable: bool  # True if this response does not contain the last record in the result set
    fromDate: int  # Value of the fromDate request parameter that generated this response
    toDate: int  # Value of the toDate request parameter that generated this response
    sort: SortOrder  # Value of the sort request parameter that generated this response
    customers: List[Institution]


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
