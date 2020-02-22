from dataclasses import dataclass


# https://community.finicity.com/s/article/Get-Institutions
@dataclass
class InstitutionAddress(object):
    addressLine1: str
    addressLine2: str
    city: str
    state: str
    postalCode: str
    country: str
