from dataclasses import dataclass


@dataclass
class CreateConsumerResponse(object):
    id: str
    createdDate: int

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        createdDate = data.pop('createdDate')
        return CreateConsumerResponse(
            id=id,
            createdDate=createdDate,
        )

# example responses:
# {
#   "id": "0h7h3r301md83",
#   "createdDate": 1472342400
# }
