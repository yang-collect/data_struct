# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

# 换句话说，第一个字符串的排列之一是第二个字符串的 子串 。
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 初始化窗口的左右端点、有效字符数
        left,right,valid=0,0,0
        # 初始化窗口待满足子串
        window={k:0 for k in s1}
        needs=dict(Counter(s1))
        # print(window)
        # print(needs)
        while  right<len(s2):
            # 扩大窗口
            c=s2[right]
            right+=1

            # 更新窗口以及有效字符数
            if  c  in needs:
                window[c]+=1
                if  window[c]==needs[c]:
                    valid+=1
            # 左端点是否需要收缩
            while right-left>len(s1):
                # 在这里判断是否找到了合法的子串
                if  valid==len(s1):
                    return True
                # 移动左端点
                d=s2[left]
                # 更新窗口
                if  d  in needs:
                    if  window[d]==needs[d]:
                        valid-=1
                    window[d]-=1
                left+=1
        if len(s1)==len(s2):
            return  True if  window==needs else False 
        return  False

if __name__=='__main__':
    s2="abcdxabcde"
    s1="abcdeabcdx"
    print(Solution().checkInclusion(s1,s2))