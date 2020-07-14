# -*- coding: utf-8 -*-

"""
剑指 Offer 57. 和为s的两个数字

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，
则输出任意一对即可。



示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]

示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]



限制：

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^6


"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        从动态规划的角度来思考：
        f(i,j)表示i至j这段子数组中是否包含和为target的两个数，包含位置i和j的数；
        f(i, j) = f(i-1, j) or f(i, j - 1)
        :param nums:
        :param target:
        :return:
        """
        if nums is None or len(nums) < 2:
            return []
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] + nums[end] < target:
                start += 1
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                return [nums[start], nums[end]]
        return []