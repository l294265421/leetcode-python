"""
剑指 Offer 58 - II. 左旋转字符串

字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋
转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。



示例 1：

输入: s = "abcdefg", k = 2
输出: "cdefgab"

示例 2：

输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"



限制：

    1 <= k < s.length <= 10000


"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        """

        :param s:
        :param n:
        :return:
        """
        if s is None or len(s) < 1:
            return ''
        real_n = n % len(s)
        chars = [c for c in s]
        while real_n > 0:
            first_c = chars.pop(0)
            chars.append(first_c)
            real_n -= 1
        result = ''.join(chars)
        return result


if __name__ == '__main__':
    solution = Solution()
    s = 'abcde'
    print(solution.reverseLeftWords(s, 0))
    print(solution.reverseLeftWords(s, 1))
    print(solution.reverseLeftWords(s, 2))
    print(solution.reverseLeftWords(s, 3))
    print(solution.reverseLeftWords(s, 4))
    print(solution.reverseLeftWords(s, 5))
    print(solution.reverseLeftWords(s, 6))