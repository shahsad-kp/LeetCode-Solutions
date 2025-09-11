from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class Solution(BaseSolution):
    title = 'Integer to Roman'
    leetcode_link = 'https://leetcode.com/problems/integer-to-roman/'
    automatic_tests = TestCases(
        TestValue(
            inputs=[3749],
            expected='MMMDCCXLIX'
        ),
        TestValue(
            inputs=[58],
            expected='LVIII'
        ),
        TestValue(
            inputs=[1994],
            expected='MCMXCIV'
        )
    )
    __solution_method__ = 'intToRoman'

    def intToRoman(self, num: int) -> str:
        roman_mapping = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }
        result = ''
        while num > 0:
            for key in roman_mapping.keys():
                if num >= key:
                    result += roman_mapping[key]
                    num -= key
                    break
        return result

