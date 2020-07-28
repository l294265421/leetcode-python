"""
面试题 02.04. 分割链表

编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包
含 x，x 只需出现在小于 x 的元素之后(如下所示)。分割元素 x 只需处于“右半部分”即可，其不需要
被置于左右两部分之间。

示例:

输入: head = 3->5->8->5->10->2->1, x = 5
输出: 3->1->2->10->5->5->8


"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """

        :param head:
        :param x:
        :return:
        """
        if head is None:
            return None

        left_head = None
        left_cursor = None

        right_head = None
        right_cursor = None

        cursor = head
        while cursor is not None:
            if cursor.val < x:
                if left_head is None:
                    left_head = cursor
                    left_cursor = cursor
                else:
                    left_cursor.next = cursor
                    left_cursor = cursor
            else:
                if right_head is None:
                    right_head = cursor
                    right_cursor = cursor
                else:
                    right_cursor.next = cursor
                    right_cursor = cursor
            temp = cursor.next
            cursor.next = None
            cursor = temp
        if left_cursor is None:
            return right_head
        else:
            left_cursor.next = right_head
            return left_head