from collections import deque
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
        return f'<TreeNode({self.val}) {self.left} {self.right}>'


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


class Solution(BaseSolution):
    title = 'Minimum Depth of Binary Tree'
    leetcode_link = 'https://leetcode.com/problems/minimum-depth-of-binary-tree'
    automatic_tests = TestCases(
        TestValue(
            inputs=[list_to_tree([3, 9, 20, None, None, 15, 7])],
            expected=2
        ),
        TestValue(
            inputs=[list_to_tree([2, None, 3, None, 4, None, 5, None, 6])],
            expected=5
        )
    )
    __solution_method__ = 'minDepth'

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.get_depth(root, 0)

    def get_depth(self, root: Optional[TreeNode], current_depth: int) -> int:
        left_depth = right_depth = 0
        current_depth += 1
        if root.left:
            left_depth = self.get_depth(root.left, current_depth)
        if root.right:
            right_depth = self.get_depth(root.right, current_depth)
        if root.left and root.right:
            return min(left_depth, right_depth)
        return left_depth or right_depth or current_depth
