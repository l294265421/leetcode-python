# -*- coding: utf-8 -*-

"""

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。



示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

给定 target = 5，返回 true。

给定 target = 20，返回 false。



限制：

0 <= n <= 1000

0 <= m <= 1000

"""

from typing import List

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        """
        (1)方案1，按元素一个一个匹配，时间复杂度为O(n)或者o(根号n * 根号n)
        (2)方案2，针对每一行，应用二分查找，时间复杂度O(根号n * log根号n)
        :param matrix:
        :param target:
        :return:
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        return self.findNumberIn2DArrayV2(matrix, target)

    def _binary_search(self, target: int, nums: List[int]):
        """
        二分查找，找到返回True，否则返回False
        :param target:
        :param nums:
        :return:
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                return True
        return False

    def findNumberIn2DArrayV2(self, matrix: List[List[int]], target: int) -> bool:
        """
        (2)方案2，针对每一行，应用二分查找，时间复杂度O(根号n * log根号n)
        :param matrix:
        :param target:
        :return:
        """
        for nums in matrix:
            is_found = self._binary_search(target, nums)
            if is_found:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    matrix = [
              [1,   4,  7, 11, 15],
              [2,   5,  8, 12, 19],
              [3,   6,  9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]
            ]
    target = 20
    print(s.findNumberIn2DArray(matrix, target))
