import enum


# https://community.finicity.com/s/article/201750779-Account-Types
# The services Add All Accounts, Add All Accounts (with MFA Answers), Discover Customer Accounts and Discover Customer Accounts (with MFA Answers) will return a list of accounts that were found using the provided credentials. Each account record includes a type> field with a value from the following list.
# Finicity can usually determine the correct type for each account, but in some rare cases the account type will be unknown. In these cases, the account number and name should be displayed to the customer, who must specify the correct account type by selecting a value from the following table.
# Calls to Activate Customer Accounts v2 (without Aggregation) will fail if the account's  field contains unknown or any unrecognized type designation. The failed request will return HTTP 400 (Bad Request) with the error code 10106 (Invalid Account Type).
class AccountType(enum.Enum):
    unknown = 'Unknown'  # Type cannot be determined (customer must specify the correct type from other supported types in this table)
    checking = 'Checking'  # Standard checking
    savings = 'Savings'  # Standard savings
    cd = 'CD'  # Certificates of deposit
    moneyMarket = 'Money Market'  # Money Market
    creditCard = 'Credit Card'  # Standard credit cards
    lineOfCredit = 'Line Of Credit'  # Home equity,line of credit
    investment = 'Investment, Taxable'  # Generic investment (no details)
    investmentTaxDeferred = 'Investment, Tax-Deferred'  # Generic tax-advantaged investment (no details)
    employeeStockPurchasePlan = 'Employee Stock Purchase Plan'  # ESPP, Employee Stock Ownership Plans (ESOP), Stock Purchase Plans
    ira = 'IRA'  # Individual Retirement Account (not Rollover or Roth)
    _401k = '401K'  # 401K Plan
    roth = 'ROTH'  # Roth IRA, Roth 401K
    _403b = '403B'  # 403B Plan
    _529 = '529'  # 529 Plan
    rollover = 'ROLLOVER'  # Rollover IRA
    ugma = 'UGMA'  # Uniform Gifts to Minors Act
    utma = 'UTMA'  # Uniform Transfers to Minors Act
    keogh = 'KEOGH'  # Keogh Plan
    _457 = '457'  # 457 Plan
    _401a = '401A'  # 401A Plan
    mortgage = 'Mortgage'  # Standard Mortgages
    loan = 'Loan'  # Auto loans, equity loans, other loans
# TODO
