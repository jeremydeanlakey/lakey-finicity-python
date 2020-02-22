from dataclasses import dataclass
from typing import Any, Optional

from finicity.models.account.account_detail import AccountDetail


# https://community.finicity.com/s/article/Account-Details-Investment
@dataclass
class InvestmentAccountDetail(AccountDetail):
    interestMarginBalance: Optional[Any]  # Net interest earned after deducting interest paid out
    shortBalance: Optional[Any]  # Sum of short balance
    availableCashBalance: Optional[Any]  # Amount available for cash withdrawal
    currentBalance: Optional[Any]  # Current balance of investment
    maturityValueAmount: Optional[Any]  # amount payable to an investor at maturity
    vestedBalance: Optional[Any]  # Vested amount in account
    empMatchAmount: Optional[Any]  # Employer matched contributions
    empPretaxContribAmount: Optional[Any]  # Employer pretax contribution amount
    empPretaxContribAmountYtd: Optional[Any]  # Employer pretax contribution amount year to date
    contribTotalYtd: Optional[Any]  # Total year to date contributions
    cashBalanceAmount: Optional[Any]  # Cash balance of account
    preTaxAmount: Optional[Any]  # Pre tax amount of total balance
    afterTaxAmount: Optional[Any]  # Post tax amount of total balance
    matchAmount: Optional[Any]  # Amount matched
    profitSharingAmount: Optional[Any]  # Amount of balance for profit sharing
    rolloverAmount: Optional[Any]  # Amount of balance rolled over from original account (401k, etc.)
    otherVestAmount: Optional[Any]  # Other vested amount
    otherNonvestAmount: Optional[Any]  # Other nonvested amount
    currentLoanBalance: Optional[Any]  # Current loan balance
    loanRate: Optional[Any]  # Interest rate of loan
    buyPower: Optional[Any]  # Money available to buy securities
    rolloverLtd: Optional[Any]  # Life to date of money rolled over
