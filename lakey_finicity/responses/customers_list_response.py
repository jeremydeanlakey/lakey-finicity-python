from dataclasses import dataclass
from typing import List

from lakey_finicity.models import Customer


# https://community.finicity.com/s/article/201703219-Customers#get_customers
@dataclass
class CustomersListResponse(object):
    found: int  # Total number of records matching search criteria
    displaying: int  # Number of records in this responses
    moreAvailable: bool  # True if this responses does not contain the last record in the result set
    customers: List[Customer]
    _unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        found = data.pop('found')
        displaying = data.pop('displaying')
        moreAvailable = data.pop('moreAvailable')
        customers_raw = data.pop('customers')
        customers = [Customer.from_dict(d) for d in customers_raw]
        return CustomersListResponse(
            found=found,
            displaying=displaying,
            moreAvailable=moreAvailable,
            customers=customers,
            _unused_fields=data,
        )
