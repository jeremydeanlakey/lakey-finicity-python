import json
import unittest

# https://community.finicity.com/s/article/Credit-Decisioning
from finicity.models.report.voa.voa_report import VoaReport
from finicity.models.report.voi.voi_report import VoiReport
from finicity.responses.new_report_response import NewReportResponse

EXAMPLE_START_VOI_RESPONSE = '''
{
    "id": "bx28qwkdbw3u",
    "requestId": "bmg7d3qrmr",
    "consumerId": "3860718db6febd83c64d9d4c523f39f7",
    "consumerSsn": "5555",
    "constraints": {},
    "type": "voi",
    "status": "inProgress"
}
'''


# https://community.finicity.com/s/article/Credit-Decisioning
EXAMPLE_START_VOA_RESPONSE = '''
{
    "id": "bx28qwkdbw3u",
    "requestId": "bmg7d3qrmr",
    "consumerId": "3860718db6febd83c64d9d4c523f39f7",
    "consumerSsn": "5555",
    "constraints": {},
    "type": "voa",
    "status": "inProgress"
}
'''

EXAMPLE_REPORTS_LIST_RESPONSE = '''
{
    "reports": [
        {
            "id": "0626a292qhnn",
            "consumerId": "c0ac694459519c09e1791010bf98be1f",
            "consumerSsn": "5555",
            "requesterName": "Lender X",
            "constraints": {},
            "type": "voa",
            "status": "success",
            "createdDate": 1549641888,
            "customerId": 0,
            "institutions": []
        },
        {
            "id": "7j93whxju61n",
            "consumerId": "c0ac694459519c09e1791010bf98be1f",
            "consumerSsn": "5555",
            "requesterName": "Lender X",
            "constraints": {},
            "type": "voi",
            "status": "success",
            "createdDate": 1549648084,
            "customerId": 0,
            "institutions": []
        }
    ]
}
'''


# https://community.finicity.com/s/article/VOI-Report
EXAMPLE_VOI_FULL = '''
{
    "id": "hacj9vn105ne-voi",
    "portfolioId": "fsbw2a4mua14-port",
    "title": "Finicity Verification of Income",
    "requestId": "iw7uda67k2",
    "consumerId": "c71122d38433f01f09d24a3ae115aa44",
    "consumerSsn": "1111",
    "requesterName": "Demo",
    "type": "voi",
    "status": "success",
    "createdDate": 1566841014,
    "startDate": 1503769014,
    "endDate": 1566841014,
    "days": 730,
    "seasoned": true,
    "institutions": [
        {
            "id": 5200278,
            "name": "FinBank",
            "urlHomeApp": "http://www.finbank.com",
            "accounts": [
                {
                    "id": 5198056,
                    "ownerName": "JOHN SMITH AND JANE SMITH",
                    "ownerAddress": "1000 N 2222 E OREM, UT 84097",
                    "name": "Super Checking",
                    "number": "5015",
                    "type": "checking",
                    "aggregationStatusCode": 0,
                    "incomeStreams": [
                        {
                            "id": "hacj9vn105ne-voi1",
                            "name": "finicity",
                            "status": "ACTIVE",
                            "estimateInclusion": "MODERATE",
                            "confidence": 59,
                            "cadence": {
                                "startDate": 1504245600,
                                "stopDate": null,
                                "days": 14.0
                            },
                            "netMonthly": [
                                {
                                    "month": 1504245600,
                                    "net": 5915.46
                                },
                                {
                                    "month": 1506837600,
                                    "net": 3856.21
                                },
                                {
                                    "month": 1509516000,
                                    "net": 3856.20
                                },
                                {
                                    "month": 1512111600,
                                    "net": 3951.25
                                }
                            ],
                            "netAnnual": 58578.69,
                            "projectedNetAnnual": 58579,
                            "estimatedGrossAnnual": 78261,
                            "projectedGrossAnnual": 78262,
                            "averageMonthlyIncomeNet": 4881.56,
                            "transactions": [
                                {
                                    "id": 2235561630,
                                    "amount": 2315.21,
                                    "postedDate": 1565935200,
                                    "description": "ACH Deposit Finicity",
                                    "institutionTransactionId": "0000000004",
                                    "category": "Income"
                                },
                                {
                                    "id": 2235561635,
                                    "amount": 2315.22,
                                    "postedDate": 1564725600,
                                    "description": "ACH Deposit Finicity",
                                    "institutionTransactionId": "0000000009",
                                    "category": "Income"
                                }
                            ]
                        }
                    ],
                    "transactions": [],
                    "miscDeposits": []
                }
            ]
        }
    ],
    "income": [
        {
            "confidenceType": "HIGH",
            "netMonthly": [
                {
                    "month": 1519887600,
                    "net": 81.70
                },
                {
                    "month": 1525154400,
                    "net": 32.00
                }
            ],
            "incomeEstimate": {
                "netAnnual": 0,
                "projectedNetAnnual": 0,
                "estimatedGrossAnnual": 0,
                "projectedGrossAnnual": 0
            }
        },
        {
            "confidenceType": "MODERATE",
            "netMonthly": [
                {
                    "month": 1504245600,
                    "net": 5915.46
                },
                {
                    "month": 1506837600,
                    "net": 3856.21
                },
                {
                    "month": 1509516000,
                    "net": 3856.20
                },
                {
                    "month": 1512111600,
                    "net": 3951.25
                }
            ],
            "incomeEstimate": {
                "netAnnual": 58578.69,
                "projectedNetAnnual": 58579,
                "estimatedGrossAnnual": 78261,
                "projectedGrossAnnual": 78262
            }
        }
    ],
    "constraints": {
        "accountIds": [
            "5200278",
            "5200279"
        ],
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
    }

}
'''


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


