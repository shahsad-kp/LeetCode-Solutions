from typing import List


class Solution:
    __question__ = 'Majority Element'
    __leetcode__ = 'https://leetcode.com/problems/majority-element'
    __solution_method__ = 'majorityElement'
    __test_cases__ = [
        {
            'input': [
                [3, 2, 3]
            ],
            'output': 3
        },
        {
            'input': [
                [2, 2, 1, 1, 1, 2, 2]
            ],
            'output': 2
        }
    ]

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
                