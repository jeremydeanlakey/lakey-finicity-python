from dataclasses import dataclass
from typing import Optional, Any

from finicity.models.account.account_detail import AccountDetail


# https://community.finicity.com/s/article/Account-Details-Checking-Savings-CD-Money-Market
@dataclass
class DepositAccountDetail(AccountDetail):
    createdDate: Any  # A timestamp showing when the account was added to the Finicity system(see Handling Dates and Times)
    availableBalanceAmount: Any  # The available balance (typically the current balance with adjustments for any pending transactions)
    openDate: Optional[Any]  # Date when account was opened
    periodStartDate: Optional[Any]  # Start date of period
    periodEndDate: Optional[Any]  # End date of period
    periodInterestRate: Optional[Any]  # The APY for the current period interest rate
    periodDepositAmount: Optional[Any]  # Amount deposited in period
    periodInterestAmount: Optional[Any]  # Interest accrued during the current period
    interestYtdAmount: Optional[Any]  # Interest accrued year-to-date
    interestPriorYtdAmount: Optional[Any]  # Interest earned in prior year
    maturityDate: Optional[Any]  # Maturity date of account type
    postedDate: Optional[Any]  # Most recent date of the following information
