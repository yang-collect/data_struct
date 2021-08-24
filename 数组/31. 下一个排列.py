# 实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

# 必须 原地 修改，只允许使用额外常数空间。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/next-permutation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

def nextPermutation(nums):

    m = len(nums)
    if m < 2:
        return nums
    # 找到第一个顺序对[i,i+1]，nums[i]<nums[i+1],i处即为较小元素
    i = m-2
    # [i+1,m) 处为逆序
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1

    if i >= 0:
        j = m-1

        # 再[i+1,m) 内从后向前遍历找到一个nums[i]<nums[j],交换顺序
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    # 逆序部分交换顺序
    left, right = i+1, len(nums)-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
