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
        self.max_queue = []

    def max_value(self) -> int:
        if len(self.max_queue) == 0:
            return -1
        else:
            return self.max_queue[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        if len(self.max_queue) == 0:
            self.max_queue.append(value)
        else:
            if value > self.max_queue[0]:
                self.max_queue = [value]
            else:
                self.max_queue.append(value)

    def reserve_the_property_of_max_queue(self):
        if len(self.max_queue) == 0:
            return None
        temp = []
        while len(self.max_queue) != 0:
            if len(temp) == 0:
                temp.append(self.max_queue.pop(0))
            else:
                front = self.max_queue.pop(0)
                if front > temp[0]:
                    temp = [front]
                else:
                    temp.append(front)
        self.max_queue = temp

    def pop_front(self) -> int:
        if len(self.queue) == 0:
            return -1
        else:
            result = self.queue.pop(0)
            if result == self.max_queue[0]:
                self.max_queue.pop(0)
                self.reserve_the_property_of_max_queue()
            return result




# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()