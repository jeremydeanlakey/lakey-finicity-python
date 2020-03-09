import json
import unittest

from finicity.responses.institution_detail_response import InstitutionDetailResponse


EXAMPLE_INSTITUTION_DETAILS = '''
{
"institution":{
"id":15436,
"name":"Mass Mutual Financial Group(Retirement Access)",
"aha":false,
"accountTypeDescription":"Workplace Retirement",
"phone":"1-866-630-5295",
"urlHomeApp":"https://www.massmutual.com/",
"urlLogonApp":"https://retirementsolutions.financialtrans.com/tf/myPLAN/Welcome?cz=d07001719051417031511001318",
"oauthEnabled":false,
"urlForgotPassword":"",
"urlOnlineRegistration":"",
"class":"retirement",
"specialText":"Please enter your Mass Mutual Financial Group (Retirement Access) Email Address and Password required for login.",
"address":{
"city":"Atlanta",
"state":"GA",
"country":"USA",
"postalCode":"30357-2566",
"addressLine1":"Post Office Box 78566",
"addressLine2":""
},
"currency":"USD",
"email":"https://www.amsouthdailyelect.com/contact.asp",
"oauthInstitutionId":null
}
}
'''


class TestInstitutionDetailsResponse(unittest.TestCase):
    def test_institution_detail_response(self):
        response_dict = json.loads(EXAMPLE_INSTITUTION_DETAILS)
        response = InstitutionDetailResponse.from_dict(response_dict)
        self.assertEqual({}, response._unused_fields)
        self.assertEqual({}, response.institution._unused_fields)
        self.assertEqual({}, response.institution.address._unused_fields)
