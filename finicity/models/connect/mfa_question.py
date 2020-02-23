from dataclasses import dataclass


# https://community.finicity.com/s/article/207505363-Multi-Factor-Authentication-MFA
@dataclass
class MfaQuestion(object):
    text: str
