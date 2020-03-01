from typing import Optional, List

from finicity.api_http_client import ApiHttpClient
from finicity.models import Account, AnsweredMfaQuestion, AccountOwner
from finicity.models.response.account_detail_response import AccountDetailResponse
from finicity.models.response.accounts_response import AccountsResponse


class Accounts(object):
    def __init__(self, http_client: ApiHttpClient):
        self.__http_client = http_client

    # https://community.finicity.com/s/article/Get-Customer-Accounts
    # GET /aggregation/v1/customers/{customerId}/accounts
    def get_customer_accounts(self, customer_id: str, status: Optional[str] = None) -> List[Account]:
        """
        Get details for all accounts owned by the specified customer.

        :param customer_id: The ID of the customer whose accounts are to be retrieved
        :param status: append, ?status=pending, to return accounts in active and pending status. Pending accounts were discovered but not activated and will not have transactions or have balance updates
        :return:
        """
        path = f"/aggregation/v1/customers/{customer_id}/accounts"
        params = {'status': status} if status else {}
        response = self.__http_client.get(path, params=params)
        response_dict = response.json()
        return AccountsResponse.from_dict(response_dict).accounts

    # https://community.finicity.com/s/article/202460255-Customer-Accounts
    # GET /aggregation/v1/customers/{customerId}/institutions/{institutionId}/accounts
    def get_by_institution(self, customer_id: str, institution_id: str) -> List[Account]:
        """
        Get details for all active accounts owned by the specified customer at the specified institution.

        :param customer_id: The ID of the customer who owns the accounts
        :param institution_id: The ID of the institution
        :return:
        """
        path = f"/aggregation/v1/customers/{customer_id}/institutions/{institution_id}/accounts"
        response = self.__http_client.get(path)
        response_dict = response.json()
        return AccountsResponse.from_dict(response_dict).accounts

    # https://community.finicity.com/s/article/202460255-Customer-Accounts
    # GET /aggregation/v1/customers/{customerId}/accounts/{accountId}
    def get(self, customer_id: str, account_id: str) -> Account:
        """
        Get details for the specified account.

        :param customer_id: ID of the customer
        :param account_id: ID of the account
        :return:
        """
        path = f"/aggregation/v1/customers/{customer_id}/accounts/{account_id}"
        response = self.__http_client.get(path)
        response_dict = response.json()
        return Account.from_dict(response_dict)

    # https://community.finicity.com/s/article/202460255-Customer-Accounts
    # PUT /aggregation/v1/customers/{customerId}/accounts/{accountId}
    def modify(self, customer_id: str, account_id: str, number: Optional[str], name: Optional[str]):
        """
        :param customer_id: The ID of the customer who owns the account
        :param account_id: The Finicity ID of the account to be modified
        :param name: New value for the account's field (optional)
        :param number: New value for the account's field (optional)
        :return:
        """
        path = f"/aggregation/v1/customers/{customer_id}/accounts/{account_id}"
        data = {
            'name': name,
            'number': number,
        }
        self.__http_client.put(path, data=data)
        # success = no content 204

    # https://community.finicity.com/s/article/202460255-Customer-Accounts
    # DELETE /aggregation/v1/customers/{customerId}/accounts/{accountId}
    def delete(self, customer_id: str, account_id: str):
        """
        Remove the specified account from the Finicity system.

        :param customer_id: The ID of the customer whose account are to be deleted
        :param account_id: The Finicity ID of the account to be deleted
        :return:
        """
        path = f"/aggregation/v1/customers/{customer_id}/accounts/{account_id}"
        self.__http_client.delete(path)
        # returns no content 204

    # Institution Logins

    # https://community.finicity.com/s/article/Get-Institution-Login-Accounts
    # GET /aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts
    def get_accounts(self, customerId: str, institutionLoginId: str) -> List[Account]:
        """
        Get details for all accounts associated with the given institution login. All accounts returned are accessible by a single set of credentials on a single institution.

        :param customerId: The ID of the customer whose accounts are to be retrieved
        :param institutionLoginId: The institution login ID (from the account record)
        :return:
        """
        path = f"/aggregation/v1/customers/{customerId}/institutionLogins/{institutionLoginId}/accounts"
        response = self.__http_client.get(path)
        response_dict = response.json()
        return AccountsResponse.from_dict(response_dict).accounts

    # ACH Account Verification

    # https://community.finicity.com/s/article/Get-Customer-Account-Details
    # https://community.finicity.com/s/article/211260386-ACH-Account-Verification#get_customer_account_details
    # GET /aggregation/v1/customers/{customerId}/accounts/{accountId}/details
    def get_details(self, customerId: str, accountId: str) -> AccountDetailResponse:
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
        path = f"/aggregation/v1/customers/{customerId}/accounts/{accountId}/details"
        response = self.__http_client.get(path)
        response_dict = response.json()
        return AccountDetailResponse.from_dict(response_dict).accounts

    # https://community.finicity.com/s/article/211260386-ACH-Account-Verification#get_customer_account_details_mfa
    # POST /aggregation/v1/customers/{customerId}/accounts/{accountId}/details/mfa
    def get_details_with_mfa_answers(self, customerId: str, accountId: str, questions: List[AnsweredMfaQuestion]) -> AccountDetailResponse:
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
        data = {
            'questions': [q.to_dict() for q in questions],
        }
        path = f"/aggregation/v1/customers/{customerId}/accounts/{accountId}/details/mfa"
        response = self.__http_client.post(path, data)
        response_dict = response.json()
        return AccountDetailResponse.from_dict(response_dict)

    # Account Owner Verification

    # https://community.finicity.com/s/article/Get-Account-Owner
    # https://community.finicity.com/s/article/Account-Owner-Verification#get_account_owner
    # GET /aggregation/v1/customers/{customerId}/accounts/{accountId}/owner
    def get_owner(self, customerId: str, accountId: str) -> AccountOwner:
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
        path = f"/aggregation/v1/customers/{customerId}/accounts/{accountId}/owner"
        response = self.__http_client.get(path)
        response_dict = response.json()
        return AccountOwner.from_dict(response_dict).accounts
        # TODO 203 means MFA needed

    # https://community.finicity.com/s/article/Account-Owner-Verification#get_account_owner_mfa
    def get_owner_with_mfa_answers(self, customerId: str, accountId: str, questions: List[AnsweredMfaQuestion]):
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
        data = {
            'questions': [q.to_dict() for q in questions],
        }
        path = f"/aggregation/v1/customers/{customerId}/accounts/{accountId}/details/mfa"
        response = self.__http_client.post(path, data)
        response_dict = response.json()
        return AccountOwner.from_dict(response_dict)
        # TODO must copy MFA-Session from other call

    # Statement Aggregation

    # Get Customer Account Statement
    # /aggregation/v1/customers/{customerId}/accounts/{accountId}/statement GET
    def get_statement(self, customerId: str, accountId: str):
        path = f"/aggregation/v1/customers/{customerId}/accounts/{accountId}/statement"
        response = self.__http_client.get(path)
        return response.content # TODO what does this function actually return?

    # Get Customer Account Statement (with MFA Answers)
    # /aggregation/v1/customers/{customerId}/accounts/{accountId}/statement/mfa POST
    def get_statement_with_mfa_answers(self, customerId: str, accountId: str, questions: List[AnsweredMfaQuestion]):
        data = {
            'questions': [q.to_dict() for q in questions],
        }
        path = f"/aggregation/v1/customers/{customerId}/accounts/{accountId}/details/mfa"
        response = self.__http_client.post(path, data)
        response_dict = response.json()
        return response.content # TODO what does this function actually return?
        # TODO must copy MFA-Session from other call
