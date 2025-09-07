from typing import Optional

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue

from helpers import list_to_tree, TreeNode


class Solution(BaseSolution):
    title = 'Minimum Depth of Binary Tree'
    leetcode_link = 'https://leetcode.com/problems/minimum-depth-of-binary-tree'
    automatic_tests = TestCases(
        TestValue(
            inputs=[list_to_tree([3, 9, 20, None, None, 15, 7])],
            expected=2
        ),
        TestValue(
            inputs=[list_to_tree([2, None, 3, None, 4, None, 5, None, 6])],
            expected=5
        )
    )
    __solution_method__ = 'minDepth'

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.get_depth(root, 0)

    def get_depth(self, root: Optional[TreeNode], current_depth: int) -> int:
        left_depth = right_depth = 0
        current_depth += 1
        if root.left:
            left_depth = self.get_depth(root.left, current_depth)
        if root.right:
            right_depth = self.get_depth(root.right, current_depth)
        if root.left and root.right:
            return min(left_depth, right_depth)
        return left_depth or right_depth or current_depth
