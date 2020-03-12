from dataclasses import dataclass
from typing import Optional

from lakey_finicity.models.account.credit_line_account_detail import CreditLineAccountDetail
from lakey_finicity.models.account.deposit_account_detail import DepositAccountDetail
from lakey_finicity.models.account.loan_account_detail import LoanAccountDetail
from lakey_finicity.models.account.account_detail import AccountDetail
from lakey_finicity.models.account.account_type import AccountType, DEPOSIT_ACCOUNT_TYPES, CREDIT_LINE_ACCOUNT_TYPES, \
    INVESTMENT_ACCOUNT_TYPES, LOAN_ACCOUNT_TYPES
from lakey_finicity.models.account.aggregation_status_code import AggregationStatusCode
from lakey_finicity.models.account.investment_account_detail import InvestmentAccountDetail


@dataclass
class Account(object):
    id: str
    number: Optional[str]
    name: Optional[str]
    type: Optional[AccountType]
    status: str
    balance: Optional[str]
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
    currency: Optional[str]
    displayPosition: Optional[int]
    _unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        number = data.pop('number', None)
        name = data.pop('name', None)
        type_str: str = data.pop('type', None)
        type = AccountType.from_description(type_str) if type_str else None
        status = data.pop('status')
        balance = data.pop('balance', None)
        aggregationStatusCode_str = data.pop('aggregationStatusCode', None)
        aggregationStatusCode = AggregationStatusCode(aggregationStatusCode_str) if aggregationStatusCode_str else None
        aggregationSuccessDate = data.pop('aggregationSuccessDate', None)
        aggregationAttemptDate = data.pop('aggregationAttemptDate', None)
        customerId = data.pop('customerId', None)
        institutionId = data.pop('institutionId', None)
        balanceDate = data.pop('balanceDate', None)
        createdDate = data.pop('createdDate', None)
        institutionLoginId = data.pop('institutionLoginId', None)
        lastUpdatedDate = data.pop('lastUpdatedDate', None)
        detail_dict = data.pop('detail', None)
        detail = account_detail_from_dict(type, detail_dict) if detail_dict else None
        currency = data.pop('currency', None)
        displayPosition = data.pop('displayPosition', None)
        return Account(
            id=id,
            number=number,
            name=name,
            type=type,
            status=status,
            balance=balance,
            aggregationStatusCode=aggregationStatusCode,
            aggregationSuccessDate=aggregationSuccessDate,
            aggregationAttemptDate=aggregationAttemptDate,
            customerId=customerId,
            institutionId=institutionId,
            balanceDate=balanceDate,
            createdDate=createdDate,
            institutionLoginId=institutionLoginId,
            lastUpdatedDate=lastUpdatedDate,
            detail=detail,
            currency=currency,
            displayPosition=displayPosition,
            _unused_fields=data,
        )


def account_detail_from_dict(account_type: AccountType, data: dict) -> Optional[AccountDetail]:
    try:
        if account_type in DEPOSIT_ACCOUNT_TYPES:
            return DepositAccountDetail.from_dict(data)
        elif account_type in CREDIT_LINE_ACCOUNT_TYPES:
            return CreditLineAccountDetail.from_dict(data)
        elif account_type in INVESTMENT_ACCOUNT_TYPES:
            return InvestmentAccountDetail.from_dict(data)
        elif account_type in LOAN_ACCOUNT_TYPES:
            return LoanAccountDetail.from_dict(data)
        else:
            return None
    except Exception as e:
        print(f"{e}: account_type: {account_type}, data: {data}")
        return None
