from dataclasses import dataclass
from typing import List, Optional

from lakey_finicity.models.report.transaction_record import TransactionRecord
from lakey_finicity.models.report.voi.income_stream_record import IncomeStreamRecord
from lakey_finicity.models.report.voi.miscellaneous_deposit_record import MiscellaneousDepositRecord


@dataclass
class VoiAccountRecord(object):
    id: int  # Finicity account ID
    number: Optional[str]  # The account number from the institution (obfuscated)
    ownerName: Optional[str]  # The name(s) of the account owner(s). This field is optional. If no owner information is available, this field will not appear in the report.
    ownerAddress: Optional[str]  # The mailing address of the account owner(s). This field is optional. If no owner information is available, this field will not appear in the report.
    name: Optional[str]  # The account name from the institution
    type: Optional[str]  # VOI: checking / savings / moneyMarket
    aggregationStatusCode: Optional[int]  # Finicity aggregation status of the most recent aggregation attempt for this account (non-zero means the account was not accessed successfully for this report, and additional fields for this account may not be reliable)
    # institutionLoginId: Optional[str]  # The institutionLoginId (represents one set of credentials at a particular institution, together with all accounts accessible using those credentials at that institution)
    transactions: Optional[List[TransactionRecord]]  # A list of all transaction records for this account during the report period (VOI report includes deposit transactions only)
    miscDeposits: Optional[List[MiscellaneousDepositRecord]]  # A list of miscellaneous deposit records
    incomeStreams: Optional[List[IncomeStreamRecord]]  # A list of income stream records
    _unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        number = data.pop('number', None)
        ownerName = data.pop('ownerName', None)
        ownerAddress = data.pop('ownerAddress', None)
        name = data.pop('name', None)
        type = data.pop('type', None)
        aggregationStatusCode = data.pop('aggregationStatusCode', None)
        # institutionLoginId = data.pop('institutionLoginId', None)
        transactions_raw = data.pop('transactions', [])
        transactions = [TransactionRecord.from_dict(d) for d in transactions_raw]
        miscDeposits_raw = data.pop('miscDeposits', None)
        miscDeposits = [MiscellaneousDepositRecord.from_dict(d) for d in miscDeposits_raw] if miscDeposits_raw else None
        incomeStreams_raw = data.pop('incomeStreams', None)
        incomeStreams = [IncomeStreamRecord.from_dict(d) for d in incomeStreams_raw] if incomeStreams_raw else None
        return VoiAccountRecord(
            id=id,
            number=number,
            ownerName=ownerName,
            ownerAddress=ownerAddress,
            name=name,
            type=type,
            aggregationStatusCode=aggregationStatusCode,
            # institutionLoginId=institutionLoginId,
            transactions=transactions,
            miscDeposits=miscDeposits,
            incomeStreams=incomeStreams,
            _unused_fields=data,
        )
