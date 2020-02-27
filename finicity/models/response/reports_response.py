from dataclasses import dataclass
from typing import List

from finicity.models.response.report_summary import ReportSummary


@dataclass
class ReportsResponse(object):
    reports: List[ReportSummary]
    unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        reports_raw = data.pop('reports')
        reports = [ReportSummary.from_dict(d) for d in reports_raw]
        return ReportsResponse(
            reports=reports,
            unused_fields=data,
        )
