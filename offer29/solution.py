"""
剑指 Offer 29. 顺时针打印矩阵

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。



示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]



限制：

    0 <= matrix.length <= 100
    0 <= matrix[i].length <= 100

"""

from typing import List


class Solution:
    def visit(self, matrix: List[List[int]], x_min: int, y_min: int, x_max: int, y_max: int) -> List[int]:
        result = []
        for i in range(y_min, y_max + 1):
            result.append(matrix[x_min][i])
        for i in range(x_min + 1, x_max):
            result.append(matrix[i][y_max])
        if x_min != x_max:
            for i in range(y_max, y_min - 1, -1):
                result.append(matrix[x_max][i])
        if y_min != y_max:
            for i in range(x_max - 1, x_min, -1):
                result.append(matrix[i][y_min])
        return result

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return result
        x_min = 0
        y_min = 0
        x_max = len(matrix) - 1
        y_max = len(matrix[0]) - 1
        while x_min <= x_max and y_min <= y_max:
            result_current = self.visit(matrix, x_min, y_min, x_max, y_max)
            result.extend(result_current)
            x_min += 1
            y_min += 1
            x_max -= 1
            y_max -= 1
        return result