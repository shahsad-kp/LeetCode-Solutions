from typing import List

from base_solution import BaseSolution


class Solution(BaseSolution):
    title = 'Pascal\'s Triangle'
    leetcode_link = 'https://leetcode.com/problems/pascals-triangle'
    automatic_tests = [
        {
            'input': [
                5
            ],
            'output': [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1]
            ]
        },
        {
            'input': [
                1
            ],
            'output': [
                [1]
            ]
        }
    ]
    __solution_method__ = 'generate'

    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row in range(numRows):
            new_row = [1] * (row + 1)
            for i in range(1, row):
                new_row[i] = triangle[row - 1][i - 1] + triangle[row - 1][i]
            triangle.append(new_row)

        return triangle
