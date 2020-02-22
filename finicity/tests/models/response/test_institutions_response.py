import unittest


SAMPLE_INSTITUTIONS_RESPONSE = '''
{
  "found": 28,
  "displaying": 3,
  "moreAvailable": true,
  "createdDate": 1470966593,
  "institutions": [
  {
    "id": 101065,
    "name": "New York College Savings Program 529",
    "accountTypeDescription": "Banking",
    "urlHomeApp": "http://www.ny529advisor.com/""",
    "urlLogonApp": "https://ny529advisor.org/nyatpl/auth/loginFormAction.do""",
    "urlProductApp": "",
    "specialText": "Please enter your New York College Savings Program User name and Password.",
    "address": {
      "addressLine1": "P.O. Box 55498",
      "addressLine2": "Boston, MA 02205",
      "city": "Boston",
      "state": "MA",
      "postalCode": "02205",
      "country": "USA"
    },
    "phone": "1-800-774-2108",
    "email": "ny.529advisor@jpmorgan.com",
    "currency": "USD"
  },
  {
    "id": 8584,
    "name": "New York Community Bank Credit Card",
    "accountTypeDescription": "Credit Cards/Accounts",
    "urlHomeApp": "http://www.qcsb.com/index.asp?divID=1""",
    "urlLogonApp": "https://global1.onlinebank.com/cgi-forte/forteisapi.dll?BankTag=1382nycb&ServiceName=WebTeller&TemplateName=Login.htm""",
    "urlProductApp": "",
    "specialText": "Please enter your New York Community Bank Credit Card User ID and Password required for login",
    "address": {
      "addressLine1": "1125 Atlantic Avenue",
      "addressLine2": "",
      "city": "Atlantic City",
      "state": "NJ",
      "postalCode": "08401",
      "country": "USA"
    },
    "phone": "1-609-348-1183",
    "email": "http://www.qcsb.com/southjersey/welcome.shtml""",
    "currency": "USD"
  },
  {
    "id": 1668,
    "name": "New York Giants MBNA CC",
    "accountTypeDescription": "Credit Cards/Accounts",
    "urlHomeApp": "https://www.bankofamerica.com/""",
    "urlLogonApp": "https://secure.bankofamerica.com/login/sign-in/signOnV2Screen.go""",
    "urlProductApp": "",
    "specialText": "Please enter your MBNA Credit Card Online ID and Online Passcode required for login. ",
    "address": {
      "addressLine1": "",
      "addressLine2": "",
      "city": "Wilmington",
      "state": "DE",
      "postalCode": "19884",
      "country": "USA"
    },
    "phone": "1-800-653-2465",
    "email": "",
    "currency": "USD"
  }
  ]
}
'''


class TestInstitutionsResponse(unittest.TestCase):
    pass
