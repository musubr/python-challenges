import pytest
from src.algorithms.level_medium import get_longest_substring_wo_repetition


class TestLevelMedium:
    @pytest.mark.unit
    @pytest.mark.parametrize(
        "input_string, expected_output",
        [
            ("abcabcbb", 3),
            ("pwwskew", 4)
        ]
    )
    def test__get_longest_substring_wo_repetition_returns_length_of_longest_substring_without_repetition(self, input_string, expected_output):
        # Given input string

        # When
        output = get_longest_substring_wo_repetition(input_string)

        # Then
        assert output == expected_output

    @pytest.mark.unit
    def test__get_longest_substring_wo_repetition_returns_1_if_all_letters_of_input_string_are_the_same_letter(self):
        # Given / When
        output = get_longest_substring_wo_repetition("bbbbbb")

        # Then
        assert output == 1

    @pytest.mark.unit
    def test__get_longest_substring_wo_repetition_returns_length_of_input_string_if_all_characters_are_unique(self):
        # Given / When
        output = get_longest_substring_wo_repetition("abcdef")

        # Then
        assert output == 6
