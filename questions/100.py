from typing import Optional

from base_solution import BaseSolution
from test_cases import TestCases
from test_value import TestValue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'<{self.val}, {self.left}-{self.right}>'


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
