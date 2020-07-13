"""
剑指 Offer 12. 矩阵中的路径

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一
格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能
再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，
路径不能再次进入这个格子。



示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false

提示：

    1 <= board.length <= 200
    1 <= board[i].length <= 200

"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """

        :param board:
        :param word:
        :return:
        """
        if len(word) == 0:
            return True
        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.exist_by_tree(board, word, x, y, {}):
                    return True
        return False

    def exist_by_tree(self, board: List[List[str]], word: str, x, y, visited_point: set()):
        """
        判断以x,y位置开始的路径是否有包含word的
        :param board:
        :param word:
        :param x:
        :param y:
        :return:
        """
        point_str = '%s-%s' % (x, y)
        if point_str in visited_point:
            return False
        if board[x][y] != word[0]:
            return False
        else:
            word = word[1:]
            if len(word) == 0:
                return True

            new_visited_point = set([e for e in visited_point])
            new_visited_point.add(point_str)
            if x > 0:
                result_up = self.exist_by_tree(board, word, x - 1, y, new_visited_point)
                if result_up:
                    return True
            if x < len(board) - 1:
                result_low = self.exist_by_tree(board, word, x + 1, y, new_visited_point)
                if result_low:
                    return True
            if y > 0:
                left_result = self.exist_by_tree(board, word, x, y - 1, new_visited_point)
                if left_result:
                    return True
            if y < len(board[0]) - 1:
                right_result = self.exist_by_tree(board, word, x, y + 1, new_visited_point)
                if right_result:
                    return True
            return False