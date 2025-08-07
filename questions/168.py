class Solution:
    __question__ = 'Excel Sheet Column Title'
    __leetcode__ = 'https://leetcode.com/problems/excel-sheet-column-title'
    __solution_method__ = 'convertToTitle'
    __test_cases__ = [
        {
            'input': [1],
            'output': 'A'
        },
        {
            'input': [28],
            'output': 'AB'
        },
        {
            'input': [701],
            'output': 'ZY'
        }
    ]

    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber:
            columnNumber -= 1
            result = chr(ord('A') + (columnNumber % 26)) + result
            columnNumber //= 26
        return result
