"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，
那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def _copy_tree(self, root: TreeNode):
        if root is None:
            return None
        copy_of_left_node = self._copy_tree(root.left)
        copy_of_right_node = self._copy_tree(root.right)
        result = TreeNode(root.val)
        result.left = copy_of_left_node
        result.right = copy_of_right_node
        return result

    def _mirror(self, root: TreeNode):
        helper = [root]
        while len(helper) != 0:
            current_node = helper.pop(0)
            temp = current_node.right
            current_node.right = current_node.left
            current_node.left = temp
            if current_node.left is not None:
                helper.append(current_node.left)
            if current_node.right is not None:
                helper.append(current_node.right)
        return root

    def _is_identical(self, A: TreeNode, B: TreeNode):
        if A is None and B is None:
            return True
        elif (A is None and B is not None) or (A is not None and B is None) or \
                (A is not None and B is not None and A.val != B.val):
            return False
        else:
            left_result = self._is_identical(A.left, B.left)
            if not left_result:
                return False
            right_result = self._is_identical(A.right, B.right)
            if not right_result:
                return False
            return True

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        copy_of_tree = self._copy_tree(root)
        mirror_of_copy = self._mirror(copy_of_tree)
        result = self._is_identical(root, mirror_of_copy)
        return result