import unittest


SAMPLE_VOI_REPORT_RESPONSE = '''
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


SAMPLE_VOA_REPORT_RESPONSE = '''
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


SAMPLE_REPORTS_RESPONSE = '''
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


class TestReportResponse(unittest.TestCase):
    pass
