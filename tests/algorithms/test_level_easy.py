import pytest
from src.algorithms.level_easy import is_palindrome, check_if_palindrome_wo_int_to_str_conversion


class TestLevelEasy:
    @pytest.mark.unit
    @pytest.mark.parametrize(
        "input_number, expected_output",
        [
            (101, True),
            (100, False)
        ]
    )
    def test__is_palindrome_returns_true_if_input_integer_is_a_palindrome(self, input_number, expected_output):
        # Given input number

        # When
        output = is_palindrome(input_number)

        # Then
        assert output == expected_output

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "input_number, expected_output",
        [
            (123321, True),
            (100011, False)
        ]
    )
    def test__check_if_palindrome_wo_int_to_str_conversion_returns_true_if_input_integer_is_a_palindrome(self, input_number, expected_output):
        # Given input number

        # When
        output = check_if_palindrome_wo_int_to_str_conversion(input_number)

        # Then
        assert output == expected_output
