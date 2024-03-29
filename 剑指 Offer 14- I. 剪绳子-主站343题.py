# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
# 每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
# 例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

# 根据数学推导可以得出如下解法
# 1. 最好每段长度相同
# 2. 每段长度最好为3
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: # 2、3拆分后的乘积之和为1、2
            return n-1
        # 与3相除的整数和余数部分
        a, b = n//3, n % 3
        if b == 0: # 整除
            result = 3**a
        if b == 1: # 余1
            result = 3**(a-1)*4
        if b == 2: # 余2
            result = 3**a*2
        return result
