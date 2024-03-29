# 整数数组 nums 按升序排列，数组中的值 互不相同 。

# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，
# 使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
# 例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的索引，否则返回 -1 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 特性1：nums[0]>nums[-1]
def reve_search(nums,target):
    m=len(nums)
    if m<1:
        return -1
    
    l,r=0,m-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            return mid
        if nums[l]<=nums[mid]: #判断[l,mid]是否为升序排列
            if nums[l]<=target<=nums[mid]:
                r=mid-1
            else:
                l=mid+1
        else:
            if nums[mid+1]<=target<=nums[r]:
                l=mid+1
            else:
                r=mid-1

    return -1