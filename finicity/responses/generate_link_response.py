from dataclasses import dataclass


@dataclass
class GenerateLinkResponse(object):
    link: str
    unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        link: str = data.pop('link')
        return GenerateLinkResponse(
            link=link,
            unused_fields=data,
        )
