from dataclasses import dataclass


@dataclass
class IncomeEstimate(object):
    unused_fields: dict  # this is for forward compatibility and should be empty
    netAnnual: float  # Sum of all values in netMonthlyIncome over the previous 12 months
    projectedNetAnnual: float  # Projected net income over the next 12 months, across all income streams, based on netAnnualIncome
    estimatedGrossAnnual: float  # Before-tax gross annual income (estimated from netAnnual) across all income stream in the past 12 months
    projectedGrossAnnual: float  # Projected gross income over the next 12 months, across all active income streams, based on projectedNetAnnual

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        netAnnual = data.pop('netAnnual')
        projectedNetAnnual = data.pop('projectedNetAnnual')
        estimatedGrossAnnual = data.pop('estimatedGrossAnnual')
        projectedGrossAnnual = data.pop('projectedGrossAnnual')
        return IncomeEstimate(
            netAnnual=netAnnual,
            projectedNetAnnual=projectedNetAnnual,
            estimatedGrossAnnual=estimatedGrossAnnual,
            projectedGrossAnnual=projectedGrossAnnual,
            unused_fields=data,
        )
