from dataclasses import dataclass


# https://community.finicity.com/s/article/207505363-Multi-Factor-Authentication-MFA
@dataclass
class AnsweredMfaQuestion(object):
    text: str
    answer: str  # Added by the partner for calls to the "MFA Answers" services
