from typing import Optional, Mapping

from finicity.api_http_client import ApiHttpClient
from finicity.models.connect.connect_type import ConnectType
from finicity.models.content_type import ContentType
from finicity.responses.generate_link_response import GenerateLinkResponse


class Connections(object):
    def __init__(self, http_client: ApiHttpClient, partner_id: str):
        self.__http_client = http_client
        self.__partner_id = partner_id

    # https://community.finicity.com/s/article/Generate-Finicity-Connect-URL
    def generate_voa_link(self,
                          customer_id: str,
                          consumer_id: str,
                          content_type: ContentType = ContentType.JSON,
                          from_date: Optional[int] = None,
                          webhook: Optional[str] = None,
                          webhook_data: Optional[Mapping[str, str]] = None,
                          analytics: Optional[str] = None,
                          ) -> str:
        data = {
            'partnerId': self.__partner_id,
            'customerId': customer_id,
            'consumerId': consumer_id,
            'redirectUrl': consumer_id,
            'type': ConnectType.voa.value,
            'ContentType': content_type.value,
        }
        if from_date:
            data['fromDate'] = from_date
        if webhook:
            data['webhook'] = webhook
        if webhook_data:
            data['webhookData'] = webhook_data
        if analytics:
            data['analytics'] = analytics
        path = f"/connect/v1/generate"
        response = self.__http_client.post(path, data)
        response_dict = response.json()
        return GenerateLinkResponse.from_dict(response_dict).link

    # https://community.finicity.com/s/article/Generate-Finicity-Connect-URL
    def generate_aggregation_link(self,
                          customer_id: str,
                          consumer_id: str,
                          content_type: ContentType = ContentType.JSON,
                          webhook: Optional[str] = None,
                          webhook_data: Optional[Mapping[str, str]] = None,
                          analytics: Optional[str] = None,
                          ) -> str:
        data = {
            'partnerId': self.__partner_id,
            'customerId': customer_id,
            'consumerId': consumer_id,
            'redirectUrl': consumer_id,
            'type': ConnectType.aggregation.value,
            'ContentType': content_type.value,
        }
        if webhook:
            data['webhook'] = webhook
        if webhook_data:
            data['webhookData'] = webhook_data
        if analytics:
            data['analytics'] = analytics
        path = f"/connect/v1/generate"
        response = self.__http_client.post(path, data)
        response_dict = response.json()
        return GenerateLinkResponse.from_dict(response_dict).link

    # TODO note: from_date only for VOA
