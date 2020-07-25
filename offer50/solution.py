"""
剑指 Offer 50. 第一个只出现一次的字符

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "



限制：

0 <= s 的长度 <= 50000

"""


class Solution:
    def firstUniqChar(self, s: str) -> str:
        """

        :param s:
        :return:
        """
        if s == ' ':
            return ''
        char_num = [0] * 26
        first_index_of_char_appear = [-1] * 26
        for i, c in enumerate(s):
            index = ord(c) - ord('a')
            char_num[index] += 1
            if first_index_of_char_appear[index] == -1:
                first_index_of_char_appear[index] = i
        result = ' '
        smallest_index = -1
        for i in range(26):
            if char_num[i] == 1:
                if result == ' ':
                    result = chr(i + ord('a'))
                    smallest_index = first_index_of_char_appear[i]
                else:
                    if smallest_index > first_index_of_char_appear[i]:
                        result = chr(i + ord('a'))
                        smallest_index = first_index_of_char_appear[i]
        return result


if __name__ == '__main__':
    s = 'aad'
    solution = Solution()
    print(solution.firstUniqChar(s))