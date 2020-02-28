import time
from typing import List, Optional

import requests
from requests import Response

from finicity.models import Institution, Customer, Account, Transaction, SortOrder, BirthDate, ReportConsumer, \
    PermissiblePurpose, TransactionStatus, AnsweredMfaQuestion, AccountOwner
from finicity.models.response.account_detail_response import AccountDetailResponse
from finicity.utils import validate_secret


# https://docs.finicity.com/guide-to-partner-authentication-and-integration/
_FINICITY_URL_BASE = "https://api.finicity.com"
_TWO_HOURS_S = 60 * 60


class Client(object):
    def __init__(self, app_key: str, partner_id: str, partner_secret: str):
        """

        :param app_key: Finicity-App-Key from Developer Portal
        :param partner_id: Partner ID from Developer Portal
        :param partner_secret: Current value of Partner Secret from Developer Portal
        """
        self.__app_key = app_key
        self.__partner_id = partner_id
        self.__secret = partner_secret
        self.__token = None
        self.__token_expiration = 0

    def _get(self, path: str, params: Optional[dict] = None, extra_headers: Optional[dict] = None) -> Response:
        url = _FINICITY_URL_BASE + path
        token = self._get_token()
        headers = {
            "Finicity-App-Key": self.__app_key,
            "Accept": "application/json",
            "Finicity-App-Token": token,
        }
        if extra_headers:
            headers.update(extra_headers)
        params = params or {}
        return requests.get(url, headers=headers, params=params)

    def _post(self, path: str, data: dict, extra_headers: Optional[dict] = None) -> Response:
        url = _FINICITY_URL_BASE + path
        token = self._get_token()
        headers = {
            "Finicity-App-Key": self.__app_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Finicity-App-Token": token,
        }
        if extra_headers:
            headers.update(extra_headers)
        return requests.post(url, data=data, headers=headers)

    def _put(self, path: str, data: dict, extra_headers: Optional[dict] = None) -> Response:
        url = _FINICITY_URL_BASE + path
        token = self._get_token()
        headers = {
            "Finicity-App-Key": self.__app_key,
            "Content-Type": "application/json",
            "Finicity-App-Token": token,
        }
        if extra_headers:
            headers.update(extra_headers)
        return requests.put(url, data=data, headers=headers)

    def _get_token(self) -> str:
        if self.__token and time.time() < self.__token_expiration:
            self.__token = self._authenticate()
        return self.__token

    # https://community.finicity.com/s/article/Partner-Authentication
    # POST /aggregation/v2/partners/authentication
    def _authenticate(self) -> str:
        """Validate the partner’s credentials (Finicity-App-Key, Partner ID, and Partner Secret) and return a temporary access token.
        The token must be passed in the HTTP header Finicity-App-Token on all subsequent API requests.
        The token is valid for two hours. You can have multiple active tokens at the same time.
        Five unsuccessful authentication attempts will cause the partner’s account to be locked.
        To unlock the account, send an email to support@finicity.com

        :return: A temporary access token, which must be passed in the HTTP header Finicity-App-Token on all subsequent API requests (see Accessing the API).
        """
        path = "/aggregation/v2/partners/authentication"
        url = _FINICITY_URL_BASE + path
        headers = {
            "Finicity-App-Key": self.__app_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        data = {
            "partnerId": self.__partner_id,
            "partnerSecret": self.__secret,
        }
        new_token_expiration = time.time() + (2 * 60 * 60) - (10 * 60)  # two hour expiration less ten minute buffer
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            self.__token = response.json()['token']
            self.__token_expiration = new_token_expiration
            return self.__token
        else:
            raise Exception(f"authentication issue ${response.status_code}: ${response.content}")

    # https://community.finicity.com/s/article/Modify-Partner-Secret
    # PUT /aggregation/v2/partners/authentication
    def modify_secret(self, new_partner_secret: str):
        """Change the partner secret that is used to authenticate this partner.
        The secret does not expire, but can be changed by calling Modify Partner Secret.
        A valid partner secret may contain upper- and lowercase characters, numbers, and the characters !, @, #, $, %, &, *, _, -, +.
        It must include at least one number and at least one letter, and its length should be between 12 and 255 characters.

        :param new_partner_secret: The new value for Partner Secret
        """
        path = "/aggregation/v2/partners/authentication"
        validate_secret(new_partner_secret)
        data = {
            "partnerId": self.__partner_id,
            "partnerSecret": self.__secret,
            "newPartnerSecret": new_partner_secret,
        }
        response = self._put(path=path, data=data)
        if response.status_code == 204:
            self.__secret = new_partner_secret
        else:
            raise Exception(f"issue modifying secret: ${response.status_code}: ${response.reason}")

    # Institutions

    # https://community.finicity.com/s/article/Get-Institutions
    # GET /institution/v2/institutions?search=[text]&start=[index]&limit=[count]
    def get_institutions(self, search_term: str = "*", start: int = 1, limit: int = 25) -> Institution:
        """Use this call to search all Financial Institutions (FI) the Finicity has connections with and supports.
        Return all financial institutions that contain the search text in the institution’s name, urlHomeApp, or urlLogonApp fields.
        To get a list of all FI’s, leave the search parameter out of the call.  If the search query is left blank, the API will return an error.
        If the value of moreAvailable in the response is true, you can retrieve the next page of results by increasing the value of the start parameter in your next request:
          ...&start=6&limit=5

        :param search_term: Text to match, or omit the search parameter.
        :param start: Starting index for this page of results
        :param limit: Maximum number of entries for this page of results
        :return:
        """
        path = "/institution/v2/institutions"
        params = {
            "start": start,
            "limit": limit,
        }
        if search_term and search_term != "*":
            params["search"] = search_term
        response = self._get(path, params=params)
        return Institution.from_dict(response.json())

    # https://community.finicity.com/s/article/Get-Institution
    # GET /institution/v2/institutions/:id
    def get_institution(self, institution_id: str) -> Institution:
        """
        Get details for the specified institution without the login form.

        :param institution_id: ID of the institution to retrieve
        :return:
        """
        # self._get_with_token()
        pass

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

    # Refreshing Accounts

    # https://community.finicity.com/s/article/Refresh-Institution-Login-Accounts-Non-Interactive
    # POST /aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts
    def refresh_institution_login_accounts(self, customerId: str, institutionLoginId: str) -> List[Account]:
        """
        Connect to a financial institution and refresh transaction data for all accounts associated with a given institutionLoginId.
        Client apps are not permitted to automate calls to the Refresh services. Active accounts are automatically refreshed by Finicity once per day. Apps may call Refresh services for a specific customer when the customer opens the app, or when the customer directly invokes a Refreshaction from the app.
        Because many financial institutions only post transactions once per day, calling Refreshrepeatedly is usually a waste of resources and is not recommended.
        The recommended timeout setting for this request is 120 seconds in order to receive a response. However you can terminate the connection after making the call the operation will still complete. You will have to pull the account records to check for an updated aggregation attempt date to know when the refresh is complete.

        :param customerId: The ID of the customer who owns the account
        :param institutionLoginId: The institution login ID (from the account record)
        :return:
        """
        pass
        # NEEDS SPECIAL HEADERS

    # https://community.finicity.com/s/article/Refresh-Customer-Accounts-non-interactive
    # POST /aggregation/v1/customers/{customerId}/accounts
    def refresh_customer_accounts(self, customerId: str) -> List[Account]:
        """
        Connect to all of the customer's financial institutions and refresh the transaction data for all of the customer's accounts. This is a non-interactive refresh, so any MFA challenge will cause the account to fail with an aggregationStatusCode value of 185 or 187.
        To recover an account that has state 185 or 187, call Refresh Institution Login Accounts during an interactive session with the customer, prompt the customer with the MFA challenge that is returned from that call, and then send that response to Refresh Institution Login Accounts (with MFA Answers).
        This service retrieves account data from the institution. This usually returns quickly, but in some scenarios may take a few minutes to complete. See Asynchronous Aggregation.
        Client apps are not permitted to automate calls to the Refresh services. Active accounts are automatically refreshed by Finicity once per day. Apps may call Refresh services for a specific customer when the customer opens the app, or when the customer directly invokes a Refreshaction from the app.
        Because many financial institutions only post transactions once per day, calling Refreshrepeatedly is usually a waste of resources and is not recommended.
        This service requires the HTTP header Content-Length: 0 because it is a POST request with no request body.
        The recommended timeout setting for this request is 120 seconds.

        :param customerId: The ID of the customer who owns the accounts
        :return:
        """
        pass
    #     self._post()  # requires Content-Length = 0 and no Content-Type header

    # https://community.finicity.com/s/article/Get-Customer-Accounts
    # GET /aggregation/v1/customers/{customerId}/accounts
    def get_customer_accounts(self, customerId: str, status: Optional[str] = None) -> List[Account]:
        """
        Get details for all accounts owned by the specified customer.

        :param customerId: The ID of the customer whose accounts are to be retrieved
        :param status: append, ?status=pending, to return accounts in active and pending status. Pending accounts were discovered but not activated and will not have transactions or have balance updates
        :return:
        """
        pass
        # self._get_with_token()

    # https://community.finicity.com/s/article/202460255-Customer-Accounts
    # GET /aggregation/v1/customers/{customerId}/institutions/{institutionId}/accounts
    def get_customer_accounts_by_institution(self, customerId: str, institutionId: str) -> List[Account]:
        """
        Get details for all active accounts owned by the specified customer at the specified institution.

        :param customerId: The ID of the customer who owns the accounts
        :param institutionId: The ID of the institution
        :return:
        """
        pass
        # self._get_with_token()

    # https://community.finicity.com/s/article/202460255-Customer-Accounts
    # GET /aggregation/v1/customers/{customerId}/accounts/{accountId}
    def get_customer_account(self, customerId: str, accountId: str) -> Account:
        """
        Get details for the specified account.

        :param customerId: ID of the customer
        :param accountId: ID of the account
        :return:
        """
        pass
        # self._get_with_token()

    # https://community.finicity.com/s/article/202460255-Customer-Accounts
    # PUT /aggregation/v1/customers/{customerId}/accounts/{accountId}
    def modify_customer_account(self, customerId: str, accountId: str, number: str, name: str):
        """
        :param customerId: The ID of the customer who owns the account
        :param accountId: The Finicity ID of the account to be modified
        :param name: New value for the account's field (optional)
        :param number: New value for the account's field (optional)
        :return:
        """
        pass
        # success = no content 204

    # https://community.finicity.com/s/article/202460255-Customer-Accounts
    # DELETE /aggregation/v1/customers/{customerId}/accounts/{accountId}
    def delete_customer_account(self, customerId: str, accountId: str):
        """
        Remove the specified account from the Finicity system.

        :param customerId: The ID of the customer whose account are to be deleted
        :param accountId: The Finicity ID of the account to be deleted
        :return:
        """
        pass
        # returns no content 204

    # Institution Logins

    # https://community.finicity.com/s/article/Get-Institution-Login-Accounts
    # GET /aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts
    def get_institution_login_accounts(self, customerId: str, institutionLoginId: str) -> List[Account]:
        """
        Get details for all accounts associated with the given institution login. All accounts returned are accessible by a single set of credentials on a single institution.

        :param customerId: The ID of the customer whose accounts are to be retrieved
        :param institutionLoginId: The institution login ID (from the account record)
        :return:
        """
        pass
        # self._get_with_token()

    # Transactions

    # https://community.finicity.com/s/article/Get-Customer-Transactions
    # GET /aggregation/v3/customers/{customerId}/transactions?fromDate=[timestamp]&toDate=[timestamp]&start=[index]&limit=[count]&sort=[asc or desc]&includePending=[true or false]
    def get_customer_transactions(self, customerId: str, fromDate: int, toDate: int, start: int, limit: int, sort: SortOrder, includePending: bool) -> List[Transaction]:
        """
        Get all transactions available for this customer within the given date range, across all accounts. This service supports paging and sorting by transactionDate (or postedDate if no transaction date is provided), with a maximum of 1000 transactions per request.
        Standard consumer aggregation provides up to 180 days of transactions prior to the date each account was added to the Finicity system. To access older transactions, you must first call the Cash Flow Verification service Load Historic Transactions for Account.
        There is no limit for the size of the window between fromDate and toDate; however, the maximum number of transactions returned in one page is 1000.
        If the value of moreAvailable in the response is true, you can retrieve the next page of results by increasing the value of the start parameter in your next request:
          ...&start=6&limit=5

        :param customerId: The ID of the customer whose transactions are to be retrieved
        :param fromDate: Starting timestamp for the date range (required) (see Handling Dates and Times)
        :param toDate: Ending timestamp for the date range (required, must be greater than fromDate) (see Handling Dates and Times)
        :param start: Starting index for this page of results
        :param limit: Maximum number of entries for this page of results (max is 1000)
        :param sort: Sort order: asc for ascending order (oldest transactions are on page 1), descfor descending order (newest transactions are on page 1).
        :param includePending: true to include pending transactions if available.
        :return:
        """
        pass
        # self._get_with_token()

    # https://community.finicity.com/s/article/Get-Customer-Account-Transactions
    # GET /aggregation/v3/customers/{customerId}/accounts/{accountId}/transactions?fromDate=[timestamp]&toDate=[timestamp]&start=[index]&limit=[count]&sort=[asc or desc]&includePending=[true or false]
    def get_customer_account_transactions(self, customerId: str, accountId: str, fromDate: int, toDate: int, sort: SortOrder = SortOrder.desc, includePending: bool = False, start: int = 1, limit: int = 1000, categories: Optional[List[str]] = None) -> List[Transaction]:
        """
        Get all transactions available for this customer account within the given date range. This service supports paging and sorting by transactionDate (or postedDate if no transaction date is provided), with a maximum of 1000 transactions per request.
        Standard consumer aggregation provides up to 180 days of transactions prior to the date each account was added to the Finicity system. To access older transactions, you must first call the Cash Flow Verification service Load Historic Transactions for Account.
        There is no limit for the size of the window between fromDate and toDate; however, the maximum number of transactions returned in one page is 1000.
        If the value of moreAvailable in the response is true, you can retrieve the next page of results by increasing the value of the start parameter in your next request:
          ...&start=6&limit=5

        :param customerId: The ID of the customer whose transactions are to be retrieved
        :param accountId: The ID of the account whose transactions are to be retrieved
        :param fromDate: Starting timestamp for the date range (required) (see Handling Dates and Times)
        :param toDate: Ending timestamp for the date range (required, must be greater than fromDate) (see Handling Dates and Times)
        :param start: Starting index for this page of results
        :param limit: Maximum number of entries for this page of results (max is 1000)
        :param sort: Sort order: asc for ascending order (oldest transactions are on page 1), descfor descending order (newest transactions are on page 1).
        :param includePending: true to include pending transactions if available.
        :param categories: Utilities, Mobile Phone, Television (this is an example of a comma delimited list)
        :return:
        """
        pass
        # self._get_with_token()

    # https://community.finicity.com/s/article/Get-Customer-Transaction
    # GET /aggregation/v2/customers/{customerId}/transactions/{transactionId}
    def get_customer_transaction(self, customerId: str, transactionId: str) -> Transaction:
        """
        Get details for the specified transaction.

        :param customerId: The ID of the customer whose transactions are to be retrieved
        :param transactionId: The ID of the transaction to be retrieved
        :return:
        """
        pass
        # self._get_with_token()

    # Report Consumers

    # https://community.finicity.com/s/article/Create-Consumer
    # POST /decisioning/v1/customers/{customerId}/consumer
    def create_consumer(self, customerId: str, firstName: str, lastName: str, address: str, city: str, state: str, zip: str, phone: str, ssn: str, birthday: BirthDate, year: str):
        """
        Create a consumer record associated with the given customer. A consumer persists as the owner of any reports that are generated, even after the original customer is deleted from the system. A consumer must be created for the given customer before calling any of the Generate Report services.
        If a consumer already exists for this customer, this service will return HTTP 409 (Conflict).

        :param customerId: ID of the customer
        :param firstName: The consumer's first name(s) / given name(s)
        :param lastName: The consumer's last name(s) / surname(s)
        :param address: The consumer's street address
        :param city: The consumer's city
        :param state: The consumer's state
        :param zip: The consumer's ZIP code
        :param phone: The consumer's phone number
        :param ssn: The consumer's 9-digit Social Security number (may include separators: nnn-nn-nnnn)
        :param birthday: The consumer's birth date
        :param year: The consumer's email address
        :return:
        """
        # example response:
        # {
        #   "id": "0h7h3r301md83",
        #   "createdDate": 1472342400
        # }
        pass
        # self._post()

    # https://community.finicity.com/s/article/Report-Consumers#get_consumer_for_customer
    # GET /decisioning/v1/customers/{customerId}/consumer
    def get_consumer_for_customer(self, customerId: str) -> ReportConsumer:
        """
        Get the details of a consumer record.
        If a consumer has not been created for this customer, the service will return HTTP 404 (Not Found)

        :param customerId:
        :return:
        """
        pass
        # self._get_with_token()

    # https://community.finicity.com/s/article/Report-Consumers#get_consumer
    # GET /decisioning/v1/consumers/{consumerId}
    def get_consumer(self, customerId) -> ReportConsumer:
        """
        Get the details of a consumer record.

        :param customerId: 	ID of the consumer (UUID with max length 32 characters)
        :return:
        """
        pass
        # self._get_with_token()

    # https://community.finicity.com/s/article/Report-Consumers#modify_consumer
    # PUT /decisioning/v1/consumers/{consumerId}
    def modify_consumer(self, customerId: str, firstName: str, lastName: str, address: str, city: str, state: str, zip: str, phone: str, ssn: str, birthday: BirthDate, year: str):
        """
        Modify the details for an existing consumer. All fields are required for a consumer record, but individual fields for this call are optional because fields that are not specified will be left unchanged.

        :param customerId: ID of the consumer (UUID with max length 32 characters)
        :param firstName: The consumer's first name(s) / given name(s)
        :param lastName: The consumer's last name(s) / surname(s)
        :param address: The consumer's street address
        :param city: The consumer's city
        :param state: The consumer's state
        :param zip: The consumer's ZIP code
        :param phone: The consumer's phone number
        :param ssn: The consumer's 9-digit Social Security number (may include separators: nnn-nn-nnnn)
        :param birthday: The consumer's birth date
        :param year: The consumer's email address
        :return:
        """
        pass

    # Credit Decisioning

    # https://community.finicity.com/s/article/Generate-VOA-Report
    # POST /decisioning/v1/customers/{customerId}/voa
    def generate_voa_report(self, customerId: str, callbackUrl: str, fromDate: Optional[int] = None, accountIds: Optional[List[str]] = None):
        """
        Generate a Verification of Assets (VOA) report for all checking, savings, money market, and investment accounts for the given customer. This service retrieves up to six months of transaction history for each account and uses this information to generate the VOA report.
        This is a premium service. The billing rate is the variable rate for Verification of Assets under the current subscription plan. The billable event is the successful generation of a VOA report.
        A report consumer must be created for the given customer before calling Generate VOA Report (see Report Consumers).
        After making this call, the client app may wait for a notification to be sent to the Report Listener Service, or it may enter a loop, which should wait 20 seconds and then call the service Get Report to see if the report is finished. While the report is being generated, Get Report will return a minimal report with status inProgress. The loop should repeat every 20 seconds until Get Report returns a different status.
        If using the listener service, the following format must be followed and the webhook must respond to the Finicity API with a 200 series code:
        https://api.finicity.com/decisioning/v1/customers/[customerId]/voa?callbackUrl=[webhookUrl]
        HTTP status of 202 (Accepted) means the report is being generated. When the report is finished, a notification will be sent to the specified report callback URL, if specified.
        If no account of type of checking, savings, money market, or investment is found, the service will return HTTP 400 (Bad Request).

        :param customerId: ID of the customer
        :param callbackUrl: The Report Listener URL to receive notifications (optional)
        :param fromDate: The `fromDate` param is an Epoch Timestamp (in seconds), such as “1494449017”.  This is an optional field.  Without this param, the report defaults to 6 months if available. Example: ?fromDate={fromDate}  If included, the epoch timestamp should be 10 digits long, and be within two years of the present day. Extending the epoch timestamp beyond 10 digits will default back to six months of data
        :param accountIds: Specific accountIds you would like included in the new report. This is used only if you want constraints to only include specific accounts in a report without deleting the other accounts
        :return:
        """
        pass
        # accountIds go in body
        # self._post()
        # return 202 accepted with accountIds

    # https://community.finicity.com/s/article/Credit-Decisioning#generate_voi_report
    # POST /decisioning/v2/customers/{customerId}/voi
    def generate_voi_report(self, customerId: str, callbackUrl: str, accountIds: Optional[List[str]] = None):
        """
        Generate a Verification of Income (VOI) report for all checking, savings, and money market accounts for the given customer. This service retrieves up to two years of transaction history for each account and uses this information to generate the VOI report.
        This is a premium service. The billing rate is the variable rate for Verification of Income under the current subscription plan. The billable event is the successful generation of a VOI report.
        A report consumer must be created for the given customer before calling Generate VOI Report (see Report Consumers).
        After making this call, the client app may wait for a notification to be sent to the Report Listener Service, or it may enter a loop, which should wait 20 seconds and then call the service Get Report to see if the report is finished. While the report is being generated, Get Report will return a minimal report with status inProgress. The loop should repeat every 20 seconds until Get Report returns a different status.
        If using the listener service, the following format must be followed and the webhook must respond to the Finicity API with a 200 series code:
        https://api.finicity.com/decisioning/v1/customers/[customerId]/voi?callbackUrl=[webhookUrl]
        HTTP status of 202 (Accepted) means the report is being generated. When the report is finished, a notification will be sent to the specified report callback URL, if specified.
        If no account of type of checking, savings, or money market is found, the service will return HTTP 400 (Bad Request).

        :param customerId: ID of the customer
        :param callbackUrl: The Report Listener URL to receive notifications (optional)
        :param accountIds:
        :return:
        """
        pass
        # accountIds go in body
        # self._post()

    # https://community.finicity.com/s/article/Credit-Decisioning#get_report
    # GET /decisioning/v1/customers/{customerId}/reports/{reportId}
    def get_report_by_customer(self, customerId: str, reportId: str, purpose: PermissiblePurpose):
        """
        Get a report that has been generated by calling one of the Generate Report services.
        The report's status field will contain inProgress, failure, or success. If the status shows inProgress, the client app should wait 20 seconds and then call again to see if the report is finished.

        :param customerId: ID of the customer
        :param reportId: ID of the report (UUID with max length 32 characters)
        :param purpose: 2-digit code from Permissible Purpose Codes, specifying the reason for retrieving this report.
        :return:
        """
        pass
        # self._get_with_token()

    # https://community.finicity.com/s/article/Credit-Decisioning#get_report
    # GET /decisioning/v1/consumers/{consumerId}/reports/{reportId}
    def get_report_by_consumer(self, consumerId: str, reportId: str, purpose: PermissiblePurpose):
        """
        Get a report that has been generated by calling one of the Generate Report services.
        The report's status field will contain inProgress, failure, or success. If the status shows inProgress, the client app should wait 20 seconds and then call again to see if the report is finished.

        :param consumerId: ID of the consumer (UUID with max length 32 characters)
        :param reportId: ID of the report (UUID with max length 32 characters)
        :param purpose: 2-digit code from Permissible Purpose Codes, specifying the reason for retrieving this report.
        :return:
        """
        pass
        # self._get_with_token()

    # https://community.finicity.com/s/article/Credit-Decisioning#get_reports_for_consumer
    # GET /decisioning/v1/consumers/{consumerId}/reports
    def get_reports_for_consumer(self, consumerId: str):
        """
        Get a list of reports that have been generated for the given consumer.
        The status fields in the returned list will contain 'inProgress', 'failure', or 'success'. If a status shows 'inProgress', wait 20 seconds and then call again.

        :param consumerId: ID of the consumer (UUID with max length 32 characters)
        :return:
        """
        pass
        # self._get_with_token()

    # https://community.finicity.com/s/article/Credit-Decisioning#get_reports_for_customer
    # GET /decisioning/v1/customers/{customerId}/reports
    def get_reports_for_customer(self, customerId: str):
        """
        Get a list of reports that have been generated for the given consumer.
        The status fields in the returned list will contain 'inProgress', 'failure', or 'success'. If a status shows 'inProgress', wait 20 seconds and then call again.

        :param customerId: ID of the customer
        :return:
        """
        pass
        # self._get_with_token()

    # TXPush Services

    # https://community.finicity.com/s/article/Enable-TxPUSH-Notifications
    # POST /aggregation/v1/customers/{customerId}/accounts/{accountId}/txpush
    def enable_transaction_push_notifications(self, customerId: str, accountId: str, callbackUrl: str):
        """
        TxPUSH services allow an app to register a TxPUSH Listener service to receive notifications whenever a new transaction appears on an account.

        :param customerId: The Finicity ID of the customer who owns the account
        :param accountId: The Finicity ID of the account whose events will be sent to the TxPUSH Listener
        :param callbackUrl: The TxPUSH Listener URL to receive TxPUSH notifications (must use https protocol for any real-world account)
        :return:
        """
        pass
        # 201 created

    # https://community.finicity.com/s/article/Disable-TxPUSH-Notifications
    # DELETE /aggregation/v1/customers/{customerId}/accounts/{accountId}/txpush
    def disable_transaction_push_notifications(self, customerId: str, accountId: str):
        """
        Disable all TxPUSH notifications for the indicated account. No more notifications will be sent for account or transaction events.

        :param customerId: The ID of the customer who owns the account
        :param accountId: The Finicity ID of the account whose events will be sent to the TxPUSH Listener
        :return:
        """
        pass
        # success = 204 no content

    # https://community.finicity.com/s/article/Delete-TxPUSH-Subscription
    # DELETE /aggregation/v1/customers/{customerId}/subscriptions/{subscriptionId}
    def delete_transaction_push_subscription(self, customerId: str, accountId: str):
        """
        Delete a specific subscription for a class of events (account or transaction events) related to an account. No more notifications will be sent for these events.

        :param customerId: The ID of the customer who owns the account
        :param accountId: The ID of the specific subscription to be deleted (returned from Enable TxPUSH Notifications
        :return:
        """
        pass

    # https://community.finicity.com/s/article/Add-Transaction-for-Testing-Account
    # POST /aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions
    def add_transaction_for_testing_account(self, customerId: str, accountId: str, amount: float, description: str, status: Optional[TransactionStatus] = None, postedDate: Optional[int] = None, transactionDate: Optional[int] = None):
        """
        Inject a transaction into the transaction list for a testing account. This allows an app to trigger TxPUSH notifications for the account in order to test the app’s TxPUSH Listener service. This causes the platform to send one transaction event and one account event (showing that the account balance has changed). This service is only supported for testing accounts (accounts on institution 101732).

        :param customerId: The ID of the customer who owns the account
        :param accountId: The Finicity ID of the account whose events will be sent to the TxPUSH Listener
        :param amount: The amount of the transaction
        :param description: The description of the transaction
        :param status: active or pending (optional)
        :param postedDate: An optional timestamp for the transaction's posted date value for this transaction (see Handling Dates and Times). Timestamp must be no more than 6 months from the current date.
        :param transactionDate: An optional timestamp for the transaction's posted date value for this transaction (see Handling Dates and Times)
        :return:
        """
        status = status or TransactionStatus.active
        # postedDate = postedDate or nowTimestamp()
        # transactionDate = transactionDate or nowTimestamp()
        # success = 201 created with
        # {
        #   "id": 712054,
        #   "createdDate": 1444259433
        # }
        pass

    # Account History Aggregation

    # https://community.finicity.com/s/article/Load-Historic-Transactions-for-Account
    # POST /aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions/historic
    def load_historic_transactions_for_account(self, customerId: str, accountId: str):
        """
        Connect to the account's financial institution and load up to twelve months of historic transactions for the account. For some institutions, up to two years of history may be available.
        This is a premium service. The billing rate is the variable rate for Cash Flow Verification under the current subscription plan. The billable event is a call to this service specifying a customerId that has not been seen before by this service. (If this service is called multiple times with the same customerId, to load transactions from multiple accounts, only one billable event has occurred.)
        HTTP status of 204 means historic transactions have been loaded successfully. The transactions are now available by calling Get Customer Account Transactions.
        HTTP status of 203 means the response contains an MFA challenge. Contact your Account Manager or Systems Engineers to determine the best route to handle this HTTP status code.
        The recommended timeout setting for this request is 180 seconds in order to receive a response. However you can terminate the connection after making the call the operation will still complete. You will have to pull the account records to check for an updated aggregation attempt date to know when the refresh is complete.
        This service usually requires the HTTP header Content-Length: 0 because it is a POST request with no request body.
        The date range sent to the institution is calculated from the account's createdDate. This means that calling this service a second time for the same account normally will not add any new transactions for the account. For this reason, a second call to this service for a known accountId will usually return immediately with HTTP 204.
        In a few specific scenarios, it may be desirable to force a second connection to the institution for a known accountId. Some examples are:
        The institution's policy has changed, making more transactions available.
        Finicity has now added Cash Flow Verification support for the institution.
        The first call encountered an error, and the resulting Aggregation Ticket has now been fixed by the Finicity Support Team.
        In these cases, the POST request can contain the parameter force=true in the request body to force the second connection.

        :param customerId: The ID of the customer who owns the account
        :param accountId: The Finicity ID of the account to be refreshed
        :return:
        """
        pass

    # # POST /aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions/historic/mfa
    # def load_historic_transactions_for_account_with_mfa_answers(self, mfaSession: str, customerId: str, accountId: str, ):
    #     # TODO
    #     # http header MFA-Session
    #
    #     pass

    # ACH Account Verification

    # https://community.finicity.com/s/article/Get-Customer-Account-Details
    # https://community.finicity.com/s/article/211260386-ACH-Account-Verification#get_customer_account_details
    # GET /aggregation/v1/customers/{customerId}/accounts/{accountId}/details
    def get_customer_account_details(self, customerId: str, accountId: str) -> AccountDetailResponse:
        """
        Connect to the account's financial institution and retrieve the ACH data for the indicated account. This may be an interactive refresh, so MFA challenges may be required.
        This service is supported only for accounts with type checking, savings, or moneyMarket. Calling this service for other account types will return HTTP 400 (Bad Request).
        This is a premium service. The billing rate is the variable rate for ACH Account Verification under the current subscription plan. The billable event is a successful call to this service.
        HTTP status of 200 means both realAccountNumber and routingNumber were returned successfully in the body of the response.
        HTTP status of 203 means the response contains an MFA challenge in XML or JSON format. Contact your Account Manager or Systems Engineers to determine the best route to handle this HTTP status code.
        HTTP status of 404 means that no ACH data is available for this account.
        The recommended timeout setting for this request is 180 seconds in order to receive a response. However you can terminate the connection after making the call the operation will still complete. You will have to pull the account records to check for an updated aggregation attempt date to know when the refresh is complete.

        :param customerId: The ID of the customer who owns the account
        :param accountId: The Finicity ID of the account
        :return:
        """
        pass

    # https://community.finicity.com/s/article/211260386-ACH-Account-Verification#get_customer_account_details_mfa
    # POST /aggregation/v1/customers/{customerId}/accounts/{accountId}/details/mfa
    def get_customer_account_details_with_mfa_answers(self, customerId: str, accountId: str, questions: List[AnsweredMfaQuestion]):
        """
        Send MFA answers for an earlier challenge while getting account details.
        HTTP status of 200 means both realAccountNumber and routingNumber were returned successfully in the body of the response.
        HTTP status of 203 means the response contains another MFA challenge. Call Get Customer Account Details (with MFA Answers) again to answer the new challenge.
        This service is invoked only if a previous call to Get Customer Account Details or Get Customer Account Details (with MFA Answers) has returned HTTP 203. The response from that previous call is referred to as ""the previous response"" below.
        The call itself is a replay of the previous call, with several changes:
        Change the request method from GET to POST.
        Append /mfa to the path.
        Add a Content-Type header with the value application/json or application/xml
        Copy the MFA-Session header from the previous response onto this request.
        Copy the MFA challenge from the previous response into the request body.
        Add the MFA answer inside the element in the MFA challenge.
        The recommended timeout setting for this request is 120 seconds.

        :param customerId: The ID of the customer who owns the account
        :param accountId: The Finicity ID of the account
        :param questions:
        :return:
        """
        # note must copy MFA-Session from other call
        pass

    # Account Owner Verification

    # https://community.finicity.com/s/article/Get-Account-Owner
    # https://community.finicity.com/s/article/Account-Owner-Verification#get_account_owner
    # GET /aggregation/v1/customers/{customerId}/accounts/{accountId}/owner
    def get_account_owner(self, customerId: str, accountId: str) -> AccountOwner:
        """
        Return the account owner's name and address. This may require connecting to the institution, so MFA challenges may be required.
        This is a premium service. The billing rate is the variable rate for Account Owner under the current subscription plan. The billable event is a successful call to this service.
        HTTP status of 200 means the account owner's name and address were retrieved successfully.
        HTTP status of 203 means the response contains an MFA challenge in XML or JSON format. Contact your Account Manager or Systems Engineers to determine the best route to handle this HTTP status code.
        This service retrieves account data from the institution. This usually returns quickly, but in some scenarios may take a few minutes to complete. In the event of a timeout condition, please retry the call.
        The recommended timeout setting for this request is 180 seconds in order to receive a response. However you can terminate the connection after making the call the operation will still complete. You will have to pull the account records to check for an updated aggregation attempt date to know when the refresh is complete.

        :param customerId: The ID of the customer who owns the account
        :param accountId: The Finicity ID of the account
        :return:
        """
        pass
        # TODO 203 means MFA needed

    # https://community.finicity.com/s/article/Account-Owner-Verification#get_account_owner_mfa
    def get_account_owner_with_mfa_answers(self, customerId: str, accountId: str, questions: List[AnsweredMfaQuestion]):
        """
        Send MFA answers for an earlier challenge while getting an account statement.
        HTTP status of 200 means the account owner's name and address were retrieved successfully.
        HTTP status of 203 means the response contains another MFA challenge. Call Get Account Owner (with MFA Answers) again to answer the new challenge.
        This service is invoked only if a previous call to Get Account Owner or Get Account Owner (with MFA Answers) has returned HTTP 203. The response from that previous call is referred to as "the previous response" below.
        The call itself is a replay of the previous call, with several changes:
        Change the request method from GET to POST.
        Append /mfa to the path.
        Add a Content-Type header with the value application/json or application/xml
        Copy the MFA-Session header from the previous response onto this request.
        Copy the MFA challenge from the previous response into the request body.
        Add the MFA answer inside the element in the MFA challenge.
        The recommended timeout setting for this request is 120 seconds.

        :param customerId: The ID of the customer who owns the account
        :param accountId: The Finicity ID of the account
        :param questions:
        :return:
        """
        pass
        # note must copy MFA-Session from other call

    # Statement Aggregation

    def get_customer_account_statement(self):
        pass
    # Get Customer Account Statement
    # /aggregation/v1/customers/{customerId}/accounts/{accountId}/statement GET

    def get_customer_account_statement_with_mfa_answers(self):
        pass
    # Get Customer Account Statement (with MFA Answers)
    # /aggregation/v1/customers/{customerId}/accounts/{accountId}/statement/mfa POST
