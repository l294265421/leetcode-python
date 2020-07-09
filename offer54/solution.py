"""
剑指 Offer 54. 二叉搜索树的第k大节点

给定一棵二叉搜索树，请找出其中第k大的节点。



示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4

示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4



限制：

1 ≤ k ≤ 二叉搜索树元素个数

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.right_visited = False


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """

        :param root:
        :param k:
        :return:
        """
        if root is None:
            raise Exception('argument error: root is None')
        stack = []
        stack.append(root)
        while len(stack) != 0:
            current = stack[-1]
            if current.right_visited:
                k -= 1
                if k == 0:
                    return current.val
                else:
                    stack.pop()
                    if current.left is not None:
                        stack.append(current.left)
            else:
                if current.right is not None:
                    stack.append(current.right)
                current.right_visited = True
        raise Exception('don\'t find the k-th largerst node')