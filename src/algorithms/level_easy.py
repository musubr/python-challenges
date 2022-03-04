import math

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


def check_if_palindrome_wo_int_to_str_conversion(num: int) -> bool:
    """Returns true if the input number is a palindrome.

    This function attempts to solve the same problem without converting the input integer to a string.

    Args:
        num: input number
    """
    order = 1
    mod_result = 0
    reverse_number = 0
    reverse_num_list = []

    if (num >= 0) and (num < 10):
        return True
    elif num < 0:
        return False
    else:
        while mod_result != num:
            mod_check = 10**order
            previous_mod_check = 10**(order-1)
            mod_result = num % mod_check

            if mod_result == (num % previous_mod_check):
                mod_result = 0
            if (mod_result == 0) and (order == 1):
                return False

            reverse_num_list += [math.floor(mod_result/previous_mod_check)]
            order += 1

        for i in range(len(reverse_num_list)):
            reverse_number += reverse_num_list[i]*(10**(len(reverse_num_list)-1-i))

        return num == reverse_number
# ------------------------------------------------------------------------------------------------------------------------------------------
