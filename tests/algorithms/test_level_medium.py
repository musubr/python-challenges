import pytest
from src.algorithms.level_medium import get_longest_substring_wo_repetition, three_sum, get_letter_combos_of_phone_number


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

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "input_nums, expected_output",
        [
            ([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]]),
            ([1, 4, -3, -2, 0], [])
        ]
    )
    def test__three_sum_returns_list_of_triplets_from_original_list_of_nums_that_sum_to_zero(self, input_nums, expected_output):
        # Given input list of numbers

        # When
        output = three_sum(input_nums)

        # Then
        assert output == expected_output

    @pytest.mark.unit
    def test__three_sum_returns_empty_list_if_input_list_has_no_numbers(self):
        # Given / When
        output = three_sum([])

        # Then
        assert output == []

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "input_nums, expected_output",
        [
            ([0], []),
            ([0, 0], [])
        ]
    )
    def test__three_sum_returns_empty_list_if_input_list_contains_less_than_three_zeros(self, input_nums, expected_output):
        # Given / When
        output = three_sum([0])

        # Then
        assert output == expected_output

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "input_digit_string, expected_output",
        [
            ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
            ("98", ['wt', 'wu', 'wv', 'xt', 'xu', 'xv', 'yt', 'yu', 'yv', 'zt', 'zu', 'zv'])
        ]
    )
    def test__get_letter_combos_of_phone_number_returns_all_possible_letter_combos_for_a_given_phone_number(self, input_digit_string, expected_output):
        # Given input digit string

        # When
        output = get_letter_combos_of_phone_number(input_digit_string)

        # Then
        assert output == expected_output

    def test__get_letter_combos_of_phone_number_raises_exception_if_input_digit_contains_zero(self):
        # Given / When / Then
        with pytest.raises(ValueError):
            get_letter_combos_of_phone_number("203")

    def test__get_letter_combos_of_phone_number_raises_exception_if_input_digit_contains_one(self):
        # Given / When / Then
        with pytest.raises(ValueError):
            get_letter_combos_of_phone_number("213")