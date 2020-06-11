"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的
一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数
组的最小值为1。

示例 1：

输入：[3,4,5,1,2]
输出：1

示例 2：

输入：[2,2,2,0,1]
输出：0
"""

from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        """
        有两种情况，
        (1)数组是旋转过的，把数组等分为两份，如果中间数字比第一个小，最小数字就在左边那部分，否则在右边那部分；
        需要注意的是，每部分都包含中间点；
        (2)数组是没有旋转过的，最小数字就是第一个
        :param numbers:
        :return:
        """
        if numbers is None or len(numbers) == 0:
            return None
        start = 0
        end = len(numbers) - 1
        while start <= end:
            if numbers[0] <= numbers[-1]:
                return numbers[0]
            mid = (start + end) // 2
            if numbers[mid] >= numbers[start]:
                start = mid + 1
            else:
                end = mid
