# 字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。
# 若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。
class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return S
        result = ''
        cur = S[0]
        count = 0
        for i in range(len(S)):
            if S[i] == cur:
                count += 1
            else:
                result += cur+str(count)
                count = 1
                cur = S[i]

        result += cur+str(count)
        if len(S) == len(result):
            result = S
        return result
