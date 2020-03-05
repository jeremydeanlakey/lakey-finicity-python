import time
from typing import Optional

from finicity.api_http_client import ApiHttpClient
from finicity.models import TransactionStatus
from finicity.responses.create_customer_response import CreateCustomerResponse
from finicity.responses.create_transaction_response import CreateTransactionResponse


class Testing(object):
    def __init__(self, http_client: ApiHttpClient):
        self.__http_client = http_client

    def add_customer(self, username: str, first_name: str, last_name: str) -> int:
        """
        Enroll a testing customer. A testing customer may only register accounts with FinBank institutions.

        :param username: The customer's username, assigned by the partner (a unique identifier), following these rules:
            minimum 6 characters
            maximum 255 characters
            any mix of uppercase, lowercase, numeric, and non-alphabet special characters ! @ . # $ % & * _ - +
            the use of email in this field is discouraged
            it is recommended to use a unique non-email identifier
            Use of special characters may result in an error (e.g. í, ü, etc.)
        :param first_name: The customer's first name(s) / given name(s) (optional)
        :param last_name: The customer's last name(s) / surname(s) (optional)
        :return: customer id
        """
        # TODO explicitly validate username
        data = {
            'username': username,
            'firstName': first_name,
            'lastName': last_name,
        }
        path = f"/aggregation/v1/customers/testing"
        response = self.__http_client.post(path, data)
        response_dict = response.json()
        return CreateCustomerResponse.from_dict(response_dict).id

    # https://community.finicity.com/s/article/Add-Transaction-for-Testing-Account
    # POST /aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions
    def add_transaction(self, customer_id: int, account_id: str, amount: float, description: str, status: TransactionStatus = TransactionStatus.active, posted_date: Optional[int] = None, transaction_date: Optional[int] = None) -> int:
        """
        Inject a transaction into the transaction list for a testing account. This allows an app to trigger TxPUSH notifications for the account in order to test the app’s TxPUSH Listener service. This causes the platform to send one transaction event and one account event (showing that the account balance has changed). This service is only supported for testing accounts (accounts on institution 101732).

        :param customer_id: The ID of the customer who owns the account
        :param account_id: The Finicity ID of the account whose events will be sent to the TxPUSH Listener
        :param amount: The amount of the transaction
        :param description: The description of the transaction
        :param status: active or pending (optional)
        :param posted_date: An optional timestamp for the transaction's posted date value for this transaction (see Handling Dates and Times). Timestamp must be no more than 6 months from the current date.
        :param transaction_date: An optional timestamp for the transaction's posted date value for this transaction (see Handling Dates and Times)
        :return:
        """
        status = status or TransactionStatus.active
        transaction_date = transaction_date or time.time()
        posted_date = posted_date or time.time()
        # success = 201 created with
        # {
        #   "id": 712054,
        #   "createdDate": 1444259433
        # }
        data = {
            'amount': amount,
            'description': description,
            'status': status.value,
            'transaction_date': transaction_date,
            'posted_date': posted_date,
        }
        path = f"/aggregation/v1/customers/{customer_id}/accounts/{account_id}/transactions"
        response = self.__http_client.post(path, data)
        response_dict = response.json()
        return CreateTransactionResponse.from_dict(response_dict).id

