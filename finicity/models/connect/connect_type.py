import enum


class ConnectType(enum.Enum):
    ach = 'ach'  # Automated Clearing House : Used to verify account balance, routing number and full account number.
    aggregation = 'aggregation'  # Aggregation Only : Used by PFM (Personal Financial Management) partners to grant access to a customer's transactions.
    fix = 'fix'  # Fix : Used to resolve authentication challenges and credential mismatch.
    lite = 'lite'  # Lite : Provides FI authentication and adding accounts. Allows for custom styling, control of the FI search experience, and does not end with a report generation call.
    trade_stream = 'tradestream'  # Tradestream : Used by Experian Boost
    voa = 'voa'  # Verification of Assets : Used by lenders to verify assets. The default time period of data retrieved is 6 months, so that lenders can reduce their liability.
    voa_history = 'voa-history'  # Verification of Assets with History : Used by the GSEs to verify assets. This differs from normal VOA in that it uses up to 2 years of data.
    voi = 'voi'  # Verification of Income : Used by lenders to verify a customer's income using their bank transaction history.
    voi_pp = 'voi-pp'  # Verification of Income from Payment Processor : Used by lenders to verify a customer's income using their payroll processor.
