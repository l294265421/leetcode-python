"""
剑指 Offer 42. 连续子数组的最大和

输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。



示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。



提示：

    1 <= arr.length <= 10^5
    -100 <= arr[i] <= 100

"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        以第i-th结尾的最大子数组的和等于i-th number + max(0, 以(i-1)-th结尾的最大子数组和)
        :param nums:
        :return:
        """
        result = -1
        maxima = [nums[i] for i in range(len(nums))]
        for i, num in enumerate(nums):
            if i == 0:
                result = num
            else:
                maxima[i] = nums[i] + max(0, maxima[i - 1])
                if maxima[i] > result:
                    result = maxima[i]
        return result