from dataclasses import dataclass


# https://community.finicity.com/s/article/207505363-Multi-Factor-Authentication-MFA
from finicity.models import AnsweredMfaQuestion


@dataclass
class MfaQuestion(object):
    text: str
    unused_fields: dict  # this is for forward compatibility and should be empty

    def answer(self, answer: str) -> AnsweredMfaQuestion:
        return AnsweredMfaQuestion(text=self.text, answer=answer, unused_fields=self.unused_fields)

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        text = data.pop('text')
        return MfaQuestion(
            text=text,
            unused_fields=data,
        )
