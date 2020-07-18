"""
剑指 Offer 14- I. 剪绳子

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的
长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的
长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

提示：

    2 <= n <= 58

"""

class Solution:
    def cuttingRope(self, n: int) -> int:
        """
        前提：
        (1) m是未知的，所以m最大等于n
        动态规划：
        (1) 状态定义，f(i, j)，将长度为i的绳子分成j段能得到的最大积是多少；当i == j时，最大积
        为1；i 大于等于j才有意义；
        (2) 状态转移：f(i, j) = max(1 * f(i - 1, j - 1), 2 * f(i - 2, j - 1), (i - j + 1) * f(j - 1, j - 1))
        (3) 最终从f(n, 1), f(n, 2),..., f(n, n)中选出一个最大的
        (4) 消除的重复计算的地方在f(i - 1, j - 1)等的计算
        :param n:
        :return:
        """
        if n < 1:
            return 0
        if n == 1:
            return 1
        max_products = []
        # 长度为i + 1
        for i in range(n):
            row = []
            # 分成j + 1段
            for j in range(n):
                if j > i:
                    continue
                if j == 0: # 代表分成1段
                    row.append(i + 1)
                    continue
                if j == i:
                    row.append(1)
                    continue
                max_product_of_ij = -1
                for segment_len in range(1, i - j + 2):
                    product_of_ij = segment_len * max_products[i - segment_len][j - 1]
                    if product_of_ij > max_product_of_ij:
                        max_product_of_ij = product_of_ij
                row.append(max_product_of_ij)
            max_products.append(row)
        result = max(max_products[-1][1:])
        return result


if __name__ == '__main__':
    solution = Solution()
    print('result of 0: %d' % solution.cuttingRope(0))
    print('result of 1: %d' % solution.cuttingRope(1))
    print('result of 2: %d' % solution.cuttingRope(2))
    print('result of 8: %d' % solution.cuttingRope(8))