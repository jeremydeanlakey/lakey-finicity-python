from dataclasses import dataclass

from finicity.models.account.account_detail import AccountDetail


# https://community.finicity.com/s/article/Account-Details-Credit-Card-Line-of-Credit
@dataclass
class CreditLineAccountDetail(AccountDetail):
    pass
# TODO
