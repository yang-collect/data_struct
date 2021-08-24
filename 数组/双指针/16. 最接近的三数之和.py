# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
# 返回这三个数的和。假定每组输入只存在唯一答案。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum-closest
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

def threeSumClosest(nums, target):
    size = len(nums)
    nums.sort()
    third = size-1
    ans = nums[0] + nums[1] + nums[2]

    for first in range(size-2):
        if first > 0 and nums[first] == nums[first-1]:
            continue
        second = first+1
        while second < third:
            if second > first+1 and nums[second] == nums[second-1]:
                continue

            if nums[third] == nums[third-1]:
                third -= 1
            sums = nums[first]+nums[second]+nums[third]

            if abs(sums-target) > abs(ans-target):
                ans = sums
            if sums > target:
                third -= 1
            elif sums < target:
                second += 1
            else:
                return target

    return ans
