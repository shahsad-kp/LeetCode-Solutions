from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue


class Solution(BaseSolution):
    title = 'Word Pattern'
    leetcode_link = 'https://leetcode.com/problems/word-pattern'
    automatic_tests = TestCases(
        TestValue(
            inputs=["abba", "dog cat cat dog"],
            expected=True
        ),
        TestValue(
            inputs=["abba", "dog cat cat fish"],
            expected=False
        ),
        TestValue(
            inputs=["aaaa", "dog cat cat dog"],
            expected=False
        ),
        TestValue(
            inputs=["aaaa", "dog dog dog dog"],
            expected=True
        ),
        TestValue(
            inputs=["abba", "dog cat cat dog"],
            expected=True
        )
    )
    __solution_method__ = 'wordPattern'

    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        characters = list(pattern)
        pattern_matcher = {}
        added_words = set()
        if len(words) != len(characters):
            return False
        for i in range(len(words)):
            word = words[i]
            character = characters[i]
            if character in pattern_matcher and pattern_matcher[character] != word:
                return False
            elif character not in pattern_matcher and word in added_words:
                return False
            elif character not in pattern_matcher:
                pattern_matcher[character] = word
                added_words.add(word)
        return True
