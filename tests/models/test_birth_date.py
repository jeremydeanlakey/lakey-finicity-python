import json
import unittest

from finicity.models import BirthDate


EXAMPLE_BIRTH_DATE_PADDED = '''
{
    "year": "1972",
    "month": "07",
    "dayOfMonth": "03"
}
'''


class TestBirthDate(unittest.TestCase):
    def test_birth_date(self):
        original_dict = json.loads(EXAMPLE_BIRTH_DATE_PADDED)
        birth_date = BirthDate.from_dict(original_dict)
        back_to_dict = birth_date.to_padded_string_dict()
        birth_date_2 = BirthDate.from_dict(back_to_dict)
        self.assertEqual(birth_date, birth_date_2)
