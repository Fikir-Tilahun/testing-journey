from password_check import is_valid_password


def test_valid_password_passes():
    assert is_valid_password("Password123!")


def test_spaces_only_fails():
    assert not is_valid_password("        ")  


def test_too_short_fails():
    assert not is_valid_password("pas0D!")


def test_no_capital_fails():
    assert not is_valid_password("password0!")


def test_no_lowercase_fails():
    assert not is_valid_password("PASSWORD123#")


def test_no_special_character_fails():
    assert not is_valid_password("Password123")


def test_no_digit_fails():
    assert not is_valid_password("Password!")


def test_password_with_space_fails():
    assert not is_valid_password("Pass 1#word")


def test_none_fails():
    assert not is_valid_password(None)


def test_empty_string_fails():
    assert not is_valid_password("")


def test_exactly_8_characters_passes():
    assert is_valid_password("Passw0r!")
    

def test_7_characters_fails():
    assert not is_valid_password("Passw0!")
    

def test_password_with_tab_fails():
    assert not is_valid_password("Pass\t1#word")