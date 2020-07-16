"""
剑指 Offer 57 - II. 和为s的连续正数序列

输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。



示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]

示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]



限制：

    1 <= target <= 10^5

"""

from typing import List


class Solution:
    def sum_one_to_n(self, n):
        return (1 + n) * n / 2

    def generate_result(self, x, n):
        return [i + x for i in range(1, n + 1)]

    def findContinuousSequence(self, target: int) -> List[List[int]]:
        """
        假设target是n个连续整数的和，
        target = (1 + 2 + ... + n) + n * x
        得到 x = (target - (1 + 2 + ... + n)) / n
        如果能整除，即可得到对应的n连续整数 (1 + x, 2 + x,...,n + x)
        如果当x等于0时，1 + 2 + ... + n > target，即可停止
        :param target:
        :return:
        """
        result = []
        n = 2
        while True:
            s = self.sum_one_to_n(n)
            if s > target:
                break
            if (target - s) % n == 0:
                x = int((target - s) / n)
                result.insert(0, self.generate_result(x, n))
            n += 1
        return result