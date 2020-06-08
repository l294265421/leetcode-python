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
        result = []
        cursor = head
        while cursor:
            result.append(cursor.val)
            cursor = cursor.next
        start = 0
        end = len(result) - 1
        while start < end:
            temp = result[start]
            result[start] = result[end]
            result[end] = temp
            start += 1
            end -= 1
        return result
