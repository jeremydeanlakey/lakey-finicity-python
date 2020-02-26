import json
import unittest

from finicity.models.response.institution_detail_response import InstitutionDetailResponse

# https://community.finicity.com/s/article/202460265-Institutions#get_institution_details
EXAMPLE_INSTITUTION_DETAILS = '''
{
  "institution": {
  "id": 11863,
  "name": "Clearfield Bank & Trust Co",
  "accountTypeDescription": "Banking",
  "urlHomeApp": "https://www.clearfieldbankandtrust.com/",
  "urlLogonApp": "https://www.netteller.com/clearfieldbankandtrust/login.cfm",
  "urlProductApp": "",
  "specialText": "Please enter your Clearfield Bank & Trust Co ONLINE24 Internet Banking ID and ONLINE24 Internet Banking Password required for login.",
  "address": {
    "addressLine1": "11 N. Second Street",
    "addressLine2": "PO Box 171",
    "city": "Clearfield",
    "state": "PA",
    "postalCode": "16830",
    "country": "USA"
  },
  "email": "support@cbtfinancial.com",
  "phone": "814-765-7551",
  "currency": "USD"
  },
  "loginForm": [
  {
    "id": "11863001",
    "name": "ID",
    "value": "",
    "description": "ONLINE24 Internet Banking ID",
    "displayOrder": 1,
    "mask": "false",
    "instructions": ""
  },
  {
    "id": "11863002",
    "name": "PIN",
    "value": "",
    "description": "ONLINE24 Internet Banking Password",
    "displayOrder": 2,
    "mask": "true",
    "instructions": ""
  }
  ]
}
'''


class TestInstitutionDetailsResponse(unittest.TestCase):
    def test_account_detail_response(self):
        response_dict = json.loads(EXAMPLE_INSTITUTION_DETAILS)
        response = InstitutionDetailResponse.from_dict(response_dict)
        self.assertEqual({}, response.unused_fields)
        self.assertEqual({}, response.institution.unused_fields)
        self.assertEqual({}, response.institution.address.unused_fields)
        for field in response.loginForm:
            self.assertEqual({}, field.unused_fields)
