import enum


# https://community.finicity.com/s/article/204819879-Transaction-Types
class TransactionType(enum.Enum):
    unknown = "unknown"  # "No <type> element present" No type provided by institution
    atm = "atm"  # ATM debit or credit (depends on signage of amount)
    cash = "cash"  # Cash withdrawal
    check = "check"  # Check
    credit = "credit"  # Generic credit
    debit = "debit"  # Generic debit
    deposit = "deposit"  # Deposit
    directDebit = "directDebit"  # Merchant initiated debit
    directDeposit = "directDeposit"  # Direct deposit
    dividend = "dividend"  # Dividend
    fee = "fee"  # Institution fee
    interest = "interest"  # Interest earned or paid (depends on signage of amount)
    other = "other"  # Type is not known or doesn't match types available in this list
    payment = "payment"  # Electronic payment
    pointOfSale = "pointOfSale"  # Point of sale debit or credit (depends on signage of amount)
    repeatPayment = "repeatPayment"  # Repeating payment/standing order
    serviceCharge = "serviceCharge"  # Service charge
    transfer = "transfer"  # Transfer

    @staticmethod
    def from_description(description):
        if description == 'No <type> element present':
            return TransactionType.unknown
        else:
            return TransactionType(description)
