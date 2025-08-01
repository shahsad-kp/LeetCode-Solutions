class Solution:
    __question__ = 'Valid Palindrome'
    __leetcode__ = 'https://leetcode.com/problems/valid-palindrome'
    __solution_method__ = 'isPalindrome'
    __test_cases__ = [
        {
            'input': ["A man, a plan, a canal: Panama"],
            'output': True
        }
    ]

    def isPalindrome(self, s: str) -> bool:
        string_length = len(s)
        start = 0
        end = string_length - 1
        while start < end:
            start_char = s[start].lower()
            end_char = s[end].lower()
            while not start_char.isalnum() and start < end:
                start += 1
                start_char = s[start].lower()

            while not end_char.isalnum() and start < end:
                end -= 1
                end_char = s[end].lower()
            if start_char != end_char:
                return False
            start += 1
            end -= 1
        return True
