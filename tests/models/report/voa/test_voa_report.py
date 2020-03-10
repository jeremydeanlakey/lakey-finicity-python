import json
import unittest

from finicity.models.report.voa.voa_report import VoaReport


# https://community.finicity.com/s/article/VOA-Report
EXAMPLE_VOA_FULL = '''
{
    "id": "9b8mknp9xdtm",
    "portfolioId": "psbw2a4mua14-port",
    "requestId": "0hk8wy054k",
    "title": "Finicity Verification of Assets",
    "consumerId": "c71122d38433f01f09d24a3ae115aa44",
    "consumerSsn": "1111",
    "requesterName": "Demo",
"constraints": {
"accountIds": [
"5200278"
],
"fromDate": 1566836008,
"reportCustomFields": [
{
"label": "loanID",
"value": "12345",
"shown": true
},
{
"label": "trackingID",
"value": "5555",
"shown": true
},
{
"label": "vendorID",
"value": "1613aa23",
"shown": true
}
]
},
    "type": "voa",
    "status": "success",
    "createdDate": 1566839649,
    "startDate": 1551204849,
    "endDate": 1566839649,
    "days": 180,
    "seasoned": false,
    "institutions": [
        {
            "id": 102105,
            "name": "FinBank",
            "accounts": [
                {
                    "id": 5200278,
                    "number": "5015",
                    "ownerName": "JOHN SMITH AND JANE SMITH",
                    "ownerAddress": "1000 N 2222 E OREM, UT 84097",
                    "name": "Super Checking",
                    "type": "checking",
                    "aggregationStatusCode": 0,
                    "balance": 1000,
                    "balanceDate": 1566799200,
                    "averageMonthlyBalance": -7971.93,
                    "transactions": [
                        {
                            "id": 2235561626,
                            "amount": -32.00,
                            "postedDate": 1566194400,
                            "description": "MAVERIK #435",
                            "normalizedPayee": "Maverik",
                            "bestRepresentation": "MAVERIK",
                            "institutionTransactionId": "0000000000",
                            "category": "Gas & Fuel"
                        }

                    ],
                    "asset": {
                        "type": "checking",
                        "currentBalance": 1000,
                        "availableBalance": 1000,
                        "twoMonthAverage": -2002.73,
                        "sixMonthAverage": -7916.89,
                        "beginningBalance": -17901.94
                    },
                    "details": {
                        "interestMarginBalance": null,
                        "availableCashBalance": null,
                        "vestedBalance": null,
                        "currentLoanBalance": null,
                        "availableBalanceAmount": null
                    }
                }
            ]
        }
    ],
    "assets": {
        "currentBalance": 1000,
        "availableBalance": 1000.00,
        "twoMonthAverage": -2002.73,
        "sixMonthAverage": -7916.89,
        "beginningBalance": -17901.94
    }
}
'''


class TestVoaReport(unittest.TestCase):

    def test_voa_full(self):
        response_dict = json.loads(EXAMPLE_VOA_FULL)
        response = VoaReport.from_dict(response_dict)
        self.assertEqual({}, response._unused_fields)
        if response.institutions:
            for institution in response.institutions:
                self.assertEqual({}, institution._unused_fields)
                for account in institution.accounts:
                    self.assertEqual({}, account._unused_fields)
                    for transaction in account.transactions:
                        self.assertEqual({}, transaction._unused_fields)
                    self.assertEqual({}, account.asset._unused_fields)
                    self.assertEqual({}, account.details._unused_fields)
        if response.constraints:
            self.assertEqual({}, response.constraints._unused_fields)
            for field in response.constraints.reportCustomFields:
                self.assertEqual({}, field._unused_fields)
