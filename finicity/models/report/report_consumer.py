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
