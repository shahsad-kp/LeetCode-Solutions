from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class Solution(BaseSolution):
    title = 'Isomorphic Strings'
    leetcode_link = 'https://leetcode.com/problems/isomorphic-strings'
    automatic_tests = TestCases(
        TestValue(
            inputs=["egg", "add"],
            expected=True
        ),
        TestValue(
            inputs=["foo", "bar"],
            expected=False
        ),
        TestValue(
            inputs=["paper", "title"],
            expected=True
        )
    )
    __solution_method__ = 'isIsomorphic'


    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_pattern = self.make_pattern_on_string(s)
        t_pattern = self.make_pattern_on_string(t)
        return s_pattern == t_pattern

    @staticmethod
    def make_pattern_on_string(s: str):
        replaces = {}
        pattern = ''
        top_char = 0
        for char in s:
            if char in replaces:
                replace = replaces[char]
            else:
                replace = str(top_char + 1)
                top_char += 1
                replaces[char] = replace
            pattern += replace
        return pattern
