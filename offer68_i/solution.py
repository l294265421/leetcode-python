"""
面试题68 - I. 二叉搜索树的最近公共祖先

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]



示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。

示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。



说明:

    所有节点的值都是唯一的。
    p、q 为不同节点且均存在于给定的二叉搜索树中。

    p、q 为不同节点且均存在于给定的二叉树中。

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _merge_flags(self, flags1, flags2):
        flags1[0] = flags1[0] or flags2[0]
        flags1[1] = flags1[1] or flags2[1]

    def _inner_lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> []:
        """
        针对每一个节点，判断最近公共节点是否在左右子树里，或者就是这个节点；当当前节点是
        最近公共祖先时，有三种情况：
        (1) 左右子树各包含一个节点
        (2) 左子树包含一个，当前节点包含一个
        (3) 右子树包含一个，当前节点包含一个
        :param root:
        :param p:
        :param q:
        :param flags:
        :return:
        """
        flags = [False, False, None]
        if root.left is not None and (p.val < root.val or q.val < root.val):
            flags_left = self._inner_lowestCommonAncestor(root.left, p, q)
            if flags_left[-1] is not None:
                return flags_left
            else:
                self._merge_flags(flags, flags_left)

        if root.right is not None and (p.val > root.val or q.val > root.val):
            flags_right = self._inner_lowestCommonAncestor(root.right, p, q)
            if flags_right[-1] is not None:
                return flags_right
            else:
                self._merge_flags(flags, flags_right)

        if flags[0] and flags[1]:
            flags[2] = root
            return flags

        if not flags[0] and p.val == root.val:
            flags[0] = True
        elif not flags[1] and q.val == root.val:
            flags[1] = True
        if flags[0] and flags[1]:
            flags[2] = root
        return flags

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        flags = self._inner_lowestCommonAncestor(root, p, q)
        return flags[-1]