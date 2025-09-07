from typing import Optional

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue

from helpers import list_to_tree, TreeNode


class Solution(BaseSolution):
    title = 'Invert Binary Tree'
    leetcode_link = 'https://leetcode.com/problems/invert-binary-tree'
    automatic_tests = TestCases(
        TestValue(
            inputs=[list_to_tree([4, 2, 7, 1, 3, 6, 9])],
            expected=list_to_tree([4, 7, 2, 9, 6, 3, 1])
        ),
        TestValue(
            inputs=[list_to_tree([2, 1, 3])],
            expected=list_to_tree([2, 3, 1])
        )
    )
    __solution_method__ = 'invertTree'

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
