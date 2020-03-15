from dataclasses import dataclass
from typing import List, Optional

from lakey_finicity.models.report.cadence import Cadence
from lakey_finicity.models.report.income_stream_transaction_record import IncomeStreamTransactionRecord
from lakey_finicity.models.report.voi.confidence_type import ConfidenceType
from lakey_finicity.models.report.voi.income_stream_status import IncomeStreamStatus
from lakey_finicity.models.report.voi.net_monthly import NetMonthly


@dataclass
class IncomeStreamRecord(object):
    _unused_fields: dict  # this is for forward compatibility and should be empty
    id: str  # Finicity’s income stream ID
    name: Optional[str]  # A human-readable name based on the normalizedPayee name of the transactions for this income stream
    status: Optional[IncomeStreamStatus]  # active or inactive (“active” means that the most-recent deposit occurred as expected by the cadence and the next expected date is still in the future.)
    estimateInclusion: Optional[ConfidenceType]  # Level of confidence of income stream (low, moderate, high)
    confidence: Optional[int]  # Level of confidence that the deposit stream represents income (example: 85%)
    cadence: Optional[Cadence]  # The chronological rhythm discovered for this set of deposits
    netMonthly: List[NetMonthly]  # A list of net monthly records. One instance for each complete calendar month in the report
    netAnnual: Optional[float]  # Sum of all values in netMonthlyIncome over the previous 12 months
    projectedNetAnnual: Optional[float]  # Projected net income over the next 12 months, across all income streams, based on netAnnualIncome
    estimatedGrossAnnual: Optional[float]  # Before-tax gross annual income (estimated from netAnnual) across all income stream in the past 12 months
    projectedGrossAnnual: Optional[float]  # Projected gross income over the next 12 months, across all active income streams, based on projectedNetAnnual
    averageMonthlyIncomeNet: Optional[float]  # Monthly average amount over the previous 24 months
    transactions: List[IncomeStreamTransactionRecord]  # A list of transaction records

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        name = data.pop('name', None)
        status_str = data.pop('status', None)
        status = IncomeStreamStatus.from_description(status_str) if status_str else None
        estimateInclusion_str = data.pop('estimateInclusion', None)
        estimateInclusion = ConfidenceType.from_description(estimateInclusion_str) if estimateInclusion_str else None
        confidence = data.pop('confidence', None)
        cadence_raw = data.pop('cadence', None)
        cadence = Cadence.from_dict(cadence_raw) if cadence_raw else None
        netMonthly_raw = data.pop('netMonthly', None)
        netMonthly = [NetMonthly.from_dict(d) for d in netMonthly_raw] if netMonthly_raw else []
        netAnnual = data.pop('netAnnual', None)
        projectedNetAnnual = data.pop('projectedNetAnnual', None)
        estimatedGrossAnnual = data.pop('estimatedGrossAnnual', None)
        projectedGrossAnnual = data.pop('projectedGrossAnnual', None)
        averageMonthlyIncomeNet = data.pop('averageMonthlyIncomeNet', None)
        transactions_raw = data.pop('transactions', None)
        transactions = [IncomeStreamTransactionRecord.from_dict(d) for d in transactions_raw] if transactions_raw else []
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
            _unused_fields=data,
        )
