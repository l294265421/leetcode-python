"""
剑指 Offer 46. 把数字翻译成字符串

给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成
“l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种
不同的翻译方法。



示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"



提示：

    0 <= num < 231


"""


class Solution:
    def translateNum(self, num: int) -> int:
        """
        以第i个数字结尾的子串编码可编码数量定为f(i)，
        可知f(i) = f(i - 1) + (if i-1,i 可以被编码，f(f - 2)，otherwise 0)
        :param num:
        :return:
        """
        num_str = str(num)
        nums = [0 for i in range(len(num_str))]
        nums[0] = 1
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            if num_str[i - 1] != '0' and int(num_str[i - 1: i + 1]) < 26:
                if i - 2 >= 0:
                    nums[i] += nums[i - 2]
                else:
                    nums[i] += 1
        return nums[-1]
