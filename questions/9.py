from base_solution import BaseSolution
from test_cases import TestCases
from test_value import TestValue


class Solution(BaseSolution):
    title = 'Palindrome Number'
    leetcode_link = 'https://leetcode.com/problems/palindrome-number'
    automatic_tests = TestCases(
        TestValue(
            inputs=[121],
            expected=True
        ),
        TestValue(
            inputs=[-121],
            expected=False
        ),
        TestValue(
            inputs=[10],
            expected=False
        ),
        TestValue(
            inputs=[0],
            expected=True
        ),
        TestValue(
            inputs=[1234321],
            expected=True
        )
    )
    __solution_method__ = 'isPalindrome'

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_number = 0
        number = x
        while x != 0:
            last_digit = x % 10
            x = x // 10
            reversed_number = (reversed_number * 10) + last_digit

        return number == reversed_number
