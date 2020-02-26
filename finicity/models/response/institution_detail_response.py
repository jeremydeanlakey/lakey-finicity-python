from dataclasses import dataclass
from typing import List

from finicity.models import Institution
from finicity.models.institution.login_field import LoginField


# https://community.finicity.com/s/article/202460265-Institutions#get_institution_details
@dataclass
class InstitutionDetailResponse(object):
    institution: Institution
    loginForm: List[LoginField]
    unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        institution_raw: dict = data.pop('institution')
        institution = Institution.from_dict(institution_raw)
        loginForm_raw = data.pop('loginForm')
        loginForm = [LoginField.from_dict(d) for d in loginForm_raw]
        return InstitutionDetailResponse(
            institution=institution,
            loginForm=loginForm,
            unused_fields=data,
        )
