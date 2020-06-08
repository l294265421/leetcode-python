# -*- coding: utf-8 -*-

"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。



示例 1：

输入：head = [1,3,2]
输出：[2,3,1]



限制：

0 <= 链表长度 <= 10000

"""

from typing import List

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head is not None:
            result: List = self.reversePrint(head.next)
            result.append(head.val)
        else:
            result = []
        return result


if __name__ == '__main__':
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(2)
    node1.next = node2
    node2.next = node3
    print(s.reversePrint(node1))
