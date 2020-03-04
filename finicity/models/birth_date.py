from dataclasses import dataclass


# https://community.finicity.com/s/article/Report-Consumers
@dataclass
class BirthDate(object):
    year: int
    month: int
    day_of_month: int

    def to_dict(self) -> dict:
        return {
            'year': f'{self.year:04}',  # The birthday's 4-digit year
            'month': f'{self.month:02}',  # The birthday's 2-digit month (01 is January)
            'dayOfMonth': f'{self.day_of_month:02}',  # The birthday's 2-digit day-of-month
        }
