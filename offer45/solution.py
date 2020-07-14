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
    def swap(self, nums: List[int], first: int, second: int):
        temp = nums[first]
        nums[first] = nums[second]
        nums[second] = temp

    def partition(self, nums: List[int], start: int, end: int):
        pivot = start - 1
        for i in range(start, end):
            if nums[i] + nums[end] < nums[end] + nums[i]:
                pivot += 1
                self.swap(nums, pivot, i)
        pivot += 1
        self.swap(nums, pivot, end)
        return pivot

    def quick_sort(self, nums: List[int], start: int, end: int):
        """
        每次将一个元素放入它应该在的位置
        :param nums:
        :return:
        """
        if start < end:
            mid = self.partition(nums, start, end)
            self.quick_sort(nums, start, mid - 1)
            self.quick_sort(nums, mid + 1, end)

    def minNumber(self, nums: List[int]) -> str:
        """
        得到的最小排列满足如下性质：
        如果num_a排在num_b前面，(0)[num_other][num_a][num_other][num_b][num_other] < [num_other][num_b][num_other][num_a][num_other],
        (1)即[num_a][num_other][num_b]< [num_b][num_other][num_a]
        (2)即 [num_a][num_b]< [num_b][num_a], 从(1)到（2）不好直接证明
        :param nums:
        :return:
        """
        if nums is None or len(nums) == 0:
            return ''
        nums = [str(num) for num in nums]
        self.quick_sort(nums, 0, len(nums) - 1)
        return ''.join(nums)


if __name__ == '__main__':
    nums = [1,1,1]
    solution = Solution()
    print(solution.minNumber(nums))