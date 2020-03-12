from dataclasses import dataclass
from typing import Optional


# https://community.finicity.com/s/article/202460245-Transactions
@dataclass
class TransactionCategorization(object):
    normalizedPayeeName: Optional[str]  # A normalized payee, derived from the transaction's description and memo fields.
    category: Optional[str]  # One of the values from Categories (assigned based on the payee name)
    bestRepresentation: Optional[str]  # Combines the description and memo data together, removes any duplicated information from description to memo, and removes any numbers or special characters
    country: Optional[str]  # Country where the transaction occurred
    state: Optional[str]  # State of transaction (if available)
    city: Optional[str]  # City of transaction (if available)
    _unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        normalizedPayeeName = data.pop('normalizedPayeeName', None)
        category = data.pop('category', None)
        bestRepresentation = data.pop('bestRepresentation', None)
        country = data.pop('country', None)
        state = data.pop('state', None)
        city = data.pop('city', None)
        return TransactionCategorization(
            normalizedPayeeName=normalizedPayeeName,
            category=category,
            bestRepresentation=bestRepresentation,
            country=country,
            state=state,
            city=city,
            _unused_fields=data,
        )
