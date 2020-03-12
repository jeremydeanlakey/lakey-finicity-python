from typing import Generator, List, Optional

from lakey_finicity.api_http_client import ApiHttpClient
from lakey_finicity.models import Customer
from lakey_finicity.responses import CustomersListResponse


DEFAULT_BATCH_SIZE = 25


class CustomersQuery(object):
    def __init__(self, http_client: ApiHttpClient, search_term: str = "*", username: str = None):
        self.__http_client = http_client
        self.__search_term = search_term
        self.__username = username

    def count(self) -> int:
        batch = self.__fetch(start=1, limit=1)
        return batch.found

    def batches(self, batch_size: int = DEFAULT_BATCH_SIZE) -> Generator[List[Customer], None, None]:
        i = 1
        while 1:
            batch = self.__fetch(start=i, limit=batch_size)
            yield batch.customers
            i += batch_size
            if not batch.moreAvailable:
                break

    def iter(self, batch_size: int = DEFAULT_BATCH_SIZE) -> Generator[Customer, None, None]:
        for batch in self.batches(batch_size):
            for item in batch:
                yield item

    def first_or_none(self) -> Optional[Customer]:
        batch = self.__fetch(start=1, limit=1)
        return batch.customers[0] if batch.customers else None

    # https://community.finicity.com/s/article/Get-Customers
    # GET /aggregation/v1/customers?search=[text]&start=[index]&limit=[count]&type=[type]&username=[username]
    def __fetch(self, start: int = 1, limit: int = 25) -> CustomersListResponse:
        """
        Find all customers enrolled by the current partner, where the search text is found in the customer's username or any combination of firstName and lastName fields. If no search text is provided, return all customers.
        Valid values for type are testing, active.
        If the value of moreAvailable in the responses is true, you can retrieve the next page of results by increasing the value of the start parameter in your next request:
        ...&start=6&limit=5

        :param start: Starting index for this page of results. The default value is 1.
        :param limit: Maximum number of entries for this page of results. The default value is 25.
        :return:
        """
        # note ripped off search_term: Must be URL-encoded (see Handling Spaces in Queries)
        # also do type = testing / active / [blank for all]
        # self._get_with_token()
        search_term = self.__search_term
        username = self.__username
        path = "/aggregation/v1/customers"
        params = {
            "start": start,
            "limit": limit,
        }
        if search_term and search_term != "*":
            params["search"] = search_term
        if username:
            params["username"] = username
        response = self.__http_client.get(path, params=params)
        response_dict = response.json()
        return CustomersListResponse.from_dict(response_dict)
