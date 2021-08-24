# 例如，

# [2,3,4] 的中位数是 3

# [2,3] 的中位数是 (2 + 3) / 2 = 2.5

# 设计一个支持以下两种操作的数据结构：

# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
# 示例 1：

# 输入：
# ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
# [[],[1],[2],[],[3],[]]
# 输出：[null,null,null,1.50000,null,2.00000]
# 示例 2：

# 输入：
# ["MedianFinder","addNum","findMedian","addNum","findMedian"]
# [[],[2],[],[3],[]]
# 输出：[null,null,2.00000,null,2.50000]


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums=[]


    def addNum(self, num: int) -> None:
        if not self.nums: return self.nums.append(num)
        import bisect
        return bisect.insort_left(self.nums,num) # 维护一个有序数组，保证数组是正序排列的

    def findMedian(self) -> float:
        n=len(self.nums)
        if n==0: return None
        if n==1: return self.nums[0]
        if n%2==1: return self.nums[n//2]
        if n%2==0: return (self.nums[n//2]+self.nums[n//2-1])/2