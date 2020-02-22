import enum


# https://community.finicity.com/s/article/Get-Institutions
class InstitutionAccountType(enum.Enum):
    Banking = "Banking"
    Investments = "Investments"
    Credit_Cards_Accounts = "Credit Cards/Accounts"
    Workplace_Retirement = "Workplace Retirement"
    Mortgages_and_Loans = "Mortgages and Loans"
    Insurance = "Insurance"
