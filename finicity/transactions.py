from typing import Optional, List

from finicity.api_http_client import ApiHttpClient
from finicity.models import Institution, TransactionStatus, SortOrder, Transaction
from finicity.queries.institutions_query import InstitutionsQuery


class Transactions(object):
    def __init__(self, http_client: ApiHttpClient):
        self.__http_client = http_client

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

