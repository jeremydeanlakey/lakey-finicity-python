from dataclasses import dataclass
from finicity.models.birth_date import BirthDate


# https://community.finicity.com/s/article/Report-Consumers
@dataclass
class ReportConsumer(object):
    id: str  # ID of the consumer (UUID with max length 32 characters)
    firstName: str  # The consumer's first name(s) / given name(s)
    lastName: str  # The consumer's last name(s) / surname(s)
    address: str  # The consumer's street address
    city: str  # The consumer's city
    state: str  # The consumer's state
    zip: str  # The consumer's ZIP code
    phone: str  # The consumer's phone number
    ssn: str  # Last 4 digits of the consumer's Social Security number
    birthday: BirthDate  # The consumer's birth date
    email: str  # The consumer's email address
    createdDate: int  # A timestamp of when the consumer was created
    unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        firstName = data.pop('firstName')
        lastName = data.pop('lastName')
        address = data.pop('address')
        city = data.pop('city')
        state = data.pop('state')
        zip = data.pop('zip')
        phone = data.pop('phone')
        ssn = data.pop('ssn')
        birthday = data.pop('birthday')
        email = data.pop('email')
        createdDate = data.pop('createdDate')
        return ReportConsumer(
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
            unused_fields=data,
        )
