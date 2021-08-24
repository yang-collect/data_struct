# 剑指 Offer 43. 1～n 整数中 1 出现的次数
# 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

# 例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

 

# 示例 1：

# 输入：n = 12
# 输出：5
# 示例 2：

# 输入：n = 13
# 输出：6


class Solution:
    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0 # digit 位因子,初始化位1,表示十位
        high, cur, low = n // 10, n % 10, 0 # 将原数据分为高中低三个部分
        while high != 0 or cur != 0:
            if cur == 0: res += high * digit # 若高位能被10整除,res应该加上的是其高位*位数
            elif cur == 1: res += high * digit + low + 1 # 能被1整除,res应该加上高位*位数+低位+1 
            else: res += (high + 1) * digit # 否则需要(high+1)*digit
            low += cur * digit # 低位需要加当前余数*位数
            cur = high % 10 
            high //= 10
            digit *= 10
        
        return res
