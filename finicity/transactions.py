from typing import Optional, List

from finicity.api_http_client import ApiHttpClient
from finicity.models import SortOrder, AnsweredMfaQuestion
from finicity.queries.transaction_query import TransactionsQuery


class Transactions(object):
    def __init__(self, http_client: ApiHttpClient):
        self.__http_client = http_client

    def query(self, customer_id: int, from_date: int, to_date: int, sort: SortOrder = SortOrder.asc, include_pending: bool = True, account_id: Optional[str] = None) -> TransactionsQuery:
        """
        Get all transactions available for this customer account within the given date range. This service supports paging and sorting by transactionDate (or postedDate if no transaction date is provided), with a maximum of 1000 transactions per request.
        Standard consumer aggregation provides up to 180 days of transactions prior to the date each account was added to the Finicity system. To access older transactions, you must first call the Cash Flow Verification service Load Historic Transactions for Account.
        There is no limit for the size of the window between fromDate and toDate; however, the maximum number of transactions returned in one page is 1000.
        If the value of moreAvailable in the response is true, you can retrieve the next page of results by increasing the value of the start parameter in your next request:
          ...&start=6&limit=5

        :param customer_id: The ID of the customer whose transactions are to be retrieved
        :param account_id: The ID of the account whose transactions are to be retrieved
        :param from_date: Starting timestamp for the date range (required) (see Handling Dates and Times)
        :param to_date: Ending timestamp for the date range (required, must be greater than fromDate) (see Handling Dates and Times)
        :param sort: Sort order: asc for ascending order (oldest transactions are on page 1), descfor descending order (newest transactions are on page 1).
        :param include_pending: true to include pending transactions if available.
        :return:
        """
        return TransactionsQuery(self.__http_client, customer_id, from_date, to_date, sort, include_pending, account_id=account_id)
        # TODO add categories to query?
        # :param categories: Utilities, Mobile Phone, Television (this is an example of a comma delimited list)

    # TXPush Services

    # https://community.finicity.com/s/article/Enable-TxPUSH-Notifications
    # POST /aggregation/v1/customers/{customerId}/accounts/{accountId}/txpush
    def enable_push_notifications(self, customerId: str, accountId: str, callbackUrl: str):
        """
        TxPUSH services allow an app to register a TxPUSH Listener service to receive notifications whenever a new transaction appears on an account.

        :param customerId: The Finicity ID of the customer who owns the account
        :param accountId: The Finicity ID of the account whose events will be sent to the TxPUSH Listener
        :param callbackUrl: The TxPUSH Listener URL to receive TxPUSH notifications (must use https protocol for any real-world account)
        :return:
        """
        data = {
            "callbackUrl": callbackUrl,
        }
        path = f"/aggregation/v1/customers/{customerId}/accounts/{accountId}/txpush"
        self.__http_client.post(path, data)
        # 201 created

    # https://community.finicity.com/s/article/Disable-TxPUSH-Notifications
    # DELETE /aggregation/v1/customers/{customerId}/accounts/{accountId}/txpush
    def disable_push_notifications(self, customerId: str, accountId: str):
        """
        Disable all TxPUSH notifications for the indicated account. No more notifications will be sent for account or transaction events.

        :param customerId: The ID of the customer who owns the account
        :param accountId: The Finicity ID of the account whose events will be sent to the TxPUSH Listener
        :return:
        """
        path = f"/aggregation/v1/customers/{customerId}/accounts/{accountId}/txpush"
        self.__http_client.delete(path)
        # success = 204 no content

    # https://community.finicity.com/s/article/Delete-TxPUSH-Subscription
    # DELETE /aggregation/v1/customers/{customerId}/subscriptions/{subscriptionId}
    def delete_push_subscription(self, customerId: str, subscriptionId: str):
        """
        Delete a specific subscription for a class of events (account or transaction events) related to an account. No more notifications will be sent for these events.

        :param customerId: The ID of the customer who owns the account
        :param subscriptionId: The ID of the specific subscription to be deleted (returned from Enable TxPUSH Notifications
        :return:
        """
        path = f"/aggregation/v1/customers/{customerId}/subscriptions/{subscriptionId}"
        self.__http_client.delete(path)

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
        path = f"/aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions/historic"
        self.__http_client.post(path, data={})

    # POST /aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions/historic/mfa
    def load_historic_transactions_for_account_with_mfa_answers(self, mfaSession: str, customerId: str, accountId: str, questions: List[AnsweredMfaQuestion]):
        headers = {
            'mfaSession': mfaSession
        }
        data = {
            'questions': [q.to_dict() for q in questions],
        }
        path = f"/aggregation/v1/customers/{customerId}/accounts/{accountId}/transactions/historic"
        self.__http_client.post(path, data=data, extra_headers=headers)

    # https://community.finicity.com/s/article/Refresh-Customer-Accounts-non-interactive
    # POST /aggregation/v1/customers/{customerId}/accounts
    def refresh_customer_accounts(self, customerId: str):
        """
        Connect to all of the customer's financial institutions and refresh the transaction data for all of the customer's accounts. This is a non-interactive refresh, so any MFA challenge will cause the account to fail with an aggregationStatusCode value of 185 or 187.
        To recover an account that has state 185 or 187, call Refresh Institution Login Accounts during an interactive session with the customer, prompt the customer with the MFA challenge that is returned from that call, and then send that response to Refresh Institution Login Accounts (with MFA Answers).
        This service retrieves account data from the institution. This usually returns quickly, but in some scenarios may take a few minutes to complete. See Asynchronous Aggregation.
        Client apps are not permitted to automate calls to the Refresh services. Active accounts are automatically refreshed by Finicity once per day. Apps may call Refresh services for a specific customer when the customer opens the app, or when the customer directly invokes a Refreshaction from the app.
        Because many financial institutions only post transactions once per day, calling Refresh repeatedly is usually a waste of resources and is not recommended.
        This service requires the HTTP header Content-Length: 0 because it is a POST request with no request body.
        The recommended timeout setting for this request is 120 seconds.

        :param customerId: The ID of the customer who owns the accounts
        :return:
        """
        headers = {
            'Content-Length': 0,
        }
        path = f"/aggregation/v1/customers/{customerId}/accounts"
        self.__http_client.post(path, None, extra_headers=headers)
    #     self._post()  # requires Content-Length = 0 and no Content-Type header

    # https://community.finicity.com/s/article/Refresh-Institution-Login-Accounts-Non-Interactive
    # POST /aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts
    def refresh_institution_login_accounts(self, customerId: str, institutionLoginId: str):
        """
        Connect to a financial institution and refresh transaction data for all accounts associated with a given institutionLoginId.
        Client apps are not permitted to automate calls to the Refresh services. Active accounts are automatically refreshed by Finicity once per day. Apps may call Refresh services for a specific customer when the customer opens the app, or when the customer directly invokes a Refreshaction from the app.
        Because many financial institutions only post transactions once per day, calling Refreshrepeatedly is usually a waste of resources and is not recommended.
        The recommended timeout setting for this request is 120 seconds in order to receive a response. However you can terminate the connection after making the call the operation will still complete. You will have to pull the account records to check for an updated aggregation attempt date to know when the refresh is complete.

        :param customerId: The ID of the customer who owns the account
        :param institutionLoginId: The institution login ID (from the account record)
        :return:
        """
        headers = {
            'Content-Length': 0,
        }
        path = f"/aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts"
        self.__http_client.post(path, None, extra_headers=headers)
        # NEEDS SPECIAL HEADERS
