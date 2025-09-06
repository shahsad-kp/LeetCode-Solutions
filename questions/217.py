from typing import List

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class Solution(BaseSolution):
    title = 'Contains Duplicate'
    leetcode_link = 'https://leetcode.com/problems/contains-duplicate'
    __solution_method__ = 'containsDuplicate'
    automatic_tests = TestCases(
        TestValue(
            inputs=[[1, 2, 3, 1]],
            expected=True
        ),
        TestValue(
            inputs=[[1, 2, 3, 4]],
            expected=False
        ),
        TestValue(
            inputs=[[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]],
            expected=True
        )
    )

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
