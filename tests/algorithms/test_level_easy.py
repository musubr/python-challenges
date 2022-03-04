import pytest
from src.algorithms.level_easy import is_palindrome


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
