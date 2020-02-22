import enum
from dataclasses import dataclass


# https://community.finicity.com/s/article/Credit-Decisioning#generate_voi_report
from typing import List, Any


class ReportType(enum.Enum):
    voa = "voa"  # Verification of Assets
    voi = "voi"  # Verification of Income


# https://community.finicity.com/s/article/Credit-Decisioning#generate_voi_report
class ReportStatus(enum.Enum):
    inProgress = "inProgress"
    success = "success"
    failure = "failure"


@dataclass
class ReportResponse(object):
    id: str  # ID of the report (UUID with max length 32 characters)
    requestId: str  # unique requestId for this specific call request
    consumerId: str  # ID of the consumer (UUID with max length 32 characters)
    consumerSsn: str  # Last 4 digits of the report consumer's Social Security number
    type: ReportType  # voa or voi
    constraints: List[str]  # specifies use of accountIds included in the call
    status: ReportStatus  # inProgress or success or failure


@dataclass
class VoaReportResponse(ReportResponse):
    pass


@dataclass
class VoiReportResponse(ReportResponse):
    institutions: List[Any]  # empty array


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
