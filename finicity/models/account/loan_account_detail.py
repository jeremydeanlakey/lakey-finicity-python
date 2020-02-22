from dataclasses import dataclass
from typing import Any, Optional

from finicity.models.account.account_detail import AccountDetail


# https://community.finicity.com/s/article/Account-Details-Mortgage-Loan
@dataclass
class LoanAccountDetail(AccountDetail):
    postedDate: Optional[Any]  # Most recent date of the following information
    termOfMl: Optional[Any]  # Length of loan in months
    mlHolderName: Optional[Any]  # Holder of the mortgage or loan
    description: Optional[Any]  # Description of loan
    lateFeeAmount: Optional[Any]  # Late fee charged
    payoffAmount: Optional[Any]  # The amount required to payoff the loan
    payoffAmountDate: Optional[Any]  # Date of final payment
    originalMaturityDate: Optional[Any]  # Original date of loan maturity
    principalBalance: Optional[Any]  # The principal balance
    escrowBalance: Optional[Any]  # The escrow balance
    interestRate: Optional[Any]  # The interest rate
    interestPeriod: Optional[Any]  # Period of interest
    initialMlAmount: Optional[Any]  # Original loan amount
    initialMlDate: Optional[Any]  # Original date of loan
    nextPaymentPrincipalAmount: Optional[Any]  # Amount towards principal in next payment
    nextPaymentInterestAmount: Optional[Any]  # Amount of interest in next payment
    nextPayment: Optional[Any]  # Minimum payment due
    nextPaymentDate: Optional[Any]  # Due date for the next payment
    lastPaymentDueDate: Optional[Any]  # Due date of last payment
    lastPaymentReceiveDate: Optional[Any]  # The date of the last payment
    lastPaymentAmount: Optional[Any]  # The amount of the last payment
    lastPaymentPrincipalAmount: Optional[Any]  # Amount towards principal in last payment
    lastPaymentInterestAmount: Optional[Any]  # Amount of interest in last payment
    lastPaymentEscrowAmount: Optional[Any]  # Amount towards escrow in last payment
    lastPaymentLastFeeAmount: Optional[Any]  # Amount of last fee in last payment
    lastPaymentLateCharge: Optional[Any]  # Amount of late charge in last payment
    ytdPrincipalPaid: Optional[Any]  # Principal paid year-to-date
    ytdInterestPaid: Optional[Any]  # Interest paid year-to-date
    ytdInsurancePaid: Optional[Any]  # Insurance paid year-to-date
    ytdTaxPaid: Optional[Any]  # Tax paid year-to-date
    autoPayEnrolled: Optional[Any]  # Enrolled in autopay (F/Y)
    collateral: Optional[Any]  # Collateral on loan
    currentSchool: Optional[Any]  # Current school
    firstPaymentDate: Optional[Any]  # First payment due date
    firstMortgage: Optional[Any]  # First mortgage (F/Y)
    loanPaymentFreq: Optional[Any]  # Frequency of payments (monthly, etc.)
    paymentMinAmount: Optional[Any]  # Minimum payment amount
    originalSchool: Optional[Any]  # Original school
    recurringPaymentAmount: Optional[Any]  # Recurring payment amount
    lender: Optional[Any]  # Owner of loan
    endingBalanceAmount: Optional[Any]  # Ending balance
    availableBalanceAmount: Optional[Any]  # Available balance
    loanTermType: Optional[Any]  # Type of loan term
    paymentsMade: Optional[Any]  # Number of payments made
    balloonAmount: Optional[Any]  # Balloon payment amount
    projectedInterest: Optional[Any]  # Projected interest on the loan
    interestPaidLtd: Optional[Any]  # Interest paid since inception of loan (life to date)
    interestRateType: Optional[Any]  # Type of interest rate
    loanPaymentType: Optional[Any]  # Type of loan payment
    paymentsRemaining: Optional[Any]  # Number of payments remaining before loan is paid off
