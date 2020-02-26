from dataclasses import dataclass
from typing import List, Any, Optional

from finicity.models.report.report_status import ReportStatus
from finicity.models.report.report_type import ReportType


@dataclass
class Report(object):
    id: str  # ID of the report (UUID with max length 32 characters)
    requestId: str  # unique requestId for this specific call request
    consumerId: str  # ID of the consumer (UUID with max length 32 characters)
    consumerSsn: str  # Last 4 digits of the report consumer's Social Security number
    type: ReportType  # voa or voi
    constraints: List[str]  # specifies use of accountIds included in the call
    status: ReportStatus  # inProgress or success or failure
    unused_fields: dict  # this is for forward compatibility and should be empty
    institutions: Optional[List[Any]]

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        requestId = data.pop('requestId')
        consumerId = data.pop('consumerId')
        consumerSsn = data.pop('consumerSsn')
        type = data.pop('type')
        constraints = data.pop('constraints')
        status = data.pop('status')
        institutions = data.pop('institutions', None)
        return Report(
            id=id,
            requestId=requestId,
            consumerId=consumerId,
            consumerSsn=consumerSsn,
            type=type,
            constraints=constraints,
            status=status,
            institutions=institutions,
            unused_fields=data,
        )
