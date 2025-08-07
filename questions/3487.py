"""
You are given an integer array nums.

You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:

All elements in the subarray are unique.
The sum of the elements in the subarray is maximized.
Return the maximum sum of such a subarray.

 

Example 1:
Input: nums = [1,2,3,4,5]

Output: 15
Explanation:
Select the entire array without deleting any element to obtain the maximum sum.


Example 2:
Input: nums = [1,1,0,1,1]

Output: 1
Explanation:
Delete the element nums[0] == 1, nums[1] == 1, nums[2] == 0, and nums[3] == 1. Select the entire array [1] to obtain the maximum sum.


Example 3:
Input: nums = [1,2,-1,-2,1,0,-1]

Output: 3
Explanation:
Delete the elements nums[2] == -1 and nums[3] == -2, and select the subarray [2, 1] from [1, 2, 1, 0, -1] to obtain the maximum sum.

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
"""
from typing import List


class Solution:
    __question__ = 'Maximum Unique Subarray Sum After Deletions'
    __leetcode__ = 'https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion'
    __test_cases__ = [
        {
            'input': [
                [1, 2, 3, 4, 5]
            ],
            'output': 15
        },
        {
            'input': [
                [1, 1, 0, 1, 1]
            ],
            'output': 1
        },
        {
            'input': [
                [1, 2, -1, -2, 1, 0, -1]
            ],
            'output': 3
        },
        {
            'input': [
                [-100]
            ],
            'output': -100
        },
        {
            'input': [
                [-20,20]
            ],
            'output': 20
        }
    ]
    __solution_method__ = 'maxSum'

    def maxSum(self, nums: List[int]) -> int:
        seen = set()
        max_sum = 0
        all_negative = True
        max_negative = float('-inf')

        for num in nums:
            if num not in seen:
                seen.add(num)
                if num > 0:
                    max_sum += num
                    all_negative = False
                else:
                    max_negative = max(max_negative, num)

        return max_sum if not all_negative else max_negative
