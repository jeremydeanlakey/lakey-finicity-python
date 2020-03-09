from dataclasses import dataclass


# https://community.finicity.com/s/article/Get-Customer-Account-Details
@dataclass
class AccountAchDetails(object):
    routingNumber: str  # The account's 9-digit Routing Transit Number
    realAccountNumber: str  # The full account number, assigned by the institution
    _unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        routingNumber = data.pop('routingNumber')
        realAccountNumber = data.pop('realAccountNumber')
        return AccountAchDetails(
            routingNumber=routingNumber,
            realAccountNumber=realAccountNumber,
            _unused_fields=data,
        )
