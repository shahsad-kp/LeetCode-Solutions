from typing import Optional

from base_solution import BaseSolution
from test_cases import TestCases
from test_value import TestValue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: 'TreeNode' = left
        self.right: 'TreeNode' = right


class Solution(BaseSolution):
    title = 'Symmetric Tree'
    leetcode_link = 'https://leetcode.com/problems/symmetric-tree'
    automatic_tests = TestCases(
        TestValue(
            inputs=[TreeNode(1, TreeNode(2), TreeNode(2))],
            expected=True
        ),
        TestValue(
            inputs=[TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))],
            expected=False
        ),
        TestValue(
            inputs=[None],
            expected=True
        ),
        TestValue(
            inputs=[TreeNode(1, TreeNode(2), TreeNode(3))],
            expected=False
        )
    )
    __solution_method__ = 'isSymmetric'

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_symmetric(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left is None or right is None:
                return left is None and right is None
            if left.val != right.val:
                return False
            return is_symmetric(left.left, right.right) and is_symmetric(left.right, right.left)

        if root is None:
            return True
        return is_symmetric(root.left, root.right)
