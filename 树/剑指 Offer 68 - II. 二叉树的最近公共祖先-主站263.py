# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]


#  

# 示例 1:

# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
# 示例 2:

# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or p.val == root.val or q.val == root.val:
            return root  # 当根节点为空，或者p、q中的一个和根节点相同时，直接返回根节点
        # 递归找到左右子节点中left和right里是的公共祖先
        l, r = self.lowestCommonAncestor(
            root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        if l and r:  # 当左边和右边同时存在公共祖先时，必然只有根节点存在公共祖先
            return root
        else:  # 否则，返回其中有值的那一个
            return l or r
