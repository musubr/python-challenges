import re

# ------------------------------------------------------------------------------------------------------------------------------------------
# Problem 1
# A valid postal code  have to fulfill both the requirements below:
#   - P must be a number in the range from  to  inclusive.
#   - P must not contain more than one alternating repetitive digit pair.
#
# Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive
# digit pair is formed by two equal digits that have just a single digit between them.


def is_postcode_valid(P: int):
    P = str(P)
    regex_integer_in_range = r'^[1-9][\d]{5}$'  # Do not delete 'r'.
    regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'  # Do not delete 'r'.

    return bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2

# ------------------------------------------------------------------------------------------------------------------------------------------
