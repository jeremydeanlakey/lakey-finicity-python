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
    _unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        addressLine1 = data.pop('addressLine1')
        addressLine2 = data.pop('addressLine2')
        city = data.pop('city')
        state = data.pop('state')
        postalCode = data.pop('postalCode')
        country = data.pop('country')
        return InstitutionAddress(
            addressLine1=addressLine1,
            addressLine2=addressLine2,
            city=city,
            state=state,
            postalCode=postalCode,
            country=country,
            _unused_fields=data,
        )
