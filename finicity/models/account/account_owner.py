from dataclasses import dataclass


# https://community.finicity.com/s/article/Get-Account-Owner
@dataclass
class AccountOwner(object):
    ownerName: str
    ownerAddress: str
