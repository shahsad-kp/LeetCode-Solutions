from typing import List


class Solution:
    __question__ = 'Best Time to Buy and Sell Stock'
    __leetcode__ = 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock'
    __solution_method__ = 'maxProfit'
    __test_cases__ = [
        {
            'input': [[7, 1, 5, 3, 6, 4]],
            'output': 5
        },
        {
            'input': [[7,6,4,3,1]],
            'output': 0
        }
    ]

    def maxProfit(self, prices: List[int]) -> int:
        min_price = None
        max_profit = 0
        for index, price in enumerate(prices):
            if min_price is None or price < min_price:
                min_price = price
            if min_price is not None and price > min_price:
                max_profit = max(max_profit, price - min_price)
        return max_profit
