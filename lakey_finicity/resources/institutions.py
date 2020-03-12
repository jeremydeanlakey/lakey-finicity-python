from typing import Optional

from lakey_finicity.api_http_client import ApiHttpClient
from lakey_finicity.models import Institution
from lakey_finicity.queries.institutions_query import InstitutionsQuery
from lakey_finicity.responses.institution_detail_response import InstitutionDetailResponse


class Institutions(object):
    def __init__(self, http_client: ApiHttpClient):
        self.__http_client = http_client

    def query(self, search_term: Optional[str] = None) -> InstitutionsQuery:
        """

        :param search_term: search text to match against the name, urlHomeApp, or urlLogonApp
        :return:
        """
        return InstitutionsQuery(self.__http_client, search_term)

    # https://community.finicity.com/s/article/Get-Institution
    def get(self, institution_id: str) -> Institution:
        """Get details for the specified institution without the login form.

        :param institution_id: ID of the institution to retrieve
        :return:
        """
        path = f"/institution/v2/institutions/{institution_id}"
        response = self.__http_client.get(path)
        response_dict = response.json()
        return InstitutionDetailResponse.from_dict(response_dict).institution
