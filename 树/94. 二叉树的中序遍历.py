# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。

# 二叉树的中序遍历：按照访问左子树——根节点——右子树的方式遍历这棵树
# 前序：根-左-右
# 后序 ： 左-右-根

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        res = []
        inorder(root, res)
        return res

    def inorder(self, root, res):
        if not root:
            return

        # 记录根节点值
        res.append(root.val)

        # 访问左节点
        inorder(root.left, res)
        # 访问右节点
        inorder(root.right, res)
