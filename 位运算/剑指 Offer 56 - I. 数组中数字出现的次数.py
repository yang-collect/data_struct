# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

#  

# 示例 1：

# 输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]
# 示例 2：

# 输入：nums = [1,2,10,4,1,4,3,3]
# 输出：[2,10] 或 [10,2]

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        '''
        假设那两个数字分别为p、q,两个相同的数取异或运算，结果为0，p^p=0

        '''
        d=functools.reduce((lambda x,y : x^y),nums) # 这里计算的结果就是p^q
        # 二进制化的结果中，p和q不相等表示1，相等表示0
        div=1 
        # 循环左移运算，得到p、q二进制表示下，不相同的第一位
        while d&div==0:
            div<<1 
        a,b=0,0
        # 循环遍历数组，将数据分为第div位和1相同的与不同的，由于2进制下一个位只能取0或者1，故用与1是否相同来将数据切分成两个组，
        for n in nums:
            if n&div: 
                a^=n # 0和任何数取异或都是原来的数,若该组数据为[a,x,x] ,则a^x^x=a
            else:
                b^=n # 同上理
        return [a,b]