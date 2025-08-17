from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class Solution(BaseSolution):
    title = 'Add Digits'
    leetcode_link = 'https://leetcode.com/problems/add-digits'
    __solution_method__ = 'addDigits'
    automatic_tests = TestCases(
        TestValue(
            inputs=[38],
            expected=2
        ),
        TestValue(
            inputs=[0],
            expected=0
        ),
        TestValue(
            inputs=[10],
            expected=11
        )
    )

    def addDigits(self, num: int) -> int:
        while num >= 10:
            a = num
            digit_sum = 0
            while a:
                digit_sum += a % 10
                a //= 10
            num = digit_sum
        return num
