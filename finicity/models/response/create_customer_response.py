from dataclasses import dataclass


@dataclass
class CreateCustomerResponse(object):
    id: str
    createdDate: int

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        createdDate = data.pop('createdDate')
        return CreateCustomerResponse(
            id=id,
            createdDate=createdDate,
        )
