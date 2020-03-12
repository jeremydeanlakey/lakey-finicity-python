from typing import Optional, List

from lakey_finicity.api_http_client import ApiHttpClient
from lakey_finicity.models import PermissiblePurpose
from lakey_finicity.models.report.report_summary import ReportSummary
from lakey_finicity.responses.reports_response import ReportsResponse


class Reports(object):
    def __init__(self, http_client: ApiHttpClient):
        self.__http_client = http_client

    # Credit Decisioning

    # https://community.finicity.com/s/article/Generate-VOA-Report
    # POST /decisioning/v1/customers/{customerId}/voa
    def generate_voa_report(self, customer_id: int, callback_url: Optional[str] = None, from_date: Optional[int] = None, account_ids: Optional[List[str]] = None) -> ReportSummary:
        """
        Generate a Verification of Assets (VOA) report for all checking, savings, money market, and investment accounts for the given customer. This service retrieves up to six months of transaction history for each account and uses this information to generate the VOA report.
        This is a premium service. The billing rate is the variable rate for Verification of Assets under the current subscription plan. The billable event is the successful generation of a VOA report.
        A report consumer must be created for the given customer before calling Generate VOA Report (see Report Consumers).
        After making this call, the client app may wait for a notification to be sent to the Report Listener Service, or it may enter a loop, which should wait 20 seconds and then call the service Get Report to see if the report is finished. While the report is being generated, Get Report will return a minimal report with status inProgress. The loop should repeat every 20 seconds until Get Report returns a different status.
        If using the listener service, the following format must be followed and the webhook must respond to the Finicity API with a 200 series code:
        https://api.finicity.com/decisioning/v1/customers/[customerId]/voa?callbackUrl=[webhookUrl]
        HTTP status of 202 (Accepted) means the report is being generated. When the report is finished, a notification will be sent to the specified report callback URL, if specified.
        If no account of type of checking, savings, money market, or investment is found, the service will return HTTP 400 (Bad Request).

        :param customer_id: ID of the customer
        :param callback_url: The Report Listener URL to receive notifications (optional)
        :param from_date: The `fromDate` param is an Epoch Timestamp (in seconds), such as “1494449017”.  This is an optional field.  Without this param, the report defaults to 6 months if available. Example: ?fromDate={fromDate}  If included, the epoch timestamp should be 10 digits long, and be within two years of the present day. Extending the epoch timestamp beyond 10 digits will default back to six months of data
        :param account_ids: Specific accountIds you would like included in the new report. This is used only if you want constraints to only include specific accounts in a report without deleting the other accounts
        :return:
        """
        data = {
        }
        headers = {}
        if account_ids:
            data['accountIds'] = account_ids
        if callback_url:
            headers["callbackUrl"] = callback_url
        if from_date:
            headers["fromDate"] = from_date
        path = f"/decisioning/v1/customers/{customer_id}/voa"
        response = self.__http_client.post(path, extra_headers=headers, data=data)
        response_dict = response.json()
        return ReportSummary.from_dict(response_dict)
        # accountIds go in body
        # self._post()
        # return 202 accepted with accountIds

    # https://community.finicity.com/s/article/Credit-Decisioning#generate_voi_report
    # POST /decisioning/v2/customers/{customerId}/voi
    def generate_voi_report(self, customer_id: int, callback_url: Optional[str] = None, account_ids: Optional[List[str]] = None) -> ReportSummary:
        """
        Generate a Verification of Income (VOI) report for all checking, savings, and money market accounts for the given customer. This service retrieves up to two years of transaction history for each account and uses this information to generate the VOI report.
        This is a premium service. The billing rate is the variable rate for Verification of Income under the current subscription plan. The billable event is the successful generation of a VOI report.
        A report consumer must be created for the given customer before calling Generate VOI Report (see Report Consumers).
        After making this call, the client app may wait for a notification to be sent to the Report Listener Service, or it may enter a loop, which should wait 20 seconds and then call the service Get Report to see if the report is finished. While the report is being generated, Get Report will return a minimal report with status inProgress. The loop should repeat every 20 seconds until Get Report returns a different status.
        If using the listener service, the following format must be followed and the webhook must respond to the Finicity API with a 200 series code:
        https://api.finicity.com/decisioning/v1/customers/[customerId]/voi?callbackUrl=[webhookUrl]
        HTTP status of 202 (Accepted) means the report is being generated. When the report is finished, a notification will be sent to the specified report callback URL, if specified.
        If no account of type of checking, savings, or money market is found, the service will return HTTP 400 (Bad Request).

        :param customer_id: ID of the customer
        :param callback_url: The Report Listener URL to receive notifications (optional)
        :param account_ids:
        :return:
        """
        data = {
            'accountIds': account_ids,
        }
        headers = {
        }
        if callback_url:
            data["callbackUrl"] =callback_url
        path = f"/decisioning/v2/customers/{customer_id}/voi"
        response = self.__http_client.post(path, extra_headers=headers, data=data)
        response_dict = response.json()
        return ReportSummary.from_dict(response_dict)
        # accountIds go in body
        # self._post()

    # https://community.finicity.com/s/article/Credit-Decisioning#get_report
    # GET /decisioning/v1/customers/{customerId}/reports/{reportId}
    def get_report_by_customer(self, customer_id: int, report_id: str, purpose: PermissiblePurpose) -> ReportSummary:
        """
        Get a report that has been generated by calling one of the Generate Report services.
        The report's status field will contain inProgress, failure, or success. If the status shows inProgress, the client app should wait 20 seconds and then call again to see if the report is finished.

        :param customer_id: ID of the customer
        :param report_id: ID of the report (UUID with max length 32 characters)
        :param purpose: 2-digit code from Permissible Purpose Codes, specifying the reason for retrieving this report.
        :return:
        """
        path = f"/decisioning/v1/customers/{customer_id}/reports/{report_id}"
        params = {
            'purpose': purpose.value,
        }
        response = self.__http_client.get(path, params=params)
        response_dict = response.json()
        return ReportSummary.from_dict(response_dict)

    # https://community.finicity.com/s/article/Credit-Decisioning#get_report
    # GET /decisioning/v1/consumers/{consumerId}/reports/{reportId}
    def get_report_by_consumer(self, consumer_id: int, report_id: str, purpose: PermissiblePurpose) -> ReportSummary:
        """
        Get a report that has been generated by calling one of the Generate Report services.
        The report's status field will contain inProgress, failure, or success. If the status shows inProgress, the client app should wait 20 seconds and then call again to see if the report is finished.

        :param consumer_id: ID of the consumer (UUID with max length 32 characters)
        :param report_id: ID of the report (UUID with max length 32 characters)
        :param purpose: 2-digit code from Permissible Purpose Codes, specifying the reason for retrieving this report.
        :return:
        """
        path = f"/decisioning/v1/consumers/{consumer_id}/reports/{report_id}"
        params = {
            'purpose': purpose.value,
        }
        response = self.__http_client.get(path, params=params)
        response_dict = response.json()
        return ReportSummary.from_dict(response_dict)

    # https://community.finicity.com/s/article/Credit-Decisioning#get_reports_for_consumer
    # GET /decisioning/v1/consumers/{consumerId}/reports
    def get_reports_for_consumer(self, customer_id: int) -> List[ReportSummary]:
        """
        Get a list of reports that have been generated for the given consumer.
        The status fields in the returned list will contain 'inProgress', 'failure', or 'success'. If a status shows 'inProgress', wait 20 seconds and then call again.

        :param customer_id: ID of the consumer (UUID with max length 32 characters)
        :return:
        """
        path = f"/decisioning/v1/consumers/{customer_id}/reports"
        response = self.__http_client.get(path)
        response_dict = response.json()
        return ReportsResponse.from_dict(response_dict).reports

    # https://community.finicity.com/s/article/Credit-Decisioning#get_reports_for_customer
    # GET /decisioning/v1/customers/{customerId}/reports
    def get_reports_for_customer(self, customer_id: int) -> List[ReportSummary]:
        """
        Get a list of reports that have been generated for the given consumer.
        The status fields in the returned list will contain 'inProgress', 'failure', or 'success'. If a status shows 'inProgress', wait 20 seconds and then call again.

        :param customer_id: ID of the customer
        :return:
        """
        path = f"/decisioning/v1/customers/{customer_id}/reports"
        response = self.__http_client.get(path)
        response_dict = response.json()
        return ReportsResponse.from_dict(response_dict).reports
