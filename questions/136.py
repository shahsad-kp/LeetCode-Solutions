from typing import List


class Solution:
    __question__ = 'Single Number'
    __leetcode__ = 'https://leetcode.com/problems/single-number'
    __solution_method__ = 'singleNumber'
    __test_cases__ = [
        {
            'input': [[2, 2, 1]],
            'output': 1
        },
        {
            'input': [[4, 1, 2, 1, 2]],
            'output': 4
        },
        {
            'input': [[1]],
            'output': 1
        }
    ]

    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res
