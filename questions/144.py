from collections import deque
from typing import Optional, List


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
    __question__ = 'Binary Tree Preorder Traversal'
    __leetcode__ = 'https://leetcode.com/problems/binary-tree-preorder-traversal'
    __test_cases__ = [
        {
            'input': [list_to_tree([1, None, 2, 3])],
            'output': [1, 2, 3]
        },
        {
            'input': [list_to_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])],
            'output': [1, 2, 4, 5, 6, 7, 3, 8, 9]
        },
        {
            'input': [None],
            'output': []
        },
        {
            'input': [list_to_tree([1])],
            'output': [1]
        }
    ]
    __solution_method__ = 'preorderTraversal'

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res: list[int] = []
        stack: list[TreeNode] = []
        if root:
            stack.append(root)
        while len(stack) != 0:
            element = stack.pop()
            if element.right:
                stack.append(element.right)
            if element.left:
                stack.append(element.left)
            res.append(element.val)
        return res
