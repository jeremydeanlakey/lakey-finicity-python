from dataclasses import dataclass
from typing import List

from finicity.models import SortOrder
from finicity.models.institution.institution import Institution


@dataclass
class TransactionsListResponse(object):
    found: int  # Total number of records matching search criteria
    displaying: int  # Number of records in this response
    moreAvailable: bool  # True if this response does not contain the last record in the result set
    fromDate: int  # Value of the fromDate request parameter that generated this response
    toDate: int  # Value of the toDate request parameter that generated this response
    sort: SortOrder  # Value of the sort request parameter that generated this response
    customers: List[Institution]
