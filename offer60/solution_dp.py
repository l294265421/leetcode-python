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
        动态规划：
        (1) 状态：f(i, s)为投第i个骰子时，和为s的次数
        (2) 状态转移： f(i, s) = f(i - 1, s - 1) + ... + f(i - 1, s - 6)
        (3) 投第i个骰子，s的范围为从i 到 6*i；s至少为1
        :param n:
        :return:
        """
        counters = [[0] + [1] * 6]
        for i in range(1, n):
            this_counter = [0] * (6 * (i + 1) + 1)
            for s in range(i + 1, 6 * (i + 1) + 1):
                c = 0
                for pre_s in range(max(1, s - 6), min(s, 6 * i + 1)):
                    c += counters[i - 1][pre_s]
                this_counter[s] = c
            counters.append(this_counter)
        result_counter = counters[-1][n:]
        total = sum(result_counter)
        result = [num / total for num in result_counter]
        return result


if __name__ == '__main__':
    solution = Solution()
    n = 2
    result = solution.twoSum(n)
    print(result)