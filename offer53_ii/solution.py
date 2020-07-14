"""
剑指 Offer 53 - II. 0～n-1中缺失的数字

一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的
n个数字中有且只有一个数字不在该数组中，请找出这个数字。



示例 1:

输入: [0,1,3]
输出: 2

示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8



限制：

1 <= 数组长度 <= 10000

"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        目标是保存的数大于index的第一个数的index；如果不存在这个index，result就是n
        :param nums:
        :return:
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > mid:
                # 至少包含一个nums[mid] > mid
                end = mid
            else:
                start = mid + 1
        # 针对没有保存的数大于index的情况
        if nums[start] == start:
            return len(nums)
        return start