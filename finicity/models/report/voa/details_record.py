from dataclasses import dataclass


# https://community.finicity.com/s/article/VOI-Report
from typing import Optional


@dataclass
class DetailsRecord(object):
    unused_fields: dict  # this is for forward compatibility and should be empty
    interestMarginBalance: Optional[float]  # Only available for investment accounts. Net interest earned after deducting interest paid out
    availableCashBalance: Optional[float]  # Only available for investment accounts. Amount available for cash withdrawal
    vestedBalance: Optional[float]  # Only available for investment accounts. Vested amount in account
    currentLoanBalance: Optional[float]  # Only available for investment accounts. Current loan balance
    availableBalanceAmount: Optional[float]  # The available balance for the account

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        interestMarginBalance = data.pop('interestMarginBalance', None)
        availableCashBalance = data.pop('availableCashBalance', None)
        vestedBalance = data.pop('vestedBalance', None)
        currentLoanBalance = data.pop('currentLoanBalance', None)
        availableBalanceAmount = data.pop('availableBalanceAmount', None)
        return DetailsRecord(
            interestMarginBalance=interestMarginBalance,
            availableCashBalance=availableCashBalance,
            vestedBalance=vestedBalance,
            currentLoanBalance=currentLoanBalance,
            availableBalanceAmount=availableBalanceAmount,
            unused_fields=data,
        )
