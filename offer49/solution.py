"""
剑指 Offer 49. 丑数

我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。



示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

说明:

    1 是丑数。
    n 不超过1690。

"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        一个丑数可以表示为2^i3^j5^k，将丑数从小到大排列，下一个丑数必定是前面某个丑数与2、3或5的乘积，即
        (1) 2^i3^j5^k = 2 * 2^{i - 1}3^j5^k
        (2) 2^i3^j5^k = 3 * 2^i3^{j-1}5^k
        (3) 2^i3^j5^k = 5 * 2^i3^j5^{k-1}
        :param n:
        :return:
        """
        if n == 0:
            return 0
        if n == 1:
            return 1

        ugly_numbers = [1]
        index_for_two = 0
        index_for_three = 0
        index_for_five = 0
        while len(ugly_numbers) < n:
            # 找到比ugly_numbers[-1]大的丑数
            candidate_from_two = ugly_numbers[index_for_two] * 2
            while candidate_from_two <= ugly_numbers[-1]:
                index_for_two += 1
                candidate_from_two = ugly_numbers[index_for_two] * 2

            candidate_from_three = ugly_numbers[index_for_three] * 3
            while candidate_from_three <= ugly_numbers[-1]:
                index_for_three += 1
                candidate_from_three = ugly_numbers[index_for_three] * 3

            candidate_from_five = ugly_numbers[index_for_five] * 5
            while candidate_from_five <= ugly_numbers[-1]:
                index_for_five += 1
                candidate_from_five = ugly_numbers[index_for_five] * 5

            if candidate_from_two <= candidate_from_three and candidate_from_two <= candidate_from_five:
                ugly_numbers.append(candidate_from_two)
                index_for_two += 1
            elif candidate_from_three <= candidate_from_two and candidate_from_three <= candidate_from_five:
                ugly_numbers.append(candidate_from_three)
                index_for_three += 1
            else:
                ugly_numbers.append(candidate_from_five)
                index_for_five += 1
        return ugly_numbers[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.nthUglyNumber(10))

