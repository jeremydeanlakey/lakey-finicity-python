import json
import unittest

from finicity.responses.reports_response import ReportsResponse


# https://community.finicity.com/s/article/Credit-Decisioning
DOCS_EXAMPLE_REPORTS_RESPONSE = '''
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


class TestReportsResponse(unittest.TestCase):

    def test_reports_response(self):
        response_dict = json.loads(DOCS_EXAMPLE_REPORTS_RESPONSE)
        response = ReportsResponse.from_dict(response_dict)
        self.assertEqual({}, response._unused_fields)
        if response.reports:
            for report in response.reports:
                self.assertEqual({}, report._unused_fields)
                if report.institutions:
                    for institution in response.institutions:
                        self.assertEqual({}, institution._unused_fields)
                        self.assertEqual({}, institution.address._unused_fields)
                if report.constraints:
                        self.assertEqual({}, report.constraints._unused_fields)
                        for field in report.constraints.reportCustomFields:
                            self.assertEqual({}, field._unused_fields)
