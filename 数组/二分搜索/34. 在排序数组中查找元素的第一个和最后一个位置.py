# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

# 如果数组中不存在目标值 target，返回 [-1, -1]。

# 进阶：

# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

def search_num(nums, target):
    m = len(nums)

    # 边界条件
    if m < 2 or nums[0] > target or nums[-1] < target:
        return [-1, -1]

    left = search(nums, target, True)
    right = search(nums, target, False)
    return [left, right]


def search(nums, target, flag):
    #  flag 表示是否为左边界点
    m = len(nums)
    left, right = 0, m-1

    while left <= right:
        #找到中间点
        mid = left+(right-left)//2

        # 大于中间点
        if nums[mid] > target:
            right = mid-1
        # 小于中间点
        elif nums[mid] < target:
            left = mid+1
        # 等于中间点
        else:
            res = mid
            if flag:
                right = mid-1
            else:
                left = mid+1
    return res


