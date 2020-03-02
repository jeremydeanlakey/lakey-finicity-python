import json
import unittest


# https://community.finicity.com/s/article/202460265-Institutions#loginfield_record
from finicity.responses.institution_login_form_response import InstitutionLoginFormResponse

EXAMPLE_LOGIN_FORM_RESPONSE = '''
{
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


class TestReportResponse(unittest.TestCase):

    def test_voi_short(self):
        response_dict = json.loads(EXAMPLE_LOGIN_FORM_RESPONSE)
        response = InstitutionLoginFormResponse.from_dict(response_dict)
        self.assertEqual({}, response.unused_fields)
        for field in response.loginForm:
            self.assertEqual({}, field.unused_fields)
