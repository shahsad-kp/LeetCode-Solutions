from typing import Optional

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue

from helpers import TreeNode


class Solution(BaseSolution):
    title = 'Same Tree'
    leetcode_link = 'https://leetcode.com/problems/same-tree'
    automatic_tests = TestCases(
        TestValue(
            inputs=[
                TreeNode(1, TreeNode(2), TreeNode(3)),
                TreeNode(1, TreeNode(2), TreeNode(3))
            ],
            expected=True
        ),
        TestValue(
            inputs=[
                TreeNode(1, TreeNode(2)),
                TreeNode(1, None, TreeNode(2))
            ],
            expected=False
        ),
        TestValue(
            inputs=[
                None,
                None
            ],
            expected=True
        ),
        TestValue(
            inputs=[
                TreeNode(1, TreeNode(2), TreeNode(1)),
                TreeNode(1, TreeNode(1), TreeNode(2))
            ],
            expected=False
        )
    )
    __solution_method__ = 'isSameTree'

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
