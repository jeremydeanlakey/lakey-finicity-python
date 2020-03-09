from dataclasses import dataclass
from typing import List, Any, Optional


@dataclass
class Cadence(object):
    startDate: int  # postedDate of the first deposit transaction
    stopDate: Optional[int]  # postedDate of the final deposit transaction (omitted if status is active)
    days: int  # Number of days between the recurring deposits
    _unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        startDate = data.pop('startDate')
        stopDate = data.pop('stopDate', None)
        days = data.pop('days')
        return Cadence(
            startDate=startDate,
            stopDate=stopDate,
            days=days,
            _unused_fields=data,
        )
