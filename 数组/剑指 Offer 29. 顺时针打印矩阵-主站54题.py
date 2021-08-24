# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

#  

# 示例 1：

# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：

# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 边界条件1，空矩阵
        if not matrix or not matrix[0]: return []
        m,n=len(matrix),len(matrix[0])
        res=[]
        # 初始化上下左右边界
        left,right,top,botoom=0,n-1,0,m-1
        # 按找边的方向移动
        while left<=right and top<=botoom:
            # 从左向右
            for col in range(left,right+1):
                res.append(matrix[top][col])
            # 从上至下
            for row in range(top+1,botoom+1):
                res.append(matrix[row][right])
            # 从右向左
            for col in range(right-1,left,-1):
                res.append(matrix[botoom][col])
            # 从下至上
            for row in range(botoom,top,-1):
                res.append(matrix[row][left])
            # 移动后，下一次移动时候去掉外面一层
            left,right,top,botoom=left+1,right-1,top+1,botoom-1
        # 删除重复添加的部分，一般而言时最中间的位置可能会重复一次
        while len(res)>m*n:
            res.pop()
        return res