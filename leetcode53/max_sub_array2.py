'''
给定一个序列（至少含有 1 个数），从该序列中寻找一个连续的子序列，使得子序列的和最大。

例如，给定序列 [-2,1,-3,4,-1,2,1,-5,4]，
连续子序列 [4,-1,2,1] 的和最大，为 6。



扩展练习:

若你已实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

https://blog.csdn.net/l294265421/article/details/44627331

'''


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 2 ** 31 * -1
        pre_max_sum_array = result
        for i in range(0, len(nums), 1):
            this_max_sum = nums[i]
            if pre_max_sum_array > 0:
                this_max_sum += pre_max_sum_array
            if this_max_sum > result:
                result = this_max_sum
            pre_max_sum_array = this_max_sum
        return result


solution = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(solution.maxSubArray(nums))