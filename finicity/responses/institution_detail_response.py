from dataclasses import dataclass

from finicity.models import Institution


@dataclass
class InstitutionDetailResponse(object):
    institution: Institution
    _unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        institution_raw: dict = data.pop('institution')
        institution = Institution.from_dict(institution_raw)
        return InstitutionDetailResponse(
            institution=institution,
            _unused_fields=data,
        )
