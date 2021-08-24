# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

# 要求时间复杂度为O(n)。

#  

# 示例1:

# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0: return None
        if n==1: return nums[0]
        # fn=max(fn-1+cur,cur)
        pre,res=0,nums[0]
        for x in nums:
            pre=max(pre+x,x) # 前一个节点加不加
            res=max(res,pre) # 最大的fn
        return res