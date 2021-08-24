# 字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m = len(first)
        n = len(second)
        if first == second:
            return True
        if abs(m-n) > 1:
            return False
        num = 0  # 记录不相等字符数量
        i, j = 0, 0  # 初始化指针
        while i < m and j < n:
            if first[i] != second[j]:  # 不论字符是否相等，都会进行下一个指针的判断
                if num > 0:  # 当不相等字符在记录前就已经大于0，直接返回flase
                    return False
                num += 1  # 记录
                if m < n:
                    # 当m<n时，将first对应的指针向前移动一位，这是由于后面会将两个指针都移动一位，
                    # 只移动较短的可以保证跳过较长的当前字符的作用
                    i -= 1
                if m > n:  # 不能直接写else，存在类似"ab" "bc"这类的情况
                    j -= 1
            # 两个指针同时向后移动一位
            i += 1
            j += 1
        return True
