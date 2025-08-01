from typing import List


class Solution:
    __question__ = 'Merge Sorted Array'
    __leetcode__ = 'https://leetcode.com/problems/merge-sorted-array'
    __test_cases__ = [
        {
            'input': [
                [1, 2, 3, 0, 0, 0],
                3,
                [2, 5, 6],
                3
            ],
            'output': [1, 2, 2, 3, 5, 6]
        },
        {
            'input': [
                [1],
                1,
                [],
                0
            ],
            'output': [1]
        },
        {
            'input': [
                [0],
                0,
                [1],
                1
            ],
            'output': [1]
        },
        {
            'input': [
                [4, 5, 6, 0, 0, 0],
                3,
                [1, 2, 3],
                3
            ],
            'output': [1, 2, 3, 4, 5, 6]
        }
    ]
    __solution_method__ = 'merge'

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        return nums1
