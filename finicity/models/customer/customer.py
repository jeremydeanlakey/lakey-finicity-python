from dataclasses import dataclass


# https://community.finicity.com/s/article/201703219-Customers#customer_record
@dataclass
class Customer(object):
    id: int
    username: str
    firstName: str
    lastName: str
    type: str
    createdDate: int
