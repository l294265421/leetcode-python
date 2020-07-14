"""
剑指 Offer 53 - I. 在排序数组中查找数字 I

统计一个数字在排序数组中出现的次数。



示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0



限制：

0 <= 数组长度 <= 50000
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        先找到，再统计
        :param nums:
        :param target:
        :return:
        """
        if len(nums) == 0:
            return 0
        index = -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                index = mid
                break
        if index == -1:
            return 0
        result = 1
        cursor = index + 1
        while cursor < len(nums) and nums[cursor] == target:
            result += 1
            cursor += 1
        cursor = index - 1
        while cursor >= 0 and nums[cursor] == target:
            result += 1
            cursor -= 1
        return result