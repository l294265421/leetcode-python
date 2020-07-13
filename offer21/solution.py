"""
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数
组的后半部分。



示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。



提示：

    1 <= nums.length <= 50000
    1 <= nums[i] <= 10000


"""

from typing import List


class Solution:
    def _is_odd(self, number):
        if number & 1 == 1:
            return True
        else:
            return False

    def swap(self, nums, first_index, second_index):
        temp = nums[first_index]
        nums[first_index] = nums[second_index]
        nums[second_index] = temp

    def exchange(self, nums: List[int]) -> List[int]:
        right_bound_of_odd = -1
        for i in range(len(nums)):
            if self._is_odd(nums[i]):
                right_bound_of_odd += 1
                self.swap(nums, right_bound_of_odd, i)
        return nums
