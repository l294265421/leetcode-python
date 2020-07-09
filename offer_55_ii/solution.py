"""
剑指 Offer 55 - II. 平衡二叉树

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度
相差不超过1，那么它就是一棵平衡二叉树。



示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7

返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

返回 false 。

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self._inner_is_balanced(root)[0]

    def _inner_is_balanced(self, root: TreeNode) -> []:
        if root is None:
            return [True, 0]
        left_result = self._inner_is_balanced(root.left)
        right_result = self._inner_is_balanced(root.right)
        return [left_result[0] and right_result[0] and (-1 <= (left_result[1] - right_result[1]) <= 1),
                max(left_result[1], right_result[1]) + 1]