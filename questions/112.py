from typing import Optional

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue

from helpers import list_to_tree


class Solution(BaseSolution):
    title = 'Path Sum'
    leetcode_link = 'https://leetcode.com/problems/path-sum'
    automatic_tests = TestCases(
        TestValue(
            inputs=[
                list_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),
                22
            ],
            expected=True
        ),
        TestValue(
            inputs=[
                list_to_tree([1, 2, 3]),
                5
            ],
            expected=False
        ),
        TestValue(
            inputs=[
                list_to_tree([]),
                0
            ],
            expected=False
        )
    )
    __solution_method__ = 'hasPathSum'

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        if root.left and self.hasPathSum(root.left, targetSum - root.val):
            return True
        elif root.right and self.hasPathSum(root.right, targetSum - root.val):
            return True
        else:
            return False
