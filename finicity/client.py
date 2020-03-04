from finicity.api_http_client import ApiHttpClient
from finicity.resources.accounts import Accounts
from finicity.resources.connections import Connections
from finicity.resources.consumers import Consumers
from finicity.resources.customers import Customers
from finicity.resources.institutions import Institutions
from finicity.resources.reports import Reports
from finicity.resources.testing import Testing
from finicity.resources.transactions import Transactions


class Client(object):
    def __init__(self, partner_id: str, partner_secret: str, app_key: str):
        """

        :param app_key: Finicity-App-Key from Developer Portal
        :param partner_id: Partner ID from Developer Portal
        :param partner_secret: Current value of Partner Secret from Developer Portal
        """
        self._http_client = client = ApiHttpClient(app_key=app_key, partner_id=partner_id, partner_secret=partner_secret)
        self.institutions = Institutions(client)
        self.customers = Customers(client)
        self.testing = Testing(client)
        self.accounts = Accounts(client)
        self.transactions = Transactions(client)
        self.reports = Reports(client)
        self.consumers = Consumers(client)
        self.connect = Connections(client, partner_id)

    def authenticate(self):
        self._http_client.authenticate()
