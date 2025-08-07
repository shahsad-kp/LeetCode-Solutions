class Solution:
    __question__ = 'Ugly Number'
    __leetcode__ = 'https://leetcode.com/problems/ugly-number'
    __solution_method__ = 'isUgly'
    __test_cases__ = [
        {
            'input': [6],
            'output': True
        },
        {
            'input': [1],
            'output': True
        },
        {
            'input': [14],
            'output': False
        }
    ]

    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        return n == 1
