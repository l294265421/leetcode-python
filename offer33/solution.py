"""
剑指 Offer 33. 二叉搜索树的后序遍历序列

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回
 false。假设输入的数组的任意两个数字都互不相同。



参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3

示例 1：

输入: [1,6,3,2,5]
输出: false

示例 2：

输入: [1,3,2,6,5]
输出: true



提示：

    数组长度 <= 1000


"""

from typing import List


class Solution:

    def _verify_postorder(self, postorder: List[int], start: int, end: int) -> bool:
        if end - start <= 0:
            return True
        last = postorder[end]
        first_index_gt_last = -1
        for i in range(start, end):
            if postorder[i] > last:
                first_index_gt_last = i
                break
        if first_index_gt_last == -1:
            return self._verify_postorder(postorder, start, end - 1)
        result = True
        for i in range(first_index_gt_last + 1, end):
            if postorder[i] < last:
                result = False
                break
        if not result:
            return False
        if first_index_gt_last == start:
            return self._verify_postorder(postorder, start, end - 1)
        else:
            return self._verify_postorder(postorder, start, first_index_gt_last - 1) and \
                   self._verify_postorder(postorder, first_index_gt_last, end - 1)

    def verifyPostorder(self, postorder: List[int]) -> bool:
        if postorder is None:
            return True
        return self._verify_postorder(postorder, 0, len(postorder) - 1)
