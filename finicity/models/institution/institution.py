from dataclasses import dataclass

from finicity.models.institution.institution_address import InstitutionAddress
from finicity.models.institution.institution_account_type import InstitutionAccountType


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
    unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        name = data.pop('name')
        accountTypeDescription_str: dict = data.pop('accountTypeDescription')
        accountTypeDescription = InstitutionAccountType(accountTypeDescription_str)
        urlHomeApp = data.pop('urlHomeApp')
        urlLogonApp = data.pop('urlLogonApp')
        urlProductApp = data.pop('urlProductApp')
        specialText = data.pop('specialText')
        address_json: dict = data.pop('address')
        address = InstitutionAddress.from_dict(address_json)
        phone = data.pop('phone')
        email = data.pop('email')
        currency = data.pop('currency')
        return Institution(
            id=id,
            name=name,
            accountTypeDescription=accountTypeDescription,
            urlHomeApp=urlHomeApp,
            urlLogonApp=urlLogonApp,
            urlProductApp=urlProductApp,
            specialText=specialText,
            address=address,
            phone=phone,
            email=email,
            currency=currency,
            unused_fields=data,
        )
