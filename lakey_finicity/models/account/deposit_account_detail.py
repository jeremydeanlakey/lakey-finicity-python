from dataclasses import dataclass, field
from typing import Optional, Any

from lakey_finicity.models.account.account_detail import AccountDetail


# https://community.finicity.com/s/article/Account-Details-Checking-Savings-CD-Money-Market
@dataclass
class DepositAccountDetail(AccountDetail):
    _unused_fields: dict  # this is for forward compatibility and should be empty
    createdDate: Optional[Any]  # A timestamp showing when the account was added to the Finicity system(see Handling Dates and Times)
    availableBalanceAmount: Any  # The available balance (typically the current balance with adjustments for any pending transactions)
    openDate: Optional[Any] = field(default=None)  # Date when account was opened
    periodStartDate: Optional[Any] = field(default=None)  # Start date of period
    periodEndDate: Optional[Any] = field(default=None)  # End date of period
    periodInterestRate: Optional[Any] = field(default=None)  # The APY for the current period interest rate
    periodDepositAmount: Optional[Any] = field(default=None)  # Amount deposited in period
    periodInterestAmount: Optional[Any] = field(default=None)  # Interest accrued during the current period
    interestYtdAmount: Optional[Any] = field(default=None)  # Interest accrued year-to-date
    interestPriorYtdAmount: Optional[Any] = field(default=None)  # Interest earned in prior year
    maturityDate: Optional[Any] = field(default=None)  # Maturity date of account type
    postedDate: Optional[Any] = field(default=None)  # Most recent date of the following information

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        createdDate = data.pop('createdDate', None)
        availableBalanceAmount = data.pop('availableBalanceAmount')
        openDate = data.pop('openDate', None)
        periodStartDate = data.pop('periodStartDate', None)
        periodEndDate = data.pop('periodEndDate', None)
        periodInterestRate = data.pop('periodInterestRate', None)
        periodDepositAmount = data.pop('periodDepositAmount', None)
        periodInterestAmount = data.pop('periodInterestAmount', None)
        interestYtdAmount = data.pop('interestYtdAmount', None)
        interestPriorYtdAmount = data.pop('interestPriorYtdAmount', None)
        maturityDate = data.pop('maturityDate', None)
        postedDate = data.pop('postedDate', None)
        return DepositAccountDetail(
            createdDate=createdDate,
            availableBalanceAmount=availableBalanceAmount,
            openDate=openDate,
            periodStartDate=periodStartDate,
            periodEndDate=periodEndDate,
            periodInterestRate=periodInterestRate,
            periodDepositAmount=periodDepositAmount,
            periodInterestAmount=periodInterestAmount,
            interestYtdAmount=interestYtdAmount,
            interestPriorYtdAmount=interestPriorYtdAmount,
            maturityDate=maturityDate,
            postedDate=postedDate,
            _unused_fields=data,
        )
