import pytest
from src.algorithms.level_hard import is_postcode_valid


class TestLevelHard:
    @pytest.mark.unit
    @pytest.mark.parametrize(
        "input_postcode, expected_is_valid",
        [
            (100001, False),
            (523560, True)
        ]
    )
    def test__get_longest_substring_wo_repetition_returns_length_of_longest_substring_without_repetition(self, input_postcode, expected_is_valid):
        # Given input string

        # When
        is_valid = is_postcode_valid(input_postcode)

        # Then
        assert is_valid == expected_is_valid
