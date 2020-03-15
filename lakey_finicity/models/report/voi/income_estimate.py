from dataclasses import dataclass
from typing import Optional


@dataclass
class IncomeEstimate(object):
    _unused_fields: dict  # this is for forward compatibility and should be empty
    netAnnual: Optional[float]  # Sum of all values in netMonthlyIncome over the previous 12 months
    projectedNetAnnual: Optional[float]  # Projected net income over the next 12 months, across all income streams, based on netAnnualIncome
    estimatedGrossAnnual: Optional[float]  # Before-tax gross annual income (estimated from netAnnual) across all income stream in the past 12 months
    projectedGrossAnnual: Optional[float]  # Projected gross income over the next 12 months, across all active income streams, based on projectedNetAnnual

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        netAnnual = data.pop('netAnnual', None)
        projectedNetAnnual = data.pop('projectedNetAnnual', None)
        estimatedGrossAnnual = data.pop('estimatedGrossAnnual', None)
        projectedGrossAnnual = data.pop('projectedGrossAnnual', None)
        return IncomeEstimate(
            netAnnual=netAnnual,
            projectedNetAnnual=projectedNetAnnual,
            estimatedGrossAnnual=estimatedGrossAnnual,
            projectedGrossAnnual=projectedGrossAnnual,
            _unused_fields=data,
        )
