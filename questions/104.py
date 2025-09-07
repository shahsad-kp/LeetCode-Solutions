from typing import Optional

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue

from helpers import TreeNode


class Solution(BaseSolution):
    title = 'Maximum Depth of Binary Tree'
    leetcode_link = 'https://leetcode.com/problems/maximum-depth-of-binary-tree'
    automatic_tests = TestCases(
        TestValue(
            inputs=[3, 9, 20, None, None, 15, 7],
            expected=3
        ),
        TestValue(
            inputs=[1, None, 2],
            expected=2
        ),
        TestValue(
            inputs=[],
            expected=0
        ),
        TestValue(
            inputs=[1],
            expected=1
        )
    )
    __solution_method__ = 'maxDepth'

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.__get_maximum_depth(root, 1)

    def __get_maximum_depth(self, node: Optional[TreeNode], current_depth: int):
        right_depth = left_depth = current_depth
        if node.left:
            left_depth = self.__get_maximum_depth(node.left, current_depth + 1)
        if node.right:
            right_depth = self.__get_maximum_depth(node.right, current_depth + 1)
        if right_depth > left_depth:
            return right_depth
        else:
            return left_depth
