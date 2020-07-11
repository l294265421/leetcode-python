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
        (1)待找数组没有被旋转
        (2) 待找数组被旋转了
        算法需要同时适应这两种情况
        logn的方法就是，将数组分成两部分，确定最小值在哪部分，我的方法：
        (1) 当numbers[mid] < numbers[-1]最小值在左侧（可同时出现在两种情况下）
        (2) 当numbers[mid] > numbers[-1]最小值在右侧（只出现在第二种情况下）
        (3) 当numbers[mid] == numbers[-1]，不确定，去掉数组中的numbers[-1]，因为去掉它不影响找最小值（
        可同时出现在两种情况下）

        :param numbers:
        :return:
        """
        if numbers is None or len(numbers) == 0:
            return None
        start = 0
        end = len(numbers) - 1
        while start < end:
            mid = (start + end) // 2
            if numbers[mid] < numbers[end]:
                end = mid
            elif numbers[mid] > numbers[end]:
                start = mid + 1
            else:
                end -= 1
        return numbers[start]
