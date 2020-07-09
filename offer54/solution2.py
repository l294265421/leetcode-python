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


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """

        :param root:
        :param k:
        :return:
        """
        if root is None:
            raise Exception('argument error: root is None')
        return self._inner_kthLargest(root, [k])

    def _inner_kthLargest(self, root: TreeNode, k: []) -> int:
        right = root.right
        left = root.left
        if right is not None:
            result = self._inner_kthLargest(right, k)
            if k[0] == 0:
                return result
        k[0] -= 1
        if k[0] == 0:
            return root.val

        if left is not None:
            result = self._inner_kthLargest(left, k)
            if k[0] == 0:
                return result
        return None

