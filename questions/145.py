from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'<{self.val} Left: {self.left} Right: {self.right}'


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
    __question__ = 'Binary Tree Postorder Traversal'
    __leetcode__ = 'https://leetcode.com/problems/binary-tree-postorder-traversal'
    __test_cases__ = [
        {
            'input': [list_to_tree([1, None, 2, 3])],
            'output': [3, 2, 1]
        },
        {
            'input': [list_to_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])],
            'output': [4, 6, 7, 5, 2, 9, 8, 3, 1]
        },
        {
            'input': [list_to_tree([])],
            'output': []
        },
        {
            'input': [list_to_tree([1])],
            'output': [1]
        }
    ]
    __solution_method__ = 'postorderTraversal'

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root:
            self.traverse(root, result)
        return result

    def traverse(self, node: TreeNode, result: list[int]):
        if node.left:
            self.traverse(node.left, result)
        if node.right:
            self.traverse(node.right, result)
        result.append(node.val)
