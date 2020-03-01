from finicity.api_http_client import ApiHttpClient
from finicity.models import CustomersListResponse


class CustomersQuery(object):
    def __init__(self, http_client: ApiHttpClient, search_term: str = "*", username: str = None):
        self.__http_client = http_client
        self.__search_term = search_term
        self.__username = username

    def batches(self, batch_size: int = 25):
        i = 1
        while 1:
            batch = self.__fetch(start=i, limit=batch_size)
            yield batch.customers
            i += batch_size
            if not batch.moreAvailable:
                break

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
