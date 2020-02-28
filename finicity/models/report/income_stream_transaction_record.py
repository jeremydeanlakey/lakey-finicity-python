from dataclasses import dataclass


@dataclass
class IncomeStreamTransactionRecord(object):
    unused_fields: dict  # this is for forward compatibility and should be empty
    id: int  # Finicity transaction ID
    amount: float  # The total amount of this transactions. Transactions for deposits are positive values; withdrawals and debits are negative values.
    postedDate: int  # A timestamp showing when the transaction was posted or cleared by the institution
    description: str  # The description of the transaction, as provided by the institution (often known as payee)
    institutionTransactionId: str  # A unique ID of the transaction, as provided by the institution (often known as FITID)
    category: str  # The assigned category for this transaction

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        amount = data.pop('amount')
        postedDate = data.pop('postedDate')
        description = data.pop('description')
        institutionTransactionId = data.pop('institutionTransactionId')
        category = data.pop('category')
        return IncomeStreamTransactionRecord(
            id=id,
            amount=amount,
            postedDate=postedDate,
            description=description,
            institutionTransactionId=institutionTransactionId,
            category=category,
            unused_fields=data,
        )
