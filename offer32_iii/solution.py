"""
剑指 Offer 32 - III. 从上到下打印二叉树 III

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。



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
  [20,9],
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
        stack_for_pop = []
        stack_for_push = []
        stack_for_pop.append(root)
        row = []
        child_first = 'left'
        while len(stack_for_pop) != 0:
            head = stack_for_pop.pop()
            if child_first == 'left':
                if head.left is not None:
                    stack_for_push.append(head.left)
                if head.right is not None:
                    stack_for_push.append(head.right)
            else:
                if head.right is not None:
                    stack_for_push.append(head.right)
                if head.left is not None:
                    stack_for_push.append(head.left)
            row.append(head.val)
            if len(stack_for_pop) == 0:
                result.append(row)
                row = []
                if child_first == 'left':
                    child_first = 'right'
                else:
                    child_first = 'left'
                if stack_for_push == 0:
                    break
                else:
                    temp = stack_for_push
                    stack_for_push = stack_for_pop
                    stack_for_pop = temp
        return result
