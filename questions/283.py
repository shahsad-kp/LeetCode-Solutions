from typing import List

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class Solution(BaseSolution):
    title = 'Move Zeroes'
    leetcode_link = 'https://leetcode.com/problems/move-zeroes'
    automatic_tests = TestCases(
        TestValue(
            inputs=[[0, 1, 0, 3, 12]],
            expected=[1, 3, 12, 0, 0]
        ),
        TestValue(
            inputs=[[0]],
            expected=[0]
        ),
        TestValue(
            inputs=[[0, 0, 1]],
            expected=[1, 0, 0]
        )
    )
    __solution_method__ = 'moveZeroes'

    def moveZeroes(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                j = i
                while j < len(nums) - 1 and nums[j] == 0:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
        return nums
