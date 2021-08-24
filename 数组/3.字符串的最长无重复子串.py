# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s) # 数组长度
        if not s:
            return 0
        if len(set(s))==n: # 全部不重复
            return len(s)
        # 用一个hashmap来记录s[left:right+1]出的元素
        result=set()
        # 初始化最大长度和right
        max_len,right=0,-1
        #  left从头至尾遍历
        for left in range(n):
            # 仅保留index在[left:right]区间内的值
            if left>0:
                result.remove(s[left-1]) # 移除前一个元素
            # 当满足s[right+1]处的值不在result中，且right并不超出边界时；
            # result增加result+1处的值，更新right
            while right<n-1 and s[right+1] not in result:
                result.add(s[right+1]) 
                right+=1
            # 记录最长的无重复子串
            max_len=max(max_len,right-left+1)

        return max_len