from typing import List

from run_leetcode_solutions.base_solution import BaseSolution
from run_leetcode_solutions.test_cases import TestCases
from run_leetcode_solutions.test_value import TestValue

class Solution(BaseSolution):
    title = 'Best Time to Buy and Sell Stock'
    leetcode_link = 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock'
    __solution_method__ = 'maxProfit'
    automatic_tests = TestCases(
        TestValue(
            inputs= [[7, 1, 5, 3, 6, 4]],
            expected= 5
        ),
        TestValue(
            inputs= [[7,6,4,3,1]],
            expected= 0
        )
    )

    def maxProfit(self, prices: List[int]) -> int:
        min_price = None
        max_profit = 0
        for index, price in enumerate(prices):
            if min_price is None or price < min_price:
                min_price = price
            if min_price is not None and price > min_price:
                max_profit = max(max_profit, price - min_price)
        return max_profit
