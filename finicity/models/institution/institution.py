from dataclasses import dataclass

from finicity.models.institution import InstitutionAccountType, InstitutionAddress


# https://community.finicity.com/s/article/Get-Institutions
@dataclass
class Institution(object):
    id: int  # The institution ID
    name: str  # The name of the institution
    accountTypeDescription: InstitutionAccountType
    urlHomeApp: str  # The URL of the institution's primary home page
    urlLogonApp: str  # The URL of the institution's login page
    urlProductApp: str
    specialText: str  # Any special text found on the institution's website
    address: InstitutionAddress
    phone: str  # The institution's primary phone number
    email: str  # The institution's primary contact email
    currency: str  # The institution's primary currency
