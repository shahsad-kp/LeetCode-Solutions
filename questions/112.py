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
