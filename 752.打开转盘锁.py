# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。
# 每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

# 字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/open-the-lock
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 最小旋转次数，对应当值相等时，不会进行重复翻转
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 双向BFS，用集合记录两边的扩散，set效率比list高，便于判断是否发生交集
        # q1记录起点，q2记录
        q1 = set()
        q1.add('0000')
        q2 = set()
        # python 集合初始化用set(), 添加元素用.add(),
        q2.add(target)
        visited = set()
        # set  也可以去重
        deadset = set(deadends)
        step = 0

        while q1 and q2:
            # 队列（集合）中的元素越多，扩散之后新的队列（集合）中的元素就越多；
            # 在双向 BFS 算法中，如果我们每次都选择一个较小的集合进行扩散，那么占用的空间增长速度就会慢一些，效率就会高一些。
            if len(q1) > len(q2):
                q1, q2 = q2, q1
            temp = set()    # 记录扩散的结点
            for cur in q1:
                if cur in deadset:
                    continue
                if cur in q2:       
                    # 如果两边扩散的元素出现交集，说明找到了最短路径
                    return step
                # 将当前字符串加入visited中
                visited.add(cur)
                # 遍历字符串长度，将未出现在visited中的上下翻转加入temp中
                for i in range(4):
                    up = self.up(cur, i)
                    if up not in visited:
                        temp.add(up)
                    down = self.down(cur, i)
                    if down not in visited:
                        temp.add(down)
            step += 1
            # 交换q1和q2，q2存储着上一次q1扩散的结果temp
            q1 = q2
            q2 = temp       # q2始终记录上一次扩散时得到的元素
        return -1
    
    def up(self, s:str, i:int) -> str:
        s_list = list(s)
        if s_list[i] == '9':
            s_list[i] = '0'
        else:
            s_list[i] = str(int(s_list[i]) + 1)
        return "".join(s_list)
    
    def down(self, s:str, i:int) -> str:
        s_list = list(s)
        if s_list[i] == '0':
            s_list[i] = '9'
        else:
            s_list[i] = str(int(s_list[i]) - 1)
        return "".join(s_list)


print(Solution().openLock(["0201","0101","0102","1212","2002"],"0202"))

