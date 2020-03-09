from dataclasses import dataclass
from typing import Optional

from finicity.models import TransactionType


# https://community.finicity.com/s/article/VOI-Report
@dataclass
class MiscellaneousDepositRecord(object):
    _unused_fields: dict  # this is for forward compatibility and should be empty
    id: str  # Finicity transaction ID
    amount: float  # The total amount of this transactions. Transactions for deposits are positive values; withdrawals and debits are negative values.
    postedDate: int  # A timestamp showing when the transaction was posted or cleared by the institution
    description: str  # The description of the transaction, as provided by the institution (often known as payee)
    memo: str  # The memo field of the transaction, as provided by the institution
    normalizedPayee: str  # A cleaned-up, standardized version of the description
    institutionTransactionId: str  # A unique ID of the transaction, as provided by the institution (often known as FITID)
    category: str  # The assigned category for this transaction
    bestRepresentation: str  # An enhanced representation of the normalized payee.
    type: Optional[TransactionType]  # One of the values from Transaction Types (optional)

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        amount = data.pop('amount')
        postedDate = data.pop('postedDate')
        description = data.pop('description')
        memo = data.pop('memo')
        normalizedPayee = data.pop('normalizedPayee')
        institutionTransactionId = data.pop('institutionTransactionId')
        category = data.pop('category')
        bestRepresentation = data.pop('bestRepresentation')
        type_str = data.pop('type', None)
        type = TransactionType.from_description(type_str) if type_str else None
        return MiscellaneousDepositRecord(
            id=id,
            amount=amount,
            postedDate=postedDate,
            description=description,
            memo=memo,
            normalizedPayee=normalizedPayee,
            institutionTransactionId=institutionTransactionId,
            category=category,
            bestRepresentation=bestRepresentation,
            type=type,
            _unused_fields=data,
        )
