"""
剑指 Offer 34. 二叉树中和为某一值的路径

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。



示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

返回:

[
   [5,4,11,2],
   [5,8,4,5]
]



提示：

    节点总数 <= 10000

key idea:
上层路径的和可以被下层路径复用，不用等到最后来个对路径上的所有值求和
"""

from typing import List
import copy


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return []
        return self._path_sum(root, sum, 0, [])

    def _path_sum(self, root: TreeNode, sum: int, total: int, nums_about_total: List[int]) -> List[List]:
        nums_about_total_copy = copy.deepcopy(nums_about_total)
        nums_about_total_copy.append(root.val)
        total += root.val
        if root.left is None and root.right is None:
            if total == sum:
                return [nums_about_total_copy]
            else:
                return []
        result = []
        if root.left is not None:
            result.extend(self._path_sum(root.left, sum, total, nums_about_total_copy))
        if root.right is not None:
            result.extend(self._path_sum(root.right, sum, total, nums_about_total_copy))
        return result
