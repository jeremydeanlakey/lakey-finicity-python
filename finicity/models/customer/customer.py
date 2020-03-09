from dataclasses import dataclass

from typing import Optional


# https://community.finicity.com/s/article/201703219-Customers#customer_record
@dataclass
class Customer(object):
    id: int
    username: str
    firstName: Optional[str]
    lastName: Optional[str]
    type: str
    createdDate: int
    _unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        username = data.pop('username')
        firstName = data.pop('firstName', None)
        lastName = data.pop('lastName', None)
        type = data.pop('type')
        createdDate = data.pop('createdDate')
        return Customer(
            id=id,
            username=username,
            firstName=firstName,
            lastName=lastName,
            type=type,
            createdDate=createdDate,
            _unused_fields=data,
        )
