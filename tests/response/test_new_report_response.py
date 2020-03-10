import json
import unittest

from finicity.responses.new_report_response import NewReportResponse

# https://community.finicity.com/s/article/Credit-Decisioning
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


class TestNewReportResponse(unittest.TestCase):

    def test_voi_short(self):
        response_dict = json.loads(EXAMPLE_START_VOI_RESPONSE)
        response = NewReportResponse.from_dict(response_dict)
        self.assertEqual({}, response._unused_fields)
        if response.institutions:
            for institution in response.institutions:
                self.assertEqual({}, institution._unused_fields)
                self.assertEqual({}, institution.address._unused_fields)

    def test_voa_short(self):
        response_dict = json.loads(EXAMPLE_START_VOA_RESPONSE)
        response = NewReportResponse.from_dict(response_dict)
        self.assertEqual({}, response._unused_fields)
        if response.institutions:
            for institution in response.institutions:
                self.assertEqual({}, institution._unused_fields)
                self.assertEqual({}, institution.address._unused_fields)
