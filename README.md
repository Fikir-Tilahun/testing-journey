# Testing Journey: Password Validator

A small Python project where I practice writing tests with pytest. It contains a password validation function and a test suite that checks each rule on its own.

## What the function checks

`is_valid_password(password)` returns `True` only if the password:

- is a string (anything else, such as `None` or a number, returns `False`)
- is at least 8 characters long
- contains at least one digit
- contains at least one uppercase letter
- contains at least one lowercase letter
- contains at least one special character (anything in `string.punctuation`)
- contains no whitespace (spaces, tabs or newlines)

## Project files

- `password_check.py`: the function
- `test_password_check.py`: the pytest tests
- `README.md`: this file

## How to run the tests

1. Install Python 3 and pytest:

   ```
   python -m pip install pytest
   ```

2. From the project folder, run:

   ```
   python -m pytest
   ```

You should see all tests pass.

## What the tests cover

- A valid password
- Each rule broken on its own (too short, no digit, no capital, no lowercase, no special character, contains whitespace)
- Boundary values: exactly 8 characters passes, 7 fails
- Bad input: empty string, `None`, whitespace-only text
- Whitespace types: a space and a tab

Each failing-password test breaks exactly one rule, so a failure shows which rule stopped working.

## Bugs the tests found

- **`None` crashed the function.** `len(None)` raised a `TypeError`. Fixed by checking `isinstance(password, str)` first.
- **Tabs were accepted.** The old rule only looked for the space character, so `"Pass\t1#word"` passed. I wrote the failing test first, watched it fail, then changed the rule to `isspace()`.

## What I learned

- Write the test first and watch it fail, so you know the test can catch the bug.
- A good test breaks exactly one rule.
- Break your own code on purpose to check that your tests notice.
- Check for a whole category of input (all whitespace), not just the one case you thought of.



## word_count

`word_count(text)` returns a dictionary of how many times each word appears.

Rules:
- Capitalization is ignored (`"The"` and `"the"` are the same word)
- Punctuation at the ends of words is ignored (`"hello,"` counts as `hello`)
- Extra spaces are ignored
- Empty text or `None` returns `{}`

Files: `word_count.py` and `test_word_count.py`

Bug the tests found: a lone punctuation mark like `-` was counted as an empty word. I wrote the failing test first, then fixed it.