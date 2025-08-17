from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class Solution(BaseSolution):
    title = 'Ugly Number'
    leetcode_link = 'https://leetcode.com/problems/ugly-number'
    __solution_method__ = 'isUgly'
    automatic_tests = TestCases(
        TestValue(
            inputs=[6],
            expected=True
        ),
        TestValue(
            inputs=[1],
            expected=True
        ),
        TestValue(
            inputs=[14],
            expected=False
        ),
    )

    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        return n == 1
