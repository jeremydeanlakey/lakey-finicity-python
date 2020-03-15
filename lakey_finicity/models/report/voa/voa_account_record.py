from dataclasses import dataclass
from typing import List, Optional

from lakey_finicity.models.report.transaction_record import TransactionRecord
from lakey_finicity.models.report.voa.account_asset_record import AccountAssetRecord
from lakey_finicity.models.report.voa.details_record import DetailsRecord


@dataclass
class VoaAccountRecord(object):
    id: int  # Finicity account ID
    number: str  # The account number from the institution (obfuscated)
    ownerName: Optional[str]  # The name(s) of the account owner(s). This field is optional. If no owner information is available, this field will not appear in the report.
    ownerAddress: Optional[str]  # The mailing address of the account owner(s). This field is optional. If no owner information is available, this field will not appear in the report.
    name: Optional[str]  # The account name from the institution
    type: Optional[str]  # VOA: checking / savings / moneyMarket / cd / investment*
    aggregationStatusCode: Optional[int]  # Finicity aggregation status of the most recent aggregation attempt for this account (non-zero means the account was not accessed successfully for this report, and additional fields for this account may not be reliable)
    # institutionLoginId: str  # The institutionLoginId (represents one set of credentials at a particular institution, together with all accounts accessible using those credentials at that institution)
    transactions: List[TransactionRecord]  # A list of all transaction records for this account during the report period (VOI report includes deposit transactions only)
    asset: Optional[AccountAssetRecord]  # An asset record for the account
    details: Optional[DetailsRecord]  # A details record for the account
    availableBalance: Optional[float]  # The available balance for the account
    balance: Optional[float]  # The cleared balance of the account as-of balanceDate
    balanceDate: Optional[int]  # A timestamp showing when the balance was captured
    averageMonthlyBalance: Optional[float]  # The average monthly balance of this account
    _unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        id = data.pop('id')
        number = data.pop('number')
        ownerName = data.pop('ownerName', None)
        ownerAddress = data.pop('ownerAddress', None)
        name = data.pop('name', None)
        type = data.pop('type', None)
        aggregationStatusCode = data.pop('aggregationStatusCode', None)
        # institutionLoginId = data.pop('institutionLoginId')
        transactions_raw = data.pop('transactions', None)
        transactions = [TransactionRecord.from_dict(d) for d in transactions_raw] if transactions_raw else []
        asset_raw = data.pop('asset', None)
        asset = AccountAssetRecord.from_dict(asset_raw) if asset_raw else None
        details_raw = data.pop('details', None)
        details = DetailsRecord.from_dict(details_raw) if details_raw else None
        availableBalance = data.pop('availableBalance', None)
        balance = data.pop('balance', None)
        balanceDate = data.pop('balanceDate', None)
        averageMonthlyBalance = data.pop('averageMonthlyBalance', None)
        return VoaAccountRecord(
            id=id,
            number=number,
            ownerName=ownerName,
            ownerAddress=ownerAddress,
            name=name,
            type=type,
            aggregationStatusCode=aggregationStatusCode,
            # institutionLoginId=institutionLoginId,
            transactions=transactions,
            asset=asset,
            details=details,
            availableBalance=availableBalance,
            balance=balance,
            balanceDate=balanceDate,
            averageMonthlyBalance=averageMonthlyBalance,
            _unused_fields=data,
        )
