from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class Solution(BaseSolution):
    title = 'Excel Sheet Column Title'
    leetcode_link = 'https://leetcode.com/problems/excel-sheet-column-title'
    __solution_method__ = 'convertToTitle'
    automatic_tests = TestCases(
        TestValue(
            inputs=[1],
            expected='A'
        ),
        TestValue(
            inputs=[28],
            expected='AB'
        ),
        TestValue(
            inputs=[701],
            expected='ZY'
        )
    )

    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber:
            columnNumber -= 1
            result = chr(ord('A') + (columnNumber % 26)) + result
            columnNumber //= 26
        return result
