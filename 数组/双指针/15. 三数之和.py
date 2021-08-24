# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
# 请你找出所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        size = len(nums) # 记录数组长度
        nums=sorted(nums) # 数组排序
        # 边界条件：
        if size<3 :
            return []
        
        # 用一个列表来记录结果
        result = []
        
        for i in range(size-2):
            # 跳过重复元素，从i=1开始跳
            if i>0 and nums[i]==nums[i-1]:
                continue
            # i至i+2处元素之和大于0.直接跳过
            if nums[i]+nums[i+1]+nums[i+2]>0:
                continue
            # i和最大两个元素之和小于0直接跳过
            if nums[i]+nums[-1]+nums[-2]<0:
                continue
            # 双指针，左右遍历
            left,right=i+1,size-1

            while left<right:

                if nums[i]+nums[left]+nums[right] ==0:
                    # 当上述元素之和为0时，把第一组元素记录下来
                    result.append([nums[i],nums[left],nums[right]])
                    # 移动left和right来跳过重复值
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    # 移动左右指针，代表当前组重复元素遍历完毕
                    left+=1
                    right-=1
                # 当三叔之和大于0时，即right值偏大，移动right
                elif nums[i]+nums[left]+nums[right]>0:
                    right-=1
                # 当三数之和小于0时，移动left
                else:
                    left+=1
        # 数组去重的操作依赖：
        # 第一个元素，依赖与前面一个元素相比较，若遍历过，则跳过该元素的遍历；
        # left和right依赖while循环，当left与left右边元素相等时，left向有移动，同理，right向左移动
        return result
        


