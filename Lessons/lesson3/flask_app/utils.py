import random
import string


def generate_passwords(length: int) -> str:
    chars = string.ascii_letters + string.digits
    str_password = ''

    for _ in range(length):
        str_password += random.choice(chars)

    return str_password
