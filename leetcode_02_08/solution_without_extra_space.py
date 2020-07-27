"""
面试题 02.08. 环路检测

给定一个有环链表，实现一个算法返回环路的开头节点。
有环链表的定义：在链表中某个节点的next元素指向在它前面出现过的节点，则表明该链表存在环路。

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。


进阶：
你是否可以不用额外空间解决此题？

（一）两个指针必定相遇，且两指针相遇时，慢指针还没有走完整个链表
这个问题你可以用数学归纳法来思考。首先，由于链表是个环，所以相遇的过程可以看作是快指针从后边追
赶慢指针的过程。那么做如下思考：
1：快指针与慢指针之间差一步。此时继续往后走，慢指针前进一步，快指针
前进两步，两者相遇。
2：快指针与慢指针之间差两步。此时唏嘘往后走，慢指针前进一步，快指针前进两步，两者之间相差一步，
转化为第一种情况。3：快指针与慢指针之间差N步。此时继续往后走，慢指针前进一步，快指针前进两步，
两者之间相差(N+1-2)-> N-1步。
因此，此题得证。所以快指针必然与慢指针相遇。又因为快指针速度是慢指针
的两倍，所以相遇时慢指针必然只绕了一圈。

（二）
然后，我们来证明，快慢指针相遇后，慢指针再往前移LenA个节点就刚好到达Join点。
假设第一次相遇点为Pos，环起点为Join，头结点到环起点的长度为LenA，环起点到第一次相遇点的长度为x，第一次相遇点到环起点的长度为y，环长为R，于是有以下结果：
（1）第一次相遇时，slow走的长度 S = LenA + x;（由证明的第一部分得到）
（2）第一次相遇时，fast走的长度 2S = LenA + n*R + x;（相遇时，快指针可能已经绕环好几圈了；至少一圈，n大于等于1，因为快指针先进入环，要追上后进入的慢指针，必须得回到环起点在起点之后才能追上）
（3）LenA + x = n*R; LenA = n*R -x;
其中，（3）是由（1）（2）推导出来的。
我们的目标是根据上面三点得出慢指针在走了S + LenA后刚好到达Join点（这是清晰说明这个问题的关键）。我们尝试根据上面三点推导出我们想要的结论：
S + LenA = S + n*R - x = S + (n - 1)*R + (R - x) = S + (n - 1)*R + y
这个表达式证明了我们的结论：慢指针在移动S + (n - 1)*R个节点后刚好在快慢指针第一次相遇的位置，再移动y个节点后就刚好达到Join点。

https://blog.csdn.net/l294265421/article/details/50478818
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: 'ListNode' = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        
        :param head:
        :return:
        """
        if head is None:
            return None
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast is None or fast.next is None:
            return None
        fast = head
        # 走过lenA
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow