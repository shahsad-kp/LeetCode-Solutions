from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: 'TreeNode' = left
        self.right: 'TreeNode' = right


class Solution:
    __question__ = 'Symmetric Tree'
    __leetcode__ = 'https://leetcode.com/problems/symmetric-tree'
    __test_cases__ = [
        {
            'input': [TreeNode(1, TreeNode(2), TreeNode(2))],
            'output': True
        },
        {
            'input': [TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))],
            'output': False
        },
        {
            'input': [None],
            'output': True
        },
        {
            'input': [TreeNode(1, TreeNode(2), TreeNode(3))],
            'output': False
        }
    ]

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
