class Solution:
    __question__ = 'Add Digits'
    __leetcode__ = 'https://leetcode.com/problems/add-digits'
    __solution_method__ = 'addDigits'
    __test_cases__ = [
        {
            'input': [38],
            'output': 2
        },
        {
            'input': [0],
            'output': 0
        },
        {
            'input': [10],
            'output': 11
        }
    ]

    def addDigits(self, num: int) -> int:
        while num >= 10:
            a = num
            digit_sum = 0
            while a:
                digit_sum += a % 10
                a //= 10
            num = digit_sum
        return num
