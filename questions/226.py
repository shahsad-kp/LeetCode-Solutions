from collections import deque
from typing import Optional

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"


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
    title = 'Invert Binary Tree'
    leetcode_link = 'https://leetcode.com/problems/invert-binary-tree'
    automatic_tests = TestCases(
        TestValue(
            inputs=[list_to_tree([4, 2, 7, 1, 3, 6, 9])],
            expected=list_to_tree([4, 7, 2, 9, 6, 3, 1])
        ),
        TestValue(
            inputs=[list_to_tree([2, 1, 3])],
            expected=list_to_tree([2, 3, 1])
        )
    )
    __solution_method__ = 'invertTree'

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
