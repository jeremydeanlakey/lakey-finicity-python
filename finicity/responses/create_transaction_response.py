from dataclasses import dataclass


@dataclass
class CreateTransactionResponse(object):
    id: int
    createdDate: int

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        createdDate = data.pop('createdDate')
        return CreateTransactionResponse(
            id=id,
            createdDate=createdDate,
        )
