# -*- coding: utf-8 -*-

"""
设计实现双端队列。
你的实现需要支持以下操作：

    MyCircularDeque(k)：构造函数,双端队列的大小为k。
    insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
    insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
    deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
    deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
    getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
    getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
    isEmpty()：检查双端队列是否为空。
    isFull()：检查双端队列是否满了。

示例：

MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
circularDeque.insertLast(1);			        // 返回 true
circularDeque.insertLast(2);			        // 返回 true
circularDeque.insertFront(3);			        // 返回 true
circularDeque.insertFront(4);			        // 已经满了，返回 false
circularDeque.getRear();  				// 返回 2
circularDeque.isFull();				        // 返回 true
circularDeque.deleteLast();			        // 返回 true
circularDeque.insertFront(4);			        // 返回 true
circularDeque.getFront();				// 返回 4




提示：

    所有值的范围为 [1, 1000]
    操作次数的范围为 [1, 1000]
    请不要使用内置的双端队列库。

"""


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        if k < 1:
            raise Exception('k must be greater than 0')
        self.data_in_queue = [0] * k
        # rear和front都是保存下一个插入操作元素的位置；
        # rear逆时针增长，顺时针减少；front顺时针增长，逆时针减少；
        self.rear = 0
        self.front = 1
        self.data_num = 0

    def _increase_clockwise(self, position: int):
        temp = position + 1
        if temp == len(self.data_in_queue):
            temp = 0
        return temp

    def _increase_anticlockwise(self, position: int):
        temp = position - 1
        if temp == -1:
            temp = len(self.data_in_queue) - 1
        return temp

    def _decrease_clockwise(self, position: int):
        return self._increase_anticlockwise(position)

    def _decrease_anticlockwise(self, position: int):
        return self._increase_clockwise(position)

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.data_in_queue[self.front] = value
            self.data_num += 1
            self.front = self._increase_clockwise(self.front)
            return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.data_in_queue[self.rear] = value
            self.data_num += 1
            self.rear = self._increase_anticlockwise(self.rear)
            return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.front = self._decrease_clockwise(self.front)
            self.data_num -= 1
            return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.rear = self._decrease_anticlockwise(self.rear)
            self.data_num -= 1
            return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            previous_front_index = self._decrease_clockwise(self.front)
            return self.data_in_queue[previous_front_index]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """

        if self.isEmpty():
            return -1
        else:
            previous_rear_index = self._decrease_anticlockwise(self.rear)
            return self.data_in_queue[previous_rear_index]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.data_num == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.data_num == len(self.data_in_queue)


if __name__ == '__main__':
    circularDeque = MyCircularDeque(3) # 设置容量大小为3
    #  返回   true
    print('%s-%s' % (True, circularDeque.insertLast(1)))
    #  返回  true
    print('%s-%s' % (True, circularDeque.insertLast(2)))
    #  返回true
    print('%s-%s' % (True, circularDeque.insertFront(3)))
    #  已经满了，返回false
    print('%s-%s' % (True, circularDeque.insertFront(4)))
    #  返回2
    print('%s-%s' % (2, circularDeque.getRear()))
    #  返回 true
    print('%s-%s' % (True, circularDeque.isFull()))
    #  返回true
    print('%s-%s' % (True, circularDeque.deleteLast()))
    #  返回true
    print('%s-%s' % (True, circularDeque.insertFront(4)))
    #  返回 4
    print('%s-%s' % (4, circularDeque.getFront()))
