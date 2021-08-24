# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

# 注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-window-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ''
        # 初始化窗口和目标字符串的字典表示，用dict是因为只要求涵盖所有字符
        window={k:0 for k in set(t)}
        needs=dict(Counter(t))
        # 获取目标窗口的有效字符数
        length=10**5
        m=len(needs)
        left,right=0,0
        # 记录有效字符数
        valid=0
        while right<len(s):
            # 扩大窗口
            c=s[right]
            right+=1
            # 当c在s中时更新 window窗口的值
            if c in needs:
                window[c]+=1
                # 当窗口值达到目标时，valid+1
                if  window[c]==needs[c]:
                    valid+=1
            # 当窗口中满足条件的字符串满足子串要求时，开始减小窗口
            while valid==m:
                # 返回最小长度
                if right-left<length:
                    start=left
                    length=right-left
                d=s[left]
                left+=1
                if d in needs:
                    if  window[d]==needs[d]:
                        valid-=1
                    window[d]-=1
        # 当窗口长度达到边界时，返回空
        return '' if length==10**5 else s[start:start+length]

if __name__ == "__main__":
    s="aaab"
    t='aa'
    print(Solution().minWindow(s,t))




        