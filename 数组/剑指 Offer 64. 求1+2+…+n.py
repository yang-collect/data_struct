# 求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
# 解法1，利用短路运算以及递归
class Solution:
    def __init__(self):
        self.res=0
    def sumNums(self, n: int) -> int:
        n>1 and self.sumNums(n-1) # 短路写法，当满足条件时才会执行递归
        self.res+=n 
        return self.res

# 解法2，利用python的reduce运算
class Solution2:
    def sumNums(self, n: int) -> int:
        from functools import reduce
        return reduce(lambda x,y:x+y, range(1,n+1), 0)
        