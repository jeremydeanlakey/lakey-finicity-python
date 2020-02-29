from typing import Optional, List

from finicity.api_http_client import ApiHttpClient
from finicity.models import Institution, ReportConsumer, BirthDate, PermissiblePurpose
from finicity.queries.institutions_query import InstitutionsQuery


class Reports(object):
    def __init__(self, http_client: ApiHttpClient):
        self.__http_client = http_client

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

