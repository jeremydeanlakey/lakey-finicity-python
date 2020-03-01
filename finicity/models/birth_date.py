from dataclasses import dataclass


# https://community.finicity.com/s/article/Report-Consumers
@dataclass
class BirthDate(object):
    year: str  # The birthday's 4-digit year
    month: str  # The birthday's 2-digit month (01 is January)
    dayOfMonth: str  # The birthday's 2-digit day-of-month

    def to_dict(self) -> dict:
        return {
            'year': self.year,
            'month': self.month,
            'dayOfMonth': self.dayOfMonth,
        }
