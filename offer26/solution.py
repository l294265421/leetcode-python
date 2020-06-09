"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false

示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true

限制：

0 <= 节点个数 <= 10000

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        """
        方案1：在树A中，以任意一个节点为根节点，看是否跟B一样
        :param A:
        :param B:
        :return:
        """
        if A is None or B is None:
            return False
        helper = [A]
        while len(helper) != 0:
            current_node = helper.pop(0)
            if current_node.left is not None:
                helper.append(current_node.left)
            if current_node.right is not None:
                helper.append(current_node.right)
            is_identical = self.isSubStructureFromRoot(current_node, B)
            if is_identical:
                return True
        return False

    def isSubStructureFromRoot(self, A: TreeNode, B: TreeNode) -> bool:
        """
        方案1：在树A中，以任意一个节点为根节点，看是否跟B一样
        :param A:
        :param B:
        :return:
        """
        if B is None and A is not None:
            return True
        elif A is None and B is not None:
            return False
        elif A is None and B is None:
            return True
        else:
            if A.val != B.val:
                return False
            else:
                identical_left_node_flag = self.isSubStructureFromRoot(A.left, B.left)
                identical_right_node_flag = self.isSubStructureFromRoot(A.right, B.right)
                return identical_left_node_flag and identical_right_node_flag