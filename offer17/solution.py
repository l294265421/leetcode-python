# -*- coding: utf-8 -*-

"""
剑指 Offer 17. 打印从1到最大的n位数

输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数
999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]



说明：

    用返回一个整数列表来代替打印
    n 为正整数


"""

from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        """
        为了避免大数超限，使用排列组合的方式得到最终结果
        :param n:
        :return:
        """
        if n < 1:
            return []
        result = []
        self._print_numbers(n, '', result)
        return result

    def _print_numbers(self, n, prefix: str, result: List[int]):
        """

        :param n:
        :param result:  保存最终结果
        :return:
        """
        for i in range(10):
            value = str(i)
            if i == 0 and len(prefix) == 0:
                value = ''
            this_prefix = prefix + value
            if n == 1:
                if len(this_prefix) != 0:
                    result.append(int(this_prefix))
            else:
                self._print_numbers(n - 1, this_prefix, result)


if __name__ == '__main__':
    solution = Solution()
    n = 2
    print(solution.printNumbers(n))

