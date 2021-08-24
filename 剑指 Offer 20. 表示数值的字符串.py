
# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。

# 数值（按顺序）可以分成以下几个部分：

# 若干空格
# 一个 小数 或者 整数
# （可选）一个 'e' 或 'E' ，后面跟着一个 整数
# 若干空格
# 小数（按顺序）可以分成以下几个部分：

# （可选）一个符号字符（'+' 或 '-'）
# 下述格式之一：
# 至少一位数字，后面跟着一个点 '.'
# 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
# 一个点 '.' ，后面跟着至少一位数字
# 整数（按顺序）可以分成以下几个部分：

# （可选）一个符号字符（'+' 或 '-'）
# 至少一位数字
# 部分数值列举如下：

# ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]
# 部分非数值列举如下：

# ["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]

class Solution:
    def isNumber(self, s: str) -> bool:
        if not s:
            return False
        s = s.strip()
        acceptded = ['+', '-', '0', '1', '2', '3', '4',
                     '5', '6', '7', '8', '9', '.', 'e', 'E']
        length = len(s)
        numflag = False
        dotflag = False
        eflag = False
        for i in range(length):
            # 判定数字
            if s[i] in acceptded[2:-3]:
                numflag = True
            # 判定为.  需要没出现过.并且没出现过e
            elif s[i] == '.' and not dotflag and not eflag:
                dotflag = True
            # 判定为e，需要没出现过e，并且出过数字了
            elif s[i] in acceptded[-2:] and not eflag and numflag:
                eflag = True
                numflag = False  # 为了避免123e这种请求，出现e之后就标志为false
            elif (i == 0 or s[i-1] in acceptded[-2:]) and s[i] in acceptded[:2]:
                continue  # 判断下一个
            else:
                return False
        return numflag  # 必须要有数字，且123e这种是不得行的
