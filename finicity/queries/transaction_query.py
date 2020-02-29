from typing import Optional

from finicity.api_http_client import ApiHttpClient
from finicity.models import SortOrder, TransactionsListResponse


class TransactionsQuery(object):
    def __init__(self, http_client: ApiHttpClient, customer_id: int, fromDate: int, toDate: int, sort: SortOrder = SortOrder.asc, include_pending: bool = True, account_id: Optional[str] = None):
        self.__http_client = http_client
        self.__customer_id: int = customer_id
        self.__account_id: Optional[str] = account_id
        self.__from_date: int = fromDate
        self.__to_date: int = toDate
        self.__sort: SortOrder = sort
        self.__include_pending: bool = include_pending

    def batches(self, batch_size: int = 25):
        i = 1
        while 1:
            batch = self.__fetch(start=i, limit=batch_size)
            yield batch.transactions
            i += batch_size
            if not batch.moreAvailable:
                break

    def __fetch(self, start: int, limit: int) -> TransactionsListResponse:
        if self.__account_id:
            path = f"/aggregation/v3/customers/{self.__customer_id}/accounts/{self.__account_id}/transactions"
        else:
            path = f"/aggregation/v3/customers/{self.__customer_id}/transactions"
        params = {
            "start": start,
            "limit": limit,
            "fromDate": self.__from_date,
            "toDate": self.__to_date,
            "includePending": self.__include_pending,
            "sort": self.__sort,
        }
        response = self.__http_client.get(path, params=params)
        response_dict = response.json()
        return TransactionsListResponse.from_dict(response_dict)

