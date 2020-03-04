# Disclaimer

This library was not made by Finicity.

# Client

The Client class handles authentication, endpoints, and mapping json responses to models.

```python
finicity = Client(PARTNER_ID, PARTNER_SECRET, APP_KEY)
```

# Customers

```python
new_customer_id: int = finicity.customers.add(username='jane_doe', first_name='John', last_name='Doe')

new_customer: Customer = finicity.customers.get(new_customer_id)

finicity.customers.modify(new_customer_id, first_name="John", last_name="Smith")

finicity.customers.delete(new_customer_id)
```

# Report Consumers

```python
consumer_id_for_new_customer: str = finicity.consumers.create(
    customer_id=new_customer_id,
    firstName="John",
    lastName="Doe",
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
    firstName="John",
    lastName="Doe",
    address="123 Main St",
    city="Salt Lake City",
    state="Utah",
    zip="84000",
    phone="8012345678",
    ssn="521-43-6987",
    birthday=BirthDate(year=1980, month=1, day_of_month=10),
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

# Transactions

TODO

# Reports

TODO

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

TODO
