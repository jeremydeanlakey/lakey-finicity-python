from dataclasses import dataclass
from typing import Optional


@dataclass
class AssetRecord(object):
    unused_fields: dict  # this is for forward compatibility and should be empty
    currentBalance: float  # Current balance of the account
    availableBalance: Optional[float]  #
    twoMonthAverage: float  # Two month average daily balance of the account
    sixMonthAverage: float  # Six month average daily balance of the account
    beginningBalance: float  # Beginning balance of account per the time period in the report

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        currentBalance = data.pop('currentBalance')
        availableBalance = data.pop('availableBalance', None)
        twoMonthAverage = data.pop('twoMonthAverage')
        sixMonthAverage = data.pop('sixMonthAverage')
        beginningBalance = data.pop('beginningBalance')
        return AssetRecord(
            currentBalance=currentBalance,
            availableBalance=availableBalance,
            twoMonthAverage=twoMonthAverage,
            sixMonthAverage=sixMonthAverage,
            beginningBalance=beginningBalance,
            unused_fields=data,
        )
