from dataclasses import dataclass
from typing import List

from finicity.models import Institution


@dataclass
class CustomersListResponse(object):
    found: int  # Total number of records matching search criteria
    displaying: int  # Number of records in this response
    moreAvailable: bool  # True if this response does not contain the last record in the result set
    customers: List[Institution]
