from typing import List

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class Solution(BaseSolution):
    title = 'Single Number'
    leetcode_link = 'https://leetcode.com/problems/single-number'
    __solution_method__ = 'singleNumber'
    automatic_tests = TestCases(
        TestValue(
            inputs=[[2, 2, 1]],
            expected=1
        ),
        TestValue(
            inputs=[[4, 1, 2, 1, 2]],
            expected=4
        ),
        TestValue(
            inputs=[[1]],
            expected=1
        )
    )

    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res
