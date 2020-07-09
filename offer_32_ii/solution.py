"""
剑指 Offer 32 - II. 从上到下打印二叉树 II

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。



例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]



提示：

    节点总数 <= 1000

"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result
        queue = []
        queue.append(root)
        queue.append(None)
        row = []
        while len(queue) != 0:
            head = queue.pop(0)
            if head is not None:
                row.append(head.val)
                if head.left is not None:
                    queue.append(head.left)
                if head.right is not None:
                    queue.append(head.right)
            else:
                result.append(row)
                row = []
                if len(queue) != 0:
                    queue.append(None)
        return result
