from typing import Optional, List

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue

from helpers import list_to_tree


class Solution(BaseSolution):
    title = 'Binary Tree Postorder Traversal'
    leetcode_link = 'https://leetcode.com/problems/binary-tree-postorder-traversal'
    automatic_tests = TestCases(
        TestValue(
            inputs=[list_to_tree([1, None, 2, 3])],
            expected=[3, 2, 1]
        ),
        TestValue(
            inputs=[list_to_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])],
            expected=[4, 6, 7, 5, 2, 9, 8, 3, 1]
        ),
        TestValue(
            inputs=[list_to_tree([])],
            expected=[]
        ),
        TestValue(
            inputs=[list_to_tree([1])],
            expected=[1]
        )
    )
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
