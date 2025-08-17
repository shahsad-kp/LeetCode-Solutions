from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class Solution(BaseSolution):
    title = 'Valid Palindrome'
    leetcode_link = 'https://leetcode.com/problems/valid-palindrome'
    __solution_method__ = 'isPalindrome'
    automatic_tests = TestCases(
        TestValue(
            inputs=["A man, a plan, a canal: Panama"],
            expected=True
        )
    )

    def isPalindrome(self, s: str) -> bool:
        string_length = len(s)
        start = 0
        end = string_length - 1
        while start < end:
            start_char = s[start].lower()
            end_char = s[end].lower()
            while not start_char.isalnum() and start < end:
                start += 1
                start_char = s[start].lower()

            while not end_char.isalnum() and start < end:
                end -= 1
                end_char = s[end].lower()
            if start_char != end_char:
                return False
            start += 1
            end -= 1
        return True
