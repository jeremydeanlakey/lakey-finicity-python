# Disclaimer

This library was made by a third party, not Finicity.  It is still being polished up before being production-ready but is ready to toy with.

# Quickstart

First, sign up for a free/testing account at https://developer.finicity.com/ to get your partner-id, partner-secret, and app-key.

Next, install the library:

```
pip3 install lakey-finicity
```

Then in python, do imports, create a client, and create a test customer and consumer:

```python
from lakey_finicity.models.birth_date import BirthDate
from lakey_finicity.models.connect.connect_type import ConnectType
from lakey_finicity.finicity_client import FinicityClient


PARTNER_ID = 'xxxxxx'  # see https://developer.finicity.com/
PARTNER_SECRET = 'xxxxxx'  # see https://developer.finicity.com/
APP_KEY = 'xxxxxx'  # see https://developer.finicity.com/

finicity = FinicityClient(PARTNER_ID, PARTNER_SECRET, APP_KEY)


customer_id = finicity.testing.add_customer(
    username='jane_doe',
    first_name='John',
    last_name='Doe'
)


consumer_id = finicity.consumers.create(
    customer_id=customer_id,
    first_name="John",
    last_name="Doe",
    address="123 Main St",
    city="Salt Lake City",
    state="Utah",
    zip="84000",
    phone="8012345678",
    ssn="521-43-6987",
    birthday=BirthDate(year=1980, month=1, day_of_month=10),
    email="johndoe@example.com",
)

connect_link: str = finicity.connect.generate_link(
    customer_id=customer_id,
    consumer_id=consumer_id,
    link_type=ConnectType.aggregation,
)

print(connect_link)
```

Now connect accounts with Finicity Connect:
- open that link
- accept terms
- search for & select "Finbank Profiles - A"
- username: Any, password: profile_02


Now you can create test transactions and query transactions:

```python
accounts = finicity.accounts.get_by_customer_id(customer_id)

test_transaction_id = finicity.testing.add_transaction(
    customer_id=customer_id,
    account_id=accounts[0].id,
    amount=5.23,
    description="test tx",
    posted_date=1584006412,  # epoch seconds
    transaction_date=1584006412,  # epoch seconds
)


qry = finicity.transactions.query(
    customer_id=customer_id,
    from_date=1460621294,  # epoch seconds
    to_date=1584006413,  # epoch seconds
)

print(f"Found {qry.count()} transactions.")

for transaction in qry.iter():
    print(transaction)
```

...and clean up.

```python
finicity.customers.delete(customer_id)
```

And that's it.  See below for more capabilities.

# Client

The Client class handles authentication and token expiration, endpoints, retries, headers, formatting, and mapping json responses to models.

```python
finicity = FinicityClient(PARTNER_ID, PARTNER_SECRET, APP_KEY)
```

# Customers

```python
new_customer_id: int = finicity.customers.add(username='jane_doe', first_name='John', last_name='Doe')

new_customer: Customer = finicity.customers.get(new_customer_id)

new_customer = finicity.customers.get_by_username(new_customer.username)

qry = finicity.customers.query("john")
new_customer = qry.first_or_none()

for customer in qry.iter():
    pass

customer_count_with_name_john = qry.count()

finicity.customers.modify(new_customer_id, first_name="John", last_name="Smith")

finicity.customers.delete(new_customer_id)
```

# Report Consumers

```python
consumer_id_for_new_customer: str = finicity.consumers.create(
    customer_id=new_customer_id,
    first_name="John",
    last_name="Doe",
    address="123 Main St",
    city="Salt Lake City",
    state="Utah",
    zip="84000",
    phone="8012345678",
    ssn="521-43-6987",
    birthday=BirthDate(year=1980, month=1, day_of_month=10),
    email="johndoe@example.com",
)

consumer: Consumer= finicity.customers.get(consumer_id_for_new_customer)

finicity.consumer.get(consumer_id_for_new_customer)

finicity.consumer.get_for_customer(new_customer_id)

finicity.consumers.modify(
    consumer_id=consumer_id_for_new_customer,
    first_name="John",
    last_name="Doe",
    address="123 Main St",
    city="Salt Lake City",
    state="Utah",
    zip="84000",
    phone="8012345678",
    ssn="521-43-6987",
    birthday=BirthDate(year=1980, month=1, day_of_month=10),
    email="johndoe@example.com",
)
```

# Institutions

```python
institution = finicity.institutions.get(12345)

query = finicity.institutions.get("Bank of America")

for institution in query.iter():
    print(institution.name)

for institution_list in query.batches():
    pass
```

# Connect

