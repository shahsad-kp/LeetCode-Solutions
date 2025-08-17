from typing import List

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class Solution(BaseSolution):
    title = 'Merge Sorted Array'
    leetcode_link = 'https://leetcode.com/problems/merge-sorted-array'
    automatic_tests = TestCases(
        TestValue(
            inputs=[
                [1, 2, 3, 0, 0, 0],
                3,
                [2, 5, 6],
                3
            ],
            expected=[1, 2, 2, 3, 5, 6]
        ),
        TestValue(
            inputs=[
                [1],
                1,
                [],
                0
            ],
            expected=[1]
        ),
        TestValue(
            inputs=[
                [0],
                0,
                [1],
                1
            ],
            expected=[1]
        ),
        TestValue(
            inputs=[
                [4, 5, 6, 0, 0, 0],
                3,
                [1, 2, 3],
                3
            ],
            expected=[1, 2, 3, 4, 5, 6]
        )
    )
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
