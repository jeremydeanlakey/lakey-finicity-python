from dataclasses import dataclass
from typing import Optional

from finicity.models.institution.institution_address import InstitutionAddress


@dataclass
class Institution(object):
    id: int  # The institution ID
    name: str  # The name of the institution
    aha: bool
    accountTypeDescription: Optional[str]
    phone: str  # The institution's primary phone number
    urlHomeApp: str  # The URL of the institution's primary home page
    urlLogonApp: str  # The URL of the institution's login page
    oauthEnabled: bool
    urlForgotPassword: str
    urlOnlineRegistration: Optional[str]
    institution_class: str
    specialText: str  # Any special text found on the institution's website
    address: InstitutionAddress
    email: str  # The institution's primary contact email
    currency: str  # The institution's primary currency
    oauthInstitutionId: Optional[int]
    unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        name = data.pop('name')
        aha = data.pop('aha')
        accountTypeDescription: str = data.pop('accountTypeDescription')
        urlHomeApp = data.pop('urlHomeApp')
        urlLogonApp = data.pop('urlLogonApp')
        oauthEnabled = data.pop('oauthEnabled')
        specialText = data.pop('specialText')
        address_json: dict = data.pop('address')
        address = InstitutionAddress.from_dict(address_json)
        phone = data.pop('phone')
        email = data.pop('email')
        currency = data.pop('currency')
        institution_class = data.pop('class')
        urlForgotPassword = data.pop('urlForgotPassword')
        urlOnlineRegistration = data.pop('urlOnlineRegistration', None)
        oauthInstitutionId = data.pop('oauthInstitutionId', None)
        return Institution(
            id=id,
            name=name,
            aha=aha,
            accountTypeDescription=accountTypeDescription,
            urlHomeApp=urlHomeApp,
            urlLogonApp=urlLogonApp,
            oauthEnabled=oauthEnabled,
            specialText=specialText,
            address=address,
            phone=phone,
            email=email,
            currency=currency,
            unused_fields=data,
            institution_class=institution_class,
            oauthInstitutionId=oauthInstitutionId,
            urlForgotPassword=urlForgotPassword,
            urlOnlineRegistration=urlOnlineRegistration,
        )