```python
connect_link: str = finicity.connect.generate_link(
    customer_id=new_customer_id,
    consumer_id=consumer_id_for_new_customer,
    link_type=ConnectType.aggregation,
    webhook_content_type=ContentType.JSON,
    webhook='https://yoursite.example.com/webhooks/finicity_connect',
    webhook_data={'value1': 'a', 'value2': 'b'},
    analytics='google:UA-123456789-1',
)
```

# Accounts

```python
accounts: List[Account] = finicity.accounts.get_by_customer_id(
    customer_id=new_customer_id,
    include_pending=True,
)

accounts: List[Account] = finicity.accounts.get_by_customer_id_and_institution_id(
    customer_id=customer_id,
    institution_id=institution_id,
)

account: Account = finicity.accounts.get(
    customer_id=customer_id,
    account_id: str
)

finicity.accounts.modify(
    customer_id=customer_id,
    account_id=account_id,
    number="123456,
    name="main account",
)

finicity.accounts.delete(customer_id=customer_id, account_id=account_id):

accounts: List[Account] = finicity.accounts.get_by_institution_login_id(
    customer_id=customer_id,
    institution_login_id=institution_login_id,
)

details: AccountDetailResponse = finicity.accounts.get_details(
    customer_id=customer_id,
    account_id=account_id,
)

answered_mfa_questions: List[AnsweredMfaQuestion] = [q.answer('bob') for q in questions]

details: AccountDetailResponse = finicity.accounts.get_details_with_mfa_answers(
    customer_id=customer_id,
    account_id=account_id,
    questions=answered_mfa_questions,
)

owner: AccountOwner = finicity.accounts.get_owner(
    customer_id=customer_id,
    account_id=account_id,
)

owner: AccountOwner = finicity.accounts.get_owner_with_mfa_answers(
    customer_id=customer_id,
    account_id=account_id,
    questions=questions,
)

pdf: bytes = finicity.accounts.get_statement(
    customer_id=customer_id,
    account_id=account_id,
)

pdf: bytes = finicity.accounts.get_statement_with_mfa_answers(
    customer_id=customer_id,
    account_id=account_id,
    questions=questions,
)
```

# Transactions

```python
query = finicity.transactions.query(
    customer_id=customer_id,
    from_date=1494449017,
    to_date=1494449017,
    sort=SortOrder.asc,
    include_pending=True,
    account_id=account_id,
)

for transaction in query.iter():
    print(transaction.description)

for transaction_list in query.batches():
    pass

subscriptions: List[SubscriptionRecord] = finicity.transactions.enable_push_notifications(
    customer_id=customer_id,
    account_id=account_id,
    callback_url='https://yoursite.example.com/webhooks/transactions',
)

finicity.transactions.disable_push_notifications(
    customer_id=customer_id,
    account_id=account_id,
)

finicity.transactions.delete_push_subscription(
    customer_id=customer_id,
    subscription_id=subscription_id,
)

finicity.transactions.load_historic_transactions_for_account(
    customer_id=customer_id,
    account_id=account_id,
)

finicity.transactions.load_historic_transactions_for_account_with_mfa_answers(
    mfaSession=mfaSession,
    customer_id=customer_id,
    account_id=account_id,
    questions=answered_mfa_questions,
)

finicity.transactions.refresh_customer_accounts(customer_id)

finicity.transactions.refresh_institution_login_accounts(
    customer_id=customer_id,
    institution_login_id=institution_login_id,
)
```

# Reports

```python
report_id = finicity.reports.generate_voa_report(
    customer_id=new_customer_id,
    callback_url='https://yoursite.example.com/webhooks/finicity_report',
    from_date=1494449017,
    accountIds=account_ids,
)

report_id = finicity.reports.generate_voi_report(
    customer_id=new_customer_id,
    callback_url='https://yoursite.example.com/webhooks/finicity_report',
    accountIds=account_ids,
)

finicity.reports.get_reports_for_customer(new_customer_id)

finicity.reports.get_reports_for_consumer(consumer_id_for_new_customer)

finicity.reports.get_report_by_consumer(
    consumer_id=consumer_id_for_new_customer,
    report_id=report_id,
    purpose=PermissiblePurpose.CODE_12,
)

finicity.reports.get_report_by_customer(
    customer_id=new_customer_id,
    report_id=report_id,
    purpose=PermissiblePurpose.CODE_12,
)
```

# Testing

```python
test_customer_id: int = finicity.testing.add_customer(
    username='jane_doe',
    first_name='John',
    last_name='Doe'
)

test_transaction_id: int = finicity.testing.add_transaction(
    customer_id=test_customer_id,
    account_id=test_account_id,
    amount=5.23,
    description="test tx",
    status=TransactionStatus.active,
    posted_date=1460621294,
    transaction_date=1460621294
)
```
