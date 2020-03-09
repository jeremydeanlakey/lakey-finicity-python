from dataclasses import dataclass
from typing import List

from finicity.models import SortOrder, Transaction


# https://community.finicity.com/s/article/202460245-Transactions#get_customer_transactions_v3
@dataclass
class TransactionsListResponse(object):
    found: int  # Total number of records matching search criteria
    displaying: int  # Number of records in this responses
    moreAvailable: bool  # True if this responses does not contain the last record in the result set
    fromDate: int  # Value of the fromDate request parameter that generated this responses
    toDate: int  # Value of the toDate request parameter that generated this responses
    sort: SortOrder  # Value of the sort request parameter that generated this responses
    transactions: List[Transaction]
    _unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        found = data.pop('found')
        displaying = data.pop('displaying')
        moreAvailable = data.pop('moreAvailable')
        fromDate = data.pop('fromDate')
        toDate = data.pop('toDate')
        sort = data.pop('sort')
        transactions_raw = data.pop('transactions')
        transactions = [Transaction.from_dict(d) for d in transactions_raw]
        return TransactionsListResponse(
            found=found,
            displaying=displaying,
            moreAvailable=moreAvailable,
            fromDate=fromDate,
            toDate=toDate,
            sort=sort,
            transactions=transactions,
            _unused_fields=data,
        )
