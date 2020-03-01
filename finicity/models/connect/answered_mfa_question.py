from dataclasses import dataclass


# https://community.finicity.com/s/article/207505363-Multi-Factor-Authentication-MFA
@dataclass
class AnsweredMfaQuestion(object):
    text: str
    answer: str  # Added by the partner for calls to the "MFA Answers" services
    unused_fields: dict  # this is for forward compatibility and should be empty

    def to_dict(self) -> dict:
        return {
            'text': self.text,
            'answer': self.answer,
        }

    @staticmethod
    def from_dict(data: dict):
        data = dict(data)  # don't mutate the original
        text = data.pop('text')
        answer = data.pop('answer')
        return AnsweredMfaQuestion(
            text=text,
            answer=answer,
            unused_fields=data,
        )
