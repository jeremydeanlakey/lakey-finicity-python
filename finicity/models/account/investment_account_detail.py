from dataclasses import dataclass, field
from typing import Any, Optional

from finicity.models.account.account_detail import AccountDetail


# https://community.finicity.com/s/article/Account-Details-Investment
@dataclass
class InvestmentAccountDetail(AccountDetail):
    _unused_fields: dict  # this is for forward compatibility and should be empty
    interestMarginBalance: Optional[Any] = field(default=None)  # Net interest earned after deducting interest paid out
    shortBalance: Optional[Any] = field(default=None)  # Sum of short balance
    availableCashBalance: Optional[Any] = field(default=None)  # Amount available for cash withdrawal
    currentBalance: Optional[Any] = field(default=None)  # Current balance of investment
    maturityValueAmount: Optional[Any] = field(default=None)  # amount payable to an investor at maturity
    vestedBalance: Optional[Any] = field(default=None)  # Vested amount in account
    empMatchAmount: Optional[Any] = field(default=None)  # Employer matched contributions
    empPretaxContribAmount: Optional[Any] = field(default=None)  # Employer pretax contribution amount
    empPretaxContribAmountYtd: Optional[Any] = field(default=None)  # Employer pretax contribution amount year to date
    contribTotalYtd: Optional[Any] = field(default=None)  # Total year to date contributions
    cashBalanceAmount: Optional[Any] = field(default=None)  # Cash balance of account
    preTaxAmount: Optional[Any] = field(default=None)  # Pre tax amount of total balance
    afterTaxAmount: Optional[Any] = field(default=None)  # Post tax amount of total balance
    matchAmount: Optional[Any] = field(default=None)  # Amount matched
    profitSharingAmount: Optional[Any] = field(default=None)  # Amount of balance for profit sharing
    rolloverAmount: Optional[Any] = field(default=None)  # Amount of balance rolled over from original account (401k, etc.)
    otherVestAmount: Optional[Any] = field(default=None)  # Other vested amount
    otherNonvestAmount: Optional[Any] = field(default=None)  # Other nonvested amount
    currentLoanBalance: Optional[Any] = field(default=None)  # Current loan balance
    loanRate: Optional[Any] = field(default=None)  # Interest rate of loan
    buyPower: Optional[Any] = field(default=None)  # Money available to buy securities
    rolloverLtd: Optional[Any] = field(default=None)  # Life to date of money rolled over

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        interestMarginBalance = data.pop('interestMarginBalance', None)
        shortBalance = data.pop('shortBalance', None)
        availableCashBalance = data.pop('availableCashBalance', None)
        currentBalance = data.pop('currentBalance', None)
        maturityValueAmount = data.pop('maturityValueAmount', None)
        vestedBalance = data.pop('vestedBalance', None)
        empMatchAmount = data.pop('empMatchAmount', None)
        empPretaxContribAmount = data.pop('empPretaxContribAmount', None)
        empPretaxContribAmountYtd = data.pop('empPretaxContribAmountYtd', None)
        contribTotalYtd = data.pop('contribTotalYtd', None)
        cashBalanceAmount = data.pop('cashBalanceAmount', None)
        preTaxAmount = data.pop('preTaxAmount', None)
        afterTaxAmount = data.pop('afterTaxAmount', None)
        matchAmount = data.pop('matchAmount', None)
        profitSharingAmount = data.pop('profitSharingAmount', None)
        rolloverAmount = data.pop('rolloverAmount', None)
        otherVestAmount = data.pop('otherVestAmount', None)
        otherNonvestAmount = data.pop('otherNonvestAmount', None)
        currentLoanBalance = data.pop('currentLoanBalance', None)
        loanRate = data.pop('loanRate', None)
        buyPower = data.pop('buyPower', None)
        rolloverLtd = data.pop('rolloverLtd', None)
        return InvestmentAccountDetail(
            interestMarginBalance=interestMarginBalance,
            shortBalance=shortBalance,
            availableCashBalance=availableCashBalance,
            currentBalance=currentBalance,
            maturityValueAmount=maturityValueAmount,
            vestedBalance=vestedBalance,
            empMatchAmount=empMatchAmount,
            empPretaxContribAmount=empPretaxContribAmount,
            empPretaxContribAmountYtd=empPretaxContribAmountYtd,
            contribTotalYtd=contribTotalYtd,
            cashBalanceAmount=cashBalanceAmount,
            preTaxAmount=preTaxAmount,
            afterTaxAmount=afterTaxAmount,
            matchAmount=matchAmount,
            profitSharingAmount=profitSharingAmount,
            rolloverAmount=rolloverAmount,
            otherVestAmount=otherVestAmount,
            otherNonvestAmount=otherNonvestAmount,
            currentLoanBalance=currentLoanBalance,
            loanRate=loanRate,
            buyPower=buyPower,
            rolloverLtd=rolloverLtd,
            _unused_fields=data,
        )
