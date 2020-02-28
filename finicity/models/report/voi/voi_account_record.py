from dataclasses import dataclass
from typing import List

from finicity.models.report.transaction_record import TransactionRecord
from finicity.models.report.voi.income_stream_record import IncomeStreamRecord
from finicity.models.report.voi.miscellaneous_deposit_record import MiscellaneousDepositRecord


@dataclass
class VoiAccountRecord(object):
    id: int  # Finicity account ID
    number: str  # The account number from the institution (obfuscated)
    ownerName: str  # The name(s) of the account owner(s). This field is optional. If no owner information is available, this field will not appear in the report.
    ownerAddress: str  # The mailing address of the account owner(s). This field is optional. If no owner information is available, this field will not appear in the report.
    name: str  # The account name from the institution
    type: str  # VOI: checking / savings / moneyMarket
    aggregationStatusCode: int  # Finicity aggregation status of the most recent aggregation attempt for this account (non-zero means the account was not accessed successfully for this report, and additional fields for this account may not be reliable)
    # institutionLoginId: str  # The institutionLoginId (represents one set of credentials at a particular institution, together with all accounts accessible using those credentials at that institution)
    transactions: List[TransactionRecord]  # A list of all transaction records for this account during the report period (VOI report includes deposit transactions only)
    miscDeposits: List[MiscellaneousDepositRecord]  # A list of miscellaneous deposit records
    incomeStreams: List[IncomeStreamRecord]  # A list of income stream records
    unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        number = data.pop('number')
        ownerName = data.pop('ownerName')
        ownerAddress = data.pop('ownerAddress')
        name = data.pop('name')
        type = data.pop('type')
        aggregationStatusCode = data.pop('aggregationStatusCode')
        # institutionLoginId = data.pop('institutionLoginId')
        transactions_raw = data.pop('transactions')
        transactions = [TransactionRecord.from_dict(d) for d in transactions_raw]
        miscDeposits_raw = data.pop('miscDeposits')
        miscDeposits = [MiscellaneousDepositRecord.from_dict(d) for d in miscDeposits_raw]
        incomeStreams_raw = data.pop('incomeStreams')
        incomeStreams = [IncomeStreamRecord.from_dict(d) for d in incomeStreams_raw]
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
            unused_fields=data,
        )
