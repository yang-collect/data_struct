# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

# 示例 1：

# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true
# 示例 2：

# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word: return False
        # dfs搜索的是borad[i][j]与word[k]和其临近点与k+1处的匹配
        def dfs(i, j, k):
            # 越界或者不相等
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: 
                return False
            # 访问到单词的末尾
            if k == len(word) - 1: 
                return True
            # 用'' 标记访问过
            board[i][j] = ''
            # 上下左右搜索字符与下一个单词中字母是否相同，符合相邻的条件
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            # 回退
            board[i][j] = word[k]
            # 返回布尔量 res ，代表是否搜索到目标字符串
            return res

        # 矩阵从左上开始遍历，字母从第一个字符开始遍历
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): 
                    return True
        return False

