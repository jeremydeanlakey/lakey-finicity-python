from dataclasses import dataclass
from typing import List, Optional

from finicity.models.report.report_constraints import ReportConstraints
from finicity.models.report.report_status import ReportStatus
from finicity.models.report.report_type import ReportType
from finicity.models.report.voi.voi_institution_record import VoiInstitutionRecord


@dataclass
class NewReportResponse(object):
    id: str  # ID of the report (UUID with max length 32 characters).
    requestId: str  # unique requestId for this specific call request
    consumerId: str  # ID of the consumer (UUID with max length 32 characters)
    consumerSsn: str  # Last 4 digits of the report consumer's Social Security number
    type: ReportType  # voa or voi
    constraints: Optional[ReportConstraints]  # specifies use of accountIds included in the call
    status: ReportStatus  # inProgress or success or failure
    institutions: Optional[List[VoiInstitutionRecord]]
    _unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        requestId = data.pop('requestId')
        consumerId = data.pop('consumerId')
        consumerSsn = data.pop('consumerSsn')
        type = data.pop('type')
        constraints_raw = data.pop('constraints')
        constraints = ReportConstraints.from_dict(constraints_raw) if constraints_raw else None
        status = data.pop('status')
        institutions_raw = data.pop('institutions', None)
        institutions = [VoiInstitutionRecord.from_dict(d) for d in institutions_raw] if institutions_raw else None
        return NewReportResponse(
            id=id,
            consumerId=consumerId,
            consumerSsn=consumerSsn,
            requestId=requestId,
            constraints=constraints,
            type=type,
            status=status,
            institutions=institutions,
            _unused_fields=data,
        )
