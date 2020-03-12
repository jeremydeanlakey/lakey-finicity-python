import json
import unittest

from lakey_finicity.models.report.voi.voi_report import VoiReport


# https://community.finicity.com/s/article/VOI-Report
DOCS_EXAMPLE_VOI_FULL = '''
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
                            "name": "lakey_finicity",
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


class TestVoiReport(unittest.TestCase):

    def test_voi_full(self):
        response_dict = json.loads(DOCS_EXAMPLE_VOI_FULL)
        response = VoiReport.from_dict(response_dict)
        self.assertEqual({}, response._unused_fields)
        if response.institutions:
            for institution in response.institutions:
                self.assertEqual({}, institution._unused_fields)
                for account in institution.accounts:
                    self.assertEqual({}, account._unused_fields)
                    for transaction in account.transactions:
                        self.assertEqual({}, transaction._unused_fields)
                    if account.miscDeposits:
                        for deposit in account.miscDeposits:
                            self.assertEqual({}, deposit._unused_fields)
                    for income in account.incomeStreams:
                        self.assertEqual({}, income._unused_fields)
                        for net in income.netMonthly:
                            self.assertEqual({}, net._unused_fields)
                        for transaction in income.transactions:
                            self.assertEqual({}, transaction._unused_fields)
        if response.constraints:
            self.assertEqual({}, response.constraints._unused_fields)
            for field in response.constraints.reportCustomFields:
                self.assertEqual({}, field._unused_fields)
        for income in response.income:
            self.assertEqual({}, income._unused_fields)
            self.assertEqual({}, income.incomeEstimate._unused_fields)
            for net in income.netMonthly:
                self.assertEqual({}, net._unused_fields)
