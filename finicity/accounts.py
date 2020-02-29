from typing import Optional, List

from finicity.api_http_client import ApiHttpClient
from finicity.models import Institution, Account, AnsweredMfaQuestion, AccountOwner
from finicity.models.response.account_detail_response import AccountDetailResponse
from finicity.queries.institutions_query import InstitutionsQuery


class Accounts(object):
    def __init__(self, http_client: ApiHttpClient):
        self.__http_client = http_client

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
