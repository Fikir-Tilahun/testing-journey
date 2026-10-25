import string
def is_valid_password(password):
    if not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char in string.punctuation for char in password):
        return False
    if any(char.isspace() for char in password):
        return False
    return True

