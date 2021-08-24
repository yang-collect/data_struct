# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

#     1
#    / \
#   2   2
#    \   \
#    3    3

#  

# 示例 1：

# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 示例 2：

# 输入：root = [1,2,2,null,3,null,3]
# 输出：false


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def cur(left, right):
            # 左右子节点同时为空，返回True
            if not left and not right:
                return True  
            
            # 左右子节点只有一个为空，或者左右子节点的值不相等,返回False
            if (not left and right) or (not right and left) or left.val != right.val:
                return False
            # 遍历左子节点的左树与右子节点的右子树和左子节点的右子树与右子节点的左子树
            return cur(left.right, right.left) and cur(left.left, right.right)

        if not root:
            return True
        return cur(root.left, root.right)
