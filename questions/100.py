from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'<{self.val}, {self.left}-{self.right}>'


class Solution:
    __question__ = 'Same Tree'
    __leetcode__ = 'https://leetcode.com/problems/same-tree'
    __test_cases__ = [
        {
            'input': [
                TreeNode(1, TreeNode(2), TreeNode(3)),
                TreeNode(1, TreeNode(2), TreeNode(3))
            ],
            'output': True
        },
        {
            'input': [
                TreeNode(1, TreeNode(2)),
                TreeNode(1, None, TreeNode(2))
            ],
            'output': False
        },
        {
            'input': [
                None,
                None
            ],
            'output': True
        },
        {
            'input': [
                TreeNode(1, TreeNode(2), TreeNode(1)),
                TreeNode(1, TreeNode(1), TreeNode(2))
            ],
            'output': False
        }
    ]
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
