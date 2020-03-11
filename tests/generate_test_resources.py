import time

from finicity.models import BirthDate, TransactionStatus
from finicity.models.connect.connect_type import ConnectType
from finicity.models.content_type import ContentType
from finicity.finicity_client import FinicityClient

APP_KEY = 'xxxxxxxxxxxxx'
PARTNER_ID = 'xxxxxxxxxxxxx'
PARTNER_SECRET = 'xxxxxxxxxxxxx'

finicity: FinicityClient = FinicityClient(app_key=APP_KEY, partner_id=PARTNER_ID, partner_secret=PARTNER_SECRET)
username = 'janedoe'
first_name = 'Jane'
last_name = 'Doe'


def save_last_response(path: str):
    path = 'test_resources/' + path
    with open(path, 'wb') as output:
        output.write(finicity._http_client.last_response.content)


# CUSTOMERS

new_customer_id: int = finicity.testing.add_customer(username=username, first_name=first_name, last_name=last_name)
save_last_response('create_customer_response.json')

_ = finicity.customers.get_by_username(username)  # just to catch errors

finicity.customers.get(new_customer_id)
save_last_response('customer.json')

finicity.customers.query().first_or_none()
save_last_response('customer_list_response.json')

new_first_name = first_name.lower()
finicity.customers.modify(new_customer_id, first_name=new_first_name, last_name=last_name)
customer = finicity.customers.get(new_customer_id)
assert(customer.firstName == new_first_name)
assert(customer.firstName != first_name)


# CONSUMERS

consumer_id: str = finicity.consumers.create(
    customer_id=new_customer_id,
    first_name=first_name,
    last_name=last_name,
    address="123 Main St",
    city="Salt Lake City",
    state="Utah",
    zip="84000",
    phone="8012345678",
    ssn="521-43-6987",
    birthday=BirthDate(year=1980, month=1, day_of_month=10),
    email="johndoe@example.com",
)
save_last_response('create_consumer_response.json')

consumer = finicity.consumers.get(consumer_id)
save_last_response('consumer.json')

finicity.consumers.modify(
    consumer_id=consumer_id,
    first_name=new_first_name,
    last_name=consumer.lastName,  # no change
    address=consumer.address,  # no change
    city=consumer.city,  # no change
    state=consumer.state,  # no change
    zip=consumer.zip,  # no change
    phone=consumer.phone,  # no change
    ssn="521-43-6987",  # no change
    birthday=consumer.birthday,  # no change
    email=consumer.email,  # no change
)
consumer = finicity.consumers.get(consumer_id)
assert(consumer.firstName == new_first_name)
assert(consumer.firstName != first_name)

consumer_by_customer = finicity.consumers.get_for_customer(new_customer_id)
assert(consumer_by_customer == consumer)

finicity.customers.delete(new_customer_id)
assert(finicity.customers.get_by_username(username) is None)


# INSTITUTIONS

institutions_qry = finicity.institutions.query('FinBank')
institution = institutions_qry.first_or_none()
save_last_response('institution_list_response.json')

institution = finicity.institutions.get(institution.id)
save_last_response('institution_detail_response.json')


# CONNECTIONS

connect_link: str = finicity.connect.generate_link(
    customer_id=new_customer_id,
    consumer_id=consumer_id,
    link_type=ConnectType.aggregation,
    # webhook_content_type=ContentType.JSON,
    # webhook='https://yoursite.example.com/webhooks/finicity_connect',
    # webhook_data={'value1': 'a', 'value2': 'b'},
    # analytics='google:UA-123456789-1',
)
print(connect_link)
# see https://community.finicity.com/s/article/Finbank-Profiles-A-102105
# Finbank Profiles - A (102105)
# username = Any
# password = profile_03

# TODO
# connect_link: str = finicity.connect.generate_voa_link(
# )


# ACCOUNTS

accounts_by_customer_id = finicity.accounts.get_by_customer_id(new_customer_id)
account = accounts_by_customer_id[0]
save_last_response('accounts_list_response.json')


accounts_by_institution_id = finicity.accounts.get_by_customer_id_and_institution_id(new_customer_id, account.institutionId)

account2 = finicity.accounts.get(new_customer_id, account.id)
assert(account == account2)
save_last_response('account.json')

accounts_by_institution_login_id = finicity.accounts.get_by_institution_login_id(new_customer_id, account.institutionLoginId)
assert(len(accounts_by_institution_login_id) == len(accounts_by_customer_id))

account_details = finicity.accounts.get_details(new_customer_id, account.id)
save_last_response('account_ach_details.json')

# TODO finicity.accounts.get_details_with_mfa_answers()

account_owner = finicity.accounts.get_owner(new_customer_id, account.id)
save_last_response('account_owner.json')

# TODO finicity.accounts.get_owner_with_mfa_answers()

statement = finicity.accounts.get_statement(new_customer_id, account.id)
# with open('test.pdf', 'wb') as output:
#     output.write(statement)

# TODO finicity.accounts.get_statement_with_mfa_answers()

new_account_name = 'test checking'
finicity.accounts.modify(
    customer_id=new_customer_id,
    account_id=account.id,
    number=account.number,
    name=new_account_name,
)
account = finicity.accounts.get(new_customer_id, account.id)
assert(account.name == new_account_name)

finicity.accounts.delete(new_customer_id, account.id)
accounts_after_delete = finicity.accounts.get_by_customer_id(new_customer_id)
assert(len(accounts_by_customer_id) - 1 == len(accounts_after_delete))

# REPORTS

# TODO
# finicity.reports.generate_voa_report()
# finicity.reports.generate_voi_report()
# finicity.reports.get_report_by_consumer()
# finicity.reports.get_report_by_consumer()
# finicity.reports.get_reports_for_consumer()
# finicity.reports.get_reports_for_consumer()


# TRANSACTIONS

now = int(time.time())
ten_days_ago = now - (10 * 24 * 60 * 60)
transactions_qry = finicity.transactions.query(new_customer_id, from_date=ten_days_ago, to_date=now)
transactions_qry.first_or_none()
save_last_response('transactions_list_empty.json')

account = finicity.accounts.get_by_customer_id(new_customer_id)[0]
new_transaction_time = now - 10
transaction_id = finicity.testing.add_transaction(
    customer_id=new_customer_id,
    account_id=account.id,
    amount=42.01,
    description="test transaction",
    status=TransactionStatus.pending,
    posted_date=new_transaction_time,
    transaction_date=new_transaction_time,
)
save_last_response('create_transaction_response.json')

transactions_qry = finicity.transactions.query(new_customer_id, from_date=ten_days_ago, to_date=now)
transactions_qry.first_or_none()
save_last_response('transactions_list_test.json')

finicity.transactions.load_historic_transactions_for_account(new_customer_id, account.id)
# TODO finicity.transactions.load_historic_transactions_for_account_with_mfa_answers()

account = finicity.accounts.get_by_customer_id(new_customer_id)[0]
accounts = finicity.transactions.refresh_institution_login_accounts(
    customer_id=new_customer_id,
    institution_login_id=account.institutionLoginId,
)
save_last_response('accounts_list_response_2.json')

finicity.transactions.refresh_customer_accounts(new_customer_id)
save_last_response('accounts_list_response_3.json')

# TODO finicity.transactions.enable_push_notifications()
# TODO finicity.transactions.disable_push_notifications()
# TODO finicity.transactions.delete_push_subscription()
