from dataclasses import dataclass
from typing import Optional


# https://community.finicity.com/s/article/202460245-Transactions
@dataclass
class TransactionCategorization(object):
    normalizedPayeeName: str  # A normalized payee, derived from the transaction's description and memo fields.
    category: str  # One of the values from Categories (assigned based on the payee name)
    bestRepresentation: str  # Combines the description and memo data together, removes any duplicated information from description to memo, and removes any numbers or special characters
    country: str  # Country where the transaction occurred
    state: Optional[str]  # State of transaction (if available)
    city: Optional[str]  # City of transaction (if available)
