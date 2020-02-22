from dataclasses import dataclass
from typing import Optional

from finicity.models.account.account_detail import AccountDetail
from finicity.models.account.account_type import AccountType
from finicity.models.account.aggregation_status_code import AggregationStatusCode


# https://community.finicity.com/s/article/202460255-Customer-Accounts#customer_account_record
@dataclass
class Account(object):
    id: str
    number: str
    name: str
    type: AccountType
    status: str
    balance: str
    # won't be in partial account records:
    aggregationStatusCode:  Optional[AggregationStatusCode]  # doesn't exist in example
    aggregationSuccessDate: Optional[int]  # doesn't exist in example
    aggregationAttemptDate: Optional[int]  # doesn't exist in example
    customerId: Optional[str]
    institutionId: Optional[str]
    balanceDate: Optional[str]
    createdDate: Optional[str]
    institutionLoginId: Optional[str]
    # not always included:
    lastUpdatedDate: Optional[str]
    detail: Optional[AccountDetail]
