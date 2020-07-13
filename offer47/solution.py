"""
剑指 Offer 47. 礼物的最大价值

在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上
角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼
物的价值，请计算你最多能拿到多少价值的礼物？



示例 1:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物



提示：

    0 < grid.length <= 200
    0 < grid[0].length <= 200


"""

from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        """
        在i, j位置能拿到的礼物的最大价值为f(i, j)：
        f(i, j) = grid[i][j] + max(f(i - 1, j), f(i, j - 1))
        :param grid:
        :return:
        """

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        max_values = []
        for i in range(len(grid)):
            row = []
            for j in range(len(grid[0])):
                row.append(0)
            max_values.append(row)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    max_values[i][j] = grid[i][j]
                elif i == 0 and j != 0:
                    max_values[i][j] = grid[i][j] + max_values[i][j - 1]
                elif i != 0 and j == 0:
                    max_values[i][j] = grid[i][j] + max_values[i - 1][j]
                else:
                    candidate1 = grid[i][j] + max_values[i][j - 1]
                    candidate2 = grid[i][j] + max_values[i - 1][j]
                    max_values[i][j] = max(candidate1, candidate2)
        return max_values[-1][-1]



