from dataclasses import dataclass
from typing import List, Optional

from finicity.models.report.report_constraints import ReportConstraints
from finicity.models.report.report_status import ReportStatus
from finicity.models.report.report_type import ReportType
from finicity.models.report.voi.voi_institution_record import VoiInstitutionRecord


@dataclass
class ReportSummary(object):
    id: str  # ID of the report (UUID with max length 32 characters).
    consumerId: str  # ID of the consumer (UUID with max length 32 characters)
    consumerSsn: str  # Last 4 digits of the report consumer's Social Security number
    requesterName: str  # Finicity account name that the report was generated under (only included when report status is "successful")
    constraints: Optional[ReportConstraints]  # specifies use of a fromDate or accountIds included in the report generation
    type: ReportType  # voa or voi
    status: ReportStatus  # inProgress or success or failure
    createdDate: int  # The date the report was generated
    customerId: str  # set to 0
    institutions: Optional[List[VoiInstitutionRecord]]  # empty array
    _unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        consumerId = data.pop('consumerId')
        consumerSsn = data.pop('consumerSsn')
        type = data.pop('type')
        constraints_raw = data.pop('constraints')
        requesterName = data.pop('requesterName')
        constraints = ReportConstraints.from_dict(constraints_raw) if constraints_raw else None
        status = data.pop('status')
        createdDate = data.pop('createdDate')
        customerId = data.pop('customerId')
        institutions_raw = data.pop('institutions', None)
        institutions = [VoiInstitutionRecord.from_dict(d) for d in institutions_raw] if institutions_raw else None
        return ReportSummary(
            id=id,
            consumerId=consumerId,
            consumerSsn=consumerSsn,
            requesterName=requesterName,
            constraints=constraints,
            type=type,
            status=status,
            createdDate=createdDate,
            customerId=customerId,
            institutions=institutions,
            _unused_fields=data,
        )
