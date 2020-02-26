from dataclasses import dataclass
from typing import List

from finicity.models import Institution


# https://community.finicity.com/s/article/202460265-Institutions#get_institutions
@dataclass
class InstitutionsListResponse(object):
    found: int  # Total number of records matching search criteria
    displaying: int  # Number of records in this response
    moreAvailable: bool  # True if this response does not contain the last record in the result set
    createdDate: int  # Date this list was generated
    institutions: List[Institution]
    unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        found = data.pop('found')
        displaying = data.pop('displaying')
        moreAvailable = data.pop('moreAvailable')
        createdDate = data.pop('createdDate')
        institutions_json_list: dict = data.pop('institutions')
        institutions = [Institution.from_dict(d) for d in institutions_json_list]
        return InstitutionsListResponse(
            found=found,
            displaying=displaying,
            moreAvailable=moreAvailable,
            createdDate=createdDate,
            institutions=institutions,
            unused_fields=data,
        )
