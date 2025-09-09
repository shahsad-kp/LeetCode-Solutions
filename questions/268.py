from typing import List

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class Solution(BaseSolution):
    title = 'Missing Numbers'
    leetcode_link = 'https://leetcode.com/problems/missing-number'
    automatic_tests = TestCases(
        TestValue(
            inputs=[[3, 0, 1]],
            expected=2
        ),
        TestValue(
            inputs=[[0, 1]],
            expected=2
        ),
        TestValue(
            inputs=[[9, 6, 4, 2, 3, 5, 7, 0, 1]],
            expected=8
        )
    )
    __solution_method__ = 'missingNumber'

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n + 1):
            if i not in nums:
                return i
        return -1
