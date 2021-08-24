# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

# 两棵树重复是指它们具有相同的结构以及相同的结点值。

# 难点：
#  如何判断重复子树？
#  反序列化为字符串来判断是否重复，
class Node:
    def __init__(self, root, left, right):
        self.val = root
        self.left = left
        self.right = right

res = []
memo = {}

def findDuplicateTree(root):
    travse(root)
    return res


def travse(root):
        # bad case
        if not root:
            return '#'

        # 遍历左右子树
        left = travse(root.left)
        right = travse(root.right)

        # 反序列化为字符串
        subtree = left+','+right+','+root.val

        # 采用字典来保存出现的字符串以及次数-1
        memo[subtree] = 0

        # 当次数等于2的时，将结果记录入，不用>1是为防止重复
        if memo[subtree] == 1:
            res.append(root)

        memo[subtree] += 1

        return subtree
