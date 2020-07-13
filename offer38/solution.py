"""
剑指 Offer 38. 字符串的排列

输入一个字符串，打印出该字符串中字符的所有排列。



你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。



示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]



限制：

1 <= s 的长度 <= 8

"""

from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        """

        :param s:
        :return:
        """
        return self.permutation_list([c for c in s], 0)

    def swap(self, s: list, first_index: int, second_index: int):
        temp = s[first_index]
        s[first_index] = s[second_index]
        s[second_index] = temp

    def permutation_list(self, s: List[str], position_need_to_fix):
        """
        对子数组s[position_need_to_fix:]进行排列
        :param s:
        :param position_need_to_fix:
        :return:
        """
        if position_need_to_fix == len(s) - 1:
            return [''.join(s)]
        unique_chars = set()
        result = []
        for i in range(position_need_to_fix, len(s)):
            if s[i] in unique_chars:
                continue
            else:
                unique_chars.add(s[i])
            # 移动元素进行排列
            self.swap(s, position_need_to_fix, i)
            current_result = self.permutation_list(s, position_need_to_fix + 1)
            result.extend(current_result)
            self.swap(s, position_need_to_fix, i)
        return result
