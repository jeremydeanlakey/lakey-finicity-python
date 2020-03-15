from dataclasses import dataclass
from typing import List, Optional

from lakey_finicity.models.report.report_constraints import ReportConstraints
from lakey_finicity.models.report.report_status import ReportStatus
from lakey_finicity.models.report.report_type import ReportType
from lakey_finicity.models.report.voa.asset_record import AssetRecord
from lakey_finicity.models.report.voa.voa_institution_record import VoaInstitutionRecord


@dataclass
class VoaReport(object):
    id: str  # ID of the report (UUID with max length 32 characters).  VOI report ID will have “-voi” appended to the end of it to denote the report type.
    portfolioId: Optional[str]
    requestId: str  # unique requestId for this specific call request
    title: Optional[str]
    consumerId: Optional[str]  # ID of the consumer (UUID with max length 32 characters)
    consumerSsn: Optional[str]  # Last 4 digits of the report consumer's Social Security number
    requesterName: Optional[str]
    constraints: Optional[ReportConstraints]
    type: Optional[ReportType]  # voa or voi
    status: Optional[ReportStatus]  # inProgress or success or failure
    createdDate: Optional[int]
    startDate: Optional[int]
    endDate: Optional[int]
    days: Optional[int]
    seasoned: Optional[bool]
    institutions: Optional[List[VoaInstitutionRecord]]
    assets: Optional[AssetRecord]
    _unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        requestId = data.pop('requestId')
        portfolioId = data.pop('portfolioId', None)
        title = data.pop('title', None)
        consumerId = data.pop('consumerId', None)
        consumerSsn = data.pop('consumerSsn', None)
        type_str = data.pop('type', None)
        type = ReportType(type_str) if type_str else None
        constraints_raw = data.pop('constraints', None)
        requesterName = data.pop('requesterName', None)
        constraints = ReportConstraints.from_dict(constraints_raw) if constraints_raw else None
        status_str = data.pop('status', None)
        status = ReportStatus(status_str) if status_str else None
        createdDate = data.pop('createdDate', None)
        startDate = data.pop('startDate', None)
        endDate = data.pop('endDate', None)
        days = data.pop('days', None)
        seasoned = data.pop('seasoned', None)
        institutions_raw = data.pop('institutions', None)
        institutions = [VoaInstitutionRecord.from_dict(d) for d in institutions_raw] if institutions_raw else None
        assets_raw = data.pop('assets', None)
        assets = AssetRecord.from_dict(assets_raw) if assets_raw else None
        return VoaReport(
            id=id,
            portfolioId=portfolioId,
            requestId=requestId,
            title=title,
            consumerId=consumerId,
            consumerSsn=consumerSsn,
            requesterName=requesterName,
            constraints=constraints,
            type=type,
            status=status,
            createdDate=createdDate,
            startDate=startDate,
            endDate=endDate,
            days=days,
            seasoned=seasoned,
            institutions=institutions,
            assets=assets,
            _unused_fields=data,
        )
