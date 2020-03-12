from dataclasses import dataclass
from typing import Optional

from lakey_finicity.models.birth_date import BirthDate


# https://community.finicity.com/s/article/Report-Consumers
@dataclass
class Consumer(object):
    id: str  # ID of the consumer (UUID with max length 32 characters)
    firstName: Optional[str]  # The consumer's first name(s) / given name(s)
    lastName: Optional[str]  # The consumer's last name(s) / surname(s)
    address: Optional[str]  # The consumer's street address
    city: Optional[str]  # The consumer's city
    state: Optional[str]  # The consumer's state
    zip: Optional[str]  # The consumer's ZIP code
    phone: Optional[str]  # The consumer's phone number
    ssn: Optional[str]  # Last 4 digits of the consumer's Social Security number
    birthday: Optional[BirthDate]  # The consumer's birth date
    email: Optional[str]  # The consumer's email address
    createdDate: Optional[int]  # A timestamp of when the consumer was created
    _unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        firstName = data.pop('firstName', None)
        lastName = data.pop('lastName', None)
        address = data.pop('address', None)
        city = data.pop('city', None)
        state = data.pop('state', None)
        zip = data.pop('zip', None)
        phone = data.pop('phone', None)
        ssn = data.pop('ssn', None)
        birthday_dict = data.pop('birthday', None)
        birthday = BirthDate.from_dict(birthday_dict) if birthday_dict else None
        email = data.pop('email', None)
        createdDate = data.pop('createdDate', None)
        return Consumer(
            id=id,
            firstName=firstName,
            lastName=lastName,
            address=address,
            city=city,
            state=state,
            zip=zip,
            phone=phone,
            ssn=ssn,
            birthday=birthday,
            email=email,
            createdDate=createdDate,
            _unused_fields=data,
        )
