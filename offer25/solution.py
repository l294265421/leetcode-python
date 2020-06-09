"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

限制：

0 <= 链表长度 <= 1000
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        elif l1 is not None and l2 is None:
            return l1
        elif l1 is None and l2 is not None:
            return l2
        result = None
        result_tail = None
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                temp = l1.next
                l1.next = None
                l = l1
                l1 = temp
            else:
                temp = l2.next
                l2.next = None
                l = l2
                l2 = temp

            if result is None:
                result = l
                result_tail = l
            else:
                result_tail.next = l
                result_tail = result_tail.next
        if l1 is not None:
            result_tail.next = l1
        else:
            result_tail.next = l2
        return result
