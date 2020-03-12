from dataclasses import dataclass
from typing import List
from lakey_finicity.models.institution.login_field import LoginField


# https://community.finicity.com/s/article/202460265-Institutions#get_institution_login_form
@dataclass
class InstitutionLoginFormResponse(object):
    loginForm: List[LoginField]
    _unused_fields: dict  # this is for forward compatibility and should be empty

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        loginForm_raw = data.pop('loginForm')
        loginForm = [LoginField.from_dict(d) for d in loginForm_raw]
        return InstitutionLoginFormResponse(
            loginForm=loginForm,
            _unused_fields=data,
        )
