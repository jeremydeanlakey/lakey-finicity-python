from typing import Optional

from finicity.api_http_client import ApiHttpClient
from finicity.models import InstitutionsListResponse


class InstitutionsQuery(object):
    def __init__(self, http_client: ApiHttpClient, search_term: Optional[str] = None):
        self.__http_client = http_client
        self.__search_term = search_term

    def batches(self, batch_size: int = 25):
        i = 1
        while 1:
            batch = self.__fetch(start=i, limit=batch_size)
            yield batch.institutions
            i += batch_size
            if not batch.moreAvailable:
                break

    def __fetch(self, start: int = 1, limit: int = 25) -> InstitutionsListResponse:
        """Use this call to search all Financial Institutions (FI) the Finicity has connections with and supports.
        Return all financial institutions that contain the search text in the institution’s name, urlHomeApp, or urlLogonApp fields.
        To get a list of all FI’s, leave the search parameter out of the call.  If the search query is left blank, the API will return an error.
        If the value of moreAvailable in the response is true, you can retrieve the next page of results by increasing the value of the start parameter in your next request:
          ...&start=6&limit=5

        :param start: Starting index for this page of results
        :param limit: Maximum number of entries for this page of results
        :return:
        """
        # https://community.finicity.com/s/article/Get-Institutions
        path = "/institution/v2/institutions"
        params = {
            "start": start,
            "limit": limit,
        }
        if self.__search_term and self.__search_term != "*":
            params["search"] = self.__search_term
        response = self.__http_client.get(path, params=params)
        response_dict = response.json()
        return InstitutionsListResponse.from_dict(response_dict)
