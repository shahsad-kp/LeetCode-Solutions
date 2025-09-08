from typing import Optional, List

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue

from helpers import TreeNode, list_to_tree


class Solution(BaseSolution):
    title = 'Binary Tree Paths'
    leetcode_link = 'https://leetcode.com/problems/binary-tree-paths'
    __solution_method__ = 'binaryTreePaths'
    automatic_tests = TestCases(
        TestValue(
            inputs=[list_to_tree([1, 2, 3, None, 5])],
            expected=["1->2->5", "1->3"]
        ),
        TestValue(
            inputs=[list_to_tree([1])],
            expected=["1"]
        )
    )

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.generate_paths(root)

    def generate_paths(self, root: TreeNode, base_path: str = None) -> List[str]:
        if root is None:
            return [base_path]
        if base_path:
            base_path += f'->{root.val}'
        else:
            base_path = str(root.val)
        if not root.left and not root.right:
            return [base_path]
        left_leafs = right_leafs = []
        if root.left:
            left_leafs = self.generate_paths(root.left, base_path)
        if root.right:
            right_leafs = self.generate_paths(root.right, base_path)
        return left_leafs + right_leafs