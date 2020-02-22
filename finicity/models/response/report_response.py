from dataclasses import dataclass
from typing import List, Any

from finicity.models.report.report_status import ReportStatus
from finicity.models.report.report_type import ReportType


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
