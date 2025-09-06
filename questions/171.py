from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class Solution(BaseSolution):
    title = 'Excel Sheet Column Number'
    leetcode_link = 'https://leetcode.com/problems/excel-sheet-column-number'
    automatic_tests = TestCases(
        TestValue(
            inputs=['A'],
            expected=1
        ),
        TestValue(
            inputs=['B'],
            expected=2
        ),
        TestValue(
            inputs=['C'],
            expected=3
        ),
        TestValue(
            inputs=['Z'],
            expected=26
        ),
        TestValue(
            inputs=['AA'],
            expected=27
        ),
        TestValue(
            inputs=['AB'],
            expected=28
        )
    )
    __solution_method__ = 'titleToNumber'

    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle.upper():
            if 'A' <= char <= 'Z':
                result = result * 26 + (ord(char) - ord('A') + 1)
            else:
                raise ValueError(f"Invalid character '{char}' in column label.")
        return result