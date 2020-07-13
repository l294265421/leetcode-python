"""
剑指 Offer 16. 数值的整数次方
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑
大数问题。



示例 1:

输入: 2.00000, 10
输出: 1024.00000

示例 2:

输入: 2.10000, 3
输出: 9.26100

示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25



说明:

    -100.0 < x < 100.0
    n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        flag = n >= 0
        if not flag:
            n *= -1
        result = self._my_pow_with_cache(x, n)
        if not flag:
            result = 1 / result
        return result

    def _my_pow_with_cache(self, x: float, n: int):
        if n == 0:
            return 1
        if n == 1:
            return x
        half = n // 2
        half_result = self._my_pow_with_cache(x, half)
        result = half_result * half_result
        if (half * 2 + 1) == n:
            result *= x
        return result