# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# 示例:

# 现有矩阵 matrix 如下：

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定 target = 5，返回 true。

# 给定 target = 20，返回 false。


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 判空
        if not matrix:
            return False
        
        m,n=len(matrix),len(matrix[0])

        # 从右上角开始比较：
        # 1. 若数字等于target则返回true ；
        # 2. 若数字大于target，列加1；
        # 3. 若数字小于target，行减1 
        # 若最终为找到，返回false
        i,j=0,n-1 
        while j>=0 and i<m:
            value=matrix[i][j]
            if value==target:
                return True
            elif value>target:
                j-=1
            else:
                i+=1
        return False
