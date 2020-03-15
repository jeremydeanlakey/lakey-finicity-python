from dataclasses import dataclass
from typing import List, Optional

from lakey_finicity.models.report.voi.confidence_type import ConfidenceType
from lakey_finicity.models.report.voi.income_estimate import IncomeEstimate
from lakey_finicity.models.report.voi.net_monthly import NetMonthly


@dataclass
class IncomeRecord(object):
    _unused_fields: dict  # this is for forward compatibility and should be empty
    confidenceType: Optional[ConfidenceType]  # Level of confidence of income stream (low, moderate, high)
    netMonthly: List[NetMonthly]  # A list of net monthly records. One instance for each complete calendar month in the report
    incomeEstimate: Optional[IncomeEstimate]

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        confidenceType_str = data.pop('confidenceType', None)
        confidenceType = ConfidenceType.from_description(confidenceType_str) if confidenceType_str else None
        netMonthly_raw = data.pop('netMonthly', None)
        netMonthly = [NetMonthly.from_dict(d) for d in netMonthly_raw] if netMonthly_raw else []
        incomeEstimate_raw = data.pop('incomeEstimate', None)
        incomeEstimate = IncomeEstimate.from_dict(incomeEstimate_raw) if incomeEstimate_raw else None
        return IncomeRecord(
            confidenceType=confidenceType,
            netMonthly=netMonthly,
            incomeEstimate=incomeEstimate,
            _unused_fields=data,
        )
