from typing import Iterable
import itertools

# ------------------------------------------------------------------------------------------------------------------------------------------
# Problem 1
# Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


def get_longest_substring_wo_repetition(s: str) -> int:
    if len(s) == len(set(s)):
        return len(s)
    else:
        for str_length in reversed(range(2, len(s)+1)):
            start_index = 0
            end_index = start_index + str_length

            while end_index <= len(s):
                fwd_word = s[start_index:end_index]
                rev_word = s[len(s)-end_index:(len(s)-end_index)+str_length]

                if (len(fwd_word) == len(set(fwd_word))) or (len(rev_word) == len(set(rev_word))):
                    return str_length

                start_index += 1
                end_index = start_index + str_length

        return 1

# ------------------------------------------------------------------------------------------------------------------------------------------
# Problem 2
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.

# Example
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]


def three_sum(nums: Iterable) -> Iterable:
    d = dict()
    i = 0

    for combo in set(itertools.combinations(nums, 3)):
        combo = sorted(combo)
        if (sum(combo) == 0) and (combo not in d.values()):
            d[i] = combo
            i += 1

    return list(d.values())

# ------------------------------------------------------------------------------------------------------------------------------------------
# Problem 3
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# Return the answer in any order.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#   1: no letters
#   2: a, b, c
#   3: d, e, f
#   4: g, h, i
#   5: j, k, l
#   6: m, n, o
#   7: p, q, r, s
#   8: t, u, v
#   9: w, x, y, z
#   0: no letters


def get_letter_combos_of_phone_number(digits_string: str) -> Iterable:
    if ("1" in digits_string) or ("0" in digits_string):
        raise(ValueError("This digit does not have any corresponding letters."))
    else:
        number_to_letter_mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        possible_letters = []

        for n in digits_string:
            possible_letters += [number_to_letter_mapping[n]]

        all_combinations = itertools.product(*possible_letters)

        return [''.join(c) for c in all_combinations]

# ------------------------------------------------------------------------------------------------------------------------------------------
# Problem 4
# An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its
# leaderboard works like this:
#
# The player with the highest score is ranked number 1 on the leaderboard.
# Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.


def climbing_leaderboard(ranked: list, player: list) -> Iterable:
    new_ranked = sorted(set(ranked+player), reverse=True)

    return [new_ranked.index(score)+1 for score in player]
# ------------------------------------------------------------------------------------------------------------------------------------------
