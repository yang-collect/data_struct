# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root  # 判空

        # 递归左右子节点
        left, right = self.mirrorTree(root.left), self.mirrorTree(root.right)
        # 交换左右子节点
        root.left, root.roght = right, left

        return root
