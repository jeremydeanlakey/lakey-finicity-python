import enum


# https://community.finicity.com/s/article/201750779-Account-Types
# Finicity can usually determine the correct type for each account, but in some
# rare cases the account type will be unknown. In these cases, the account
# number and name should be displayed to the customer, who must specify the
# correct account type by selecting a value from the following table.
# Calls to Activate Customer Accounts v2 (without Aggregation) will fail if the
# account's  field contains unknown or any unrecognized type designation. The
# failed request will return HTTP 400 (Bad Request) with the error code 10106
# (Invalid Account Type).
class AccountType(enum.Enum):
    unknown = "unknown"  # Type cannot be determined (customer must specify the correct type from other supported types in this table)
    checking = "checking"  # Standard checking
    savings = "savings"  # Standard savings
    cd = "cd"  # Certificates of deposit
    moneyMarket = "moneyMarket"  # Money Market
    creditCard = "creditCard"  # Standard credit cards
    lineOfCredit = "lineOfCredit"  # Home equity,line of credit
    investment = "investment"  # Generic investment (no details)
    investmentTaxDeferred = "investmentTaxDeferred"  # Generic tax-advantaged investment (no details)
    employeeStockPurchasePlan = "employeeStockPurchasePlan"  # ESPP, Employee Stock Ownership Plans (ESOP), Stock Purchase Plans
    ira = "ira"  # Individual Retirement Account (not Rollover or Roth)
    acct_401k = "acct_401k"  # 401K Plan
    roth = "roth"  # Roth IRA, Roth 401K
    acct_403b = "acct_403b"  # 403B Plan
    acct_529 = "acct_529"  # 529 Plan
    rollover = "rollover"  # Rollover IRA
    ugma = "ugma"  # Uniform Gifts to Minors Act
    utma = "utma"  # Uniform Transfers to Minors Act
    keogh = "keogh"  # Keogh Plan
    acct_457 = "acct_457"  # 457 Plan
    acct_401a = "acct_401a"  # 401A Plan
    mortgage = "mortgage"  # Standard Mortgages
    loan = "loan"  # Auto loans, equity loans, other loans


DEPOSIT_ACCOUNT_TYPES = {
    AccountType.checking,
    AccountType.savings,
    AccountType.cd,
    AccountType.moneyMarket,
}


INVESTMENT_ACCOUNT_TYPES = {
    AccountType.investment,
    AccountType.investmentTaxDeferred,
    AccountType.employeeStockPurchasePlan,
    AccountType.ira,
    AccountType.roth,
    AccountType.rollover,
    AccountType.ugma,
    AccountType.utma,
    AccountType.keogh,
    AccountType.acct_401k,
    AccountType.acct_403b,
    AccountType.acct_529,
    AccountType.acct_457,
    AccountType.acct_401a,
}


CREDIT_LINE_ACCOUNT_TYPES = {
    AccountType.creditCard,
    AccountType.lineOfCredit,
}


LOAN_ACCOUNT_TYPES = {
    AccountType.mortgage,
    AccountType.loan,
}
