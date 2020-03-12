from dataclasses import dataclass
from typing import List, Optional

from lakey_finicity.models.report.report_custom_field import ReportCustomField


# https://community.finicity.com/s/article/VOA-Report
@dataclass
class ReportConstraints(object):
    _unused_fields: dict  # this is for forward compatibility and should be empty
    accountIds: Optional[List[str]]
    fromDate: Optional[int]
    reportCustomFields: Optional[List[ReportCustomField]]

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        accountIds = data.pop("accountIds", None)
        fromDate = data.pop("fromDate", None)
        reportCustomFields_raw = data.pop("reportCustomFields", None)
        reportCustomFields = [ReportCustomField.from_dict(d) for d in reportCustomFields_raw] if reportCustomFields_raw else None
        return ReportConstraints(
            accountIds=accountIds,
            fromDate=fromDate,
            reportCustomFields=reportCustomFields,
            _unused_fields=data,
        )
