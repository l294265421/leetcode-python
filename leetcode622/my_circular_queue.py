# -*- coding: utf-8 -*-

"""

设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）
原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，
我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存
储新的值。

你的实现应该支持如下操作：

    MyCircularQueue(k): 构造器，设置队列长度为 k 。
    Front: 从队首获取元素。如果队列为空，返回 -1 。
    Rear: 获取队尾元素。如果队列为空，返回 -1 。
    enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
    deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
    isEmpty(): 检查循环队列是否为空。
    isFull(): 检查循环队列是否已满。



示例：

MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3

circularQueue.enQueue(1);  // 返回 true

circularQueue.enQueue(2);  // 返回 true

circularQueue.enQueue(3);  // 返回 true

circularQueue.enQueue(4);  // 返回 false，队列已满

circularQueue.Rear();  // 返回 3

circularQueue.isFull();  // 返回 true

circularQueue.deQueue();  // 返回 true

circularQueue.enQueue(4);  // 返回 true

circularQueue.Rear();  // 返回 4




提示：

    所有的值都在 0 至 1000 的范围内；
    操作数将在 1 至 1000 的范围内；
    请不要使用内置的队列库。
"""


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        if k < 1:
            raise Exception('k must be greater than 1')
        self.data_in_queue = [0] * k
        # 保存下一个元素要插入的位置
        self.rear = 0
        # 保存头元素所在的位置
        self.front = 0
        self.data_num = 0

    def _decrease_clockwise(self, position: int):
        temp = position - 1
        if temp == -1:
            temp = len(self.data_in_queue) - 1
        return temp

    def _increase_clockwise(self, position: int):
        temp = position + 1
        if temp == len(self.data_in_queue):
            temp = 0
        return temp

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.data_in_queue[self.rear] = value
            self.rear = self._decrease_clockwise(self.rear)
            self.data_num += 1
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.front = self._decrease_clockwise(self.front)
            self.data_num -= 1
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.data_in_queue[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            rear_position = self._increase_clockwise(self.rear)
            return self.data_in_queue[rear_position]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.data_num == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.data_num == len(self.data_in_queue)


if __name__ == '__main__':
    circularQueue = MyCircularQueue(3)
    # 返回  true
    print('%s-%s' % (True, circularQueue.enQueue(1)))
    # 返回  true
    print('%s-%s' % (True, circularQueue.enQueue(2)))
    # 返回 true
    print('%s-%s' % (True, circularQueue.enQueue(3)))
    # 返回  false，队列已满
    print('%s-%s' % (False, circularQueue.enQueue(4)))
    # 返回  3
    print('%s-%s' % (3, circularQueue.Rear()))
    # 返回  true
    print('%s-%s' % (True, circularQueue.isFull()))
    # 返回  true
    print('%s-%s' % (True, circularQueue.deQueue()))
    # 返回 true
    print('%s-%s' % (4, circularQueue.enQueue(4)))
    circularQueue.Rear() # 返回 4
    print('%s-%s' % (4, circularQueue.Rear()))