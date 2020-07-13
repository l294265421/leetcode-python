"""
剑指 Offer 13. 机器人的运动范围

地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？



示例 1：

输入：m = 2, n = 3, k = 1
输出：3

示例 2：

输入：m = 3, n = 1, k = 0
输出：1

提示：

    1 <= n,m <= 100
    0 <= k <= 20


"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited_node = set()
        self._move(m, n, 0, 0, k, visited_node)
        return len(visited_node)

    def _move(self, m: int, n: int, x: int, y: int, k, visited_node: {}):
        point_str = '%s-%s' % (x, y)
        if point_str in visited_node:
            return None
        visit_judge_result = self._can_visit(m, n, x, y, k)
        if not visit_judge_result:
            return None
        visited_node.add(point_str)
        self._move(m, n, x - 1, y, k, visited_node)
        self._move(m, n, x + 1, y, k, visited_node)
        self._move(m, n, x, y - 1, k, visited_node)
        self._move(m, n, x, y + 1, k, visited_node)

    def _can_visit(self, m: int, n: int, x: int, y: int, k: int):
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        if self._digit_sum(x) + self._digit_sum(y) > k:
            return False
        return True

    def _digit_sum(self, number):
        result = 0
        while number != 0:
            remainder = number % 10
            result += remainder
            number = number // 10
        return result