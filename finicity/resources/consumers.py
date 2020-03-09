from finicity.api_http_client import ApiHttpClient
from finicity.models import Consumer, BirthDate
from finicity.responses.create_consumer_response import CreateConsumerResponse


class Consumers(object):
    def __init__(self, http_client: ApiHttpClient):
        self.__http_client = http_client

    # https://community.finicity.com/s/article/Create-Consumer
    # POST /decisioning/v1/customers/{customerId}/consumer
    def create(self, customer_id: int, first_name: str, last_name: str, address: str, city: str, state: str, zip: str, phone: str, ssn: str, birthday: BirthDate, email: str) -> str:
        """
        Create a consumer record associated with the given customer. A consumer persists as the owner of any reports that are generated, even after the original customer is deleted from the system. A consumer must be created for the given customer before calling any of the Generate Report services.
        If a consumer already exists for this customer, this service will return HTTP 409 (Conflict).

        :param customer_id: ID of the customer
        :param first_name: The consumer's first name(s) / given name(s)
        :param last_name: The consumer's last name(s) / surname(s)
        :param address: The consumer's street address
        :param city: The consumer's city
        :param state: The consumer's state
        :param zip: The consumer's ZIP code
        :param phone: The consumer's phone number
        :param ssn: The consumer's 9-digit Social Security number (may include separators: nnn-nn-nnnn)
        :param birthday: The consumer's birth date
        :param email: The consumer's email address
        :return:
        """
        data = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "city": city,
            "state": state,
            "zip": zip,
            "phone": phone,
            "ssn": ssn,
            "birthday": birthday.to_padded_string_dict(),
            "email": email,
        }
        path = f"/decisioning/v1/customers/{customer_id}/consumer"
        response = self.__http_client.post(path, data)
        response_dict = response.json()
        return CreateConsumerResponse.from_dict(response_dict).id

    # https://community.finicity.com/s/article/Report-Consumers#get_consumer_for_customer
    # GET /decisioning/v1/customers/{customerId}/consumer
    def get_for_customer(self, customer_id: int) -> Consumer:
        """
        Get the details of a consumer record.
        If a consumer has not been created for this customer, the service will return HTTP 404 (Not Found)

        :param customer_id:
        :return:
        """
        path = f"/decisioning/v1/customers/{customer_id}/consumer"
        response = self.__http_client.get(path)
        response_dict = response.json()
        return Consumer.from_dict(response_dict)

    # https://community.finicity.com/s/article/Report-Consumers#get_consumer
    # GET /decisioning/v1/consumers/{consumerId}
    def get(self, consumer_id: str) -> Consumer:
        """
        Get the details of a consumer record.

        :param consumer_id: ID of the consumer (UUID with max length 32 characters)
        :return:
        """
        path = f"/decisioning/v1/consumers/{consumer_id}"
        response = self.__http_client.get(path)
        response_dict = response.json()
        return Consumer.from_dict(response_dict)

    # https://community.finicity.com/s/article/Report-Consumers#modify_consumer
    # PUT /decisioning/v1/consumers/{consumerId}
    def modify(self, consumer_id: str, first_name: str, last_name: str, address: str, city: str, state: str, zip: str, phone: str, ssn: str, birthday: BirthDate, year: str):
        """
        Modify the details for an existing consumer. All fields are required for a consumer record, but individual fields for this call are optional because fields that are not specified will be left unchanged.

        :param consumer_id: ID of the consumer (UUID with max length 32 characters)
        :param first_name: The consumer's first name(s) / given name(s)
        :param last_name: The consumer's last name(s) / surname(s)
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
        path = f"/decisioning/v1/consumers/{consumer_id}"
        data = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "city": city,
            "state": state,
            "zip": zip,
            "phone": phone,
            "ssn": ssn,
            "birthday": birthday.to_padded_string_dict(),
            "year": year,
        }
        self.__http_client.put(path, data=data)
