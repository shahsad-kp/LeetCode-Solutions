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
    __question__ = 'Minimum Depth of Binary Tree'
    __leetcode__ = 'https://leetcode.com/problems/minimum-depth-of-binary-tree'
    __test_cases__ = [
        {
            'input': list_to_tree([3, 9, 20, None, None, 15, 7]),
            'output': 2
        },
        {
            'input': list_to_tree([2,None,3,None,4,None,5,None,6]),
            'output': 5
        }
    ]

    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.get_depth(root, 0)

    def get_depth(self, root: Optional[TreeNode], current_depth: int) -> int:
        if not root:
            return current_depth
        left_depth = self.get_depth(root.left, current_depth + 1)
        right_depth = self.get_depth(root.right, current_depth + 1)
        return min(left_depth, right_depth)

