from dataclasses import dataclass
from typing import Optional


@dataclass
class IncomeStreamTransactionRecord(object):
    _unused_fields: dict  # this is for forward compatibility and should be empty
    id: int  # Finicity transaction ID
    amount: float  # The total amount of this transactions. Transactions for deposits are positive values; withdrawals and debits are negative values.
    postedDate: Optional[int]  # A timestamp showing when the transaction was posted or cleared by the institution
    description: Optional[str]  # The description of the transaction, as provided by the institution (often known as payee)
    institutionTransactionId: Optional[str]  # A unique ID of the transaction, as provided by the institution (often known as FITID)
    category: Optional[str]  # The assigned category for this transaction

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        amount = data.pop('amount')
        postedDate = data.pop('postedDate', None)
        description = data.pop('description', None)
        institutionTransactionId = data.pop('institutionTransactionId', None)
        category = data.pop('category', None)
        return IncomeStreamTransactionRecord(
            id=id,
            amount=amount,
            postedDate=postedDate,
            description=description,
            institutionTransactionId=institutionTransactionId,
            category=category,
            _unused_fields=data,
        )
