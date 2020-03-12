import json
import unittest

from lakey_finicity.models.report.report_summary import ReportSummary
from lakey_finicity.models.report.voi.voi_report import VoiReport

TEST_EXAMPLE_REPORT_SUMMARY_VOI = """
{"id":"4zn3mkdah9pj","portfolioId":"bvhus4usg894-4-port","customerType":"testing","customerId":1002249444,"requestId":"bkx7h7e43g","requesterName":"Purple Leaf Software LLC","createdDate":1583965854,"title":"Finicity Verification of Assets","consumerId":"dfe74fd96d34f68a9c6c19d430093a70","consumerSsn":"6987","constraints":{},"type":"voa","status":"inProgress"}
"""


class TestReportsResponse(unittest.TestCase):

    def test_reports_response(self):
        response_dict = json.loads(TEST_EXAMPLE_REPORT_SUMMARY_VOI)
        report = VoiReport.from_dict(response_dict)
        self.assertEqual({}, report._unused_fields)
        if report.institutions:
            for institution in report.institutions:
                self.assertEqual({}, institution._unused_fields)
                self.assertEqual({}, institution.address._unused_fields)
        if report.constraints:
                self.assertEqual({}, report.constraints._unused_fields)
                for field in report.constraints.reportCustomFields:
                    self.assertEqual({}, field._unused_fields)
