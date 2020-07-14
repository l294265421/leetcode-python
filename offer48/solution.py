"""
剑指 Offer 48. 最长不含重复字符的子字符串

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。



示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。



提示：

    s.length <= 40000

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        f(i)表示以i-th char结尾的最长子串；如果i-th char没有出现f(i-1)中，f(i)=f(i-1) + i-th char;
        否则，假设跟i-th char一样的char在f(i-1)的index为j，f(i)=f(i-1)[j:] + i-th char
        :param s:
        :return:
        """
        if len(s) == 0:
            return 0
        longest_substring = s[0]
        longest_substring_of_i_minus_one = longest_substring
        for i in range(1, len(s)):
            char_i = s[i]
            index_of_char_i = longest_substring_of_i_minus_one.find(char_i)
            prefix = longest_substring_of_i_minus_one
            if index_of_char_i != -1:
                prefix = longest_substring_of_i_minus_one[index_of_char_i + 1:]
            longest_substring_of_i_minus_one = prefix + char_i
            if len(longest_substring_of_i_minus_one) > len(longest_substring):
                longest_substring = longest_substring_of_i_minus_one
        return len(longest_substring)


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("pwwkew"))