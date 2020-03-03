# Disclaimer

This library was not made by Finicity.

# Client

The Client class handles authentication, endpoints, and mapping json responses to models.

```python
finicity = Client(APP_KEY, PARTNER_ID, PARTNER_SECRET)
```

# Customers

```python
new_customer_id: int = finicity.customers.add(username='jane_doe', first_name='John', last_name='Doe')

new_customer: Customer = finicity.customers.get(new_customer_id)

finicity.customers.modify(new_customer_id, first_name="John", last_name="Smith")

finicity.customers.delete(new_customer_id)
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
