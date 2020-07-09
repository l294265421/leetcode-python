"""
剑指 Offer 59 - II. 队列的最大值

请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和
pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]

示例 2：

输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]



限制：

    1 <= push_back,pop_front,max_value的总操作数 <= 10000
    1 <= value <= 10^5


"""


class MaxQueue:

    def __init__(self):
        self.queue = []
        # 有个特性：
        # 1. 当新来一个元素是，前面的比它小的元素都出队，使得该队列里，前面的元素总是不比后面的小
        self.deque = []

    def max_value(self) -> int:
        if len(self.deque) == 0:
            return -1
        else:
            return self.deque[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        if len(self.deque) == 0:
            self.deque.append(value)
        else:
            while len(self.deque) != 0 and self.deque[-1] < value:
                self.deque.pop()
            self.deque.append(value)

    def pop_front(self) -> int:
        if len(self.queue) == 0:
            return -1
        else:
            result = self.queue.pop(0)
            if result == self.deque[0]:
                self.deque.pop(0)
            return result




# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()