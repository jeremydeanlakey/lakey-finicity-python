

@dataclass
class CustomersListResponse(object):
    found: int  # Total number of records matching search criteria
    displaying: int  # Number of records in this response
    moreAvailable: bool  # True if this response does not contain the last record in the result set
    customers: List[Institution]


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
