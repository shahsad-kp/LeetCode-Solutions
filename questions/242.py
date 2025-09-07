from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class Solution(BaseSolution):
    title = 'Valid Anagram'
    leetcode_link = 'https://leetcode.com/problems/valid-anagram'
    automatic_tests = TestCases(
        TestValue(
            inputs=["anagram", "nagaram"],

            expected=True
        ),
        TestValue(
            inputs=["rat", "car"],
            expected=False
        )
    )
    __solution_method__ = 'isAnagram'

    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower()
        t = t.lower()
        if len(s) != len(t):
            return False
        values_counter_s = {}
        values_counter_t = {}
        for char in s:
            values_counter_s[char] = values_counter_s.get(char, 0) + 1

        for char in t:
            values_counter_t[char] = values_counter_t.get(char, 0) + 1

        for letter in values_counter_s:
            if values_counter_t.get(letter, 0) != values_counter_s.get(letter, 0):
                return False
        return True
