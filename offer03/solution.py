# -*- coding: utf-8 -*-

"""
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

2 <= len(nums) <= 100000
"""

from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        """
        2 <= len(nums) <= 100000
        :param nums:
        :return: 没有找到返回None
        """
        return self.findRepeatNumberV3(nums)

    def findRepeatNumberV1(self, nums: List[int]) -> int:
        """
        最直白的方案，用set作为辅助数据结构，记录之前出现过的数据，遇到第二次出现的数即刻返回；
        存储空间是N，时间复杂度是O(N);
        存在的问题：
        1. 需要占用额外的存储空间；
        :param nums:
        :return: 没有找到返回None
        """
        unique_nums = set()
        result = None
        for num in nums:
            if num in unique_nums:
                result = num
                break
            else:
                unique_nums.add(num)
        return result

    def findRepeatNumberV2(self, nums: List[int]) -> int:
        """
        通过二进制来统计次数，降低空间使用
        问题：
        1. 依旧需要占用额外空间

        :param nums:
        :return:
        """
        pass

    def findRepeatNumberV3(self, nums: List[int]) -> int:
        """
        考虑到“数组 nums 里的所有数字都在 0～n-1 的范围内”，是否可以原地统计呢？

        :param nums:
        :return:
        """
        for i in range(len(nums)):
            # 停止条件1
            # 如果不存在环，最多n-1步，就能找到等于i的num
            while nums[i] != i:
                # 停止条件2
                # 如果存在环
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                # 每一次都将一个num放回正确的位置，这种操作最多进行n次
                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp
        return None


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2]
    solution = Solution()
    print(solution.findRepeatNumber(nums))
