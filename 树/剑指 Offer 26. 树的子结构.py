# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

# B是A的子结构， 即 A中有出现和B相同的结构和节点值。

# 例如:
# 给定的树 A:

#      3
#     / \
#    4   5
#   / \
#  1   2
# 给定的树 B：

#    4 
#   /
#  1
# 返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def search(a,b):
            if not b: return True # B的节点为空，表示匹配完毕
            if not a or a.val!=b.val: return False # a空，或者a、b节点值不同
            return search(a.left,b.left) and search(a.right,b.right) # 递归a，b的左右两边
        # A和B是否同时不为空，且遍历A的左子节点和B、遍历A的右子节点和B、遍历A和B的节点是否满足条件
        return bool(A and B) and(self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B) or search(A,B))