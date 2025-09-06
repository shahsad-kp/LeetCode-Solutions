from collections import deque
from typing import Optional, List

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'

    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right


def list_to_tree(data):
    if not data or data[0] is None:
        return None

    root = TreeNode(data[0])
    queue = deque([root])
    i = 1

    while queue and i < len(data):
        current = queue.popleft()

        if i < len(data) and data[i] is not None:
            current.left = TreeNode(data[i])
            queue.append(current.left)
        i += 1

        if i < len(data) and data[i] is not None:
            current.right = TreeNode(data[i])
            queue.append(current.right)
        i += 1

    return root


class Solution(BaseSolution):
    title = 'Convert Sorted Array to Binary Search Tree'
    automatic_tests = TestCases(
        TestValue(
            inputs=[
                [-10, -3, 0, 5, 9]
            ],
            expected=list_to_tree([0, -3, 9, -10, None, 5])
        ),
        TestValue(
            inputs=[
                [1, 3]
            ],
            expected=list_to_tree([3, 1])
        )
    )
    leetcode_link = 'https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree'
    __solution_method__ = 'sortedArrayToBST'

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        return self.make_bst(nums)

    def make_bst(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])
        center = len(nums) // 2
        root = TreeNode(nums[center])
        left_numbers = nums[:center]
        root.left = self.make_bst(left_numbers)
        if center + 1 < len(nums):
            root.right = self.make_bst(nums[center + 1:])
        return root
