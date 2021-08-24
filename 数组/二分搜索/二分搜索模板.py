# 对顺序数组进行搜索
def search(nums,target):

    m=len(nums)
    res=0
    # 边界条件
    if  nums[0]<target or nums[-1]>target:
        return -1

    left,right=0,m-1

    while (left<=right):
        mid=left+(right-left)//2

        if  nums[mid]<target:
            left=mid+1
        
        elif nums[mid]>target:
            right=mid-1
        
        else :
            # 当nums[mid]==target时，有不同的限定条件

        
        return  res
    
