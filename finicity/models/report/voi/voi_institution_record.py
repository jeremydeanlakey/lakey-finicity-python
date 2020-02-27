from dataclasses import dataclass
from typing import List, Optional

from finicity.models.report.voi.voi_account_record import VoiAccountRecord


@dataclass
class VoiInstitutionRecord(object):
    unused_fields: dict  # this is for forward compatibility and should be empty
    id: int
    name: str
    urlHomeApp: Optional[str]  # voa only
    accounts: List[VoiAccountRecord]

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        name = data.pop('name')
        urlHomeApp = data.pop('urlHomeApp', None)
        accounts = data.pop('accounts')
        return VoiInstitutionRecord(
            id=id,
            name=name,
            urlHomeApp=urlHomeApp,
            accounts=accounts,
            unused_fields=data,
        )
