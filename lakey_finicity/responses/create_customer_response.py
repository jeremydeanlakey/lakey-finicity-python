from dataclasses import dataclass


@dataclass
class CreateCustomerResponse(object):
    id: int
    createdDate: int
    _unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = int(data.pop('id'))
        createdDate = data.pop('createdDate')
        return CreateCustomerResponse(
            id=id,
            createdDate=createdDate,
            _unused_fields=data,
        )
