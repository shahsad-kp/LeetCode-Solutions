from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


class Solution:
    __question__ = 'Path Sum'
    __leetcode__ = 'https://leetcode.com/problems/path-sum'
    __test_cases__ = [
        {
            'input': [
                list_to_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),
                22
            ],
            'output': True
        },
        {
            'input': [
                list_to_tree([1,2,3]),
                5
            ],
            'output': False
        },
        {
            'input': [
                list_to_tree([]),
                0
            ],
            'output': False
        }
    ]
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
