# -*- coding: utf-8 -*-

"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。



示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."



限制：

0 <= s 的长度 <= 10000

"""

class Solution:
    def replaceSpace(self, s: str) -> str:
        char_array = []
        for c in s:
            if c == ' ':
                char_array.append('%20')
            else:
                char_array.append(c)
        return ''.join(char_array)