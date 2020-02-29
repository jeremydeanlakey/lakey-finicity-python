from finicity.api_http_client import ApiHttpClient
from finicity.institutions import Institutions


class Client(object):
    def __init__(self, app_key: str, partner_id: str, partner_secret: str):
        """

        :param app_key: Finicity-App-Key from Developer Portal
        :param partner_id: Partner ID from Developer Portal
        :param partner_secret: Current value of Partner Secret from Developer Portal
        """
        self._http_client = client = ApiHttpClient(app_key=app_key, partner_id=partner_id, partner_secret=partner_secret)
        self.institutions = Institutions(client)
