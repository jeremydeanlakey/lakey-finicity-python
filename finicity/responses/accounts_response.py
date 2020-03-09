from dataclasses import dataclass
from typing import List

from finicity.models import Account


# https://community.finicity.com/s/article/202460255-Customer-Accounts#get_customer_accounts
@dataclass
class AccountsResponse(object):
    accounts: List[Account]
    _unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        accounts_raw = data.pop('accounts')
        accounts = [Account.from_dict(d) for d in accounts_raw]
        return AccountsResponse(
            accounts=accounts,
            _unused_fields=data,
        )
