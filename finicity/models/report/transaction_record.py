from dataclasses import dataclass
from typing import Optional

from finicity.models import TransactionType


@dataclass
class TransactionRecord(object):
    unused_fields: dict  # this is for forward compatibility and should be empty
    id: int  # Finicity transaction ID
    amount: float  # The total amount of this transactions. Transactions for deposits are positive values; withdrawals and debits are negative values.
    postedDate: int  # A timestamp showing when the transaction was posted or cleared by the institution
    description: str  # The description of the transaction, as provided by the institution (often known as payee)
    memo: str  # The memo field of the transaction, as provided by the institution
    normalizedPayee: str  # A cleaned-up, standardized version of the description
    bestRepresentation: Optional[str]
    institutionTransactionId: str  # A unique ID of the transaction, as provided by the institution (often known as FITID)
    category: str  # The assigned category for this transaction
    securityType: Optional[str]  # The type of investment security, only on voa reports
    symbol: Optional[str]  # Investment symbol, only on voa reports
    type: TransactionType  # One of the values from Transaction Types (optional)

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        amount = data.pop('amount')
        postedDate = data.pop('postedDate')
        description = data.pop('description')
        memo = data.pop('memo')
        bestRepresentation = data.pop('bestRepresentation', None)
        normalizedPayee = data.pop('normalizedPayee')
        institutionTransactionId = data.pop('institutionTransactionId')
        category = data.pop('category')
        type_str = data.pop('type')
        type = TransactionType.from_description(type_str) if type_str else None
        securityType = data.pop('securityType', None)
        symbol = data.pop('symbol', None)
        return TransactionRecord(
            id=id,
            amount=amount,
            postedDate=postedDate,
            description=description,
            memo=memo,
            bestRepresentation=bestRepresentation,
            normalizedPayee=normalizedPayee,
            institutionTransactionId=institutionTransactionId,
            category=category,
            type=type,
            securityType=securityType,
            symbol=symbol,
            unused_fields=data,
        )
