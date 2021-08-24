# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。
class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        整体思路是将x**n转换为x**sum(mi*2**k),
        '''
        if x==0:
            return 0
        res=1
        if x<0:
            x,n=1/x,-n
        while n:
            if n&1:
                res*=x # 当n的二进制形式的最后一位是1时，即当n能被2整除时，mi=1，存在权重，res*2**k
            x*=x # x^2k
            n>>=1 # 相等于n//2
        return res