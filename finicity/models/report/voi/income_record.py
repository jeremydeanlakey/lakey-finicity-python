from dataclasses import dataclass
from typing import List

from finicity.models.report.voi.confidence_type import ConfidenceType
from finicity.models.report.voi.income_estimate import IncomeEstimate
from finicity.models.report.voi.net_monthly import NetMonthly


@dataclass
class IncomeRecord(object):
    unused_fields: dict  # this is for forward compatibility and should be empty
    confidenceType: ConfidenceType  # Level of confidence of income stream (low, moderate, high)
    netMonthly: List[NetMonthly]  # A list of net monthly records. One instance for each complete calendar month in the report
    incomeEstimate: IncomeEstimate

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        confidenceType_str = data.pop('confidenceType')
        confidenceType = ConfidenceType.from_description(confidenceType_str)
        netMonthly_raw = data.pop('netMonthly')
        netMonthly = [NetMonthly.from_dict(d) for d in netMonthly_raw]
        incomeEstimate_raw = data.pop('incomeEstimate')
        incomeEstimate = IncomeEstimate.from_dict(incomeEstimate_raw)
        return IncomeRecord(
            confidenceType=confidenceType,
            netMonthly=netMonthly,
            incomeEstimate=incomeEstimate,
            unused_fields=data,
        )
