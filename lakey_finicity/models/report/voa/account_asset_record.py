from dataclasses import dataclass
from typing import Optional

from lakey_finicity.models import AccountType


@dataclass
class AccountAssetRecord(object):
    _unused_fields: dict  # this is for forward compatibility and should be empty
    type: Optional[AccountType]  # VOA: checking / savings / moneyMarket / cd / investment*
    currentBalance: Optional[float]  # Current balance of the account
    availableBalance: Optional[float]  #
    twoMonthAverage: Optional[float]  # Two month average daily balance of the account
    sixMonthAverage: Optional[float]  # Six month average daily balance of the account
    beginningBalance: Optional[float]  # Beginning balance of account per the time period in the report

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        type_str: str = data.pop('type', None)
        type = AccountType.from_description(type_str) if type_str else None
        currentBalance = data.pop('currentBalance', None)
        availableBalance = data.pop('availableBalance', None)
        twoMonthAverage = data.pop('twoMonthAverage', None)
        sixMonthAverage = data.pop('sixMonthAverage', None)
        beginningBalance = data.pop('beginningBalance', None)
        return AccountAssetRecord(
            type=type,
            currentBalance=currentBalance,
            availableBalance=availableBalance,
            twoMonthAverage=twoMonthAverage,
            sixMonthAverage=sixMonthAverage,
            beginningBalance=beginningBalance,
            _unused_fields=data,
        )
