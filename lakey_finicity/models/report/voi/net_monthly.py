from dataclasses import dataclass


# https://community.finicity.com/s/article/VOI-Report
from typing import Optional


@dataclass
class NetMonthly(object):
    _unused_fields: dict  # this is for forward compatibility and should be empty
    month: Optional[int]  # Timestamp for the first day of this month
    net: Optional[float]  # Total income during the given month, across all income streams

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        month = data.pop('month', None)
        net = data.pop('net', None)
        return NetMonthly(
            month=month,
            net=net,
            _unused_fields=data,
        )
