from dataclasses import dataclass
from typing import Optional


@dataclass
class AssetRecord(object):
    _unused_fields: dict  # this is for forward compatibility and should be empty
    currentBalance: Optional[float]  # Current balance of the account
    availableBalance: Optional[float]  #
    twoMonthAverage: Optional[float]  # Two month average daily balance of the account
    sixMonthAverage: Optional[float]  # Six month average daily balance of the account
    beginningBalance: Optional[float]  # Beginning balance of account per the time period in the report

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        currentBalance = data.pop('currentBalance', None)
        availableBalance = data.pop('availableBalance', None)
        twoMonthAverage = data.pop('twoMonthAverage', None)
        sixMonthAverage = data.pop('sixMonthAverage', None)
        beginningBalance = data.pop('beginningBalance', None)
        return AssetRecord(
            currentBalance=currentBalance,
            availableBalance=availableBalance,
            twoMonthAverage=twoMonthAverage,
            sixMonthAverage=sixMonthAverage,
            beginningBalance=beginningBalance,
            _unused_fields=data,
        )
