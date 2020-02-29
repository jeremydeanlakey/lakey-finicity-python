from typing import Optional, List

from finicity.api_http_client import ApiHttpClient
from finicity.models import Institution, Customer
from finicity.queries.institutions_query import InstitutionsQuery


class Customers(object):
    def __init__(self, http_client: ApiHttpClient):
        self.__http_client = http_client

    # Customers

    # https://community.finicity.com/s/article/Get-Customers
    # GET /aggregation/v1/customers?search=[text]&start=[index]&limit=[count]&type=[type]&username=[username]
    def get_customers(self, search_term: str = "*", username: str = None, start: int = 1, limit: int = 25) -> List[Customer]:
        """
        Find all customers enrolled by the current partner, where the search text is found in the customer's username or any combination of firstName and lastName fields. If no search text is provided, return all customers.
        Valid values for type are testing, active.
        If the value of moreAvailable in the response is true, you can retrieve the next page of results by increasing the value of the start parameter in your next request:
        ...&start=6&limit=5

        :param search_term: The text you wish to match. Leave this empty if you wish to return all customers.
        :param username: Username for exact match. (Will return 0 or 1 records.)
        :param start: Starting index for this page of results. The default value is 1.
        :param limit: Maximum number of entries for this page of results. The default value is 25.
        :return:
        """
        # note ripped off search_term: Must be URL-encoded (see Handling Spaces in Queries)
        # also do type = testing / active / [blank for all]
        # self._get_with_token()
        pass

    # GET /aggregation/v1/customers/{customerId}
    def get_customer(self, customer_id: str) -> Customer:
        """
        :param customer_id: ID of the customer
        :return:
        """
        # self._get_with_token()
        pass

    # https://community.finicity.com/s/article/Add-Testing-Customer
    # POST /aggregation/v1/customers/testing
    def add_testing_customer(self, username: str, first_name: str, last_name: str):
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
        :return:
        """
        # Add Testing Customer
        # self._post()
        # response = {
        #    "id": "41442",
        #    "createdDate": "1412792539"
        # }
        # pass
        # self._post()

    # https://community.finicity.com/s/article/Add-Customer
    # POST /aggregation/v1/customers/active
    def add_customer(self, username: str, first_name: str, last_name: str):
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
        # self._post()
        pass

    # https://community.finicity.com/s/article/Modify-Customer
    # PUT /aggregation/v1/customers/{customerId}
    def modify_customer(self, customer_id: str, first_name: str, last_name: str):
        """
        Modify the details for an enrolled customer. You must specify either the first name, the last name, or both in the request.
        If the service is successful, HTTP 204 (No Content) will be returned.

        :param customer_id: ID of the customer to modify
        :param first_name: The customer's first name(s) / given name(s) (optional)
        :param last_name: The customer's last name(s) / surname(s) (optional)
        :return:
        """
        # no content response so no need for accept param
        pass

    # https://community.finicity.com/s/article/Delete-Customer
    # DELETE /aggregation/v1/customers/{customerId}
    def delete_customer(self, customerId: str):
        """
        Completely remove a customer from the system. This will remove the customer and all associated accounts and transactions.
        (Note that the request and response is the same for JSON or XML clients.)
        Use this service carefully! It will not pause for confirmation before performing the operation!

        :param customerId:  ID of the customer to modify
        :return:
        """
        pass
        # needs key and token headers no content response

