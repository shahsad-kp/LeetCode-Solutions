class Solution:
    __question__ = 'Palindrome Number'
    __leetcode__ = 'https://leetcode.com/problems/palindrome-number'
    __test_cases__ = [
        {
            'input': [121],
            'output': True
        },
        {
            'input': [-121],
            'output': False
        },
        {
            'input': [10],
            'output': False
        },
        {
            'input': [0],
            'output': True
        },
        {
            'input': [1234321],
            'output': True
        }
    ]

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_number = 0
        number = x
        while x != 0:
            last_digit = x % 10
            x = x // 10
            reversed_number = (reversed_number * 10) + last_digit

        return number == reversed_number
