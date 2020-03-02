import json
import unittest

from finicity.models import AccountOwner


# https://community.finicity.com/s/article/Get-Account-Owner
EXAMPLE_ACCOUNT_OWNER = '''
{
  "ownerName": "SUZI BUILDER",
  "ownerAddress": "APT C 5600 S SPRINGFIELD GARDENS CIR SPRINGFIELD, VA 22162-1058"
}
'''


class TestAccountOwner(unittest.TestCase):
    def test_account_detail_response(self):
        response_dict = json.loads(EXAMPLE_ACCOUNT_OWNER)
        response = AccountOwner.from_dict(response_dict)
        self.assertEqual({}, response.unused_fields)
