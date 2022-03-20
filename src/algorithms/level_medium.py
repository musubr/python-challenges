from typing import Iterable
from itertools import combinations

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

    for combo in set(combinations(nums, 3)):
        combo = sorted(combo)
        if (sum(combo) == 0) and (combo not in d.values()):
            d[i] = combo
            i += 1

    return list(d.values())

# ------------------------------------------------------------------------------------------------------------------------------------------
