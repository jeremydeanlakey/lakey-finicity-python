from dataclasses import dataclass


# https://community.finicity.com/s/article/VOI-Report
@dataclass
class NetMonthly(object):
    unused_fields: dict  # this is for forward compatibility and should be empty
    month: int  # Timestamp for the first day of this month
    net: float  # Total income during the given month, across all income streams

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        month = data.pop('month')
        net = data.pop('net')
        return NetMonthly(
            month=month,
            net=net,
            unused_fields=data,
        )
