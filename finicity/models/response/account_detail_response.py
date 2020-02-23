from dataclasses import dataclass


# https://community.finicity.com/s/article/Get-Customer-Account-Details
@dataclass
class AccountDetailResponse(object):
    routingNumber: str  # The account's 9-digit Routing Transit Number
    realAccountNumber: str  # The full account number, assigned by the institution
