import json
import unittest

from lakey_finicity.responses.create_consumer_response import CreateConsumerResponse


DOCS_EXAMPLE_CREATE_CONSUMER_RESPONSE = """
{
  "id": "0h7h3r301md83",
  "createdDate": 1472342400
}
"""


class TestCreateConsumerResponse(unittest.TestCase):

    def test_create_consumer_response(self):
        response_dict = json.loads(DOCS_EXAMPLE_CREATE_CONSUMER_RESPONSE)
        response = CreateConsumerResponse.from_dict(response_dict)
        self.assertEqual({}, response._unused_fields)
