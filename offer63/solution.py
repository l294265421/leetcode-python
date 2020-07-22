"""
剑指 Offer 63. 股票的最大利润

假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？



示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。



限制：

0 <= 数组长度 <= 10^5
"""

from typing import List


class Solution:
    def max_price(self, prices: List[int], start_index: int):
        max_price = -1
        max_price_index = -1
        for i in range(start_index, len(prices)):
            if prices[i] > max_price:
                max_price = prices[i]
                max_price_index = i
        return max_price_index, max_price

    def maxProfit_simple(self, prices: List[int]) -> int:
        """
        针对每一个买点，它的最大收益是在它之后的最大值处卖出；
        移动到一个买点时，如果它是之前的最大值，就需要重新找后面元素的最大值，
        否则直接用之前的最大值减去当前值;
        减少计算量的点在于复用之前求得的最大值
        :param prices:
        :return:
        """
        if prices is None or len(prices) < 2:
            return 0
        max_profit = 0
        max_price_index, max_price = self.max_price(prices, 0)
        for i, price in enumerate(prices):
            if i == max_price_index:
                max_price_index, max_price = self.max_price(prices, i + 1)
                continue
            max_profit_of_this_point = max_price - price
            if max_profit_of_this_point > max_profit:
                max_profit = max_profit_of_this_point
        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        """
        动态规划:
        (1) 状态定义：f(i) 前i天的最大收益
        (2) 状态转移: f(i) = max(f(i - 1), nums[i] - min)
        :param prices:
        :return:
        """
        if prices is None or len(prices) < 2:
            return 0
        max_profits = [0] * len(prices)
        minimum = prices[0]
        for i in range(1, len(prices)):
            max_profits[i] = max(max_profits[i - 1], prices[i] - minimum)
            if prices[i] < minimum:
                minimum = prices[i]
        return max_profits[-1]
