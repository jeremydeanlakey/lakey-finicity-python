from dataclasses import dataclass
from typing import List

from finicity.models import Institution


@dataclass
class InstitutionsListResponse(object):
    found: int  # Total number of records matching search criteria
    displaying: int  # Number of records in this response
    moreAvailable: bool  # True if this response does not contain the last record in the result set
    createdDate: int  # Date this list was generated
    institutions: List[Institution]
