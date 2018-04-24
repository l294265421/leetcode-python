# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root is None:
            return result
        parents = [root]
        children = []
        current_level_val = []
        while len(parents) != 0:
            for parent in parents:
                current_level_val.append(parent.val)
                if not (parent.left is None):
                    children.append(parent.left)
                if not (parent.right is None):
                    children.append(parent.right)
            result.append(current_level_val)
            current_level_val = []
            parents = children
            children = []
        return result
