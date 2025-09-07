from typing import Optional, List

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue

from helpers import list_to_tree


class Solution(BaseSolution):
    title = 'Binary Tree Preorder Traversal'
    leetcode_link = 'https://leetcode.com/problems/binary-tree-preorder-traversal'
    automatic_tests = TestCases(
        TestValue(
            inputs=[list_to_tree([1, None, 2, 3])],
            expected=[1, 2, 3]
        ),
        TestValue(
            inputs=[list_to_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])],
            expected=[1, 2, 4, 5, 6, 7, 3, 8, 9]
        ),
        TestValue(
            inputs=[None],
            expected=[]
        ),
        TestValue(
            inputs=[list_to_tree([1])],
            expected=[1]
        )
    )
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
