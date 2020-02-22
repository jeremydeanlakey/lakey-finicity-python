from dataclasses import dataclass
from typing import Optional

from finicity.models.account.account_detail import AccountDetail
from finicity.models.account.account_type import AccountType


# https://community.finicity.com/s/article/202460255-Customer-Accounts#customer_account_record
@dataclass
class Account(object):
    id: str
    number: str
    name: str
    type: AccountType
    status: str
    balance: str
    customerId: str
    institutionId: str
    balanceDate: str
    createdDate: str
    institutionLoginId: str
    lastUpdatedDate: Optional[str]
    detail: Optional[AccountDetail]

# TODO handle partial accounts, see link
