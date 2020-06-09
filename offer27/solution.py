"""
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1



示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        helper = [root]
        while len(helper) !=0 :
            current_node = helper.pop(0)
            temp = current_node.right
            current_node.right = current_node.left
            current_node.left = temp
            if current_node.left is not None:
                helper.append(current_node.left)
            if current_node.right is not None:
                helper.append(current_node.right)
        return root

