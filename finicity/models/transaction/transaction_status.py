import enum


# https://community.finicity.com/s/article/202460245-Transactions
class TransactionStatus(enum.Enum):
    active = "active"
    pending = "pending"
    shadow = "shadow"
