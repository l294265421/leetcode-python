"""
剑指 Offer 10- II. 青蛙跳台阶问题

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2

示例 2：

输入：n = 7
输出：21

提示：

    0 <= n <= 100

"""


class Solution:
    def numWays(self, n: int) -> int:
        """
        跳n级台阶，有f(n)种跳法
        当第一步跳1级台阶，剩下的台阶有f(n-1)种跳法；
        当第一步跳2级台阶，剩下的台阶有f(n-2)种跳法；

        :param n:
        :return:
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        last_last = 1
        last = 2
        modular = 1e9 + 7
        for i in range(3, n + 1):
            temp = last + last_last
            last_last = last
            last = temp if temp < modular else int(temp % modular)
        return last
