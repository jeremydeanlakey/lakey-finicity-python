from dataclasses import dataclass

from finicity.models.account.account_detail import AccountDetail


# https://community.finicity.com/s/article/Account-Details-Checking-Savings-CD-Money-Market
@dataclass
class DepositAccountDetail(AccountDetail):
    pass
# TODO
