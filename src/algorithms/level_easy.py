# ------------------------------------------------------------------------------------------------------------------------------------------
# Problem 1
# Given an integer x, return true if x is palindrome integer. An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

def is_palindrome(num: int) -> bool:
    """Returns true if the input number is a palindrome.

    Args:
        num: input number
    """
    return num == int(str(num)[::-1])

# ------------------------------------------------------------------------------------------------------------------------------------------
