from typing import List

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue

class Solution(BaseSolution):
    title = 'Majority Element'
    leetcode_link = 'https://leetcode.com/problems/majority-element'
    __solution_method__ = 'majorityElement'
    automatic_tests = TestCases(
        TestValue(
            inputs= [
                [3, 2, 3]
            ],
            expected= 3
        ),
        TestValue(
            inputs= [
                [2, 2, 1, 1, 1, 2, 2]
            ],
            expected= 2
        )
    )

    def majorityElement(self, nums: List[int]) -> int:
        element_exists = {}

        for num in nums:
            if num in element_exists:
                element_exists[num] += 1
            else:
                element_exists[num] = 1
                
        major_element = [nums[0], element_exists[nums[0]]]
        for num in element_exists:
            if element_exists[num] > major_element[1]:
                major_element = [num, element_exists[num]]

        return major_element[0]
                