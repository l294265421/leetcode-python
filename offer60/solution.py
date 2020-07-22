"""
剑指 Offer 60. n个骰子的点数

把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。



你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。



示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]

示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]



限制：

1 <= n <= 11

"""

from typing import List


class Solution:
    def twoSum(self, n: int) -> List[float]:
        """
        求和，最小值，n；最大值 6n；中间是连续的，因为每次可以只增加1；
        :param n:
        :return:
        """
        num_len = 5 * n + 1
        num_counter = [0] * num_len
        self._two_sum(n, num_counter, 0, n)
        total = sum(num_counter)
        result = [num / total for num in num_counter]
        return result

    def _two_sum(self, n: int, num_counter: List[int], sum: int, total_n: int):
        """

        :param n:
        :param num_counter:
        :param sum:
        :return:
        """
        if n == 1:
            for i in range(1, 7):
                sum_new = sum + i
                num_counter[sum_new - total_n] += 1
        else:
            for i in range(1, 7):
                sum_new = sum + i
                self._two_sum(n - 1, num_counter, sum_new, total_n)


if __name__ == '__main__':
    solution = Solution()
    n = 10
    result = solution.twoSum(n)
    print(result)