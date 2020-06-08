# -*- coding: utf-8 -*-

"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中
都不含重复的数字。



例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7



限制：

0 <= 节点个数 <= 5000

"""

from typing import List, Dict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        1. 存在右子树的节点算是构建完成，不会继续赋予新的子节点
        2. 中序遍历中，左子树中的所有节点都先于根节点出现，右子树中的所有节点都后于根节点出现，
        可以用于判断前序遍历中一个节点出现在另一个节点的左子树中，还是右子树中
        3. 方案1： 往已经构建好的树中插入节点
        :param preorder:
        :param inorder:
        :return:
        """
        if preorder is None or len(preorder) == 0:
            return None
        value_index_mapping = {}
        for index, value in enumerate(inorder):
            value_index_mapping[value] = index
        root_node = TreeNode(preorder[0])
        for value in preorder[1:]:
            new_node = TreeNode(value)
            self._insert_node(root_node, new_node, value_index_mapping)
        return root_node

    def _insert_node(self, root: TreeNode, new_node: TreeNode, value_index_mapping_in_inorder: Dict):
        root_index = value_index_mapping_in_inorder[root.val]
        new_node_index = value_index_mapping_in_inorder[new_node.val]
        if new_node_index < root_index:
            left_node = root.left
            if left_node is None:
                root.left = new_node
            else:
                self._insert_node(left_node, new_node, value_index_mapping_in_inorder)
        else:
            right_node = root.right
            if right_node is None:
                root.right = new_node
            else:
                self._insert_node(right_node, new_node, value_index_mapping_in_inorder)


if __name__ == '__main__':
    s = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    result = s.buildTree(preorder, inorder)
    print(result)
