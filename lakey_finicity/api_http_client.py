import json
import time
from typing import Optional
from requests import Response
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from lakey_finicity.utils import validate_secret


# https://docs.finicity.com/guide-to-partner-authentication-and-integration/
_FINICITY_URL_BASE = "https://api.finicity.com"
_TWO_HOURS_S = 60 * 60


def _retry_session(retries=3, backoff_factor=0.5) -> requests.Session:
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=(500, 502, 504),
    )
    adapter = HTTPAdapter(max_retries=retry)
    session = requests.Session()
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


class ApiHttpClient(object):
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
        self.last_response = None

    def get(self, path: str, params: Optional[dict] = None, extra_headers: Optional[dict] = None) -> Response:
        url = _FINICITY_URL_BASE + path
        token = self.__get_token()
        headers = {
            "Finicity-App-Key": self.__app_key,
            "Accept": "application/json",
            "Finicity-App-Token": token,
        }
        if extra_headers:
            headers.update(extra_headers)
        params = params or {}
        self.last_response = _retry_session().get(url, headers=headers, params=params)
        return self.last_response

    def post(self, path: str, data: Optional[dict], extra_headers: Optional[dict] = None) -> Response:
        url = _FINICITY_URL_BASE + path
        token = self.__get_token()
        headers = {
            "Finicity-App-Key": self.__app_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Finicity-App-Token": token,
        }
        if extra_headers:
            headers.update(extra_headers)
        self.last_response = _retry_session().post(url, data=json.dumps(data), headers=headers)
        return self.last_response

    def put(self, path: str, data: dict, extra_headers: Optional[dict] = None) -> Response:
        url = _FINICITY_URL_BASE + path
        token = self.__get_token()
        headers = {
            "Finicity-App-Key": self.__app_key,
            "Content-Type": "application/json",
            "Finicity-App-Token": token,
        }
        if extra_headers:
            headers.update(extra_headers)
        self.last_response = _retry_session().put(url, data=json.dumps(data), headers=headers)
        return self.last_response

    def delete(self, path: str, extra_headers: Optional[dict] = None) -> Response:
        url = _FINICITY_URL_BASE + path
        token = self.__get_token()
        headers = {
            "Finicity-App-Key": self.__app_key,
            "Content-Type": "application/json",
            "Finicity-App-Token": token,
        }
        if extra_headers:
            headers.update(extra_headers)
        self.last_response = _retry_session().delete(url, headers=headers)
        return self.last_response

    def __get_token(self) -> str:
        if not self.__token or time.time() >= self.__token_expiration:
            self.authenticate()
        return self.__token

    # https://community.finicity.com/s/article/Partner-Authentication
    # POST /aggregation/v2/partners/authentication
    def authenticate(self):
        """Validate the partner’s credentials (Finicity-App-Key, Partner ID, and Partner Secret) and return a temporary access token.
        The token must be passed in the HTTP header Finicity-App-Token on all subsequent API requests.
        The token is valid for two hours. You can have multiple active tokens at the same time.
        Five unsuccessful authentication attempts will cause the partner’s account to be locked.
        To unlock the account, send an email to support@lakey_finicity.com

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
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            self.__token = response.json()['token']
            self.__token_expiration = new_token_expiration
            return self.__token
        else:
            raise Exception(f"authentication issue {response.status_code}: {response.content}")

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
        response = self.put(path=path, data=data)
        if response.status_code == 204:
            self.__secret = new_partner_secret
        else:
            raise Exception(f"issue modifying secret: {response.status_code}: {response.reason}")
