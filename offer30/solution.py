"""
剑指 Offer 30. 包含min函数的栈

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。



示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.



提示：

    各函数的调用总次数不超过 20000 次

key idea:
1. 用stack保存最小值，每次新到的值，小于等于原来的最小值，就压入新的最小值
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.all_data = []
        self.min_data = []

    def push(self, x: int) -> None:
        self.all_data.append(x)
        if len(self.min_data) == 0 or x <= self.min_data[-1]:
            self.min_data.append(x)

    def pop(self) -> None:
        if len(self.all_data) == 0:
            raise Exception('pop form empty stack')
        if self.all_data[-1] == self.min_data[-1]:
            self.min_data.pop()
        self.all_data.pop()

    def top(self) -> int:
        if len(self.all_data) == 0:
            raise Exception('top from empty stack')
        return self.all_data[-1]

    def min(self) -> int:
        if len(self.all_data) == 0:
            raise Exception('min from empty stack')
        return self.min_data[-1]
