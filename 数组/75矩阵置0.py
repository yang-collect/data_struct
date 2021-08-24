class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n=len(matrix),len(matrix[0])
        col0=any([matrix[i][0]==0 for i in range(m)])
        row0=any([matrix[0][j]==0 for j in range(n)])

        # 处理从第1行和第一列开始，第0行和第0列作为标记行和列

        # 遍历，给标记行和列添加标记
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=matrix[0][j]=0 # 记录应该变成0的行和列
        
        # 更具标记的行或者列来将元素置0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0 # 将行或列里存在0的元素变成0
        
        # 处理第0行或者第0列

        if col0:
            for i in range(m):
                matrix[i][0]=0
        
        if row0:
            for j in range(n):
                matrix[0][j]=0
        