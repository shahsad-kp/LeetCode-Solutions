from typing import List

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class Solution(BaseSolution):
    title = 'Summary Ranges'
    leetcode_link = 'https://leetcode.com/problems/summary-ranges'
    automatic_tests = TestCases(
        TestValue(
            inputs=[[0, 1, 2, 4, 5, 7]],
            expected=["0->2","4->5","7"]
        ),
        TestValue(
            inputs=[[0, 2, 3, 4, 6, 8, 9]],
            expected=["0","2->4","6","8->9"]
        )
    )
    __solution_method__ = 'summaryRanges'

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]
                ranges.append(f"{start}->{end}" if start != end else str(start))
                start = nums[i]

        end = nums[-1]
        ranges.append(f"{start}->{end}" if start != end else str(start))

        return ranges
