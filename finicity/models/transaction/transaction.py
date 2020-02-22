from dataclasses import dataclass
from typing import Optional

from finicity.models.transaction.transaction_categorization import TransactionCategorization
from finicity.models.transaction.transaction_status import TransactionStatus
from finicity.models.transaction.transaction_type import TransactionType


# https://community.finicity.com/s/article/202460245-Transactions
@dataclass
class Transaction(object):
    accountId: int
    amount: float  # The total amount of the transaction. Transactions for deposits are positive values, withdrawals and debits are negative values.
    createdDate: int  # A timestamp showing when the transaction was added to the Finicity system. (See Handling Dates and Times.) This value usually is not interesting outside of Finicity.
    customerId: int  # The Finicity ID of the customer associated with this transaction
    description: str  # The description of the transaction, as provided by the institution (often known as payee). In the event that this field is left blank by the institution, Finicity will pass a value of "[No description provided by institution]". All other values are provided by the institution.
    id: int  # The Finicity ID of the account associated with this transaction
    postedDate: int  # A timestamp showing when the transaction was posted or cleared by the institution (see Handling Dates and Times)
    status: TransactionStatus
    bonusAmount: Optional[float]  # The portion of the transaction allocated to bonus, if available
    checkNum: Optional[str]  # The check number of the transaction, as provided by the institution
    escrowAmount: Optional[float]  # The portion of the transaction allocated to escrow, if available
    feeAmount: Optional[float]  # The portion of the transaction allocated to fee, if available
    interestAmount: Optional[float]  # The portion of the transaction allocated to interest, if available
    memo: Optional[str]  # The memo field of the transaction, as provided by the institution. The institution must provide either a description, a memo, or both. It is recommended to concatenate the two fields into a single value
    principalAmount: Optional[float]  # The portion of the transaction allocated to principal, if available
    # subaccount:   # deprecated  https://community.finicity.com/s/article/210507963-Release-Notes-November-2016
    transactionDate: Optional[int]  # An optional timestamp showing when the transaction occurred, as provided by the institution (see Handling Dates and Times)
    type: Optional[TransactionType]
    unitQuantity: Optional[int]  # The number of units (e.g. individual shares) in the transaction, if available
    unitValue: Optional[float]  # The value of each unit in the transaction, if available
    categorization: Optional[TransactionCategorization]
