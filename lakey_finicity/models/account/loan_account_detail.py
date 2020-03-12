from dataclasses import dataclass, field
from typing import Any, Optional

from lakey_finicity.models.account.account_detail import AccountDetail


# https://community.finicity.com/s/article/Account-Details-Mortgage-Loan
@dataclass
class LoanAccountDetail(AccountDetail):
    _unused_fields: dict  # this is for forward compatibility and should be empty
    postedDate: Optional[Any] = field(default=None)  # Most recent date of the following information
    termOfMl: Optional[Any] = field(default=None)  # Length of loan in months
    mlHolderName: Optional[Any] = field(default=None)  # Holder of the mortgage or loan
    description: Optional[Any] = field(default=None)  # Description of loan
    lateFeeAmount: Optional[Any] = field(default=None)  # Late fee charged
    payoffAmount: Optional[Any] = field(default=None)  # The amount required to payoff the loan
    payoffAmountDate: Optional[Any] = field(default=None)  # Date of final payment
    originalMaturityDate: Optional[Any] = field(default=None)  # Original date of loan maturity
    principalBalance: Optional[Any] = field(default=None)  # The principal balance
    escrowBalance: Optional[Any] = field(default=None)  # The escrow balance
    interestRate: Optional[Any] = field(default=None)  # The interest rate
    interestPeriod: Optional[Any] = field(default=None)  # Period of interest
    initialMlAmount: Optional[Any] = field(default=None)  # Original loan amount
    initialMlDate: Optional[Any] = field(default=None)  # Original date of loan
    nextPaymentPrincipalAmount: Optional[Any] = field(default=None)  # Amount towards principal in next payment
    nextPaymentInterestAmount: Optional[Any] = field(default=None)  # Amount of interest in next payment
    nextPayment: Optional[Any] = field(default=None)  # Minimum payment due
    nextPaymentDate: Optional[Any] = field(default=None)  # Due date for the next payment
    lastPaymentDueDate: Optional[Any] = field(default=None)  # Due date of last payment
    lastPaymentReceiveDate: Optional[Any] = field(default=None)  # The date of the last payment
    lastPaymentAmount: Optional[Any] = field(default=None)  # The amount of the last payment
    lastPaymentPrincipalAmount: Optional[Any] = field(default=None)  # Amount towards principal in last payment
    lastPaymentInterestAmount: Optional[Any] = field(default=None)  # Amount of interest in last payment
    lastPaymentEscrowAmount: Optional[Any] = field(default=None)  # Amount towards escrow in last payment
    lastPaymentLastFeeAmount: Optional[Any] = field(default=None)  # Amount of last fee in last payment
    lastPaymentLateCharge: Optional[Any] = field(default=None)  # Amount of late charge in last payment
    ytdPrincipalPaid: Optional[Any] = field(default=None)  # Principal paid year-to-date
    ytdInterestPaid: Optional[Any] = field(default=None)  # Interest paid year-to-date
    ytdInsurancePaid: Optional[Any] = field(default=None)  # Insurance paid year-to-date
    ytdTaxPaid: Optional[Any] = field(default=None)  # Tax paid year-to-date
    autoPayEnrolled: Optional[Any] = field(default=None)  # Enrolled in autopay (F/Y)
    collateral: Optional[Any] = field(default=None)  # Collateral on loan
    currentSchool: Optional[Any] = field(default=None)  # Current school
    firstPaymentDate: Optional[Any] = field(default=None)  # First payment due date
    firstMortgage: Optional[Any] = field(default=None)  # First mortgage (F/Y)
    loanPaymentFreq: Optional[Any] = field(default=None)  # Frequency of payments (monthly, etc.)
    paymentMinAmount: Optional[Any] = field(default=None)  # Minimum payment amount
    originalSchool: Optional[Any] = field(default=None)  # Original school
    recurringPaymentAmount: Optional[Any] = field(default=None)  # Recurring payment amount
    lender: Optional[Any] = field(default=None)  # Owner of loan
    endingBalanceAmount: Optional[Any] = field(default=None)  # Ending balance
    availableBalanceAmount: Optional[Any] = field(default=None)  # Available balance
    loanTermType: Optional[Any] = field(default=None)  # Type of loan term
    paymentsMade: Optional[Any] = field(default=None)  # Number of payments made
    balloonAmount: Optional[Any] = field(default=None)  # Balloon payment amount
    projectedInterest: Optional[Any] = field(default=None)  # Projected interest on the loan
    interestPaidLtd: Optional[Any] = field(default=None)  # Interest paid since inception of loan (life to date)
    interestRateType: Optional[Any] = field(default=None)  # Type of interest rate
    loanPaymentType: Optional[Any] = field(default=None)  # Type of loan payment
    paymentsRemaining: Optional[Any] = field(default=None)  # Number of payments remaining before loan is paid off

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        postedDate = data.pop('postedDate', None)
        termOfMl = data.pop('termOfMl', None)
        mlHolderName = data.pop('mlHolderName', None)
        description = data.pop('description', None)
        lateFeeAmount = data.pop('lateFeeAmount', None)
        payoffAmount = data.pop('payoffAmount', None)
        payoffAmountDate = data.pop('payoffAmountDate', None)
        originalMaturityDate = data.pop('originalMaturityDate', None)
        principalBalance = data.pop('principalBalance', None)
        escrowBalance = data.pop('escrowBalance', None)
        interestRate = data.pop('interestRate', None)
        interestPeriod = data.pop('interestPeriod', None)
        initialMlAmount = data.pop('initialMlAmount', None)
        initialMlDate = data.pop('initialMlDate', None)
        nextPaymentPrincipalAmount = data.pop('nextPaymentPrincipalAmount', None)
        nextPaymentInterestAmount = data.pop('nextPaymentInterestAmount', None)
        nextPayment = data.pop('nextPayment', None)
        nextPaymentDate = data.pop('nextPaymentDate', None)
        lastPaymentDueDate = data.pop('lastPaymentDueDate', None)
        lastPaymentReceiveDate = data.pop('lastPaymentReceiveDate', None)
        lastPaymentAmount = data.pop('lastPaymentAmount', None)
        lastPaymentPrincipalAmount = data.pop('lastPaymentPrincipalAmount', None)
        lastPaymentInterestAmount = data.pop('lastPaymentInterestAmount', None)
        lastPaymentEscrowAmount = data.pop('lastPaymentEscrowAmount', None)
        lastPaymentLastFeeAmount = data.pop('lastPaymentLastFeeAmount', None)
        lastPaymentLateCharge = data.pop('lastPaymentLateCharge', None)
        ytdPrincipalPaid = data.pop('ytdPrincipalPaid', None)
        ytdInterestPaid = data.pop('ytdInterestPaid', None)
        ytdInsurancePaid = data.pop('ytdInsurancePaid', None)
        ytdTaxPaid = data.pop('ytdTaxPaid', None)
        autoPayEnrolled = data.pop('autoPayEnrolled', None)
        collateral = data.pop('collateral', None)
        currentSchool = data.pop('currentSchool', None)
        firstPaymentDate = data.pop('firstPaymentDate', None)
        firstMortgage = data.pop('firstMortgage', None)
        loanPaymentFreq = data.pop('loanPaymentFreq', None)
        paymentMinAmount = data.pop('paymentMinAmount', None)
        originalSchool = data.pop('originalSchool', None)
        recurringPaymentAmount = data.pop('recurringPaymentAmount', None)
        lender = data.pop('lender', None)
        endingBalanceAmount = data.pop('endingBalanceAmount', None)
        availableBalanceAmount = data.pop('availableBalanceAmount', None)
        loanTermType = data.pop('loanTermType', None)
        paymentsMade = data.pop('paymentsMade', None)
        balloonAmount = data.pop('balloonAmount', None)
        projectedInterest = data.pop('projectedInterest', None)
        interestPaidLtd = data.pop('interestPaidLtd', None)
        interestRateType = data.pop('interestRateType', None)
        loanPaymentType = data.pop('loanPaymentType', None)
        paymentsRemaining = data.pop('paymentsRemaining', None)
        return LoanAccountDetail(
            postedDate=postedDate,
            termOfMl=termOfMl,
            mlHolderName=mlHolderName,
            description=description,
            lateFeeAmount=lateFeeAmount,
            payoffAmount=payoffAmount,
            payoffAmountDate=payoffAmountDate,
            originalMaturityDate=originalMaturityDate,
            principalBalance=principalBalance,
            escrowBalance=escrowBalance,
            interestRate=interestRate,
            interestPeriod=interestPeriod,
            initialMlAmount=initialMlAmount,
            initialMlDate=initialMlDate,
            nextPaymentPrincipalAmount=nextPaymentPrincipalAmount,
            nextPaymentInterestAmount=nextPaymentInterestAmount,
            nextPayment=nextPayment,
            nextPaymentDate=nextPaymentDate,
            lastPaymentDueDate=lastPaymentDueDate,
            lastPaymentReceiveDate=lastPaymentReceiveDate,
            lastPaymentAmount=lastPaymentAmount,
            lastPaymentPrincipalAmount=lastPaymentPrincipalAmount,
            lastPaymentInterestAmount=lastPaymentInterestAmount,
            lastPaymentEscrowAmount=lastPaymentEscrowAmount,
            lastPaymentLastFeeAmount=lastPaymentLastFeeAmount,
            lastPaymentLateCharge=lastPaymentLateCharge,
            ytdPrincipalPaid=ytdPrincipalPaid,
            ytdInterestPaid=ytdInterestPaid,
            ytdInsurancePaid=ytdInsurancePaid,
            ytdTaxPaid=ytdTaxPaid,
            autoPayEnrolled=autoPayEnrolled,
            collateral=collateral,
            currentSchool=currentSchool,
            firstPaymentDate=firstPaymentDate,
            firstMortgage=firstMortgage,
            loanPaymentFreq=loanPaymentFreq,
            paymentMinAmount=paymentMinAmount,
            originalSchool=originalSchool,
            recurringPaymentAmount=recurringPaymentAmount,
            lender=lender,
            endingBalanceAmount=endingBalanceAmount,
            availableBalanceAmount=availableBalanceAmount,
            loanTermType=loanTermType,
            paymentsMade=paymentsMade,
            balloonAmount=balloonAmount,
            projectedInterest=projectedInterest,
            interestPaidLtd=interestPaidLtd,
            interestRateType=interestRateType,
            loanPaymentType=loanPaymentType,
            paymentsRemaining=paymentsRemaining,
            _unused_fields=data,
        )
