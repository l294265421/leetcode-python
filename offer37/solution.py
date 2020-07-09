"""
剑指 Offer 37. 序列化二叉树

请实现两个函数，分别用来序列化和反序列化二叉树。

示例:

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return 'null'
        strs = [str(root.val)]
        left_str = self.serialize(root.left)
        strs.append(left_str)

        right_str = self.serialize(root.right)
        strs.append(right_str)
        print(','.join(strs))
        return ','.join(strs)

    def deserialize(self, data) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if isinstance(data, str):
            data = data.split(',')
        if len(data) == 0:
            return None
        val = data[0]
        data.pop(0)
        if val == 'null':
            return None
        root = TreeNode(val)
        left = self.deserialize(data)
        right = self.deserialize(data)
        root.left = left
        root.right = right
        return root