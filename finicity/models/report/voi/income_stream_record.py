from dataclasses import dataclass
from typing import List

from finicity.models.report.cadence import Cadence
from finicity.models.report.income_stream_transaction_record import IncomeStreamTransactionRecord
from finicity.models.report.voi.confidence_type import ConfidenceType
from finicity.models.report.voi.income_stream_status import IncomeStreamStatus
from finicity.models.report.voi.net_monthly import NetMonthly


@dataclass
class IncomeStreamRecord(object):
    unused_fields: dict  # this is for forward compatibility and should be empty
    id: str  # Finicity’s income stream ID
    name: str  # A human-readable name based on the normalizedPayee name of the transactions for this income stream
    status: IncomeStreamStatus  # active or inactive (“active” means that the most-recent deposit occurred as expected by the cadence and the next expected date is still in the future.)
    estimateInclusion: ConfidenceType  # Level of confidence of income stream (low, moderate, high)
    confidence: int  # Level of confidence that the deposit stream represents income (example: 85%)
    cadence: Cadence  # The chronological rhythm discovered for this set of deposits
    netMonthly: List[NetMonthly]  # A list of net monthly records. One instance for each complete calendar month in the report
    netAnnual: float  # Sum of all values in netMonthlyIncome over the previous 12 months
    projectedNetAnnual: float  # Projected net income over the next 12 months, across all income streams, based on netAnnualIncome
    estimatedGrossAnnual: float  # Before-tax gross annual income (estimated from netAnnual) across all income stream in the past 12 months
    projectedGrossAnnual: float  # Projected gross income over the next 12 months, across all active income streams, based on projectedNetAnnual
    averageMonthlyIncomeNet: float  # Monthly average amount over the previous 24 months
    transactions: List[IncomeStreamTransactionRecord]  # A list of transaction records

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        name = data.pop('name')
        status_str = data.pop('status')
        status = IncomeStreamStatus.from_description(status_str)
        estimateInclusion_str = data.pop('estimateInclusion')
        estimateInclusion = ConfidenceType.from_description(estimateInclusion_str)
        confidence = data.pop('confidence')
        cadence_raw = data.pop('cadence')
        cadence = Cadence.from_dict(cadence_raw)
        netMonthly_raw = data.pop('netMonthly')
        netMonthly = [NetMonthly.from_dict(d) for d in netMonthly_raw]
        netAnnual = data.pop('netAnnual')
        projectedNetAnnual = data.pop('projectedNetAnnual')
        estimatedGrossAnnual = data.pop('estimatedGrossAnnual')
        projectedGrossAnnual = data.pop('projectedGrossAnnual')
        averageMonthlyIncomeNet = data.pop('averageMonthlyIncomeNet')
        transactions_raw = data.pop('transactions')
        transactions = [IncomeStreamTransactionRecord.from_dict(d) for d in transactions_raw]
        return IncomeStreamRecord(
            id=id,
            name=name,
            status=status,
            estimateInclusion=estimateInclusion,
            confidence=confidence,
            cadence=cadence,
            netMonthly=netMonthly,
            netAnnual=netAnnual,
            projectedNetAnnual=projectedNetAnnual,
            estimatedGrossAnnual=estimatedGrossAnnual,
            projectedGrossAnnual=projectedGrossAnnual,
            averageMonthlyIncomeNet=averageMonthlyIncomeNet,
            transactions=transactions,
            unused_fields=data,
        )