class TestReport(unittest.TestCase):

    def test_voi_short(self):
        response_dict = json.loads(EXAMPLE_START_VOI_RESPONSE)
        response = NewReportResponse.from_dict(response_dict)
        self.assertEqual({}, response.unused_fields)
        if response.institutions:
            for institution in response.institutions:
                self.assertEqual({}, institution.unused_fields)
                self.assertEqual({}, institution.address.unused_fields)

    def test_voa_short(self):
        response_dict = json.loads(EXAMPLE_START_VOA_RESPONSE)
        response = NewReportResponse.from_dict(response_dict)
        self.assertEqual({}, response.unused_fields)
        if response.institutions:
            for institution in response.institutions:
                self.assertEqual({}, institution.unused_fields)
                self.assertEqual({}, institution.address.unused_fields)

    def test_voi_full(self):
        response_dict = json.loads(EXAMPLE_VOI_FULL)
        response = VoiReport.from_dict(response_dict)
        self.assertEqual({}, response.unused_fields)
        if response.institutions:
            for institution in response.institutions:
                self.assertEqual({}, institution.unused_fields)
                for account in institution.accounts:
                    self.assertEqual({}, account.unused_fields)
                    for transaction in account.transactions:
                        self.assertEqual({}, transaction.unused_fields)
                    for deposit in account.miscDeposits:
                        self.assertEqual({}, deposit.unused_fields)
                    for income in account.incomeStreams:
                        self.assertEqual({}, income.unused_fields)
                        for net in income.netMonthly:
                            self.assertEqual({}, net.unused_fields)
                        for transaction in income.transactions:
                            self.assertEqual({}, transaction.unused_fields)
        if response.constraints:
            self.assertEqual({}, response.constraints.unused_fields)
            for field in response.constraints.reportCustomFields:
                self.assertEqual({}, field.unused_fields)
        for income in response.income:
            self.assertEqual({}, income.unused_fields)
            self.assertEqual({}, income.incomeEstimate.unused_fields)
            for net in income.netMonthly:
                self.assertEqual({}, net.unused_fields)

    def test_voa_full(self):
        response_dict = json.loads(EXAMPLE_VOA_FULL)
        response = VoaReport.from_dict(response_dict)
        self.assertEqual({}, response.unused_fields)
        if response.institutions:
            for institution in response.institutions:
                self.assertEqual({}, institution.unused_fields)
                for account in institution.accounts:
                    self.assertEqual({}, account.unused_fields)
                    for transaction in account.transactions:
                        self.assertEqual({}, transaction.unused_fields)
                    self.assertEqual({}, account.asset.unused_fields)
                    self.assertEqual({}, account.details.unused_fields)
        if response.constraints:
            self.assertEqual({}, response.constraints.unused_fields)
            for field in response.constraints.reportCustomFields:
                self.assertEqual({}, field.unused_fields)
