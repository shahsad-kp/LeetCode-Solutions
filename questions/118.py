from typing import List

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class Solution(BaseSolution):
    title = 'Pascal\'s Triangle'
    leetcode_link = 'https://leetcode.com/problems/pascals-triangle'
    automatic_tests = TestCases(
        TestValue(
            inputs=[
                5
            ],
            expected=[
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1]
            ]
        ),
        TestValue(
            inputs=[
                1
            ],
            expected=[
                [1]
            ]
        )
    )
    __solution_method__ = 'generate'

    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row in range(numRows):
            new_row = [1] * (row + 1)
            for i in range(1, row):
                new_row[i] = triangle[row - 1][i - 1] + triangle[row - 1][i]
            triangle.append(new_row)

        return triangle
