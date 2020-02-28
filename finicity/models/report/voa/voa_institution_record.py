from dataclasses import dataclass
from typing import List

from finicity.models.report.voa.voa_account_record import VoaAccountRecord


@dataclass
class VoaInstitutionRecord(object):
    unused_fields: dict  # this is for forward compatibility and should be empty
    id: int
    name: str
    accounts: List[VoaAccountRecord]

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        name = data.pop('name')
        accounts_raw = data.pop('accounts')
        accounts = [VoaAccountRecord.from_dict(d) for d in accounts_raw]
        return VoaInstitutionRecord(
            id=id,
            name=name,
            accounts=accounts,
            unused_fields=data,
        )
