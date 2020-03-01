from dataclasses import dataclass


@dataclass
class CreateReportResponse(object):
    accountIds: str

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        accountIds = data.pop('accountIds')
        return CreateReportResponse(
            accountIds=accountIds,
        )
