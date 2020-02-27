from dataclasses import dataclass


# https://community.finicity.com/s/article/VOA-Report
@dataclass
class ReportCustomField(object):
    unused_fields: dict  # this is for forward compatibility and should be empty
    label: str
    value: str
    shown: bool

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        label = data.pop("label")
        value = data.pop("value")
        shown = data.pop("shown")
        return ReportCustomField(
            label=label,
            value=value,
            shown=shown,
            unused_fields=data,
        )
