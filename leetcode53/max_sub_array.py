'''
给定一个序列（至少含有 1 个数），从该序列中寻找一个连续的子序列，使得子序列的和最大。

例如，给定序列 [-2,1,-3,4,-1,2,1,-5,4]，
连续子序列 [4,-1,2,1] 的和最大，为 6。



扩展练习:

若你已实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

'''


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 2 ** 31 * -1
        for i in range(0, len(nums), 1):
            sum_temp = 0
            for j in range(i, len(nums), 1):
                sum_temp += nums[j]
                if sum_temp > result:
                    result = sum_temp
        return result


solution = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(solution.maxSubArray(nums))