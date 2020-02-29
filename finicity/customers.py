from typing import Optional

from finicity.api_http_client import ApiHttpClient
from finicity.models import Customer
from finicity.models.response.create_customer_response import CreateCustomerResponse


class Customers(object):
    def __init__(self, http_client: ApiHttpClient):
        self.__http_client = http_client

    def get(self, customer_id: str) -> Customer:
        """
        :param customer_id: ID of the customer
        :return:
        """
        path = f"/aggregation/v1/customers/{customer_id}"
        response = self.__http_client.get(path)
        response_dict = response.json()
        return Customer.from_dict(response_dict)

    # https://community.finicity.com/s/article/Add-Customer
    def add(self, username: str, first_name: str, last_name: str):
        """
        Enroll an active customer (the actual owner of one or more real-world accounts). The customer's account transactions will be refreshed every night.
        This service is not available from the Test Drive. Calls to this service before enrolling in a paid plan will return HTTP 429 (Too Many Requests).

        :param username: The customer's username, assigned by the partner (a unique identifier), following these rules:
            minimum 6 characters
            maximum 255 characters
            any mix of uppercase, lowercase, numeric, and non-alphabet special characters ! @ . # $ % & * _ - +
            the use of email in this field is discouraged
            it is recommended to use a unique non-email identifier
            Use of special characters may result in an error (e.g. í, ü, etc.)
        :param first_name: The customer's first name(s) / given name(s) (optional)
        :param last_name: The customer's last name(s) / surname(s) (optional)
        :return:
        """
        # TODO explicitly validate username
        data = {
            'username': username,
            'firstName': first_name,
            'lastName': last_name,
        }
        path = f"/aggregation/v1/customers/active"
        response = self.__http_client.post(path, data)
        response_dict = response.json()
        return CreateCustomerResponse.from_dict(response_dict).id

    # https://community.finicity.com/s/article/Modify-Customer
    def modify(self, customer_id: str, first_name: Optional[str], last_name: Optional[str]):
        """
        Modify the details for an enrolled customer. You must specify either the first name, the last name, or both in the request.
        If the service is successful, HTTP 204 (No Content) will be returned.

        :param customer_id: ID of the customer to modify
        :param first_name: The customer's first name(s) / given name(s) (optional)
        :param last_name: The customer's last name(s) / surname(s) (optional)
        :return:
        """
        path = f"/aggregation/v1/customers/{customer_id}"
        data = {}
        if first_name:
            data['firstName'] = first_name
        if first_name:
            data['lastName'] = last_name
        self.__http_client.put(path, data=data)

    # https://community.finicity.com/s/article/Delete-Customer
    def delete(self, customer_id: str):
        """
        Completely remove a customer from the system. This will remove the customer and all associated accounts and transactions.
        (Note that the request and response is the same for JSON or XML clients.)
        Use this service carefully! It will not pause for confirmation before performing the operation!

        :param customer_id:  ID of the customer to delete
        :return:
        """
        path = f"/aggregation/v1/customers/{customer_id}"
        self.__http_client.delete(path)

