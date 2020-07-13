"""
剑指 Offer 45. 把数组排成最小的数

输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。



示例 1:

输入: [10,2]
输出: "102"

示例 2:

输入: [3,30,34,5,9]
输出: "3033459"



提示:

    0 < nums.length <= 100

"""

from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        """
        得到的最小排列满足如下性质：
        如果num_a排在num_b前面，[num_other][num_a][num_other][num_b][num_other] < [num_other][num_b][num_other][num_a][num_other],
        即[num_a][num_other][num_b]< [num_b][num_other][num_a]
        即 [num_a][num_b]< [num_b][num_a]
        :param nums:
        :return:
        """