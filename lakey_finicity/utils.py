import re


def validate_secret(secret: str) -> bool:
    # see https://community.finicity.com/s/article/Modify-Partner-Secret
    # A valid partner secret may contain upper- and lowercase characters, numbers, and the characters !, @, #, $, %, &, *, _, -, +.
    if not re.match(r'^[A-Za-z0-9!@#$%&*_+-]*$', secret):  # note: '-' must be the last listed
        raise Exception("secret may only contain upper- and lowercase characters, numbers, and the characters !, @, #, $, %, &, *, _, -, +. see https://community.lakey_finicity.com/s/article/Modify-Partner-Secret")
    # It must include at least one number
    if not re.match(r'.*[0-9]+.*', secret):
        raise Exception("secret must include at least one number. see https://community.lakey_finicity.com/s/article/Modify-Partner-Secret")
    # and at least one letter,
    if not re.match(r'.*[a-zA-Z]+.*', secret):
        raise Exception("secret must include at least one letter. see https://community.lakey_finicity.com/s/article/Modify-Partner-Secret")
    # and its length should be between 12 and 255 characters.
    if len(secret) < 12 or len(secret) > 255:
        raise Exception("secret length should be between 12 and 255 characters.. see https://community.lakey_finicity.com/s/article/Modify-Partner-Secret")
    return True
